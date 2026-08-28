from enum import Enum

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import coo_matrix

from foxyface.stream.core.StreamReadOnly import StreamReadOnly
from foxyface.stream.core.components.BlendshapeMigrationBufferStream import BlendshapeMigrationBufferStream
from foxyface.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from foxyface.stream.postprocessing.frames.BlendShapesFrame import BlendShapesFrame
from foxyface.stream.postprocessing.mixer import CollisionList
from foxyface.stream.postprocessing.mixer.MixerRoute import MixerRoute
from foxyface.stream.postprocessing.mixer.MixerSelectionList import MixerSelectionList


class MixerFilterStream(StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]]):
    def __init__(self, stream: BlendshapeMigrationBufferStream):
        self.__stream: BlendshapeMigrationBufferStream = stream

        self.__blendshape_mapping: dict[GeneralBlendShapeEnum, Enum] = {}
        self.__current_routes: dict[GeneralBlendShapeEnum, MixerRoute] = {}

        self.__custom_route: dict[GeneralBlendShapeEnum, MixerRoute] = {}
        self.__disabled_routes: set[MixerRoute] = set()
        self.__collision_list: dict[GeneralBlendShapeEnum, GeneralBlendShapeEnum] = {}

        self.__all_routes_cache: dict[GeneralBlendShapeEnum, list[MixerRoute]] = {}

        for blendshape in GeneralBlendShapeEnum:
            routes = [MixerRoute.DISABLED, MixerRoute.AUTO]
            for route in MixerRoute:
                r_type = route.encoder_enum
                if r_type is not None and any(isinstance(sa, r_type) for sa in blendshape.value.same_as):
                    routes.append(route)
            self.__all_routes_cache[blendshape] = routes

        self.update_routes(dict(), set())

    def update_routes(self, custom_route: dict[GeneralBlendShapeEnum, MixerRoute], disabled_routes: set[MixerRoute]):
        self.__custom_route = custom_route
        self.__disabled_routes = disabled_routes

        out_list: dict[GeneralBlendShapeEnum, Enum] = {}
        current_route_dict: dict[GeneralBlendShapeEnum, MixerRoute] = {}

        blocked_types = tuple(r.encoder_enum for r in self.__disabled_routes if r.encoder_enum is not None)

        type_to_route = {r.encoder_enum: r for r in MixerRoute if r.encoder_enum is not None}

        for general_blendshape in GeneralBlendShapeEnum:
            route = self.__custom_route.get(general_blendshape, MixerRoute.AUTO)
            if route is MixerRoute.DISABLED:
                continue

            mapped_blendshape = None

            if route is MixerRoute.AUTO:
                for same_as in general_blendshape.value.same_as:
                    if not isinstance(same_as, blocked_types):
                        mapped_blendshape = same_as
                        break
            else:
                route_type = route.encoder_enum
                if route_type is not None:
                    for same_as in general_blendshape.value.same_as:
                        if isinstance(same_as, route_type):
                            mapped_blendshape = same_as
                            break

            if mapped_blendshape is not None:
                out_list[general_blendshape] = mapped_blendshape
                current_route_dict[general_blendshape] = type_to_route[type(mapped_blendshape)]

        nodes = {general_blendshape: self.__custom_route.get(general_blendshape, MixerRoute.AUTO)
                 for general_blendshape in out_list.keys()}

        disabled_nodes, collision_manual_nodes = self.resolve_conflicts(nodes, CollisionList.collision_list)

        for node in disabled_nodes:
            out_list.pop(node, None)
            current_route_dict.pop(node, None)

        self.__collision_list = collision_manual_nodes
        self.__blendshape_mapping = out_list
        self.__current_routes = current_route_dict

    @staticmethod
    def resolve_conflicts(
            nodes: dict[GeneralBlendShapeEnum, MixerRoute],
            conflicts: dict[GeneralBlendShapeEnum, list[GeneralBlendShapeEnum]]
    ) -> tuple[set[GeneralBlendShapeEnum], dict[GeneralBlendShapeEnum, GeneralBlendShapeEnum]]:
        node_list = list(nodes.keys())
        node_count = len(node_list)

        if node_count == 0:
            return set(), dict()

        node_idx = {n: i for i, n in enumerate(node_list)}

        weight_auto = 1
        weight_manual = node_count + 1

        c = np.zeros(node_count)
        for i, node in enumerate(node_list):
            route = nodes[node]
            c[i] = weight_auto if route is MixerRoute.AUTO else weight_manual

        edges = set()

        for u, neighbors in conflicts.items():
            if u not in node_idx:
                continue
            for v in neighbors:
                if v not in node_idx:
                    continue

                edge = (u, v) if u.name < v.name else (v, u)
                edges.add(edge)

        if not edges:
            return set(), dict()

        num_edges = len(edges)
        row_indices, col_indices, data = [], [], []

        for row_idx, (u, v) in enumerate(edges):
            row_indices.extend([row_idx, row_idx])
            col_indices.extend([node_idx[u], node_idx[v]])
            data.extend([1, 1])

        a_matrix = coo_matrix((data, (row_indices, col_indices)), shape=(num_edges, node_count))

        constraints = LinearConstraint(a_matrix, lb=1, ub=np.inf)
        bounds = Bounds(0, 1)
        integrality = np.ones(node_count)

        res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

        if not res.success:
            raise ValueError(f"MILP Failed: {res.message}")

        result = {node_list[i] for i, val in enumerate(res.x) if round(val) == 0}

        disabled_nodes = {node_list[i] for i, val in enumerate(res.x) if round(val) == 1}

        collision_manual_nodes = {}
        for u in disabled_nodes:
            if nodes[u] is not MixerRoute.AUTO:
                for edge in edges:
                    if u in edge:
                        v = edge[1] if edge[0] == u else edge[0]
                        if nodes[v] is not MixerRoute.AUTO:
                            collision_manual_nodes[u] = v
                            if v in result:
                                break

        return disabled_nodes, collision_manual_nodes

    def get_selection_list(self, blendshape: GeneralBlendShapeEnum) -> MixerSelectionList:
        all_routes = self.__all_routes_cache.get(blendshape, [MixerRoute.DISABLED, MixerRoute.AUTO])

        return MixerSelectionList(
            selected=self.__custom_route.get(blendshape, MixerRoute.AUTO),
            current_route=self.__current_routes.get(blendshape, MixerRoute.DISABLED),
            collision=self.__collision_list.get(blendshape, None),
            all_routes=all_routes,
            blocked_routes=set(all_routes) & self.__disabled_routes
        )

    def poll(self, timeout: float | None = None) -> BlendShapesFrame[GeneralBlendShapeEnum]:
        result_blendshapes: dict[GeneralBlendShapeEnum, float] = {}

        flushed_blendshapes = self.__stream.poll(timeout)

        for general_blendshape, required_blendshape in self.__blendshape_mapping.items():
            value = flushed_blendshapes.blend_shapes.get(required_blendshape)
            if value is not None:
                result_blendshapes[general_blendshape] = float(value)

        return BlendShapesFrame(result_blendshapes, flushed_blendshapes.timestamp_ns)

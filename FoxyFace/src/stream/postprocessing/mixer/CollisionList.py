from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum

collision_list: dict[GeneralBlendShapeEnum, list[GeneralBlendShapeEnum]] = {

    GeneralBlendShapeEnum.CheekPuffLeft: [GeneralBlendShapeEnum.CheekPuff],
    GeneralBlendShapeEnum.CheekPuffRight: [GeneralBlendShapeEnum.CheekPuff]

}

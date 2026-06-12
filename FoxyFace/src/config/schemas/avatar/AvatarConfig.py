from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from AppConstants import AppConstants


@dataclass(slots=True)
class AvatarConfig(JSONWizard):
    file_version: str = str(AppConstants.VERSION)

    disable_solver_input_nodes: set[str] = field(default_factory=lambda: [
        "sol_eyeLookOut_L",
        "sol_eyeLookDown_L",
        "sol_eyeLookDown_R",
        "sol_eyeLookIn_L",
        "sol_eyeLookUp_L",
        "sol_eyeLookIn_R",
        "sol_eyeLookOut_R",
        "sol_eyeLookUp_R"
    ])
    disable_solver_output_nodes: set[str] = field(default_factory=lambda: [
        "EyeLookInLeft",
        "EyeLookDownLeft",
        "EyeLookDownRight",
        "EyeLookUpRight",
        "EyeLookUpLeft",
        "EyeLookOutRight",
        "EyeLookInRight",
        "EyeLookOutLeft"
    ])
    disable_output_encoders: set[str] = field(default_factory=set)

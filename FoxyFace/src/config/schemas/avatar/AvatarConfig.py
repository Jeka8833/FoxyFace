from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from AppConstants import AppConstants


@dataclass(slots=True)
class AvatarConfig(JSONWizard):
    file_version: str = str(AppConstants.VERSION)

    disable_solver_input_nodes: set[str] = field(default_factory=set)
    disable_solver_output_nodes: set[str] = field(default_factory=set)
    disable_output_encoders: set[str] = field(default_factory=set)

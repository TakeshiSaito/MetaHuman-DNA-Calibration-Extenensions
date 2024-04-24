import json
from pathlib import Path
from typing import List, Dict


class FacsDrivenController:

    def __init__(self, name, attribute):
        self.__name = name
        self.__attribute = attribute

    @property
    def name(self):
        return self.__name

    @property
    def attribute(self):
        return self.__attribute

    @property
    def name_and_attribute(self):
        return f"{self.__name}.{self.__attribute}"


arkit_table_file = Path(__file__).parent.parent / "resources" / 'arkit_table.json'


def load_ctrls() -> Dict[str, List[FacsDrivenController]]:
    arkit_table_file = Path(__file__).parent.parent / 'resources' / 'arkit_ctrl.json'
    with arkit_table_file.open('r') as file:
        arkit_table: Dict[str, Dict[str, float]] = json.load(file)

    action_unit_ctrls = {}

    for facs, ctrls in arkit_table.items():

        driven_ctrls = []
        for ctrl, attr in ctrls.items():
            ctrl = FacsDrivenController(ctrl, attr)
            driven_ctrls.append(ctrl)

        action_unit_ctrls[facs] = driven_ctrls

    return action_unit_ctrls

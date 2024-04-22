import json
import os
from typing import List, Dict
from pathlib import Path


class FacsDrivenController:

    def __init__(self, name, attribute, multiplier):
        self.__name = name
        self.__attribute = attribute
        self.__multiplier = multiplier

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
        for driven_ctrl_attr in ctrls:
            print(driven_ctrl_attr)
            ctrl_name = driven_ctrl_attr.split('.')[0]
            attr_name = driven_ctrl_attr.split('.')[1]

            ctrl = FacsDrivenController(ctrl_name, attr_name, ctrls[driven_ctrl_attr])
            driven_ctrls.append(ctrl)

        action_unit_ctrls[facs] = driven_ctrls

    return action_unit_ctrls
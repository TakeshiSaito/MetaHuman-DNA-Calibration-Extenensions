import unittest
from pathlib import Path

from MetaHumanFacialImporter.Model import FacialRig


class TestFacialRig(unittest.TestCase):

    def setUp(self):
        FacialRig.arkit_table_file = Path(
            __file__).parent.parent.parent.parent / "scripts" / "MetaHumanFacialImporter" / "resources" / "arkit_ctrl.json"

    def test_load_ctrls(self):
        ctrls = FacialRig.load_ctrls()
        self.assertEqual(len(ctrls["BrowDownLeft"]), 1)

        brow_down_left = ctrls["BrowDownLeft"]
        ctrl = brow_down_left[0]
        self.assertEqual(ctrl.name, "CTRL_L_brow_down")
        self.assertEqual(ctrl.attribute, "translateY")
        self.assertEqual(ctrl.name_and_attribute, "CTRL_L_brow_down.translateY")

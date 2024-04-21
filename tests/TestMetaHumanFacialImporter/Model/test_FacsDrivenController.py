import unittest

from MetaHumanFacialImporter.Model.FacialRig import FacsDrivenController


class TestFacsDrivenController(unittest.TestCase):

    def test_name_and_attr(self):
        ctrl=FacsDrivenController("test_ctrl","tx",1)
        self.assertEqual(f"test_ctrl", ctrl.name)
        self.assertEqual("tx", ctrl.attribute)
        self.assertEqual("test_ctrl.tx",ctrl.name_and_attribute)
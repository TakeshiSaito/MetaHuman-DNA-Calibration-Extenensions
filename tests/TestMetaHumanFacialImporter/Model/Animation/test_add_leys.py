from unittest import TestCase

from maya import cmds, standalone

from MetaHumanFacialImporter.Model import Animation
from MetaHumanFacialImporter.Model.FacialRig import FacsDrivenController


class TestAddKeys(TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cmds.ls()
        except AttributeError:
            standalone.initialize(name='python')

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_add_keys(self):
        locator = cmds.spaceLocator(name='head_loc')[0]
        facs_driven_ctrl = FacsDrivenController(locator, 'translateX')

        Animation.add_keys(facs_driven_ctrl, [0.5, 0.7], [0.0, 1.0])

        cmds.currentTime(0.5)
        self.assertEqual(cmds.getAttr(f'{locator}.translateX'), 0.0)

        cmds.currentTime(0.7)
        self.assertEqual(cmds.getAttr(f'{locator}.translateX'), 1.0)

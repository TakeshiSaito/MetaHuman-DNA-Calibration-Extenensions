import unittest
from maya.api import OpenMayaAnim as oma2, OpenMaya as om2
from maya import cmds

from MetaHumanFacialImporter.Model import Animation


class TestAnimation(unittest.TestCase):

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_get_depend_node(self):
        cube = cmds.polyCube(n='testCube')
        node = Animation.get_depend_node("testCubeShape")
        self.assertEqual(node.getName(), "testCubeShape")


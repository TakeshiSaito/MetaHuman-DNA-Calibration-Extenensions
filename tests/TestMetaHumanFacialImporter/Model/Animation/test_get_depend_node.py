import unittest

from maya import cmds, standalone
from maya.api import OpenMaya as om2

from MetaHumanFacialImporter.Model import Animation


class TestAnimation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cmds.ls()
        except AttributeError:
            standalone.initialize()

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_get_depend_node(self):
        """
        名前からMObjectを取得できているか
        """

        _ = cmds.polyCube(n='testCube')

        node = Animation.get_depend_node("testCubeShape")

        dag_path = om2.MDagPath.getAPathTo(node)
        self.assertEqual('testCubeShape', dag_path.partialPathName())

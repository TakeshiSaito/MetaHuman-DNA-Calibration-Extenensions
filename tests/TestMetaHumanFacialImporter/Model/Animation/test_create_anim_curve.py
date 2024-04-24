import unittest

from MetaHumanFacialImporter.Model import Animation
from maya import cmds, standalone
from maya.api import OpenMayaAnim as oma2, OpenMaya as om2


class TestCreateAnimCurve(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cmds.ls()
        except AttributeError:
            standalone.initialize()

    def setUp(self):
        cmds.file(new=True, force=True)

    def test(self):
        # まずcubeのattr plugを作成
        _ = cmds.polyCube(n="testCube")

        selection_list = om2.MSelectionList()
        selection_list.add('testCube')
        dag_path = selection_list.getDagPath(0)
        dep_node = om2.MFnDependencyNode(dag_path.node())
        tx_plug = dep_node.findPlug('translateX', False)

        tx_curve = Animation.create_anim_curve(tx_plug)
        self.assertEqual(type(tx_curve), oma2.MFnAnimCurve)

        selections: om2.MSelectionList = om2.MGlobal.getSelectionListByName("testCube_translateX")
        self.assertEqual(selections.length(), 1)

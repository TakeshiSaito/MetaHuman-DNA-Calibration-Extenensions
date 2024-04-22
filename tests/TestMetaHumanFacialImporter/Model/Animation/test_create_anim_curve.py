import unittest

from MetaHumanFacialImporter.Model import Animation
from maya import cmds
from maya.api import OpenMayaAnim as oma2, OpenMaya as om2


class TestCreateAnimCurve(unittest.TestCase):

    def setUp(self):
        cmds.file(new=True, force=True)

    def test(self):
        # まずcubeのattr plugを作成
        cube = cmds.polyCube(n="testCube")
        selection_list = om2.MSelectionList()
        selection_list.add('testCube')
        dag_path = selection_list.getDagPath(0)
        dep_node = om2.MFnDependencyNode(dag_path.node())
        tx_plug = dep_node.findPlug('translateX', False)

        tx_curve = Animation.create_anim_curve(tx_plug)
        self.assertEqual(type(tx_curve), oma2.MFnAnimCurve)

        curve_name = "testCube_translateX"

        selections = om2.MGlobal.getSelectionListByName(curve_name)
        self.assertEqual(len(selections), 1)

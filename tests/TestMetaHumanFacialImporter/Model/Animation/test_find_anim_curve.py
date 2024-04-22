import unittest
from maya.api import OpenMayaAnim as oma2, OpenMaya as om2
from maya import cmds

from MetaHumanFacialImporter.Model import Animation


class TestFindAnimCurve(unittest.TestCase):

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_find_anim_curve(self):
        cube, _ = cmds.polyCube()
        cmds.setKeyframe(f"{cube}.translateX", value=10)

        # 関数に渡すためのtx属性をMPlugにする
        selections = om2.MGlobal.getSelectionListByName(cube)
        node = selections[0]
        fn_node = om2.MFnDependencyNode(node)
        tx_mplug = fn_node.findPlug("tx", False)

        curve = Animation.find_anim_curve(tx_mplug)
        self.assertTrue(curve)

    def test_anim_curve_not_found_case(self):
        cube, _ = cmds.polyCube()

        # 関数に渡すためのtx属性をMPlugにする
        selections = om2.MGlobal.getSelectionListByName(cube)
        node = selections[0]
        fn_node = om2.MFnDependencyNode(node)
        tx_mplug = fn_node.findPlug("tx", False)

        curve = Animation.find_anim_curve(tx_mplug)
        self.assertFalse(curve)

import unittest
from maya import cmds, standalone

from MetaHumanFacialImporter.Model import Framerate


class TestFramerate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cmds.ls()
        except AttributeError:
            standalone.initialize()

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_get_fps(self):
        cmds.currentUnit(time='game')
        self.assertEqual(15, Framerate.get_fps())

        cmds.currentUnit(time='film')
        self.assertEqual(24, Framerate.get_fps())

        cmds.currentUnit(time='pal')
        self.assertEqual(25, Framerate.get_fps())

        cmds.currentUnit(time='ntsc')
        self.assertEqual(30, Framerate.get_fps())

        cmds.currentUnit(time='show')
        self.assertEqual(48, Framerate.get_fps())

        cmds.currentUnit(time='palf')
        self.assertEqual(50, Framerate.get_fps())

        cmds.currentUnit(time='ntscf')
        self.assertEqual(60, Framerate.get_fps())

        cmds.currentUnit(time='29.97fps')
        self.assertEqual(29.97, Framerate.get_fps())

        cmds.currentUnit(time='23.976fps')
        self.assertEqual(23.976, Framerate.get_fps())

        cmds.currentUnit(time='47.952fps')
        self.assertEqual(47.952, Framerate.get_fps())

        cmds.currentUnit(time='59.94fps')
        self.assertEqual(59.94, Framerate.get_fps())

        cmds.currentUnit(time='44100fps')
        self.assertEqual(44100, Framerate.get_fps())

        cmds.currentUnit(time='48000fps')
        self.assertEqual(48000, Framerate.get_fps())

from unittest import TestCase

from maya import cmds, standalone

from MetaHumanFacialImporter.Model import Animation


class TestSetPlaybakrange(TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cmds.ls()
        except AttributeError:
            standalone.initialize()

    def setUp(self):
        cmds.file(new=True, force=True)

    def test_set_keys(self):
        frames = [1, 2, 3]
        Animation.set_playbackrange(frames)

        self.assertEqual(cmds.playbackOptions(q=True, minTime=True), 1)
        self.assertEqual(cmds.playbackOptions(q=True, maxTime=True), 3)

        frames = [1, 10, 2]
        Animation.set_playbackrange(frames)

        self.assertEqual(cmds.playbackOptions(q=True, minTime=True), 1)
        self.assertEqual(cmds.playbackOptions(q=True, maxTime=True), 10)

import unittest
import tempfile
import os
import shutil
from pathlib import Path

from MetaHumanFacialImporter.Model import FacialFile


class TestFacialFile(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_csv_file = os.path.join(self.temp_dir, 'test.csv')

    def test_check_exits(self):
        exists = FacialFile.check_exists(self.test_csv_file)
        self.assertFalse(exists)

        Path(self.test_csv_file).touch()
        exists = FacialFile.check_exists(self.test_csv_file)
        self.assertTrue(exists)

    def test_check_extension(self):
        is_csv = FacialFile.check_extension(self.test_csv_file)
        self.assertTrue(is_csv)

        not_csv_fil = os.path.join(self.temp_dir, 'aaa.txt')
        self.assertFalse(FacialFile.check_extension(not_csv_fil))

    def test_timecode_to_fps(self):
        time_code = '00:00:01:00'
        frame_rate = 30
        fps = FacialFile.timecode_to_fps(time_code, frame_rate)
        self.assertEqual(30, fps)

        frame_rate = 60
        fps = FacialFile.timecode_to_fps(time_code, frame_rate)
        self.assertEqual(60, fps)

        frame_rate = ''
        self.assertRaises(TypeError, FacialFile.timecode_to_fps, time_code, frame_rate)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

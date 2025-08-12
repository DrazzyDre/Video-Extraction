import unittest
from src.utils import load_video, save_highlights

class TestUtils(unittest.TestCase):

    def test_load_video(self):
        # Test loading a video file
        video_path = 'path/to/test/video.mp4'
        video = load_video(video_path)
        self.assertIsNotNone(video)

    def test_save_highlights(self):
        # Test saving highlight data
        highlight_data = [{'start_time': 10, 'end_time': 20}, {'start_time': 30, 'end_time': 40}]
        save_path = 'path/to/save/highlights.json'
        result = save_highlights(highlight_data, save_path)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
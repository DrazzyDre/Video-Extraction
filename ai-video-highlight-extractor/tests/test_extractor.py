import unittest
from src.extractor import VideoExtractor

class TestVideoExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = VideoExtractor()

    def test_extract_highlights(self):
        video_path = "path/to/test/video.mp4"
        highlights = self.extractor.extract_highlights(video_path)
        self.assertIsInstance(highlights, list)
        self.assertGreater(len(highlights), 0)

    def test_extract_highlights_invalid_path(self):
        video_path = "invalid/path/to/video.mp4"
        with self.assertRaises(FileNotFoundError):
            self.extractor.extract_highlights(video_path)

if __name__ == '__main__':
    unittest.main()
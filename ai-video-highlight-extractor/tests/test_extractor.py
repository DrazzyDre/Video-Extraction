import unittest
from src.extractor import VideoExtractor

class TestVideoExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = VideoExtractor()

    def test_extract_highlight_segments(self):
        # Use a small test video or mock load_video
        video_path = "path/to/test/video.mp4"
        segments = self.extractor.extract_highlight_segments(video_path)
        self.assertIsInstance(segments, list)

    def test_extract_text_highlights(self):
        # This test should mock extract_audio_segment, speech_to_text, summarize_text
        video_path = "path/to/test/video.mp4"
        # You'd need to mock dependencies here for a real test
        highlights = self.extractor.extract_text_highlights(video_path)
        self.assertIsInstance(highlights, list)

    def test_extract_highlights_invalid_path(self):
        video_path = "invalid/path/to/video.mp4"
        with self.assertRaises(FileNotFoundError):
            self.extractor.extract_highlight_segments(video_path)

if __name__ == '__main__':
    unittest.main()
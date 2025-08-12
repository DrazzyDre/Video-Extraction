import unittest
from src.utils import load_video, save_text_highlights

class TestUtils(unittest.TestCase):

    def test_load_video(self):
        video_path = 'path/to/test/video.mp4'
        # You may want to mock cv2.VideoCapture for unit testing
        video = load_video(video_path)
        self.assertIsNotNone(video)

    def test_save_text_highlights(self):
        highlight_data = [
            {'start_frame': 10, 'end_frame': 20, 'summary': 'Test summary 1'},
            {'start_frame': 30, 'end_frame': 40, 'summary': 'Test summary 2'}
        ]
        save_path = 'path/to/save/highlights.json'
        save_text_highlights(highlight_data, save_path)
        # Check if file exists or content is correct (mock file I/O for real tests)

if __name__ == '__main__':
    unittest.main()
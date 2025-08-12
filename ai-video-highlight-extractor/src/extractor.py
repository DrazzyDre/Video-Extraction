import os
import cv2
import numpy as np
from utils import load_video, extract_audio_segment, speech_to_text, summarize_text

class VideoExtractor:
    def __init__(self, scene_threshold=30.0):
        self.scene_threshold = scene_threshold

    def extract_highlight_segments(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")

        frames = load_video(video_path)
        scene_changes = [0]  # Start with first frame
        prev_frame = None

        for i, frame in enumerate(frames):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if prev_frame is not None:
                diff = cv2.absdiff(gray, prev_frame)
                score = np.mean(diff)
                if score > self.scene_threshold:
                    scene_changes.append(i)
            prev_frame = gray

        # Add last frame as end of last scene
        scene_changes.append(len(frames) - 1)

        # Create segments (start, end)
        segments = []
        for i in range(len(scene_changes) - 1):
            start = scene_changes[i]
            end = scene_changes[i + 1]
            segments.append((start, end))

        return segments
    
    def extract_text_highlights(self, video_path, fps=30):
        segments = self.extract_highlight_segments(video_path)
        text_highlights = []
        for idx, (start, end) in enumerate(segments):
            audio_path = f"segment_{idx}.wav"
            extract_audio_segment(video_path, start, end, fps, audio_path)
            transcript = speech_to_text(audio_path)
            summary = summarize_text(transcript)
            text_highlights.append({
                "start_frame": start,
                "end_frame": end,
                "summary": summary
            })
        return text_highlights
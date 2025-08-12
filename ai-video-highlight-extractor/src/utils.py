import sys
import cv2
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import whisper
from transformers import pipeline
import json

def load_video(video_path):
    """
    Loads video frames from the specified path.
    Returns a list of frames (as numpy arrays).
    Raises FileNotFoundError if the file does not exist.
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def save_highlights(highlight_frames, output_path, fps=30):
    """
    Saves the extracted highlight frames as a video to the specified output path.
    """
    if not highlight_frames:
        print("No highlights to save.")
        return
    height, width, layers = highlight_frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame in highlight_frames:
        out.write(frame)
    out.release()
    print(f"Highlights saved to {output_path}")
    
def extract_audio_segment(video_path, start_frame, end_frame, fps=30, output_audio_path="segment.wav"):
    """
    Extracts audio from a video segment defined by start and end frames.
    Saves the audio to output_audio_path and returns the path.
    """
    start_time = start_frame / fps
    end_time = end_frame / fps
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    clip.audio.write_audiofile(output_audio_path)
    return output_audio_path

def speech_to_text(audio_path):
    """
    Transcribes audio to text using OpenAI Whisper.
    Returns the transcript string.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def summarize_text(text):
    """
    Summarizes the given text using a transformer model.
    Returns the summary string.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    return summary[0]['summary_text']

def save_text_highlights(text_highlights, output_path="highlights.json"):
    """
    Saves the list of text highlights (dicts) to a JSON file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(text_highlights, f, indent=2, ensure_ascii=False)
    print(f"Text highlights saved to {output_path}")
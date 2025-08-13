import argparse
from extractor import VideoExtractor
from utils import save_highlights, save_text_highlights
import tkinter as tk
from tkinter import filedialog

def select_video_file():
    """
    Opens a file dialog for selecting a video file.
    Returns the selected file path or None if cancelled.
    """
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return file_path

def main():
    parser = argparse.ArgumentParser(description="AI Video Highlight Extraction")
    parser.add_argument("--gui", action="store_true", help="Use file dialog to select video")
    parser.add_argument("--output", default="highlights.mp4", help="Output highlights file")
    parser.add_argument("video_path", nargs="?", help="Path to input video file")
    args = parser.parse_args()

    # Choose video file
    if args.gui or not args.video_path:
        video_path = select_video_file()
        if not video_path:
            print("No video selected. Exiting.")
            return
    else:
        video_path = args.video_path

    print(f"Loading video: {video_path}")
    extractor = VideoExtractor()

    # Extract highlights
    print("Extracting highlights...")
    text_highlights = extractor.extract_text_highlights(video_path)

    if not text_highlights:
        print("No highlights were extracted.")
        return

    # Display in console
    for highlight in text_highlights:
        print(f"Frames {highlight['start_frame']} - {highlight['end_frame']}: {highlight['summary']}")

    # Save results
    save_text_highlights(text_highlights, "highlights.json")
    print("Text highlight extraction complete.")
    print("Results saved to 'highlights.json'.")

if __name__ == "__main__":
    main()

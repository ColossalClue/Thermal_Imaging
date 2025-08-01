# ... (imports and config)
POLYGON = np.array([[0, 0], [50, 0], [50, 50], [0, 50]])  # Customize polygon

def process_video(video_path: str, output_path: str):
    # ... (video processing setup)
    def callback(frame: np.ndarray, _: int):
        # ... (tracking + zone logic)
    sv.process_video(video_path, output_path, callback)
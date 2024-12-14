import os
import cv2

def extract_frames(video_path, output_dir):
    vidObj = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = vidObj.read()
        if not ret:
            break
        cv2.imwrite(f"{output_dir}/frame_{frame_count:04d}.jpg",frame)
        frame_count +=1
    vidObj.release()

def frames_to_video(frame_dir, output_video_path, fps):
    frames = sorted([os.path.join(frame_dir, f) for f in os.listdir(frame_dir) if f.endswith(".jpg")])
    #Read the first frame to get video dimensions
    frame = cv2.imread(frames[0])
    height, width, _ = frame.shape
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    for frame_path in frames:
        frame = cv2.imread(frame_path)
        out.write(frame)
    out.release()



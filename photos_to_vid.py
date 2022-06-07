import cv2
import os
from moviepy.editor import *


def run():
    image_folder = 'steps'
    video_name = 'steps.avi'
    out_loc = 'instagram_post.mp4'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

    # Import video clip
    clip = VideoFileClip(video_name)
    print("fps: {}".format(clip.fps))

    # Modify the FPS
    clip = clip.set_fps(clip.fps * 30)

    # Apply speed up
    final = clip.fx(vfx.speedx, 30)
    final_resized = final.resize(height=1080)

    # Save video clip
    final_resized.write_videofile(out_loc)

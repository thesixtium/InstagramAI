import credentials
from pathlib import Path
from PIL import Image
from instagrapi import Client
import photos_to_vid

def make_image():
    image = Image.open("progress.png")
    image = image.convert("RGB")
    new_image = image.resize((1080, 1080))
    new_image.save("instagram_post.jpg")

def post(prompt):
    make_image()
    photos_to_vid.run()

    cl = Client()
    cl.login(credentials.username, credentials.password)

    phot_path = "instagram_post.jpg"
    phot_path = Path(phot_path)

    vid_path = "instagram_post.mp4"
    vid_path = Path(vid_path)

    paths = [phot_path, vid_path]

    caption = "AI Generated Image Based Off Of '" \
              + prompt \
              + "'" \
              + "\n\n" \
              + "#machinelearning #ai #artwork #digitalart #instaart " \
              + "#machinelearningart #deeplearning #machinelearningwithpython" \
              + "#oc #technology #abstract #abstractart #modern #modernart"

    cl.album_upload(paths, caption)
    # cl.photo_upload(phot_path, "AI Generated Image Based Off Of '" + prompt + "'")

import credentials
from pathlib import Path
from PIL import Image
from instagrapi import Client


def post(image_path, prompt):
    image = Image.open(image_path)
    image = image.convert("RGB")
    new_image = image.resize((1080, 1080))
    new_image.save("instagram_post.jpg")

    cl = Client()
    cl.login(credentials.username, credentials.password)

    phot_path = "instagram_post.jpg"
    phot_path = Path(phot_path)

    vid_path = "instagram_post.mp4"
    vid_path = Path(vid_path)

    paths = [phot_path, vid_path]

    cl.album_upload(paths, "AI Generated Image Based Off Of '" + prompt + "'")
    # cl.photo_upload(phot_path, "AI Generated Image Based Off Of '" + prompt + "'")

from datetime import datetime

from src.unsplash_connector.unsplash_connector import download_image
from src.utils import set_wallpaper
from src.utils.path import get_download_path

if __name__ == '__main__':
    path = download_image(
        "https://images.unsplash.com/34/BA1yLjNnQCI1yisIZGEi_2013-07-16_1922_IMG_9873.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2702&q=80",
        get_download_path(),
        f"{int(datetime.now().timestamp())}.jpg")
    set_wallpaper(path)

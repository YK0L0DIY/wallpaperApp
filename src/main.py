from datetime import datetime

from src.unsplash_connector.unsplash_connector import download_image
from src.utils import set_wallpaper
from src.utils.path import get_download_path

if __name__ == '__main__':
    path = download_image(
        "https://images.unsplash.com/photo-1560603472-7a7e0ae67a5d?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE1NDYxNn0",
        get_download_path(),
        f"{int(datetime.now().timestamp())}.jpg")
    set_wallpaper(path)

import os
import platform

from logger import logger
from utils.path import get_download_path
from utils.set_wallpaper import set_set_wallpaper_win, set_set_wallpaper_unix

system_platform = platform.system()
download_folder = get_download_path()


def set_wallpaper():
    path = os.path.join(download_folder, "teste.jpg")

    if system_platform == 'Windows':
        logger.info("Windows platform")
        set_set_wallpaper_win(path)
    else:
        logger.info("Unix platform")
        set_set_wallpaper_unix(download_folder)

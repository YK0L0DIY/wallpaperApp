import platform

from src.logger import logger
from src.utils.set_wallpaper import set_set_wallpaper_win, set_set_wallpaper_unix

system_platform = platform.system()


def set_wallpaper(path: str):
    if system_platform == 'Windows':
        logger.info("Windows platform")
        set_set_wallpaper_win(path)
    else:
        logger.info("Unix platform")
        set_set_wallpaper_unix(path)

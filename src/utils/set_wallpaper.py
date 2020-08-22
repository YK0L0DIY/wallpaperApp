import ctypes
import os

from logger import logger


def set_set_wallpaper_win(path: str):
    logger.debug(path)
    logger.debug("WIN")
    r = ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

    if not r:
        logger.error(ctypes.WinError())

    return


def set_set_wallpaper_unix(path: str):
    logger.debug(path)
    logger.debug("UNIX")

    os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri {path}")

    return

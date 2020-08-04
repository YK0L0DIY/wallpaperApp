import ctypes

from logger import logger


def set_set_wallpaper_win(path: str):
    logger.debug(path)
    logger.debug("WIN")
    r = ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

    if not r:
        logger.error(ctypes.WinError())

    return


def set_set_wallpaper_unix(path: str):
    logger.error(path)
    logger.error("UNIX")
    raise NotImplementedError

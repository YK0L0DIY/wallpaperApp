import os

import wget

from src.logger import logger


def download_image(url: str, folder: str, name: str):
    output = os.path.join(folder, name)
    image_filename = wget.download(url, out=output)

    logger.debug('Image Successfully Downloaded: ', image_filename)
    return image_filename

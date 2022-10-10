#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:59:57 2022

@author: hasier
"""

import os
import glob
import logging
from epub2txt import epub2txt

# Environment Variables
EPUB_DIR_PATH = "books/epub"
TXT_DIR_PATH = "books/txt"

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def _makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def _get_file_names(input_path, output_path):
    try:
        os.chdir(output_path)
        output_list = [f for f in glob.glob("*.txt")]
        output_file_names = list(map(lambda x: x.split(".txt")[0], output_list))
        os.chdir(input_path)
        input_list = [f for f in glob.glob("*.epub")]
        input_file_names = list(map(lambda x: x.split(".epub")[0], input_list))
        return list(set(input_file_names) - set(output_file_names))
    except Exception as e:
        logger.error(e)


def _epub2txt(file_names, output_path):
    assert (
        len(file_names) != 0
    ), f"{EPUB_DIR_PATH} is empty. Put some '.epub' files there."
    success = 0
    for count, file_name in enumerate(file_names, start=1):
        try:
            file_text = epub2txt(f"{file_name}.epub")
            with open(os.path.join(output_path, f"{file_name}.txt"), "w") as f:
                f.write(file_text)
                logger.info(f"[FILE]: {file_name}.txt Done!")
                f.close()
                success += 1
        except Exception as e:
            logger.error(f"[FILE-ERROR]: {file_name}.txt failed.\n{e}\n")
    logger.info(f"{success}/{count} files successfully converted.")
    return None


def generate_epub2txt():
    input_path = os.path.join(os.getcwd(), EPUB_DIR_PATH)
    output_path = os.path.join(os.getcwd(), TXT_DIR_PATH)
    _makedir(input_path)
    _makedir(output_path)
    file_names = _get_file_names(input_path, output_path)
    _epub2txt(file_names, output_path)
    return None

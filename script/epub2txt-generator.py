#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:59:57 2022

@author: hasier
"""

import os
import glob
import argparse
from epub2txt import epub2txt

# Environment Variables
EPUB_DIR_PATH = "books/epub"
TXT_DIR_PATH = "books/txt"


# Define Argument Parser
def get_args():
    parser = argparse.ArgumentParser(
        description=f"""Generates .txt format files from .epub files"""
    )
    parser.add_argument("--workdir", type=str, help="Workdir path")
    return parser.parse_args()


def get_paths(workdir):
    input_path = os.path.join(workdir, EPUB_DIR_PATH)
    output_path = os.path.join(workdir, TXT_DIR_PATH)
    return input_path, output_path


def make_dirs(input_path, output_path):
    if not os.path.exists(input_path):
        os.makedirs(input_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return None


def get_file_names(input_path, output_path):
    try:
        os.chdir(output_path)
        output_list = [f for f in glob.glob("*.txt")]
        os.chdir(input_path)
        input_list = [f for f in glob.glob("*.epub")]
        files = list(set(input_list) - set(output_list))
        return list(map(lambda x: x.split(".epub")[0], files))
    except Exception as e:
        print(f"[GET-FILE-NAMES-ERROR]: {e}")


def generate_epub2txt(file_names):
    assert len(file_names) != 0, f"{EPUB_DIR_PATH} is empty. Put some '.epub' files there."
    success = 0
    for count, file_name in enumerate(file_names, start=1):
        try:
            file_text = epub2txt(f"{file_name}.epub")
            with open(os.path.join(output_path, f"{file_name}.txt"), "w") as f:
                f.write(file_text)
                print(f"[FILE]: {file_name}.txt Done!")
                f.close()
                success += 1
        except Exception as e:
            print(f"[FILE-ERROR]: {file_name}.txt failed.\n{e}\n")
    print(f'{success}/{count} files successfully converted.')
    return None


if __name__ == "__main__":
    args = get_args()
    input_path, output_path = get_paths(args.workdir)
    make_dirs(input_path, output_path)
    file_names = get_file_names(input_path, output_path)
    #generate_epub2txt(file_names)

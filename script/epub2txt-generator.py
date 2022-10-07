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


def generate_paths(workdir):
    print(workdir)
    input_path = os.path.join(workdir, EPUB_DIR_PATH)
    output_path = os.path.join(workdir, TXT_DIR_PATH)
    print(input_path)
    return input_path, output_path


def epub2txt_from_file(input_path, output_path):
    try:
        os.chdir(output_path)
        output_list = [f for f in glob.glob("*.txt")]
        os.chdir(input_path)
        input_list = [f for f in glob.glob("*.epub")]
        files = list(set(input_list) - set(output_list))
        file_names = list(map(lambda x: x.split(".epub")[0], files))
        print(f"file_names: {file_names}")
        for file_name in file_names:
            try:
                file_text = epub2txt(f"{file_name}.epub")
                with open(os.path.join(output_path, f"{file_name}.txt"), "w") as f:
                    f.write(file_text)
                    print(f"[FILE]: {file_name}.txt Done!")
                    f.close()
            except Exception as e:
                print(f"[FILE-ERROR]: {file_name}.txt failed.\n{e}\n")
        return True
    except Exception as e:
        print(f"[GENERATOR-ERROR]: {e}")


if __name__ == "__main__":
    args = get_args()
    input_path, output_path = generate_paths(args.workdir)
    epub2txt_from_file(input_path, output_path)

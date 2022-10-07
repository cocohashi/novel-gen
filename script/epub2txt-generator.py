#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:59:57 2022

@author: hasier
"""

import os
import glob
from epub2txt import epub2txt

# Environment Variables
INPUT_PATH = '/home/hasier/projects/novel-gen/books/epub'
OUTPUT_PATH = '/home/hasier/projects/novel-gen/books/txt'

# Configuration
def epub2txt_from_file():
    try:    
        os.chdir(OUTPUT_PATH)
        output_list = [f for f in glob.glob("*.txt")]
        os.chdir(INPUT_PATH)
        input_list = [f for f in glob.glob("*.epub")]
        files = list(set(input_list) - set(output_list))
        file_names = list(map(lambda x: x.split('.epub')[0],files))
        print(f'file_names: {file_names}')
        for file_name in file_names:
            try:
                file_text = epub2txt(f'{file_name}.epub')
                with open(os.path.join(OUTPUT_PATH, f'{file_name}.txt'), 'w') as f:
                    f.write(file_text)
                    print(f'[FILE]: {file_name}.txt Done!')
                    f.close()
            except Exception as e:
                print(f'[FILE-ERROR]: {file_name}.txt failed.\n{e}\n')
        return True
    except Exception as e:
        print(f'[GENERATOR-ERROR]: {e}')
    

if __name__=="__main__":
    epub2txt_from_file()

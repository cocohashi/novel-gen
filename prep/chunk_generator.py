import logging
import os
import glob
from dotenv import load_dotenv
from textwrap import wrap
from tqdm import tqdm

# Environment Variables
load_dotenv()
EPUB_DIR_PATH = os.getenv('EPUB_DIR_PATH')
TXT_DIR_PATH = os.getenv('TXT_DIR_PATH')
CHUNK_DIR_PATH = os.getenv('CHUNK_DIR_PATH')
CHUNK_LENGTH = int(os.getenv('CHUNK_LENGTH'))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def _get_chunks(input_path, file):
    try:
        with open(os.path.join(input_path, file), "r") as f:
            txt = f.read()
            chunks = wrap(txt, CHUNK_LENGTH)
            f.close()
            return chunks
    except Exception as e:
        logger.error(f"Cannot open files. Error: {e}")


def _write_chunk_files(output_path, file, chunks):
    for index, chunk in enumerate(chunks, start=1):
        try:
            file_name = file.split(".txt")
            with open(os.path.join(output_path, f"{file_name}_{index}.txt"), "w") as f:
                f.write(chunk)
                f.close()
        except Exception as e:
            logger.error(f"Cannot create chunk files. Error: {e}")


def _generate_chunks(input_path, output_path):
    try:
        os.chdir(input_path)
        input_files = [f for f in glob.glob(f"*.txt")]
        for count, file in enumerate(tqdm(input_files), start=1):
            chunks = _get_chunks(input_path, file)
            _write_chunk_files(output_path, file, chunks)
    except Exception as e:
        logger.error(e)


def generate_chunks():
    logger.info(os.getcwd())
    os.chdir(os.getcwd())
    input_path = os.path.join(os.getcwd(), TXT_DIR_PATH)
    output_path = os.path.join(os.getcwd(), CHUNK_DIR_PATH)
    make_dir(output_path)
    _generate_chunks(input_path, output_path)
    return None


if __name__ == "__main__":
    generate_chunks()
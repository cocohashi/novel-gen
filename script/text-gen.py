import os
import logging
import argparse
from dotenv import load_dotenv

from transformers import AutoTokenizer, AutoModel, BloomForCausalLM

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()
MODEL_DIR_NAME = os.getenv('MODEL_DIR_NAME')
MODEL_BLOOM = os.getenv('MODEL_BLOOM')

MAX_NEW_TOKENS = int(os.getenv('MAX_NEW_TOKENS'))
TEMPERATURE = float(os.getenv('TEMPERATURE'))
TOP_P = float(os.getenv('TOP_P'))
MAX_TIME = int(os.getenv('MAX_TIME'))
USE_CACHE = bool(os.getenv('USE_CACHE'))

text_prompt = "Basketball is a team sport in which two teams, most commonly of five players each, "


# Define Argument Parser
def get_args():
    parser = argparse.ArgumentParser(
        description=f""" Text Generation """
    )
    parser.add_argument("--prompt", type=str, help="The input text prompt")
    return parser.parse_args()


if __name__ == "__main__":
    model_path = os.path.join(os.getcwd(), MODEL_DIR_NAME, MODEL_BLOOM)
    logger.info(model_path)
    logger.info(f'Loading {MODEL_BLOOM} model...')
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path)
    model_bloom = BloomForCausalLM.from_pretrained(model_path)
    logger.info("OK!")
    logger.info(f'Input Text Prompt:\n{text_prompt}')
    logger.info("Generating output text...")
    input_ids = tokenizer(text_prompt, return_tensors="pt")
    output_ids = model_bloom.generate(\
        **input_ids,\
        max_new_tokens=MAX_NEW_TOKENS,\
        temperature=TEMPERATURE)
    output = tokenizer.decode(output_ids[0])
    logger.info(f'[OUTPUT]: {output}')



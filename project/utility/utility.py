import re
import os
import pandas as pd

from core.logging import LOGGER

logger = LOGGER.get_logger()


def get_QnA(job_description):
    logger.info(job_description)
    question = "test"
    answer = "answer"
    
    return "test"


def get_data_dir_path():
    base_dir = get_base_path()
    return os.path.join(base_dir, 'resources', 'data')


def get_base_path():
    return os.path.abspath('./')


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

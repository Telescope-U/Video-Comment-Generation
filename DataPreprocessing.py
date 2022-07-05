import os
import numpy as np
import pandas as pd

COMMENT_PATH = 'Dataset/comments.csv'
TRANSCRIPT_FOLDER = "Dataset/Transcripts/"
INFO_PATH = "new_infos.csv"
LOG_ERROR_PATH = "DataCollection/error_log.csv"
LOG_SUCCESS_PATH = "DataCollection/success_log.csv"

comments = pd.read_csv(COMMENT_PATH)
# 处理votes数值转换
def trans_votes(string):
    if isinstance(string, str):
        if 'k' == string[-1].lower():
            return float(string[:-1])*1000
        return float(string)
comments['votes'].fillna('0')
comments['votes'].apply(trans_votes)
print(comments['votes'])
# comments.to_csv(COMMENT_PATH, index=None)


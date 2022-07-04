import os
import numpy as np
import pandas as pd

COMMENT_PATH = 'Dataset/comments.csv'
TRANSCRIPT_FOLDER = "Dataset/Transcripts/"
INFO_PATH = "Dataset/videos.csv"
LOG_ERROR_PATH = "DataCollection/error_log.csv"
LOG_SUCCESS_PATH = "DataCollection/success_log.csv"

# 去除没有获取到comment的video信息
comment_df = pd.read_csv(COMMENT_PATH)
info_df = pd.read_csv(INFO_PATH)

comment_df = comment_df.drop_duplicates()
comment_vid = set(comment_df.vid)
valid_vid = [vid for vid in info_df.vid if vid in comment_vid]
print(info_df.shape)
info_df = info_df[info_df['vid'].isin(valid_vid)]
print(info_df.shape)
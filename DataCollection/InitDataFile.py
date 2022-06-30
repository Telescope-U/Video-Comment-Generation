from config import *
import csv

with open(INFO_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(INFO_HEAD)


with open(COMMENT_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(COMMENT_HEAD)

from config import *
import csv
'''
一定要小心！
'''
with open(INFO_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(INFO_HEAD)


with open(COMMENT_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(COMMENT_HEAD)

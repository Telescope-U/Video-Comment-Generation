from config import *
import csv

with open(INFO_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['vid', 'title', 'duration', 'views'])

# [video_id,comment["id"], comment["content"].strip(), comment["votes"]['simpleText']

with open(COMMENT_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['vid', 'uid', 'content', 'votes'])

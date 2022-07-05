from youtubesearchpython import Transcript, Comments, Video, VideosSearch
import csv
import os
from config import *

def write_csv(path,contents):
    with open(path, 'a')as f:
        writer = csv.writer(f)
        writer.writerows(contents)
    # print(path+' write complete')

def get_video_info(video_link):
    video = Video.get(video_link)
    return video['id'], video['title'].strip(), video['duration']['secondsText'], video['viewCount']['text']

def get_video_transcript(video_id):
    transcript = Transcript.get(video_id)["segments"]
    return [[video_id, segment['startMs'], segment['endMs'], segment['text'].replace('\n', ' ')] for segment in transcript]


def get_video_comments(video_id):
    comments_response = Comments(video_id)
    i = 0
    while i < 3 and comments_response.hasMoreComments:
        comments = comments_response.comments["result"]
        yield [[video_id,comment["id"], comment["content"].strip(), comment["votes"]['simpleText']] for comment in comments]
        comments_response.getNextComments()
        i += 1
def search_video(tag):
    count = 0
    videosSearch = VideosSearch(tag, limit=100)
    results = videosSearch.result()['result']
    while count <= 1500 and len(results) != 0:
        results = videosSearch.result()['result']
        for video in results:
            yield [video['id'], video['title'], tag, video['publishedTime'], video['duration'], video['viewCount']['text'], video['link']]
        count += len(results)
        print(count)
        videosSearch.next()

def log(path, *msg):
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(msg)

# video_link ='https://www.youtube.com/watch?v=ZVYqB0uTKlE'
# video_info = get_video_info(video_link)
# video_id = video_info[0]
# write_csv(INFO_PATH, [video_info])
# for comments in get_video_comments(video_id):
#     write_csv(COMMENT_PATH, comments)
# transcript = get_video_transcript(video_id)
# transcript.insert(0, TRANSCRIPT_HEAD)
# write_csv(os.path.join(TRANSCRIPT_FOLDER, video_id+'.csv'), transcript)

# for tag in KEYWORDS:
#     write_csv(INFO_PATH, search_video(tag))

# import pandas as pd
# videos = pd.read_csv(INFO_PATH)
# for index, video in videos.iterrows():
#     video_id = video.loc['vid']
#     print(index, video_id, video['link'])
#     try:
#         for comments in get_video_comments(video_id):
#             write_csv(COMMENT_PATH, comments)
#         log(LOG_SUCCESS_PATH,'comment',video_id)
#     except:
#         log(LOG_ERROR_PATH, 'comment', video_id)
#     try:
#         transcript = get_video_transcript(video_id)
#         transcript.insert(0, TRANSCRIPT_HEAD)
#         write_csv(os.path.join(TRANSCRIPT_FOLDER, video_id+'.csv'), transcript)
#         log(LOG_SUCCESS_PATH,'transcript', video_id)
#     except:
#         log(LOG_ERROR_PATH, "transcript", video_id)
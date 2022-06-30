from youtubesearchpython import Transcript, Comments, Video
import csv
import os

COMMENT_PATH = 'Dataset/comments.csv'
TRANSCRIPT_FOLDER = "Dataset/Transcripts/"
INFO_PATH = "Dataset/videos.csv"

def write_csv(path,contents):
    with open(path, 'a')as f:
        writer = csv.writer(f)
        writer.writerows(contents)
    print(path+' write complete')

def get_video_info(video_link):
    video = Video.get(video_link)
    # print(video)
    return video['id'], video['title'].strip(), video['duration']['secondsText'], video['viewCount']['text']



def get_video_transcript(video_id):
    transcript = Transcript.get(video_id)["segments"]
    return [[segment['startMs'], segment['endMs'], segment['text'].replace('\n', ' ')] for segment in transcript]

def get_video_comments(video_id):
    comments_response = Comments(video_id)
    i = 0
    while i < 3 and comments_response.hasMoreComments:
        comments = comments_response.comments["result"]
        yield [[video_id,comment["id"], comment["content"].strip(), comment["votes"]['simpleText']] for comment in comments]
        comments_response.getNextComments()
        i += 1

video_link ='https://www.youtube.com/watch?v=ZVYqB0uTKlE'
video_info = get_video_info(video_link)
video_id = video_info[0]
write_csv(INFO_PATH, [video_info])
for comments in get_video_comments(video_id):
    write_csv(COMMENT_PATH, comments)
write_csv(os.path.join(TRANSCRIPT_FOLDER, video_id+'.csv'), get_video_transcript(video_id))


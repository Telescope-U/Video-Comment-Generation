COMMENT_PATH = '../Dataset/comments.csv'
TRANSCRIPT_FOLDER = "../Dataset/Transcripts/"
INFO_PATH = "../Dataset/videos.csv"
LOG_ERROR_PATH = "error_log.csv"
LOG_SUCCESS_PATH = "success_log.csv"

TRANSCRIPT_HEAD = ('vid','start', "end", "text")
INFO_HEAD = ('vid', 'title','tag','time','duration', 'views','link')
COMMENT_HEAD = ('vid', 'uid', 'content', 'votes')

KEYWORDS = ('News', 'Sport','Food', 'Game', 'Fashion', 'Entertainment', 'Tech', 'Education', 'Motivation', 'Vlog', 'Art', 'Music')
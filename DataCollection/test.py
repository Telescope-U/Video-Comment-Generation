from youtubesearchpython import VideosSearch
tag = 'News'
videosSearch = VideosSearch(tag, limit = 100)
for video in videosSearch.result()['result']:
    print(video['id'], video['title'], tag, video['publishedTime'], video['duration'], video['viewCount']['text'], video['link'])
    # for _ in video:
    #     print(_)
    #     print(video[_])
    #     print('-'*50)
    # break
# print(videosSearch.result())
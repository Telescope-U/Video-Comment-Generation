from youtubesearchpython import VideosSearch
tag = 'News'
videosSearch = VideosSearch(tag, limit = 100)
count = 0
while count <= 1500:
    results = videosSearch.result()['result']
    # for video in results:
    #     print(video['id'], video['title'], tag, video['publishedTime'], video['duration'], video['viewCount']['text'], video['link'])
    count += len(results)
    print(count)
    videosSearch.next()
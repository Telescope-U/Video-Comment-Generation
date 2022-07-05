from YoutubeChannelsSelection import *
import pandas as pd
'''确保收集的transcript都是英文的'''
for path in os.listdir(TRANSCRIPT_FOLDER):
    vid = path.split('.')[0]
    print('-' * 50)
    print('vid: ', vid)
    try:
        transcript = Transcript.get(vid)
        languages = pd.DataFrame.from_dict(transcript['languages'])
        if languages.empty:
            continue
        print(languages)
        selected_language = languages[languages['selected'] == True]
        print('selected_language:   ',selected_language['title'].item())
        if 'English' not in selected_language['title'].item():
            # para = languages[languages['title'] == "English"]['params']
            # print('para:    ', para)
            # if not para.empty:
            #     para = para.item()
            #     print('*** recatch: {} **'.format(para))
            #     transcript = Transcript.get(vid, para)
            # else:
            #     print('no English Transcript Available')
            pass
        else:
            transcript = transcript['segments']
            transcript = [[vid, segment['startMs'], segment['endMs'], segment['text'].replace('\n', ' ')] for segment in transcript]

            transcript.insert(0, TRANSCRIPT_HEAD)
            write_csv(os.path.join('Transcripts', vid+'.csv'), transcript)
            log(LOG_SUCCESS_PATH,'transcript', vid)
            print('Success!')
    except:
        log(LOG_ERROR_PATH, "transcript", vid)
        print("Failed!")
    print('-' * 50)
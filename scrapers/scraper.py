##automated data scraping

#pip3 install youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
from nltk import word_tokenize, pos_tag

jump_word = ['then', 'and', 'therefore', 'further more', 'which', 'because', 'but']

raw = YouTubeTranscriptApi.get_transcript("Bf0XcgzsPig")
data = []
for i in raw:
    temp = [i['text'].replace('\n', ' '), i['start'], i['duration']]
    data.append(temp)
# for i in data:
#     print(i)

jokes = []
for i in data:
    if 'Laughter' in i[0]:
        jokes.append(data[data.index(i) - 1][0].lower())
        # temp_tokenized = data[data.index(i) - 1][0].lower()
        # temp_tokenized = word_tokenize(data[data.index(i) - 1][0])
        # print(temp_tokenized)
        # counter = 0
        # while temp_tokenized[counter] not in ['``', 
        for j in range(data.index(i) - 2, 0, -1):
            cont = False
            if data[j + 1][0].startswith('-'):
                cont = True
            if data[j][0].endswith('.') and not cont:
                break
            else:
                jokes[len(jokes) - 1] = (data[j][0] + ' ' + jokes[len(jokes) - 1]).lower()

print('\n')
for i in jokes:
    print(i)

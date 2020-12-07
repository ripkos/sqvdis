import requests
import re
import random
import nltk


mainurl = 'https://streamcraft.net/api/forum/category/SurvivalMG3'
discurl = 'https://streamcraft.net/api/forum/discussion/'
file = open('./res/trash.txt', "r", encoding="utf8")
filecontent = file.readlines()
filesize = len(filecontent) - 1


def parse(type):
    allt = []
    # nltk.download('punkt')
    username = 'Morginallinez'
    # 1.
    cv = '1. ' + username + '\n'
    response = requests.get(mainurl + '?page=1')
    if response:
        response = response.json()
        for i in range(0, 9):
            if response['discussions']['data'][i]['slug'] != 'forma-podachi-zayavki-v-personal':
                disc = requests.get(discurl + response['discussions']['data'][i]['slug'])
                if disc:
                    disc = disc.json()
                    data = remove_html(disc['posts']['data'][0]['body'])
                    data = data.replace('\n', ' ')
                    allt.append(data)
                else:
                    cv = 'БОТА ЗАБАНИЛИ СЕРЕГА ИЗВИНЯЙСЯ'
                    return cv
        if response['discussions']['total'] > 11:
            pagenums = (response['discussions']['total'] - 1) // 10
            pagerandom = random.randint(2, 2+pagenums)
            response = requests.get(mainurl + '?page=' + str(pagerandom))
            if response:
                response = response.json()
                for i in range(0, 9):
                    if response['discussions']['data'][i]['slug'] != 'forma-podachi-zayavki-v-personal':
                        disc = requests.get(discurl + response['discussions']['data'][i]['slug'])
                        if disc:
                            disc = disc.json()
                            data = remove_html(disc['posts']['data'][0]['body'])
                            data = data.replace('\n', ' ')
                            allt.append(data)
                        else:
                            cv = 'БОТА ЗАБАНИЛИ СЕРЕГА ИЗВИНЯЙСЯ'
                            return cv
            else:
                cv = 'БОТА ЗАБАНИЛИ СЕРЕГА ИЗВИНЯЙСЯ'
                return cv
    else:
        cv = 'БОТА ЗАБАНИЛИ СЕРЕГА ИЗВИНЯЙСЯ'
        return cv

    # 2. - 7.
    curpoint = 2
    while curpoint < 8:
        pattern = '' + str(curpoint) + '\.(.*?)' + str(curpoint + 1) + '\.'
        data = allt[random.randint(0, len(allt)) - 1]
        result = re.search(pattern, data)
        if result:
            cv = cv + str(curpoint) + '.' + result.group(1) + '\n'
            curpoint = curpoint + 1
    # 8.
    pattern = '' + str(curpoint) + '\.(.*?)' + str(curpoint + 1) + '\.'
    cv = cv + '8. '
    sentnum = 0
    wc = 0
    text8 = ''
    settled = []
    sentmax = random.randint(5, 10)
    counter =0
    while sentnum < sentmax or wc < 500 and wc < 1000:
        randnum = random.randint(0, len(allt)) - 1
        while randnum in settled:
            randnum = random.randint(0, len(allt)) - 1
        data = allt[randnum]  # берем рандомную тему тему
        result = re.search(pattern, data)
        found = False
        if result:
            text = result.group(1)
            sentences = nltk.sent_tokenize(text, language="russian")
            # 1 предложение
            if sentnum < 1:
                text8 = text8 + sentences[0] + ' '
                found = True
            # 2 предложение
            else:
                if sentnum < 2:
                    if len(sentences) > 1:
                        text8 = text8 + sentences[1] + ' '
                        found = True
                # 3+ предложение
                else:
                    if type == 1:
                        if len(sentences) > 2:
                            text8 = text8 + sentences[random.randint(0, len(sentences) - 1)] + ' '
                            found = True
                    if type == 2:
                        text8 = text8 + filecontent[random.randint(0, filesize)]
                        found = True
        if found:
            sentnum = sentnum + 1
            wc = len(text8)
            settled.append(randnum)
        counter=counter+1
        if counter > 10:
            settled.clear()


    cv = cv + text8

    # return
    # 9.
    cv = cv + '9. vk.com/' + username + ' , ' + username + '#' + str(random.randint(1000, 9999))

    return cv


def trash():
    text8=''
    sentnum = 0
    sentmax = random.randint(7, 12)
    wc = 0
    while sentnum < sentmax or wc < 600 and wc < 1400:
        text8 = text8 + filecontent[random.randint(0, filesize)]
        sentnum = sentnum + 1
        wc = len(text8)
    return text8


def remove_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

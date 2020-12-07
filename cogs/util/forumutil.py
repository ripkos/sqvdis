import requests
from cogs.util.util import tweak_text, remove_underscore
from cogs.util.jediutil import remove_html

discurl = 'https://streamcraft.net/api/forum/discussion/'
forumurl = 'https://streamcraft.net/forum/discussion/'
categoryapi = 'https://streamcraft.net/api/forum/category/'
exceptionslug = ['platnyy-razban-v-vkdiscord-servere']

"""
def parseforum(url):
    reply = []
    # парсим категорию
    discslug = []
    extrapages = 0
    response = requests.get(categoryapi + url + '?page=1')
    if response:
        response = response.json()
        extrapages = (response['discussions']['total'] - 1) // 10
        for disc in response['discussions']['data']:
            # ссылки на закрытые темы добавляем в массив
            if disc['no_reply'] == 0:
                discslug.append(disc['slug'])
        # тоже самое только для всего остального
        if extrapages > 0:
            for i in range(2, extrapages + 1):
                response = requests.get(categoryapi + url + '?page=' + str(i))
                if response:
                    response = response.json()
                    extrapages = (response['discussions']['total'] - 1) // 10
                    for disc in response['discussions']['data']:
                        # ссылки на закрытые темы добавляем в массив
                        if disc['no_reply'] == 0:
                            discslug.append(disc['slug'])
                else:
                    # если бота забанили
                    reply.clear()
                    reply.append('Бота забанили')
                    return reply

        # парсим саму ссылку
        for slug in discslug:
            reply.append(parse_disc(slug))
    else:
        # если бота забанили
        reply.clear()
        reply.append('Бота забанили')
        return reply
    return reply
"""


def parse_forum_short(url):
    reply = []
    extrapages = 0
    response = requests.get(categoryapi + url + '?page=1')
    if response is not None:
        response = response.json()
        extrapages = (response['discussions']['total'] - 1) // 10
        for disc in response['discussions']['data']:
            # ссылки на закрытые темы добавляем в массив
            if disc['no_reply'] == 0 and disc['slug'] not in exceptionslug:
                reply.append({
                    'title': disc['title'],
                    'link': forumurl + disc['slug'],
                    'author': disc['user']['login'],
                    'time': disc['updated_at'],
                    'reps': disc['posts_count'][0]['total']
                })
        # тоже самое только для всего остального
        if extrapages > 0:
            for i in range(2, extrapages + 1):
                response = requests.get(categoryapi + url + '?page=' + str(i))
                if response is not None:
                    response = response.json()
                    for disc in response['discussions']['data']:
                        # ссылки на закрытые темы добавляем в массив
                        if disc['no_reply'] == 0 and disc['slug'] not in exceptionslug:
                            reply.append({
                                'title': disc['title'],
                                'link': forumurl + disc['slug'],
                                'author': disc['user']['login'],
                                'time': disc['updated_at'],
                                'reps': disc['posts_count'][0]['total']
                            })
                else:
                    # если бота забанили
                    reply.clear()
                    reply.append('Бота забанили')
                    return reply
    else:
        # если бота забанили
        reply.clear()
        return False
    return reply


def parse_disc(slug):
    reply = []
    response = requests.get(discurl + slug)
    if response is not None:
        response = response.json()
        reply.append({  # собираю базовую инфу о теме
            'title': response['discussion']['title'],  # название темы
            'link': forumurl + slug,  # slug темы
            # 'text': remove_html(response['posts']['data'][0]['body'])[0:1500],
            'topicStarter': response['posts']['data'][0]['user']['login'],  # автор темы темы
            # 'modername': get_moder(response)[0],
            # 'moderrole': get_moder(response)[1],
            'time': response['posts']['data'][0]['created_at']  # время создания темы
        })
        # а тут собираю сами посты
        for post in response['posts']['data']:
            reply.append({
                'author': post['user']['login'],  # post author
                'text': remove_html(post['body'])[0:1500],  # post text
                'pref': remove_html(post['user']['siterole']),  # post author prefix
                'moder': is_moder(remove_html(post['user']['siterole']))  # post author moder?
            })
    else:
        # если бота забанили
        reply.clear()
        reply.append('Бота забанили')
        return reply
    return reply


def is_moder(pref):
    if not (pref == 'Игрок' or pref == 'Legend' or pref == 'VIP' or pref == 'Deluxe' or pref == 'Premium'):
        return True
    else:
        return False


def construct_message(raw: dict, postnum=0):
    modername = ''
    moderrole = ''
    has_moder = False
    postnumstr = str(postnum)
    count = 0
    for data in raw:
        if count != 0:
            if data['moder']:
                has_moder = True
                modername = data['author']
                moderrole = data['pref']
        count = count + 1
    if not has_moder:
        modertext = '> Никто из модерации не ответил на тему '
    else:
        modertext = '<' + moderrole + ' ' + modername + ' ответил(а) в теме, но тема не закрыта>'
    msg = '```md\n' \
          + '#' + remove_underscore(raw[0]['topicStarter']) + '\n' \
                                                              '[' + remove_underscore(raw[0]['title']) + '](' + raw[0][
              'time'] + ')\n' \
                        '(' + postnumstr + ') ' + \
          raw[postnum + 1]['pref'] + ' ' + remove_underscore(raw[postnum + 1]['author']) + ' пишет:\n===\n' \
          + tweak_text(raw[postnum + 1]['text']) + '\n' \
          + remove_underscore(modertext) \
          + '```<' + raw[0]['link'] + '>\n' \
        # + '------------------------------------------'
    return msg


def construct_short(raw):
    msg = '```md\n' \
          '#' + remove_underscore(raw['author']) + '\n' \
                                                   '[' + remove_underscore(raw['title']) + '](' + raw['time'] + ')\n' \
          + str(raw['reps']) + ' ответов в теме\n' \
                               '```<' + raw['link'] + '>\n' \
        # '------------------------------------------'

    return msg

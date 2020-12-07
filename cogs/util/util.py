import re


def get_url_from_msg(msg):
    return re.search("(?P<url>https?://streamcraft[^\s]+)", msg).group("url")


def url_to_api(url):
    pattern = re.compile('https://streamcraft\.net/forum/discussion/')
    url2 = re.sub(pattern, '', url)
    pattern2 = re.compile('>')
    return re.sub(pattern2, '', url2)


def remove_underscore(text):
    pattern = re.compile('_')
    return re.sub(pattern, '', text)


def tweak_text(fulltext):
    pattern1 = re.compile('1\)')
    text1 = re.sub(pattern1, '1. ', fulltext)
    pattern2 = re.compile('2\)')
    text2 = re.sub(pattern2, '2. ', text1)
    pattern3 = re.compile('3\)')
    text3 = re.sub(pattern3, '3. ', text2)
    pattern4 = re.compile('4\)')
    text4 = re.sub(pattern4, '4. ', text3)
    pattern11 = re.compile('^1\.')
    text11 = re.sub(pattern11, '1. ', text4)
    pattern22 = re.compile('^2\.')
    text22 = re.sub(pattern22, '2. ', text11)
    pattern33 = re.compile('^3\.')
    text33 = re.sub(pattern33, '3. ', text22)
    pattern44 = re.compile('^4\.')
    text44 = re.sub(pattern44, '4. ', text33)
    patternspace = re.compile('( ){2,}')
    return remove_underscore(re.sub(patternspace, ' ', text44))

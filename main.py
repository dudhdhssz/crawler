import requests
from lxml import etree

# get post-data
def getData(url):
    r = session.get(url, headers= headers)
    html = etree.HTML(r.text)
    LT = html.xpath('//li/input[@name="lt"]/@value')
    execution = html.xpath('//li/input[@name="execution"]/@value')
    return LT,execution

# login
def login(login_url, data):
    session.post(login_url, data=data, headers= headers)
    r = session.get('http://online.zhihuishu.com/onlineSchool/student/index')
    print(r.text[:-1000])
    return ''

def main():
    username = input('username:')
    password = input('password:')
    url = 'https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/'
    login_url = 'https://passport.zhihuishu.com/login'
    LT,execution = getData(url)
    print(LT,execution)
    data = {
        'lt': LT,
        'execution': execution,
        '_eventId': 'submit',
        'username': username,
        'password': password,
        'clCode': '',
        'clPassword': '',
        'tlCode': '',
        'tlPassword': '',
    }
    login(login_url, data)
    return ''


headers = {
        'Referer': 'https: // passport.zhihuishu.com / login?service = http: // online.zhihuishu.com / onlineSchool /',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 64.0.3282.168Safari / 537.36'
    }

session = requests.session()
main()

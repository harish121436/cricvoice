import pyttsx3
import requests
from bs4 import BeautifulSoup
import time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

print(("""{0}

████████████████████████████████████████
████████████████████████████████████████
███████║║║║║║║║█████████████████████████
██████║║██████║█████████████████████████
█████║██████████████████████████████████
█████║██████████████████████╬╬╬╬╬███████
█████║███████╬█╬╬╬╬██║██╬╬╬█╬███████████
█████║██╬╬███╬█╬██╬██║██╬███╬║║║║███████
█████║███╬╬█╬╬█╬╬╬╬██║██╬╬╬█╬███████████
█████║████╬╬╬███████████████║███████████
█████║██████████████████████║║║║║███████
█████║██████████████████████████████████
██████║║██████║║████████████████████████
███████║║║║║║║║█████████████████████████
████████████████████████████████████████
████████████████████████████████████████


{1}""").format(WHITE,END))

print('\nNote : Enter Live Cricket Score, Commentary Tab URL\n')
url=input("enter url : ")
overs=float(input('overs : '))
while(True):
    try:
        cookies = {
            '__cfduid': 'db4be30c5e0a6bdfe3c7677d2a33217151513155987',
            'cbzads': 'IN|AS|02|Hyderabad',
            'cb_config': '%7B%7D',
            '_ga': 'GA1.2.1579167722.1513155988',
            '_gid': 'GA1.2.1737439608.1513155988',
            '_col_uuid': '105d986e-e222-481c-8778-b3ab127e2f41-10oa0~1',
            'RT': 'r=http%3A%2F%2Fwww.cricbuzz.com%2Flive-cricket-scores%2F19194%2Find-vs-sl-2nd-odi-sri-lanka-tour-of-india-2017&ul=1513156305420',
            '__gads': 'ID=726d03d9d7470bd5:T=1513155990:S=ALNI_MbsQaosk_4SGCSPSc1tXVlbbrHF7Q',
            'G_ENABLED_IDPS': 'google',
        }

        headers = {
            'Host': 'www.cricbuzz.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'http://www.cricbuzz.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
        engine = pyttsx3.init()
        res=requests.get(url, headers=headers, cookies=cookies,timeout=(120,180))
        soup=BeautifulSoup(res.text,'html.parser')
        # print(soup.prettify())
        # a=soup.findAll('div':{'class':'cb-min-bat-rw'})
        a=soup.find_all('div', { "class" : 'cb-min-bat-rw'})
        b=soup.find_all('div', {'class':"cb-col cb-col-10 ab text-right"})
        b1=soup.findAll('a',{'class':'cb-text-link'})
        scores=[]
        players=[]
        for j in b:
            scores.append(j.text)
        for i in b1:
            players.append(i.text)
        score=a[0].find('span').text
        print(score)
        score=score.replace('Ovs)','overs').replace('(','').replace('/',' per ')
        split_score=score.split()
        # print(split_score)
        score_voice="team "+split_score[0]+" scored "+split_score[1]+" runs  with loss of "+split_score[3]+" wickets in  "+split_score[4]+" overs"
        engine.setProperty('voice', 'english-us')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-75)
        engine.say(score_voice)
        spl=score.split()
        if(spl[4]==str(overs)):
            exit(0)
        else:
            if(len(scores) is 2):
                print(players[0],scores[0],"runs in ",scores[1],"balls")
                one=players[0],scores[0],"runs in ",scores[1],"balls"
                engine.say(one)
                engine.runAndWait()
            else:
                print(players[0],scores[0],"runs in ",scores[1],"balls")
                one=players[0],scores[0],"runs in ",scores[1],"balls"
                engine.say(one)
                print(players[1],scores[2],"runs in ",scores[3],"balls")
                two=players[1],scores[2],"runs in ",scores[3],"balls"
                engine.say(two)
                engine.runAndWait()
            time.sleep(30)
    except Exception as e:
        print(e)
        engine.say(e)
        engine.runAndWait()
        exit(0)

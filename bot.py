import discord
import os
import pyowm
import requests
import asyncio
import datetime
import calendar
import time
from selenium import webdriver
from parser import *
from bs4 import BeautifulSoup
client = discord.Client()



#호스팅 서버가 미국에 있기 때문에 9시간을 추가 해준다

#################
def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def get_diet(ymd,weekday):   #동원중
    schYmd = ymd
    num = weekday + 1
    URL =("https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=%s"%schYmd) 
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("tr")
    site = site[2].find_all('td')
    try:
        site = site[num]
        site = str(site)
        site = site.replace('[', '')
        site = site.replace(']', '')
        site = site.replace('<br/>', '\n')
        site = site.replace('<td class="textC last">', '')
        site = site.replace('<td class="textC">', '')
        site = site.replace('</td>', '')
        site = site.replace('amp;', '')
    except:
        site = " "
    return site

def get_diet_bong(ymd,weekday):
    schYmd = ymd
    num = weekday + 1
    URL =("https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001371&schulCrseScCode=3&schulKndScCode=03&schYmd=%s"%schYmd) 
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("tr")
    site = site[2].find_all('td')
    try:
        site = site[num]
        site = str(site)
        site = site.replace('[', '')
        site = site.replace(']', '')
        site = site.replace('<br/>', '\n')
        site = site.replace('<td class="textC last">', '')
        site = site.replace('<td class="textC">', '')
        site = site.replace('</td>', '')
        site = site.replace('amp;', '')
    except:
        site = " "
    return site


def get_diet_both_dong_and_bong():
    today = datetime.datetime.today()  + datetime.timedelta(hours=9)
    local_date2 = today.strftime("%Y.%m.%d")
    local_weekday2 = today.weekday() + 1
    URL =("https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=%s"%local_date2) 
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("tr")
    site = site[2].find_all('td')
    try:
        site = site[local_weekday2]
        site = str(site)
        site = site.replace('[', '')
        site = site.replace(']', '')
        site = site.replace('<br/>', '\n')
        site = site.replace('<td class="textC last">', '')
        site = site.replace('<td class="textC">', '')
        site = site.replace('</td>', '')
        site = site.replace('amp;', '')
    except:
        site = " "         ####동원###여기까찌


    URL =("https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001371&schulCrseScCode=3&schulKndScCode=03&schYmd=%s"%local_date2)
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    site1 = soup.find_all("tr")
    site1 = site1[2].find_all('td')
    try:
        site1 = site1[local_weekday2]
        site1 = str(site1)
        site1 = site1.replace('[', '')
        site1 = site1.replace(']', '')
        site1 = site1.replace('<br/>', '\n')
        site1 = site1.replace('<td class="textC last">', '')
        site1 = site1.replace('<td class="textC">', '')
        site1 = site1.replace('</td>', '')
        site1 = site1.replace('amp;', '')
    except:
        site1 = " "
                #####여기까지 봉화#####


    if site == " " and site1 == " ":
        a = ["오늘은 동원중\n급식이 없어요","오늘은 봉화중\n급식이 없어요"]
    elif site != " " and site1 == " ":
        a = ['오늘 동원중 급식\n\n'+site,"오늘은 봉화중\n급식이 없습니다."]
        
    elif site == " " and site1 != " ":
        a = ['오늘은 동원중\n급식이 없습니다.','오늘 봉화중 급식\n\n'+site1]
    else:
        a = ["오늘 동원중 급식\n\n"+site,"오늘 봉화중 급식\n\n"+site1]
    return a
    


def get_lol_solo_info(name):
    URL = ("https://poro.gg/ko/s/KR/%s"%name)
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("div")
    site = site[355]
    site1 = site.find_all("b")
    site1 = str(site1)
    site1 = site1[site1.find('">')+2:site1.find('</b>')]
    site2 = site.find_all('span')
    site2 = str(site2)
    site2 = site2[site2.find('">')+2:site2.find("LP")+2]
    ls = [site2,site1]
    if  "Unranked" in ls[1] :
        st = "언랭이라서 전적이 안나와요 ㅠㅠ"
    else:
        st = "솔랭티어 : "+ls[1].upper()+"\n리그 포인트 : "+ls[0]
    return st


def get_lol_free_info(name):
    URL = ("https://poro.gg/ko/s/KR/%s"%name)
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("div")
    site = site[365]
    site1 = site.find_all("b")
    site1 = str(site1)
    site1 = site1[site1.find('">')+2:site1.find('</b>')]
    site2 = site.find_all('span')
    site2 = str(site2).replace('<span>자유랭크 5x5</span>, ','')
    site2 = str(site2)
    site2 = site2[site2.find('">')+2:site2.find("LP")+2]
    ls = [site2,site1]
    site = str(site)
    if  not('<b class="summoner__tier' in site):
        st = "언랭이라서 전적이 안나와요 ㅠㅠ"
    else:
        st = "자랭티어 : "+ls[1].upper()+"\n리그 포인트 : "+ls[0]
    return st


def han_river():
    URL = ("https://www.wpws.kr/hangang/")
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')

    site = soup.find_all('p')
    site = site[2]
    site = str(site)
    site = site.replace('<p id="temp"><i class="xi-tint"></i>','')
    site = site.replace('</p>','')

    return site

def lyrics(name):
    driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    driver.implicitly_wait(1)
    driver.get(f'https://www.google.com/search?ei=9752XqiLJsPM-Qb3gJnAAw&q={name}&oq={name}&gs_l=psy-ab.3..0i67j0l9.141825.145579..145667...2.0..1.167.1383.1j11......0....1..gws-wiz.....0..0i30j0i131.Q_BCYuzKfQ0&ved=0ahUKEwjo4rfb9qzoAhVDZt4KHXdABjgQ4dUDCAs&uact=5')
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    site = soup.select('div.ujudUb')
    site = site[1:]
    site = str(site)
    site = site.replace('[','')
    site = site.replace(']','')
    site = site.replace('<div class="ujudUb WRZytc" jsname="U8S5sf">','')
    site = site.replace('<span jsname="YS01Ge">','')
    site = site.replace('</br>','')
    site = site.replace('</span><br','')
    site = site.replace('</span></div>','')
    site = site.replace('<div class="ujudUb" jsname="U8S5sf">','')
    site = str(site)
    site_ls = site.split(">")
    st = ''
    for i in range(len(site_ls)):
        st += site_ls[i]+"\n"
    return st



def Collona():
    url = 'http://ncov.mohw.go.kr/'
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    site = soup.find_all('span','num')
    site = site[:4]
    site = str(site).replace('[','')
    site = site.replace(']','')
    site = site.replace('<span class="num">','')
    site = site.replace('<span class="mini">(누적)','')
    site = site.replace('</span>','')
    site = site.replace(',','')
    site = site.split(' ')
    site1 = soup.select('span.before')

    site1 = site1[:4]
    site1 = str(site1).replace('<span class="before">','')
    site1 = site1.replace('</span>','')
    site1 = site1.replace('전일대비 ','')
    site1 = site1.replace('[','')
    site1 = site1.replace(']','')
    site1 = site1.split(',')
    for i in range(len(site1)):
        site1[i] = str(site1[i]).strip()

    site.extend(site1)
    st = "확진자   : "+site[0]+" "+site[4]+"\n완치     : "+site[1]+"  "+site[5]+"\n치료환자 : "+site[2]+"  "+site[6]+"\n사망자   : "+site[3]+"   "+site[7]
    return st



def lyrics(name):
    driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    driver.implicitly_wait(1) 
    driver.get(f'https://www.google.com/search?ei=9752XqiLJsPM-Qb3gJnAAw&q={name}&oq={name}&gs_l=psy-ab.3..0i67j0l9.141825.145579..145667...2.0..1.167.1383.1j11......0....1..gws-wiz.....0..0i30j0i131.Q_BCYuzKfQ0&ved=0ahUKEwjo4rfb9qzoAhVDZt4KHXdABjgQ4dUDCAs&uact=5')
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    site = soup.select('div.ujudUb')
    site = site[1:]
    site = str(site)
    site = site.replace('[','')
    site = site.replace(']','')
    site = site.replace('<div class="ujudUb WRZytc" jsname="U8S5sf">','')
    site = site.replace('<span jsname="YS01Ge">','')
    site = site.replace('</br>','')
    site = site.replace('</span><br','')
    site = site.replace('</span></div>','')
    site = site.replace('<div class="ujudUb" jsname="U8S5sf">','')
    site = str(site)
    site_ls = site.split(">")
    st = ''
    for i in range(len(site_ls)):
        st += site_ls[i]+"\n"
    return st




def live_search():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    site = soup.select('span.item_title')
    site = str(site)
    site = site.replace('[','')
    site = site.replace(']','')
    site = site.replace('<span class="item_title">','')
    site = site.replace('/span>, ','')
    site_ls = site.split('<')
    st = ''
    for i in range(20):
        st += str(i+1)+"위 : "+site_ls[i]+"\n"
    return st





def Change(a):
    a = str(a)
    if a == "01":
        a = a.replace("0","")
    if a == "02":
        a = a.replace("0","")
    if a == '03':
        a = a.replace("0","")
    if a == '04':
        a = a.replace("0","")
    if a == '05':
        a = a.replace("0","")
    if a == '06':
        a = a.replace("0","")
    if a == '07':
        a = a.replace("0","")
    if a == '08':
        a = a.replace("0","")
    if a == '09':
        a = a.replace("0","")
    a = int(a)
    return a
############

# API_Key = '52a192d87186e871d8ad7c1300c3730d'
# owm = pyowm.OWM(API_Key)
 
# City_ID = 1835848
# obs = owm.weather_at_id(City_ID)    
 
# # get_location은 지역에 대한 정보를 가져 옵니다.
# L = obs.get_location()
# City_name = L.get_name()




 





#############################경고경고경고 명령어#############################################################################
print("안녕")


####
ii = 1
i = 0
############################################
baseURL = 'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=2020.03.12'


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("저는 히공의 디스코드 봇")
    await client.change_presence(status=discord.Status.online, activity=game)





@client.event
async def on_message(message):
    # print("하이")
    if message.content.startswith("/날씨"):
    # get_weather는 기상정보에 대한 정보를 가져옵니다.
        W = obs.get_weather()
        Temp = W.get_temperature(unit='celsius')

        a = City_name + '의 최고기온은 ' + str(Temp['temp_max']) + ' 도 입니다.\n'
        b = City_name + '의 최저기온은 ' + str(Temp['temp_min']) + ' 도 입니다.\n'
        c = City_name + '의 현재기온은 ' + str(Temp['temp']) + ' 도 입니다.\n'
 
        Status = W.get_status()
        d = City_name + '의 현재날씨는 ' + Status + ' 입니다.'
        aa = a+b+c+d
        embed = discord.Embed(title="날씨", description=aa, color=0x00ff00)
        await message.channel.send(embed=embed)





    if message.content.startswith("/dm"):
        if message.author.name == "히공":
            author = message.guild.get_member(int(message.content[4:22]))
            msg = message.content[23:]
            await author.send(msg)
        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')


    if message.content.startswith("/조용히"):
        if message.author.name == "히공":
            author = message.guild.get_member(int(message.content[5:23]))
            role = discord.utils.get(message.guild.roles, name="조용")
            await author.add_roles(role)
        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')


    if message.content.startswith("/언조용히"):
        if message.author.name == "히공":
            author = message.guild.get_member(int(message.content[6:24]))
            role = discord.utils.get(message.guild.roles, name="조용")
            await author.remove_roles(role)
        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.') 
    

##schulcode = B100001369, schulCrseScCode = 3, schulKndScCode = 03
#https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=2020.03.12



    if message.content.startswith('/날짜'):
        today = datetime.datetime.today() + datetime.timedelta(hours=9)
        today = str(today)
        tommorow = str(datetime.datetime.today() + datetime.timedelta(hours=9) + datetime.timedelta(days=1))
        embed = discord.Embed(title="날짜", description="오늘 날짜\n\n"+today+'\n\n\n'+"내일 날짜\n\n"+tommorow, color=0x00ff00)
        await message.channel.send(embed=embed)




    if message.content.startswith('/동원중 급식'):
        today = datetime.datetime.today() + datetime.timedelta(hours=9)
        local_date2 = today.strftime("%Y.%m.%d")
        local_weekday2 = today.weekday()
        

        l_diet = get_diet(local_date2, local_weekday2)    
        lunch = local_date2 + "   오늘 동원중 급식 \n\n" + l_diet + "\n\n\n"   
        if l_diet == " ":
            st = "오늘은 급식이 없어요"
        else:
            st = lunch


        tommorw = datetime.datetime.today() + datetime.timedelta(hours=9) + datetime.timedelta(days=1)    
        local_date2 = tommorw.strftime("%Y.%m.%d")  
        local_weekday2 = tommorw.weekday()


        l_diet = get_diet(local_date2, local_weekday2)    
        lunch = "\n\n"+ local_date2 + "   내일 동원중 급식 \n\n" + l_diet    
        if l_diet == " ":
            sst = "내일은 급식이 없어요"
        else: 
            sst = lunch


        embed = discord.Embed(title="동원중 급식", description="", color=0x00ff00)
        embed.add_field(name='오늘 급식', value=st, inline=True)
        embed.add_field(name='내일 급식', value=sst, inline=True)
        await message.channel.send(embed=embed)
            



    if message.content.startswith('/봉화중 급식'):
        today = datetime.datetime.today() + datetime.timedelta(hours=9)
        local_date2 = today.strftime("%Y.%m.%d")
        local_weekday2 = today.weekday()
        

        l_diet = get_diet_bong(local_date2, local_weekday2)    
        lunch = local_date2 + "   오늘 봉화중 급식  \n\n" + l_diet + "\n\n\n"
        if l_diet == " ":
            st = '오늘은 급식이 없어요'
        else:
            st = lunch  


        tommorw = datetime.datetime.today() + datetime.timedelta(days=1) + datetime.timedelta(hours=9)
        local_date2 = tommorw.strftime("%Y.%m.%d")
        local_weekday2 = tommorw.weekday()

        l_diet = get_diet_bong(local_date2, local_weekday2)    
        lunch = "\n\n"+ local_date2 + "   내일 봉화중 급식 \n\n" + l_diet    
        if l_diet == " ":
            sst = "내일은 급식이 없어요"
        else: 
            sst = lunch
        embed = discord.Embed(title="봉화중 급식", description="", color=0x00ff00)
        embed.add_field(name='오늘 급식', value=st, inline=True)
        embed.add_field(name='내일 급식', value=sst, inline=True)
        await message.channel.send(embed=embed)




    if message.content.startswith('/급식 봉화중 날짜 '):
        year = message.content[11:15]
        month = message.content[16:18]
        month2 = month
        day = message.content[19:21]
        month = Change(month)
        date2 = year+"."+month2+"."+day
        _weekday = calendar.weekday(int(year),int(month),int(day)) 
        lunch = "\n\n" + date2 + "의 봉화중 급식 \n\n"+get_diet_bong(date2,_weekday)
        if get_diet_bong(date2,_weekday) == " ":
            embed = discord.Embed(title="급식", description="그날은 급식이 없어요 ㅠㅠㅠ", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="급식", description=lunch, color=0x00ff00)
            await message.channel.send(embed=embed)


    elif message.content.startswith('/급식 동원중 날짜 '):
        year = message.content[11:15]
        month = message.content[16:18]
        month2 = month
        day = message.content[19:21]
        month = Change(month)
        date2 = year+"."+month2+"."+day
        _weekday = calendar.weekday(int(year),int(month),int(day)) 
        lunch = "\n\n" + date2 + "의 동원중 급식 \n\n"+get_diet(date2,_weekday)
        if get_diet(date2,_weekday) == " ":
            embed = discord.Embed(title="급식", description="그날은 급식이 없어요 ㅠㅠㅠ", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="급식", description=lunch, color=0x00ff00)
            await message.channel.send(embed=embed)




    elif message.content.startswith('/급식'):
        a = get_diet_both_dong_and_bong()
        today = datetime.datetime.today() + datetime.timedelta(hours=9)
        local_date2 = today.strftime("%Y.%m.%d")
        embed = discord.Embed(title=local_date2+"의 급식", description="", color=0x00ff00)
        embed.add_field(name='동원중 급식', value=a[0], inline=True)
        embed.add_field(name='봉화중 급식', value=a[1], inline=True)
        await message.channel.send(embed=embed)


    if message.content.startswith('/롤 솔랭 전적'):
        name = message.content[9:]
        st = get_lol_solo_info(name)
        sst = ''
        embed = discord.Embed(title="롤 전적", description=st, color=0x00ff00)
        if "IRON" in st:
            sst = "\n\n사람샛기 신가요?"
        embed = discord.Embed(title="롤 전적", description=st+sst, color=0x00ff00)
        await message.channel.send(embed=embed)
            

    elif message.content.startswith('/롤 자랭 전적'):
        name = message.content[9:]
        st = get_lol_free_info(name)
        embed = discord.Embed(title="롤 전적", description=st, color=0x00ff00)
        sst = ''
        if "IRON" in st:
            sst = '\n\n사람샛기 신가요?'
        embed = discord.Embed(title="롤 전적", description=st+sst, color=0x00ff00)
        await message.channel.send(embed=embed)


    elif message.content.startswith('/롤 전적'):
        name = message.content[6:]
        st = get_lol_solo_info(name)
        sst = get_lol_free_info(name)
        embed = discord.Embed(title="롤 전적", description="", color=0x00ff00)
        embed.add_field(name="솔랭", value=st, inline=True)
        embed.add_field(name="자랭", value=sst, inline=True)
        await message.channel.send(embed=embed)






    if message.content.startswith('/코로나'):
        a = Collona()
        embed = discord.Embed(title="코로나", description=a, color=0x00ff00)
        await message.channel.send(embed=embed)






    if message.content.startswith('/파일만들기') or message.content.startswith('/파일만드기'):
        f = open('경고.txt','w',encoding='utf-8')
        f.close()
        embed = discord.Embed(title="파일만들기", description="파일을 만들었습니다.", color=0x00ff00)
        await message.channel.send(embed=embed)






    if message.content.startswith('/경고 확인') or message.content.startswith('/경고확인'):
        f = open('경고.txt','r',encoding='utf-8')
        readfile = f.read()
        embed = discord.Embed(title="경고 확인", description=readfile, color=0x00ff00)
        await message.channel.send(embed=embed)
            




    elif message.content.startswith('/경고 삭제') or message.content.startswith('/경고삭제'):
        if message.author.name == "히공":
            name = message.content[7:]
            f = open('경고.txt','r',encoding='utf-8')
            readfile = f.read()
            f.close()
            if name in readfile:
                f = open('경고.txt','a',encoding='utf-8')
                find_num = readfile[readfile.rfind(name)+len(name):readfile.rfind(name)+len(name)+4]
                find_num = find_num.replace(' ','')
                find_num = find_num.replace('\n','')
                find_num = find_num.replace('\\','')
                find_num = int(find_num) - 1
                find_num = str(find_num)
                f.write("\n"+name+" "+find_num+"         ")
                f.close()
                f = open('경고.txt','r',encoding='utf-8')
                readfile = f.read()
                f.close()
                find_num = int(find_num)
                find_num = find_num + 1
                find_num = str(find_num)
                readfile = readfile.replace('\n'+name+" "+find_num+"         ",'')
                readfile = readfile.replace(name+" "+find_num+"         ",'')
                f = open('경고.txt','w',encoding='utf-8')
                f.write(readfile)
                f.close()
                find_num = int(find_num) - 1
                find_num = str(find_num)
                if find_num == "0":
                    f = open('경고.txt','r',encoding='utf-8')
                    readfile = f.read()
                    f.close()
                    find_num = readfile[readfile.rfind(name)+len(name):readfile.rfind(name)+len(name)+4]
                    find_num = find_num.replace(' ','')
                    find_num = find_num.replace('\n','')
                    find_num = find_num.replace('\\','')
                    readfile = readfile.replace('\n'+name+" "+find_num+"         ",'')
                    readfile = readfile.replace(name+" "+find_num+"         ",'')
                    f = open('경고.txt','w',encoding='utf-8')
                    f.write(readfile)
                    f.close()
                    embed = discord.Embed(title="경고 삭제", description=name+"님의 경고를 1회 삭제했습니다.\n"+name+"님은 이제 경고가 없습니다.", color=0x00ff00)
                    await message.channel.send(embed=embed)

                else:
                    embed = discord.Embed(title="경고 삭제", description=name+"님의 경고를 1회 삭제했습니다.\n총 경고 : "+find_num+"회 입니다.", color=0x00ff00)
                    await message.channel.send(embed=embed)
            

            else:
                embed = discord.Embed(title="경고 삭제", description=name+"님은 경고를 받은적이 없습니다.", color=0x00ff00)
                await message.channel.send(embed=embed)

        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')


    elif message.content.startswith('/전체 경고 삭제'):
        if message.author.name == "히공":
            st = ""
            f = open('경고.txt','w')
            f.write(st)
            f.close
            embed = discord.Embed(title="전체 경고 삭제", description="경고를 전체 삭제 했습니다.", color=0x00ff00)
            await message.channel.send(embed=embed)


    elif message.content.startswith('/경고'):
        if message.author.name == "히공":
            name = message.content[4:]
            f = open('경고.txt','r',encoding='utf-8')
            readfile = f.read()
            f.close()
            if name in readfile:
                f = open('경고.txt','a',encoding='utf-8')
                find_num = readfile[readfile.rfind(name)+len(name):readfile.rfind(name)+len(name)+4]
                find_num = find_num.replace(' ','')
                find_num = find_num.replace('\n','')
                find_num = find_num.replace('\\','')
                find_num = int(find_num) + 1
                find_num = str(find_num)
                f.write("\n"+name+" "+find_num+"         ")
                f.close()
                f = open('경고.txt','r',encoding='utf-8')
                readfile = f.read()
                f.close()
                readfile = readfile.replace(name+" "+"1"+"         ",'')
                for i in  range(int(find_num)):
                    readfile = readfile.replace("\n"+name+" "+str(i)+"         ",'')
                    f = open('경고.txt','w',encoding='utf-8')
                    f.write(readfile)
                    f.close()
                embed = discord.Embed(title="경고", description=name+"님의 경고는 총 "+find_num+"회 입니다.", color=0x00ff00)
                await message.channel.send(embed=embed)

            else:
                f = open('경고.txt','a',encoding='utf-8')
                f.write("\n"+name+" 1"+"              ")
                f.close()
                embed = discord.Embed(title="경고", description=name+"님의 경고는 총 1회 입니다.", color=0x00ff00)
                await message.channel.send(embed=embed)

        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')




    if message.content.startswith("/도움말"):
        a = '관리자 명령어\n'
        b = '/dm : 사용자에게 dm을 보냅니다.\n\n'
        e = '/파일만들기 : 경고.txt 파일을 만듭니다.\n\n'
        f = '/경고 : 사용자에게 경고를 부여합니다.\n\n'
        g = '/경고 삭제 : 사용자의 경고를 1회 삭제합니다.\n\n'
        h = '/경고 확인 : 사용자들의 경고를 확인합니다.\n\n/전체 경고 삭제 : 사용자들의 경고를 다 삭제합니다.\n\n'
        st = b+c+d+e+f+g+h
        aa = '일반 사용자 명령어'
        b = '/날짜 : 현재 날짜, 내일 날짜를 알려줍니다.\n\n'
        c = '/날씨 : 날씨를 알려줍니다.(정확하지않음)\n\n'
        d = '/동원중 급식 : 동원중의 오늘과 내일 급식을 알려줍니다.\n\n'
        e = '/봉화중 급식 : 봉화중의 오늘과 내일 급식을 알려줍니다.\n\n'
        f = '/급식 동원중 날짜 : 입력한 날짜의 동원중 급식을 알려줍니다.\n\n/급식 봉화중 날짜 : 입력한 날짜의 봉화중 급식을 알려줍니다.\n\n'
        g = '/급식 : 동원중과 봉화중의 오늘 급식을 알려줍니다.\n\n'
        h = '/롤 솔랭 전적 : 입력한 닉네임의 롤 솔랭 전적을 알려줍니다.\n\n/롤 자랭 전적 : 입력한 닉네임의 롤 자랭 전적을 알려줍니다.\n\n'
        i = '/롤 전적 : 입력한 닉네임의 솔랭,자랭 전적을 알려줍니다.'
        sst = b+e+f+g+h+i
        b = "/코로나 : 현재 코로나 상태를 알려줍니다.\n\n"
        d = "/노래 가사 : 입력한 노래 가사를 알려줍니다.\n\n"
        e = "/실검 : 네이버 실시간 검색어를 알려줍니다.\n\n"
        embed = discord.Embed(title='도움말', description="", color=0x00ff00)
        embed.add_field(name=a, value=st, inline=True)
        embed.add_field(name=aa, value=sst+b+d+e, inline=True)

        await message.channel.send(embed=embed)


    if message.content.startswith('/노래 가사'):
        name = message.content[7:]
        st = lyrics(name)
        embed = discord.Embed(title=name+' 가사', description=st, color=0x00ff00)
        await message.channel.send(embed=embed)
     

    if message.content.startswith('/실검') or message.content.startswith('/실시간 검색어'):
        st = live_search()
        embed = discord.Embed(title='네이버 실검', description='', color=0x00ff00)
        embed.add_field(name='전체 연령 기준', value=st, inline=False)
        await message.channel.send(embed=embed)

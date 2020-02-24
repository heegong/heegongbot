import discord
import os
import pyowm
import requests
import asyncio
import datetime
import calendar
from parser import *
from bs4 import BeautifulSoup
client = discord.Client()

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



def get_lol_solo_info(name):
    URL = ("http://fow.kr/find/%s" % (name))
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all('div')
    site = site[252]
    try:
        site = str(site)
        site = site.replace('<div style="top:7px; left:155px; line-height:14px; position:absolute;">','')
        site = site.replace('<','')
        site = site.replace('>','')
        site = site.replace('/','')
        site = site.replace('\\','')
        site = site.replace('br','')
        site = site.replace('fontb','')
        site = site.replace('div','')
        site = site.replace('bfont','')
        site = site.replace('color','')
        site = site.replace('=','')
        site = site.replace('\n','')
    except:
        site = " "
    return site


def lol_free_info(name):
    URL = ("https://poro.gg/ko/s/KR/%s"%name)
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all("div")
    site = site[365]
    site1 = site.find_all('span')
    site1 = str(site1)
    site1 = site1[site1.find('">')+2:site1.find('</span')]
    site2 = site.find_all('b')
    site2 = str(site2)
    site2 = site2[site2.find('">')+2:site2.rfind('</b>,')]
    ls = [site2,site1]
    
    if  "Unranked" in ls[0] :
        st = "언랭이라서 전적이 안나와요 ㅠㅠ"
    else:
        st = "자랭티어 : "+ls[0].upper()+"\t\t리그 포인트 : "+ls[1]
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


def live_search():
    URL = ("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=ㅇ ㅇ")
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all('span')
    site = str(site)
    site = site[43300:45000]
    site = site.replace('"','')
    site = site.replace('<','')
    site = site.replace('>','')
    site = site.replace('/','')
    site = site.replace('s=tit _text','')
    site = site.replace('span','')
    site = site.replace('clas','')
    site = site.replace('class','')
    site = site.replace(' s=keyword em s=num1em  ','')
    site = site.replace('  s=spim, NEW,  s=keyword em s=num2em  ','')
    site = site.replace('  ','')
    site = site.replace('s=spim, NEW,s=keyword em s=num3em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num4em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num5em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num6em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num7em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num8em','')
    site = site.replace('s=keyword em s=num9em','')
    site = site.replace('s=keyword em s=num8em','')
    site = site.replace('s=keyword em s=num7em','')
    site = site.replace('s=keyword em s=num6em','')
    site = site.replace('s=keyword em s=num5em','')
    site = site.replace('s=keyword em s=num4em','')
    site = site.replace('s=keyword em s=num3em','')
    site = site.replace('s=keyword em s=num2em','')
    site = site.replace('s=keyword em s=num1em','')
    site = site.replace('s=keyword em s=num10em','')
    site = site.replace('s=spim, NEW,s=keyword em s=num10em','')
    site = site.replace('s=spim','')
    site_ls = site.split(',')
    for i in range(10):
        del(site_ls[i])
        
    return site_ls


def Colona():
    URL = ("https://coronamap.site/")
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.find_all('div')
    site = str(site)
    site = site[3211:3604]
    site = site.replace('</div>, <div>602</div>, <div class="content1 clear" style="font-size: 15px;justify-content:space-evenly;padding: 0 11px;">','')
    site = site.replace('<div>','')
    site = site.replace('</div>','')
    site = site.replace('<div style="font-size:13px;color:rgb(47,181,105);font-weight:bolder;">완치','')
    site = site.replace('<div style="width: 1px; height:100%; background:black;">','')
    site = site.replace('<div style="font-size:13px;color:red;font-weight:bolder;">사망','')
    site_ls = site.split('\n')
    del(site_ls[1])
    del(site_ls[1])
    del(site_ls[1])
    del(site_ls[2])
    del(site_ls[2])
    del(site_ls[2])
    del(site_ls[2])
    site_ls.pop()
    st_colona = '확진자 : ' + site_ls[0]+",         완치 : "+site_ls[1]+',         사망 : '+site_ls[2]
    return st_colona


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

API_Key = '52a192d87186e871d8ad7c1300c3730d'
owm = pyowm.OWM(API_Key)
 
City_ID = 1835848
obs = owm.weather_at_id(City_ID)    
 
# get_location은 지역에 대한 정보를 가져 옵니다.
L = obs.get_location()
City_name = L.get_name()




 





#############################경고경고경고 명령어#############################################################################



####
ii = 1
i = 0
############################################
baseURL = 'https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=2020.03.12'


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("저는 히공님의 노예1호 지금은 테스트 용도라서 나중에 버려질꺼랍니다.")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("/날씨"):
# get_weather는 기상정보에 대한 정보를 가져옵니다.
        W = obs.get_weather()
        Temp = W.get_temperature(unit='celsius')
        await message.channel.send(City_name + '의 최고기온은 ' + str(Temp['temp_max']) + ' 도 입니다.')
        await message.channel.send(City_name + '의 최저기온은 ' + str(Temp['temp_min']) + ' 도 입니다.')
        await message.channel.send(City_name + '의 현재기온은 ' + str(Temp['temp']) + ' 도 입니다.')
 
        Status = W.get_status()
        await message.channel.send(City_name + '의 현재날씨는 ' + Status + ' 입니다.')





    if message.content.startswith("/dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)


    if message.content.startswith("/아가리"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="병신")
        await author.add_roles(role)


    if message.content.startswith("/언아가리"):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="병신")
        await author.remove_roles(role)   
    

##schulcode = B100001369, schulCrseScCode = 3, schulKndScCode = 03
#https://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100001369&schulCrseScCode=3&schulKndScCode=03&schYmd=2020.03.12

    if message.content.startswith("/안녕"):
        await message.channel.send("안녕")
    if message.content.startswith("/시발람아"):
        await message.channel.send("왜 이새끼야")
    if message.content.startswith("/엄마있어?"):
        await message.channel.send("없어 시벌럼아")
    if message.content.startswith("/아빠는?"):
        await message.channel.send("없어 개새야")
    if message.content.startswith("/현민이 좋아해?"):
        await message.channel.send("어 많이 좋아해")



    if message.content.startswith('/동원중 급식'):
        today = datetime.datetime.today()
        local_date2 = today.strftime("%Y.%m.%d")
        local_weekday2 = today.weekday() - 1
        

        l_diet = get_diet(local_date2, local_weekday2)    
        lunch = local_date2 + "   오늘 동원중 급식 \n\n" + l_diet + "\n\n\n"   
        if l_diet == " ":
            await message.channel.send("오늘은 급식이 없어요 ㅠㅠㅠ")
        else: 
            await message.channel.send(lunch)  


        tommorw = datetime.datetime.today() + datetime.timedelta(days=1)    
        local_date2 = tommorw.strftime("%Y.%m.%d")  
        local_weekday2 = tommorw.weekday() 


        l_diet = get_diet(local_date2, local_weekday2)    
        lunch = "\n\n"+ local_date2 + "   내일 동원중 급식 \n\n" + l_diet    
        if l_diet == " ":
            await message.channel.send("내일은 급식이 없어요 ㅠㅠㅠ")
        else: 
            await message.channel.send(lunch)



    if message.content.startswith('/봉화중 급식'):
        today = datetime.datetime.today()
        local_date2 = today.strftime("%Y.%m.%d")
        local_weekday2 = today.weekday() - 1
        

        l_diet = get_diet_bong(local_date2, local_weekday2)    
        lunch = local_date2 + "   오늘 봉화중 급식  \n\n" + l_diet + "\n\n"
        if l_diet == " ":
            await message.channel.send("오늘은 급식이 없어요 ㅠㅠㅠ")
        else: 
            await message.channel.send(lunch)  


        tommorw = datetime.datetime.today() + datetime.timedelta(days=1)  
        local_date2 = tommorw.strftime("%Y.%m.%d")  
        local_weekday2 = tommorw.weekday() 

        l_diet = get_diet_bong(local_date2, local_weekday2)    
        lunch = "\n\n"+ local_date2 + "   내일 봉화중 급식 \n\n" + l_diet    
        if l_diet == " ":
            await message.channel.send("내일은 급식이 없어요 ㅠㅠㅠ")
        else: 
            await message.channel.send(lunch)

    if message.content.startswith('/급식 봉화중 날짜 : '):
        year = message.content[13:17]
        month = message.content[18:20]
        month2 = month
        day = message.content[21:23]
        month = Change(month)
        date2 = year+"."+month2+"."+day
        _weekday = calendar.weekday(int(year),int(month),int(day)) 
        lunch = "\n\n" + date2 + "의 봉화중 급식 \n\n"+get_diet_bong(date2,_weekday)
        if get_diet_bong(date2,_weekday) == " ":
            await message.channel.send("그날은 급식이 없어요 ㅠㅠㅠ")
        else:
            await message.channel.send(lunch)

    if message.content.startswith('/급식 동원중 날짜 : '):
        year = message.content[13:17]
        month = message.content[18:20]
        month2 = month
        day = message.content[21:23]
        month = Change(month)
        date2 = year+"."+month2+"."+day
        _weekday = calendar.weekday(int(year),int(month),int(day)) 
        lunch = "\n\n" + date2 + "의 동원중 급식 \n\n"+get_diet(date2,_weekday)
        if get_diet(date2,_weekday) == " ":
            await message.channel.send("그날은 급식이 없어요 ㅠㅠㅠ")
        else:
            await message.channel.send(lunch)


    if message.content.startswith('/롤 솔랭 전적'):
        name = message.content[9:]
        hee = get_lol_solo_info(name)
        tier = hee[hee.rfind('리그') - 14:hee.rfind('승급전') - 3]
        tier = tier.replace('822"','')
        tier = tier.replace('22"','')
        tier = tier.replace('2"','')
        tier = tier.replace('"','')
        tier_ls = tier.split('\t')
        del(tier_ls[1:3])
        await message.channel.send("솔랭티어 : "+tier_ls[0]+"\t\t"+tier_ls[1])
        if "IRON" in hee:
            await message.channel.send("\n\n사람샛기 신가요?")
    


    if message.content.startswith('/롤 자랭 전적'):
        name = message.content[9:]
        st = lol_free_info(name)
        await message.channel.send(st)
        if "IRON" in st:
            await message.channel.send('\n\n사람샛기 신가요?')


    if message.content.startswith('/한강물'):
        suon = han_river()
        await message.channel.send("현재 한강물의 온도는 "+suon+" 입니다.")
    


    if message.content.startswith('/코로나'):
        await message.channel.send(Colona())

     

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

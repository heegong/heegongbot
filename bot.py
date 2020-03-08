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
        a = ["오늘은 동원중\n급식이 없어요 ㅠㅠㅠ","오늘은 봉화중\n급식이 없어요 ㅠㅠㅠ"]
    elif site != " " and site1 == " ":
        a = ['오늘 동원중 급식\n\n'+site,"오늘은 봉화중\n급식이 없습니다."]
        
    elif site == " " and site1 != " ":
        a = ['오늘은 동원중\n급식이 없습니다.','오늘 봉화중 급식\n\n'+site1]
    else:
        a = ["오늘 동원중 급식\n\n"+site,"오늘 봉화중 급식\n\n"+site1]
    return a
    


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
    site1 = site1.replace('<span>자유랭크 5x5</span>, ','')
    site1 = site1[site1.find('">')+2:site1.find('</span')]
    site2 = site.find_all('b')
    site2 = str(site2)
    site2 = site2[site2.find('">')+2:site2.rfind('</b>,')]
    ls = [site2,site1]
    if  "Unranked" in ls[0] :
        st = "언랭이라서 전적이 안나와요 ㅠㅠ"
    else:
        st = "자랭티어 : "+ls[0].upper()+"\n리그 포인트 : "+ls[1]+"LP"
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





def Collona():
    URL = ("http://www.seoul.go.kr/coronaV/coronaStatus.do")
    html = get_html(URL)
    
    soup = BeautifulSoup(html, 'html.parser')
    site = soup.select('p.counter')
    site = site[9:12]
    site = str(site)
    site = site.replace('[','')
    site = site.replace(']','')
    site = site.replace('<p class="counter','')
    site = site.replace('</p>','')
    site = site[2:]
    site_ls = site.split(', ">')
    st = "확진자 : "+site_ls[0]+"명\n완치 : "+site_ls[1]+"명\n사망자 : "+site_ls[2]+"명"

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


    if message.content.startswith("/아가리"):
        if message.author.name == "히공":
            author = message.guild.get_member(int(message.content[5:23]))
            role = discord.utils.get(message.guild.roles, name="병신")
            await author.add_roles(role)
        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')


    if message.content.startswith("/언아가리"):
        if message.author.name == "히공":
            author = message.guild.get_member(int(message.content[6:24]))
            role = discord.utils.get(message.guild.roles, name="병신")
            await author.remove_roles(role)
        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.') 
    

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
        local_weekday2 = tommorw.weekday() + 1


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
        local_weekday2 = tommorw.weekday() + 1

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
        hee = get_lol_solo_info(name)
        tier = hee[hee.rfind('리그') - 14:hee.rfind('승급전') - 3]
        tier = tier.replace('822"','')
        tier = tier.replace('22"','')
        tier = tier.replace('2"','')
        tier = tier.replace('"','')
        tier_ls = tier.split('\t')
        del(tier_ls[1:3])
        st = "솔랭티어 : "+tier_ls[0]+"\n"+tier_ls[1]
        sst = ''
        if "IRON" in hee:
            sst = "\n\n사람샛기 신가요?"
        embed = discord.Embed(title="롤 전적", description=st+sst, color=0x00ff00)
        await message.channel.send(embed=embed)
            
    


    if message.content.startswith('/롤 자랭 전적'):
        name = message.content[9:]
        st = lol_free_info(name)
        embed = discord.Embed(title="롤 전적", description=st, color=0x00ff00)
        sst = ''
        if "IRON" in st:
            sst = '\n\n사람샛기 신가요?'
        embed = discord.Embed(title="롤 전적", description=st+sst, color=0x00ff00)
        await message.channel.send(embed=embed)


    if message.content.startswith('/한강물'):
        suon = han_river()
        if suon[suon.find('.')+1] == "0":
            suon = suon.replace('.0','')
            suon = suon+"도"
        embed = discord.Embed(title="한강물", description="현재 한강물의 온도는 "+suon+" 입니다.", color=0x00ff00)
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
                f.write("\n"+name+" "+"1"+"              ")
                f.close()
                embed = discord.Embed(title="경고", description=name+"님의 경고는 총 1회 입니다.", color=0x00ff00)
                await message.channel.send(embed=embed)

        else:
            await message.channel.send('당신은 이 명령어를 사용할 권한이 없습니다.')




    if message.content.startswith("/도움말"):
        a = '관리자 명령어\n'
        b = '/dm : 사용자에게 dm을 보냅니다.\n\n'
        c = '/아가리 : 사용자를 닥치게 만듭니다.\n\n'
        d = '/언아가리 : 사용자를 닥치게 했던것을 풀어줍니다.\n\n'
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
        g = '/급식 : 동원중과 봉화중의 오늘 급식을 알려줍니다.\n'
        h = '/롤 솔랭 전적 : 입력한 닉네임의 롤 솔랭 전적을 알려줍니다.\n\n/롤 자랭 전적 : 입력한 닉네임의 롤 자랭 전적을 알려줍니다.\n\n'
        sst = b+c+d+e+f+g+h
        b = "/코로나 : 현재 코로나 상태를 알려줍니다.\n\n"
        c = '/한강물 : 현재 한강물의 온도를 알려줍니다.'
        sst += b+c
        embed = discord.Embed(title='도움말', description="", color=0x00ff00)
        embed.add_field(name=a, value=st, inline=True)
        embed.add_field(name=aa, value=sst, inline=True)       
        await message.channel.send(embed=embed)

        
     
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

###
# 컴프야 2015~2020 팀 성적 크롤링

run profile1
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('chromedriver.exe')

# 2015년
home_result=[] ; away_result=[] ; game_date=[] ; ground_name=[]
for i in range(77,100):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=201500{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(100,956):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=20150{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

result_2015_home = pd.DataFrame(home_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2015_away = pd.DataFrame(away_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2015_home['ground'] = ground_name
result_2015_away['ground'] = ground_name


# 2016년
home_result=[] ; away_result=[] ; game_date=[] ; ground_name=[]
for i in range(3,10):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=2016000{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(10,100):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=201600{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(100,952):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=20160{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

result_2016_home = pd.DataFrame(home_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2016_away = pd.DataFrame(away_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2016_home['ground'] = ground_name
result_2016_away['ground'] = ground_name


# 2017년
home_result=[] ; away_result=[] ; game_date=[] ; ground_name=[]
for i in range(1,10):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=2017000{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(10,100):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=201700{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(100,832):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=20170{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

result_2017_home = pd.DataFrame(home_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2017_away = pd.DataFrame(away_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2017_home['ground'] = ground_name
result_2017_away['ground'] = ground_name


# 2018년
home_result=[] ; away_result=[] ; game_date=[] ; ground_name=[]
for i in range(1,10):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=2018000{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(10,100):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=201800{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(100,813):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=20180{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

result_2018_home = pd.DataFrame(home_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2018_away = pd.DataFrame(away_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2018_home['ground'] = ground_name
result_2018_away['ground'] = ground_name


# 2019년
home_result=[] ; away_result=[] ; game_date=[] ; ground_name=[]
for i in range(10,100):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=201900{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

for i in range(100,837):
    url= f'http://cpbpoint.mbcplus.com/stats/scoreboard/?mode=view&gamecode=20190{i}'
    driver.get(url)
    driver.implicitly_wait(5)
    
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    home_result.append(soup.select('tfoot')[1].get_text().replace('Total','')[3:].split('\n')[:-2])
    away_result.append(soup.select('tfoot')[0].get_text().replace('Total','')[3:].split('\n')[:-2])
    game_date.append(soup.select('p')[8].get_text()[:13])
    ground_name.append(soup.select('p')[8].get_text()[26:28])

result_2019_home = pd.DataFrame(home_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2019_away = pd.DataFrame(away_result, index=[game_date], columns=['PA','AB','H','1B','2B','3B','HR','R','RBI','BB','HP','SO','SB','CS','SH','GDP','E','컴프야P'])
result_2019_home['ground'] = ground_name
result_2019_away['ground'] = ground_name

result_2015_home.to_csv('result_2015_home.csv')
result_2015_away.to_csv('result_2015_away.csv')

result_2016_home.to_csv('result_2016_home.csv')
result_2016_away.to_csv('result_2016_away.csv')

result_2017_home.to_csv('result_2017_home.csv')
result_2017_away.to_csv('result_2017_away.csv')

result_2018_home.to_csv('result_2018_home.csv')
result_2018_away.to_csv('result_2018_away.csv')

result_2019_home.to_csv('result_2019_home.csv')
result_2019_away.to_csv('result_2019_away.csv')



import requests
from bs4 import BeautifulSoup
import xlsxwriter as xls
import os

FILE_PATH = 'pokemon full list.xlsx'


#Set up parser for the pokémon list
poke_list = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_VIII-present)'
list_page = requests.get(poke_list)
list_soup = BeautifulSoup(list_page.text, 'html.parser')

index = 1054


#Scrape pokémon number
numtags = list_soup.find_all('td', class_='r')[index]
num = numtags.find_all('b')[0].string


#Scrape pokémon name
nametags = list_soup.find_all('td', class_='l')[index]
try:
    namesubtags = nametags.find_all('small')[0].string
    name = [nametags.find_all('a')[0].string, namesubtags]
except:
    name = [nametags.find_all('a')[0].string, None]


#Set up parser for individual pokémon
poke_single = 'https://bulbapedia.bulbagarden.net/wiki/{}'.format(name[0] + '_(Pokémon)')
single_page = requests.get(poke_single)
single_soup = BeautifulSoup(single_page.text, 'html.parser')


#Scrape pokémon types
typetags = single_soup.find_all('td', width='45px')[0]
type1 = typetags.find_all('a')[0].string
typetags = single_soup.find_all('td', width='45px')[1]
type2 = typetags.find_all('a')[0].string
type = [type1, type2]


#Scrape pokémon base stats
stattags = list_soup.find_all('tr', style='text-align: center; background:#FFF')[index].contents
statsubtags = stattags[9]


stats = []
stat_index = 7

while stat_index <= 21:
    stats.append(float(stattags[stat_index].string[:-1]))
    stat_index +=2


#Scrape pokémon gender ratio
gendertags = single_soup.find_all('table', class_='roundy', width='100%', style='background:#FFF;')[2]
gendersubtags = gendertags.find_all('a')[0]
male = gendersubtags.find_all('span')[0].string
try:
    female = gendersubtags.find_all('span')[2].string
    gender = [male, female]
except:
    gender = [male]


#Scrape pokémon catch rate
try:
    catchtags = single_soup.find_all('table', class_='roundy', width ='100%',  style='background:#FFF; padding-top:0.6em; padding-bottom:0.6em;')[0]
    catchtbody = catchtags.find_all('tbody')[0]
    catchtr = catchtbody.find_all('tr')[0]
    catchtd = catchtr.find_all('td')[0].contents
    catchval = float(catchtd[0])
    catchperc = float(catchtd[1].find_all('span')[0].string.split('%')[0])
    catch = [catchval, catchperc]
except:
    try:
        catchtags = single_soup.find_all('table', class_='roundy', width ='100%',  style='background:#FFF;')[3]
        catchtbody = catchtags.find_all('tbody')[0]
        catchtr = catchtbody.find_all('tr')[0]
        catchtd = catchtr.find_all('td')[0].contents
        catchval = float(catchtd[0])
        catchperc = float(catchtd[1].find_all('span')[0].string.split('%')[0])
        catch = [catchval, catchperc]
    except:
        catch = [0.0, 0.0]


#Scrape pokémon picture
num_text = str(num)
while len(num_text) < 3:
    num_text = '0' + num_text

name_text = name[0] + '-' + name[1][1:-1]  if name[1] == True else name[0]

picture_address = 'https://bulbapedia.bulbagarden.net/wiki/File:{}{}.png'.format( num_text, name_text)
picture_page = requests.get(picture_address)
picture_soup= BeautifulSoup(picture_page.text, 'html.parser')
picturetags = picture_soup.find_all('div', class_="fullImageLink", id="file")[0]
picturea = str(picturetags.find_all('a', href=True)[0]).split('"')
picture = picturea[1]


print(num)
print(name)
print(poke_single)
print(type)
print(stats)
print(gender)
print(catch)
print(picture)
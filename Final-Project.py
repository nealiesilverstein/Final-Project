from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import unittest
import json
import sqlite3

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"finaldb.db")
cur = conn.cursor()


r = requests.get("https://brilliantmaps.com/top-100-tourist-destinations/")
r_text = r.text
soup = BeautifulSoup(r_text, 'lxml')
rank = soup.find_all('td', class_='column-1')
city = soup.find_all('td', class_='column-2')
country = soup.find_all('td', class_='column-3')
tourists_in_millions = soup.find_all('td', class_='column-4')
print(len(city))

cur.execute("DROP TABLE IF EXISTS Destinations")
cur.execute("CREATE TABLE IF NOT EXISTS Destinations (rank INTEGER PRIMARY KEY, city TEXT, country TEXT, tourists_in_millions REAL)")
for i in range(len(rank)):
    cur.execute('''INSERT INTO Destinations (rank,city,country,tourists_in_millions) VALUES (?,?,?,?)''', (rank[i].text, city[i].text, country[i].text, tourists_in_millions[i].text))
conn.commit()

r1 = requests.get("https://www.worldometers.info/world-population/population-by-country/")
r1_text = r1.text
soup1 = BeautifulSoup(r1_text, "lxml")
#table = soup1.find('table', {'id':'example2'})
#print(table)
table = soup1.find_all("tbody")
rows = table[0].find_all('tr')[0:100]
print(len(rows))
pop_countries = []
country_population = []
world_share = []
percent_urban_pop = []
for row in rows:
    a = row.find('a').text
    pop_countries.append(a)
    td_list = row.find_all('td')
    country_population.append(td_list[2].text)
    percent_urban_pop.append(td_list[-2].text)
    world_share.append(td_list[-1].text)
print(len(pop_countries))
print(len(country_population))
print(len(world_share))
#print(pop_countries)


cur.execute("DROP TABLE IF EXISTS Countries")
cur.execute("CREATE TABLE Countries (rank INTEGER PRIMARY KEY, country TEXT, country_population INTEGER, percent_urban_pop TEXT, percent_world_pop TEXT)")
for i in range(100):
    cur.execute('''INSERT OR IGNORE INTO Countries (rank,country,country_population,percent_urban_pop,percent_world_pop) VALUES (?,?,?,?,?)''', (i+1, pop_countries[i], country_population[i], percent_urban_pop[i], world_share[i]))
conn.commit()






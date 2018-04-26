import mysql.connector as mariadb
import requests
from bs4 import BeautifulSoup
busca = raw_input('Digite sua Busca: ')
page = requests.get("https://www.google.dz/search?q='{}".format(busca))
soup = BeautifulSoup(page.content, "lxml")
import re
for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    resposta = re.split(":(?=http)",link["href"].replace("/url?q=",""))
    print resposta

mariadb_connection = mariadb.connect(user='testeuser', password='teste', database='host')
cursor = mariadb_connection.cursor()
cursor.execute('INSERT INTO google (links,links2) VALUES (%s,%s)', (busca,resposta)
mariadb_connection.commit()
cursor.close()


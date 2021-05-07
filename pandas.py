import requests
from bs4 import BeautifulSoup
url = 'http://ostranah.ru/_lists/capitals.php'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all("table")
print(table[0])
for each_table in table:
    print(each_table.find("tbody"))
    print(each_table.find("td"))
    print(each_table.find("a"))


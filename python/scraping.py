import requests
from bs4 import BeautifulSoup
# variaveis
html = requests.get("https://www.scrapethissite.com/pages/simple/").text
html_parsed = BeautifulSoup(html,"html.parser")

countryList = html_parsed.find_all(class_ = "country-name")
capitalList = html_parsed.find_all(class_ = "country-capital")
finalList = []
#extracao
for country,capital in zip(countryList,capitalList):
    dici = {'country':country.text.strip(),
    'capital':capital.text.strip()}
    finalList.append(dici)
# print do resultado final
print(finalList)
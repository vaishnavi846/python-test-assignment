import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    'https://www.staples.com/Computer-office-desks/cat_CL210795/663ea?icid=BTS:2020:STUDYSPACE:DESKS')
bs = BeautifulSoup(html, 'html.parser')

table = bs.findAll('div', {'class': 'SearchResults-UX2__searchRow'})[0]
rows = table.findAll('div',{'class' : 'standard-tile__title'})

csvFile = open('Text-Editor-Data.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['a']):
            csvRow.append(cell.get_text())
            print(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()
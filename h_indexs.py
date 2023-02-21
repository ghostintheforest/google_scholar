from bs4 import BeautifulSoup
import requests
#add headers to the request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://scholar.google.com/citations?hl=en&user=t53jWtYAAAAJ'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'id': 'gsc_rsb_st'})
rows = table.find_all('tr')
if table:
    # get all the rows in the table
    rows = table.find_all('tr')
    for row in rows:
        # extract the cells in the row
        cells = row.find_all('td')
        if cells:
            row_one = cells[0].text.strip()
            all_citation = cells[1].text.strip()
            #print(row_one, all_citation)
            citations_18 = cells[2].text.strip()
            print(row_one, all_citation, citations_18)

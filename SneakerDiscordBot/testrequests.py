from bs4 import BeautifulSoup
from requests import get

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})

url='https://www.checkcardetails.co.uk/cardetails/fp63yvf'
webscrapingapi = "https://api.webscrapingapi.com/v1?api_key=xEZFkJiRdU1S7umc96y4ncTC1xlqBuhL&url="+url

response = get(webscrapingapi, headers=headers)

soup = BeautifulSoup(response.text,'html.parser')
print(soup)

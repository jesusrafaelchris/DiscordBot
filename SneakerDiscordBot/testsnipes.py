import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

start = time.time()
#style id
#type:restock
#site:snipes
#sizes load ATC (size)
#QT
#links

def stripnewlinesofarray(array):
    real = []
    for element in array:
        element = element.strip('\n')
        real.append(element)
    return real

def returnsizesfromarray(array):
    real = []
    for size in array:
        size = size['aria-describedby']
        real.append(size)
    return real

def stripnewlinesofitem(item):
    item = item.strip('\n')
    return item

def getmultilinestring(array):
    string = '\n'.join([i for i in array[:]])
    return string

def sendsneakerWebhook(name,styleID,colour,price,brand,sizes,imageurl):
    print("start of webhook"+str(time.time() - start))
    url = "https://discord.com/api/webhooks/879777116927950858/zLDTtIJRZ-LlFTLQvMfOD-4K2WNzMy26BWIDjhGKvu3ey4sGwBkEMo8aEwbctR-x-s2B"

    webhook = DiscordWebhook(url=url)

    embed = DiscordEmbed(
        title=name + colour, description=styleID, color='03b2f8'
    )
    embed.set_author(
        name="Author Name",
        url="https://github.com/lovvskillz",
        icon_url="https://avatars0.githubusercontent.com/u/14542790",
    )
    embed.set_footer(text="Christian Grinling")
    embed.set_thumbnail(url=imageurl)
    embed.set_timestamp()
    # Set `inline=False` for the embed field to occupy the whole line
    embed.add_embed_field(name="Price", value= price, inline=False)
    embed.add_embed_field(name="Type", value="Restock", inline=False)
    embed.add_embed_field(name="Site", value="Snipes", inline=False)
    string = getmultilinestring(sizes)
    print(string)
    embed.add_embed_field(name='Sizes',value= string, inline = False)
    embed.add_embed_field(name="QT", value= brand,inline=False)
    embed.add_embed_field(name="Links", value="Pending",inline=False)
    print("end of webhook"+str(time.time() - start))
    webhook.add_embed(embed)
    response = webhook.execute()

print("start" +str(time.time() - start))
session = requests.Session()
sneakerurl = 'https://www.snipesusa.com/air-max-90-nike-usa-white---chile-red---navy-dj5170-100-1000090895.html'
#https://api.webscrapingapi.com/v1?api_key=xEZFkJiRdU1S7umc96y4ncTC1xlqBuhL&url=
fetchURL = "https://api.scrapingdog.com/scrape?api_key=61251348bcf9682ec44d2fd6&url=" + sneakerurl# + "&render_js=1"
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = session.get(fetchURL,timeout=5)
print("requests.get"+str(time.time() - start))
page.raw.chunked = True
page.encoding = 'utf-8'
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='maincontent')
print("soup page" + str(time.time() - start))
#print(results.prettify())

name = results.find("h1", class_="product-name").text
print("name" +str(time.time() - start))
images = results.find_all("img", class_= "d-block img-fluid js-blazy")
print("images"+str(time.time() - start))
styleID = [element.text for element in results.find_all("span", class_="product-id")]
print("style"+str(time.time() - start))
colour = [element.text for element in results.find_all("span", class_="attr-selected-value ml-2")]
print("colour"+str(time.time() - start))
price = [element.text for element in results.find_all("span", class_="value")]
print("price"+str(time.time() - start))
brand = [element.text for element in results.find_all("div", class_="product-brand")]
print("brand"+str(time.time() - start))
sizes = results.find_all("button", class_="size-attribute")
print("sizes"+str(time.time() - start))


print(stripnewlinesofitem(name))
print(stripnewlinesofitem(styleID[0]))
print(stripnewlinesofitem(colour[0]))
print(stripnewlinesofitem(price[0]))
print(stripnewlinesofitem(brand[0]))
print(returnsizesfromarray(sizes))
print(images[0]['data-src'])


name = stripnewlinesofitem(name)
styleID = stripnewlinesofitem(styleID[0])
colour = stripnewlinesofitem(colour[0])
price = stripnewlinesofitem(price[0])
brand = stripnewlinesofitem(brand[0])
sizes = returnsizesfromarray(sizes)
imageurl = images[0]['data-src']
print("just before webhook send"+str(time.time() - start))
sendsneakerWebhook(name,styleID,colour,price,brand,sizes,imageurl)

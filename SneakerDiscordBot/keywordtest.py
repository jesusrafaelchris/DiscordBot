import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed

def sendsneakerWebhook(name,sneakerurl,imageurl):
    url = "https://discord.com/api/webhooks/879777116927950858/zLDTtIJRZ-LlFTLQvMfOD-4K2WNzMy26BWIDjhGKvu3ey4sGwBkEMo8aEwbctR-x-s2B"

    webhook = DiscordWebhook(url=url)

    embed = DiscordEmbed(title=name+" added to watchlist.", description='\u200b', color='00FF00')
    embed.set_author(
        name="Sneaker Added!",
        url= sneakerurl,
    )
    embed.set_footer(text="Christian Grinling")
    embed.set_thumbnail(url=imageurl)
    embed.set_timestamp()
    # Set `inline=False` for the embed field to occupy the whole line
    embed.add_embed_field(name="Link", value= "["+name+"]"+"("+ sneakerurl+")",inline=False)

    webhook.add_embed(embed)
    response = webhook.execute()

def get_url_from_keyword(search_term):
    session = requests.Session()
    keyword_url = 'https://www.snipesusa.com/search?q=' + search_term
    #broken for some reason.. https://api.webscrapingapi.com/v1?api_key=xEZFkJiRdU1S7umc96y4ncTC1xlqBuhL&url=
    api_url = "https://api.scrapingdog.com/scrape?api_key=61251348bcf9682ec44d2fd6&url="+ keyword_url
    page = session.get(api_url,timeout=5)
    page.raw.chunked = True
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='maincontent')

    imagediv = results.find("div", class_= "image-container")
    image = imagediv.find("img")["data-src"]
    print(image)
    #name = image['title']
    name = 'sneaker'
    sneaker_href = results.find("div", class_="product-tile").find('a').get('href')
    sneaker_name = results.find("div", class_="product-tile").find('img').get('title')
    start_of_url = 'https://www.snipesusa.com/'
    finished_sneaker_url = start_of_url + sneaker_href
    sendsneakerWebhook(search_term,finished_sneaker_url,image)
    return finished_sneaker_url

get_url_from_keyword('Nike Air Force')

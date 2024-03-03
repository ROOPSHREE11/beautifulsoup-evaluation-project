#!/usr/bin/env python
# coding: utf-8

# In[1]:answer 1





# In[3]:answer 1


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape IMDb's Top rated 100 Indian movies' data
def scrape_imdb_top_100_indian_movies(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        movies = soup.find_all('div', class_='lister-item-content')
        data = []
        for movie in movies:
            name = movie.find('a').text.strip()
            rating = movie.find('span', class_='ipl-rating-star__rating').text.strip()
            year = movie.find('span', class_='lister-item-year').text.strip('()')
            data.append({'Name': name, 'Rating': rating, 'Year': year})
        return data
    else:
        print("Failed to retrieve data from IMDb.")
        return None


imdb_url = 'https://www.imdb.com/list/ls056092300/'


movies_data = scrape_imdb_top_100_indian_movies(imdb_url)


df = pd.DataFrame(movies_data)


print(df)







# In[4]:answer 2


import requests
from bs4 import BeautifulSoup


def scrape_peachmode_products(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', class_='product-details')
        data = []
        for product in products:
            name = product.find('h2', class_='product-title').text.strip()
            price = product.find('span', class_='price').text.strip()
            discount = product.find('span', class_='price-compare').text.strip()
            data.append({'Name': name, 'Price': price, 'Discount': discount})
        return data
    else:
        print("Failed to retrieve data from Peachmode.")
        return None


url = 'https://peachmode.com/search?q=bags'


products_data = scrape_peachmode_products(url)


if products_data:
    for product in products_data:
        print("Product Name:", product['Name'])
        print("Price:", product['Price'])
        print("Discount:", product['Discount'])
        print()
else:
    print("No data scraped from Peachmode.")


# In[6]:answer 3


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_icc_cricket_rankings(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Failed to retrieve data from ICC Cricket.")

def scrape_top_odi_teams(soup):
    teams_data = []
    table = soup.find('table', class_='table rankings-table')
    rows = table.find('tr')[1:11]  # excluding the header row, getting top 10 teams
    for row in rows:
        cols = row.find_all('td')
        team = cols[1].text.strip()
        matches = cols[2].text.strip()
        points = cols[3].text.strip()
        rating = cols[4].text.strip()
        teams_data.append({'Team': team, 'Matches': matches, 'Points': points, 'Rating': rating})
    return pd.DataFrame(teams_data)

def scrape_top_odi_players(soup, category):
    players_data = []
    table = soup.find('table', class_='table rankings-table')
    rows = table.find_all('tr')[1:11]  # excluding the header row, getting top 10 players
    for row in rows:
        cols = row.find_all('td')
        player = cols[1].text.strip()
        team = cols[2].text.strip()
        rating = cols[3].text.strip()
        players_data.append({'Player': player, 'Team': team, 'Rating': rating, 'Category': category})
    return pd.DataFrame(players_data)

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'


soup = scrape_icc_cricket_rankings(url)


odi_teams_df = scrape_top_odi_teams(soup)
print("Top 10 ODI Teams:")
print(odi_teams_df)


url_batsmen = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
soup_batsmen = scrape_icc_cricket_rankings(url_batsmen)
odi_batsmen_df = scrape_top_odi_players(soup_batsmen, 'Batsmen')
print("\nTop 10 ODI Batsmen:")
print(odi_batsmen_df)


url_bowlers = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
soup_bowlers = scrape_icc_cricket_rankings(url_bowlers)
odi_bowlers_df = scrape_top_odi_players(soup_bowlers, 'Bowlers')
print("\nTop 10 ODI Bowlers:")
print(odi_bowlers_df)


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd



def scrape_odi_teams(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        teams_data = []
        table = soup.find('table', class_='table rankings-table')
        if table:
            rows = table.find_all('tr')[1:11]  teams
            for row in rows:
                cols = row.find_all('td')
                team = cols[1].text.strip()
                matches = cols[2].text.strip()
                points = cols[3].text.strip()
                rating = cols[4].text.strip()
                teams_data.append({'Team': team, 'Matches': matches, 'Points': points, 'Rating': rating})
            return pd.DataFrame(teams_data)
        else:
            print("Table not found in HTML content.")
            return None
    else:
        print("Failed to retrieve data from ICC Cricket.")
        return None

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'


odi_teams_df = scrape_odi_teams(url)

if odi_teams_df is not None:
    print("Top 10 ODI Teams:")
    print(odi_teams_df)
else:
    print("Failed to scrape ODI teams rankings.")


# In[12]:answer 4


import requests
from bs4 import BeautifulSoup
import re
url = "https://www.patreon.com/coreyms"

def scrape_patreon_posts(url):
   
    response = requests.get(url)
    
   
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.content, 'html.parser')
        
    
        post_containers = soup.find_all('div', class_='post')
        
    
        for post in post_containers:
         
            heading = post.find('h4', class_='post__title').text.strip()
            
           
            date = post.find('time')['datetime']
            
           
            content = post.find('div', class_='post__content').text.strip()
            
            youtube_link = post.find('a', href=re.compile(r'^https://www\.youtube\.com/watch\?v='))
            if youtube_link:
                youtube_video_url = youtube_link['href']
                
               
                
            likes = post.find('button', class_='post__like').text.strip()
            
          
            print("Heading:", heading)
            print("Date:", date)
            print("Content:", content)
            print("Likes:", likes)
            print()
    else:
        print("Failed to retrieve page")



scrape_patreon_posts(url)


# In[13]:answer 5


import requests
from bs4 import BeautifulSoup

def scrape_house_details(localities):
    for locality in localities:
        print(f"Scraping house details for {locality}...")
        url = f"https://www.nobroker.in/property/sale/{locality}/?searchParam=W3sibGF0IjoxMi44NDU5MTQ3LCJsb24iOjc3LjYwMzM4NjMsInBsYWNlSWQiOiJDaElKMnJyZWJiZVNSa2FmXzhjdGc5WkZqM3ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=&radius=2.0&type=BHK4&propertyAge=0&propertyType=residential"
        
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            
            house_containers = soup.find_all('div', class_='card')
            
            
            for house in house_containers:
                
                title = house.find('h2', class_='heading-6 font-semi-bold nb__1AShY').text.strip()
                location = house.find('div', class_='nb__2CMjv').text.strip()
                area = house.find('div', class_='nb__3oNyC').text.strip()
                emi = house.find('div', class_='font-semi-bold heading-6').text.strip()
                price = house.find('div', class_='heading-7').text.strip()
                
                
                print("Title:", title)
                print("Location:", location)
                print("Area:", area)
                print("EMI:", emi)
                print("Price:", price)
                print()
        else:
            print(f"Failed to retrieve house details for {locality}")


localities = ["Indira-Nagar", "Jayanagar", "Rajaji-Nagar"]


scrape_house_details(localities)


# In[14]:answer 5


import requests
from bs4 import BeautifulSoup

def scrape_product_details( "https://www.bewakoof.com/bestseller?sort=popular"):
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
     
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        product_containers = soup.find_all('div', class_='productCard')
        
        
        for product in product_containers[:10]:
         
            product_name = product.find('p', class_='productCard-title').text.strip()
            price = product.find('span', class_='productCard-price').text.strip()
            image_url = product.find('img')['src']
            
            print("Product Name:", product_name)
            print("Price:", price)
            print("Image URL:", image_url)
            print()
    else:
        print("Failed to retrieve page")


url = "https://www.bewakoof.com/bestseller?sort=popular"


scrape_product_details(url)


# In[16]:answer 6


import requests
from bs4 import BeautifulSoup

def scrape_product_details("https://www.bewakoof.com/bestseller?sort=popular"):
   
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        product_containers = soup.find_all('div', class_='productCard')
        
        
        for product in product_containers[:10]:
            
            product_name = product.find('p', class_='productCard-title').text.strip()
            price = product.find('span', class_='productCard-price').text.strip()
            image_url = product.find('img')['src']
            
            print("Product Name:", product_name)
            print("Price:", price)
            print("Image URL:", image_url)
            print()
    else:
        print("Failed to retrieve page")


url = "https://www.bewakoof.com/bestseller?sort=popular"


scrape_product_details(url)


# In[ ]:import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"
Send a GET request to the URL and create a BeautifulSoup object:

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
Find the elements containing the headings, dates, and news links using the appropriate CSS selectors:

headings = soup.select("h3.title")
dates = soup.select("time")
news_links = soup.select("a.title")
Extract the text and URLs from the elements:

headings_text = [heading.get_text(strip=True) for heading in headings]
dates_text = [date.get_text(strip=True) for date in dates]
news_links_urls = [link["href"] for link in news_links]
Print or process the scraped data as desired:

for i in range(len(headings_text)):
    print("Heading:", headings_text[i])
    print("Date:", dates_text[i])
    print("News Link:", news_links_urls[i])
    print()
    




import requests
from bs4 import BeautifulSoup

url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"


response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.select("h4.title")
dates = soup.select("div.date")
authors = soup.select("div.author")


titles_text = [title.get_text(strip=True) for title in titles]
dates_text = [date.get_text(strip=True) for date in dates]
authors_text = [author.get_text(strip=True) for author in authors]


for i in range(len(titles_text)):
    print("Paper Title:", titles_text[i])
    print("Date:", dates_text[i])
    print("Author:", authors_text[i])
    print()




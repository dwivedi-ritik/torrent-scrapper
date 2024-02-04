import requests
query = "ice age"
url = f"https://ww2.7movierulz.sh/?s={query}"
res = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.content , 'html.parser')

li = soup.find(class_="content home_style")
obj = {
    "movies": []
}
for el in li.find_all("li"):
  obj["movies"].append ( { "title" : el.p.text})

movie_url = "https://ww2.7movierulz.sh/the-ice-age-adventures-of-buck-wild-2022-hdrip-full-movie-watch-online-free/"
movie_content = requests.get(movie_url)
soup = BeautifulSoup(movie_content.content , 'html.parser')
main_content = soup.find(class_="entry-content")
new_obj = {}
main_content.find(class_="mv_button_css")['href']

main_content.find_all('p')[2].text
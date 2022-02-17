import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


class Tor1377x(object):
    __slots__ = ('movie_data' , 'seeders_list' , 'leeches_list' , 'movie_links')
    def __init__(self):
        self.movie_data = defaultdict()
        self.movie_data = {
                "head":"terrible api",
                "movie_info":[]
            }
        self.seeders_list = []
        self.leeches_list = []
        self.movie_links =  []

    def get_thread_magnate_link(self , movie_url , seeders , leeches ):
        obj = defaultdict()
        res = requests.get(movie_url , headers={"User-Agent":'Mozilla Firefox'}).content
        soup2 = BeautifulSoup(res , "lxml")
        mag_link = "l3426749b3b895e9356348e295596e5f2634c98d8 la1038a02a9e0ee51f6e4be8730ec3edea40279a2 l0d669aa8b23687a65b2981747a14a1be1174ba2c"
        mag = soup2.find(class_= mag_link)  
        magnet_link = mag["href"]
        title_g = re.search(r"[0-9]+\/(.+)/" , movie_url)
        title = title_g.group(1)
        obj["title"] = title
        obj["seeders"] = seeders
        obj["leeches"] = leeches
        obj["magnet_url"] = magnet_link
        self.movie_data["movie_info"].append(dict(obj))
        return


    def get_json(self , query):
        original_url = "https://www.1337xx.to"
        url = "https://www.1337xx.to/search/{}/1/".format(query)
        res = requests.get(url)
        soup = BeautifulSoup(res.content , "lxml")
        tbody = soup.find_all("td")
        seeders , leechers , link = None , None , None 
        for el in tbody:
            seeds = re.search(r"seeds\"\>([0-9]+)</td>" , str(el))
            leeches = re.search(r"leeches\"\>([0-9]+)</td>" , str(el))
            url = re.search(r"</a><a href=\"(.+)\"" , str(el))
            if seeds:
                seeders = seeds.group(1)
                self.seeders_list.append(seeders)
            if leeches:
                leechers = leeches.group(1)
                self.leeches_list.append(leechers)
            if url:
                link = url.group(1)
                self.movie_links.append(original_url+link)
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.get_thread_magnate_link , self.movie_links , self.seeders_list , self.leeches_list)
        return self.movie_data

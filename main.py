import requests
from bs4 import BeautifulSoup
import pprint

video_base_url = "https://cache.libria.fun"

parse_base_url = "https://api.anilibria.tv/v3/title/search?search=человек&limit=1"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(parse_base_url , headers=headers).json()
#response = requests.get(parse_base_url , headers=headers).text


#soup = BeautifulSoup(response.)

#print(response["list"][0]["id"])
#print(response["list"][0]["names"]["ru"])
#print(response["list"][0]["status"]["string"])
#print(r"https://anilibria.tv" + str(response["list"][0]["posters"]["original"]["url"]))
episodes = response["list"][0]["player"]["episodes"]["last"]
print(f"Количество серий {episodes}")
print(video_base_url + str(response["list"][0]["player"]["list"]["1"]["hls"]["fhd"]))
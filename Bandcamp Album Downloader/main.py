from bs4 import BeautifulSoup as bs
import requests


#url = input("Album URL: ")
#downpath = input("Directory for download (full path): ")

url = "https://shigeto.bandcamp.com/album/no-better-time-than-now"
downpath = "D:\Downloads\+Musga"

page = requests.get(url)

soup = bs(page.text, 'html.parser')

track_nums = []
track_labels = []

# for track in soup.find_all('tr', {'class' : 'track_row_view linked', 'rel' : True}):
#     track_nums.append(track.get('rel').split('=')[-1])
#
# for track in soup.find_all('span', {'class' : 'track-title'}):
#      track_labels.append(track.contents[0])

thing = []

# for track in soup.find_all('audio'):
#     print(track)

script_num = 0

for script in soup.find_all('script', {'type' : 'text/javascript',
                                       'crossorigin' : 'anonymous',
                                       'nonce' : True,
                                       'data-tralbum' : True}):
    script_num += 1
print(script_num)


audio = "/html/body/audio[1]"

total_tracks = 1
current_track = "/html/body/div[6]/div/div[1]/div[2]/div[3]/div/table/tbody/tr[" + str(total_tracks) + "]"



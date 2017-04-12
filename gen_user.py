from urllib.request import urlopen, URLError
import json

api_url = 'https://randomuser.me/api/?inc=gender,id,nat,dob'
NUM = 50

with open('users_info.txt', 'w') as f:
    for _ in range(NUM):
        res = urlopen(api_url)
        data = json.loads(res.read())
        simple_data = {
            'name': data['results'][0]['id']['name'],
            'gender': data['results'][0]['gender'],
            'dob': data['results'][0]['dob'],
            'nat': data['results'][0]['nat']
            }
        #print(str(simple_data))
        f.write(str(simple_data)+'\n')
    




    


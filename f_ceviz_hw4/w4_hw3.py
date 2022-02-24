import requests
import random
from colorama import Fore

my_list=[]
for i in range(0,100):    
    r       = requests.get("https://randomuser.me/api/")
    first   = (r.json()["results"][0]["name"]["first"]).lower().replace(" ","")
    last    = (r.json()["results"][0]["name"]["last"]).lower().replace(" ","")
    city    = (r.json()["results"][0]["location"]["city"]).lower().replace(" ","")
    country = (r.json()["results"][0]["location"]["country"]).lower().replace(" ","")
    total   = first+last+city+country
    total   = list(total)
    random.shuffle(total)
    my_list.append(total)
    #''.join(random.sample(total,len(total)))
    #print("".join(total))
    print(f"{i+1:3}.","".join(total))

longest_string = max(my_list, key=len)
d="-"*(len(longest_string)+len("LongestString :")+1)
CRED = '\033[91m'
print(CRED+d+CRED)
print("LongestString :","".join(longest_string))
print(d)

import requests
import random

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
    print(i+1,".","".join(total))

longest_string = max(my_list, key=len)
d="-"*(len(longest_string)+len("LongestString :")+1)
print(d)
print("LongestString :","".join(longest_string))
print(d)

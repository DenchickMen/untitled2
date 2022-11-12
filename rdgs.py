class very_big:
    speed= 1
    heidgt = 120
class big(very_big):
    speed = 5
    heidgt = 125
class Small(big):
    speed = 10
    height = 25
    def __init__(self):
        print(self.heidgt)
        print(self.speed)
den = Small()
import requests
help(requests)
rq = requests
print('for den', requests.__cake__)
print(rq.__name__)
print(rq.__url__)
print(type(3))
ls = []
for i in dir(ls):
    print(i)
print(dir(ls))

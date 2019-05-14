import urllib.request
import json
import vk

#https://oauth.vk.com/blank.html#access_token=2e570f219984496620bde0d44e42e7822dd813be499cbedbd53d493c1597ff0dbb2583b275ab423bc7b14&expires_in=86400&user_id=308903303
TOKEN = '2e570f219984496620bde0d44e42e7822dd813be499cbedbd53d493c1597ff0dbb2583b275ab423bc7b14'
session = vk.Session(access_token=TOKEN)
api = vk.API(session)

def add_into_file(file_name, text):
    file = open(file_name, 'a', encoding="utf-8")
    file.write(text)
    file.close()

def get_sex(x):
    # 1 - female
    # 2 - male
    return api.users.get(user_ids=x, fields = 'sex', v=5.95)[0]['sex']


    
for i in range(9741):
    try:
        smth = api.wall.getComments(owner_id = -125842747, post_id = (i + 1), preview_length=1000, v=5.95)   
        print(smth)
        count = len(smth['items'])
        for j in range(count):
            curr = smth['items'][j]
            user = curr['from_id']
            text = curr['text'] + ' '
            if get_sex(user) == 1:  
                add_into_file('fem.txt', text)
            else:   
                add_into_file('male.txt', text)
    except vk.exceptions.VkAPIError:
        print('well')
# потом была ошибка, поэтому я заново запустила с последней записи, которую рассмотрела
for i in range(9778, 10988):
    try:
        smth = api.wall.getComments(owner_id = -125842747, post_id = (i + 1), preview_length=1000, v=5.95)   
        print(smth)
        count = len(smth['items'])
        for j in range(count):
            curr = smth['items'][j]
            user = curr['from_id']
            text = curr['text'] + ' '
            if get_sex(user) == 1:  
                add_into_file('fem.txt', text)
            else:   
                add_into_file('male.txt', text)
    except vk.exceptions.VkAPIError:
        print('well')


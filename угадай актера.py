import vk_api
import time
import random


def game():
    slov = {'photo-194714948_457239017': 'уивер', 'photo-194714948_457239447': 'доминик', 'photo-194714948_457239448': 'крис', 'photo-194714948_457239831': 'нортон', 'photo-194714948_457240136': 'бредли', 'photo-194714948_457240383': 'гибсон'}
    flag = True
    while flag:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] >= 1:
                for key, val in slov.items():
                    vk.method("messages.send", {"peer_id": id, "message": "угадай, кто это", "attachment": key, "random_id": 0})
                    if value in body.lower():
                        vk.method("messages.send", {"peer_id": id, "message": "привильно!", "random_id": random.randint(1, 2147483647)})
                    elif 'конец' in body.lower():
                        flag = False

        except Exception as E:
            time.sleep(1)

token = 'a938c4126562ab4333e9cee5c4237ddbf1fff2d6994ebeccb4bc591672cb696d854099ed9ea26b3aa328f'
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()
 
spis = []
for i in range(100):
    spis.append(i)
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if 'привет' in body.lower():
                vk.method("messages.send", {"peer_id": id, "message": "TEST", "attachment": "photo316186679_457241733", "random_id": 0})
            elif body.lower() == "как дела":
                vk.method("messages.send", {"peer_id": id, "message": "нормально", "random_id": 0})
            elif "игра" in body.lower():
                game()
            elif 'лох' in body.lower():
                vk.method("messages.send", {"peer_id": id, "message": "сам ты лох", "random_id": 0})
            elif ' и ' in body.lower():
                vk.method("messages.send", {"peer_id": id, "message": 'совместимость имен {}%'.format(random.choice(spis)), "random_id": 0})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "напиши мне словр ИГРА и попробуй отгадать знаменитость, а чтобы закончить игру, напиши слово КОНЕЦ", "random_id": 0})
    except Exception as E:
        time.sleep(1)
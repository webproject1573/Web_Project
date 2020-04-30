import vk_api
import time
import random



token = '41537d52b3ae7e31d9e49f9310e16b958d1a8b3ff00ad2cc1e785ffbf465d1f608ebf50c82974869f097a'
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if 'привет' in body.lower():
                vk.method("messages.send", {"peer_id": id, "message": "привет", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как дела":
                vk.method("messages.send", {"peer_id": id, "message": "нормально", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я тебя не понимаю", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
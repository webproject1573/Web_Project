import vk_api
import time
import random

rpg= {'Monster Hunter Freedom Unite - Существует легенда, будто много веков назад леса и равнины \n'
 'населяли исполинские чудовища, чья сила и свирепость могла сравниться только с их кровожадностью. \n'
 'Люди не смели приближаться к монстрам, но, даже соблюдая предельную осторожность, становились добычей \n'
 'могучих хищников.Так было, пока не пришли таинственные Охотники, наделенные неслыханной ловкостью, \n'
 ' хорошо вооруженные, отважные и дерзкие. Долгие годы они выслеживали и убивали чудовищ, а когда от \n '
 'последних не осталось и следа, сами исчезли, став героями детских сказок. Однако ходят слухи, что есть \n' 
 ' еще на свете земли, где можно встретить Охотников — и их смертельно опасную добычу…': 
'https://cloud.mail.ru/public/G4xs/Jws3SVjSj', 
'The Lord of the Rings: Tactics - Действие игры разворачивается во время Войны Кольца. Вас ждет отчаянное \n'
' путешествие в сердце Мордора, где в центре огромной пещеры бурлит адский котел. Лишь утопив Кольцо в \n' 
'кипящей магме, можно вернуть мир и покой в Средиземье. Но если вы устали от торжества добра, переметнитесь \n'
' в ряды сауроновых войск, возглавьте экспедицию по ликвидации Братства Кольца!': 'https://yadi.sk/d/5vEavYqpc6zjM', 
'God Eater 2 - Действие игры происходит спустя 3 года после событий God Eater Burst. Дальневосточный регион \n '
'оказался под воздействие пандемии, вызванной "Red Rain", и члены специального отряда Blood призваны провести \n '
' расследование.Используя уникальные способности, огнестрельное и холодное оружие, протагонисты God Eater 2 \n'
'сражаются с различными противниками.': 'https://yadi.sk/d/yDw1Pv3-Co4b7',
 'Marvel: Ultimate Alliance 2 - Лучшие герои и опаснейшие злодеи всех времен возвращаются в Marvel: \n '
 'Ultimate Alliance 2. Вторая часть знаменитого боевика с элементами ролевой игры Marvel: \n '
 'Ultimate Alliance — это еще более зрелищные схватки и рискованные приключения в компании \n' 
 ' знаменитых персонажей комиксов Marvel.': 'https://yadi.sk/d/oNs_D_VR65v1E',
  'Dungeon Siege: Throne of Agony - это настоящая легенда, ставшая идеальным продолжением истории \n'
  'Diablo. У неё есть несколько эпизодов, которые уже успели покорить аудиторию прямо-таки идеальным\n'
  ' исполнением. Очень много захватывающих моментов, хватает сюрпризов, много неожиданного. Есть герои,\n'
  ' которых никак нельзя назвать похожими друг на друга': 'https://yadi.sk/d/K1TeMV1y65WLW'}
spis_rpg = ['Monster Hunter Freedom Unite', 'The Lord of the Rings: Tactics', 'God Eater 2', 'Marvel: Ultimate Alliance 2', 'Dungeon Siege: Throne of Agony']

arc = {'LittleBigPlanet - Здесь перед тобой открывается мир невероятного количества возможностей.\n'
' У игры есть портативная версия, которая унаследовала все базовые достоинства. Мир на удивление красочный,\n'
' персонажи радуют тем, какие они милые. Имеется возможность заниматься созиданием столько, сколько \n'
'это возможно. Ограничения – исключительно на уровне фантазии игрока.': 'https://yadi.sk/d/mqcqDDVu6i0zA',
 'LocoRoco 2 - Жизнерадостные «пузыри» LocoRoco возвращаются! Однако наслаждаться миром и спокойствием \n' 
 'им вновь мешают злые Моджа. Как спасти удивительный красочный мир и одолеть захватчиков? Конечно, с вашей\n'
 ' помощью: умело управляя веселыми шарообразными существами, вы приведете их к победе и справитесь со\n'
 ' всеми врагами. Чтобы заставить малышей двигаться, нужно кренить их мир в разные стороны — такое необычное\n'
 ' управление делает вселенную LocoRoco уникальной.': 'https://yadi.sk/d/D9Ad8OcdNDZ6t',
  'История игрушек 3: Большой побег / Toy Story 3 - Переживите заново лучшие моменты фильма История игрушек:\n'
  ' Большой побег вместе с любимыми героями: астронавт, ковбой, красавица и пришелец (и все-все-все) должны \n'
  ' найти новый смысл жизни после того, как их выросший любимый хозяин уезжает учиться в колледж.': 'https://yadi.sk/d/0O-8wuhGbNL7y',
   'Worms: Открытая война 2 - Захватывающие приключения забавных вояк в эксклюзивном проекте для PSP Worms: \n' 
   'Open Warfare не могли обойтись без продолжения. Worms: Open Warfare 2 заимствовала у предшественника \n '
   'все лучше и сдобрила привычные действия дополнительными возможностями. В новой игре появилась интересная \n '
   'одиночная кампания и свежие режимы коллективных баталий: Rope Race и Fort.': 'https://yadi.sk/d/tc60zR0Ebcus3'}
spis_arc = ['LittleBigPlanet', 'LocoRoco 2', 'История игрушек 3', 'Worms: Открытая война 2']   

adv = {'Grand Theft Auto: Истории Вайс-Сити - Симулятор жизни в 80-х. Не считаясь с полицией, бандитские \n'
'группировки боролись за отдельные районы, промышляли рэкетом и грабежами. В их среде Вик почувствовал себя \n'
'более-менее привычно: оружие и мышцы здесь оказались в цене. Но Вэнс не был бы Вэнсом, удовлетворись он \n'
'местом «шестерки» в кровожадной шайке. Вик начинает восхождение на вершину криминального Олимпа, однако \n'
'ему нужна помощь — ваша помощь!': 'https://yadi.sk/d/nXccGm3EbU5tc', 
'TEKKEN 6 - Хук, апперкот, удар с разворота, подкат, прыжок, удар в приседе-герои Tekken 6 осыпают друг друга\n'
' градом приемов,молниеносно выполняя трюки,от которых закружится голова даже у бывалых акробатов.Новая игра \n'
'впитала в себя все лучшее,что было в серии,и значительно продвинула легендарные виртуальные драки вперед, \n'
'навстречу к совершенству.': 'https://yadi.sk/d/lKspyM-x6AT14',
 'God of War: Призрак Спарты / God of War: Ghost of Sparta - Отправляйтесь вместе с Кратосом путешествовать \n'
 'по мрачному и жестокому миру греческих богов и узнайте, какие тайны скрывает прошлое героя. Почувствуйте \n'
 'силу нового оружия, освойте новые приемы и движения и погрузите мир в пучины хаоса.': 'https://yadi.sk/d/deAEtHZfbU2sQ', 
 'Dante’s Inferno - Вас ждет грандиозное путешествие по девяти кругам ада. Какой путь вы выберете? Добродетели\n'
 ' и искупления - или мщения и вечных мук?': 'https://yadi.sk/d/rMp47E_oAezfm', 
 'Silent Hill: Shattered Memories - Вам снова предстоит исполнить роль Гарри Мэнсона в новой реинкарнации игры \n'
 'Silent Hill.Вас ждет уникальная в своем роде игра с захватывающим сюжетом, где каждое ваше решение и каждое \n'
 'ваше действие могут иметь необратимые последствия.': 
 'https://yadi.sk/d/yqzf2UMxbAZAJ',
  'Sonic Rivals 2 - Приключения Супер-ежика продолжаются! Старые враги вернулись, чтобы раз и навсегда уничтожить \n'
  'героя, а вместе с ним и весь мир. Ужасные создания Эггмана Нега, смертельные ловушки и коварные заговорщики встали \n'
  ' на пути отважного Соника. Но ничто не в силах остановить самого быстрого ежа, тем более когда речь идет о \n'
  'спасении друзей!': 'https://yadi.sk/d/461md9k1bxwjV'}
spis_adv = ['Grand Theft Auto', 'TEKKEN 6', 'God of War', 'Dante’s Inferno', 'Silent Hill', 'Sonic Rivals 2']

print('Введите токен:')
tok = input()
token = tok
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if 'привет' in body.lower():
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Я настоящий специалист по играм для psp! какую игру ты хочешь скачать(рпг, приключения, аркада)?", "random_id": 0})
            elif body.lower() == "как дела":
                vk.method("messages.send", {"peer_id": id, "message": "нормально", "random_id": 0})
            elif "rpg" in body.lower() or 'рпг' in body.lower():
                m = random.choice(spis_rpg)
                for key, val in rpg.items():
                    if m in key:
                        vk.method("messages.send", {"peer_id": id, "message": "{}  А скачать игру можно тут: {}".format(key, val), "random_id": 0})
                        break
                    else:
                        continue

            elif 'аркада' in body.lower():
                k = random.choice(spis_arc)
                for key, val in arc.items():
                    if k in key:
                        vk.method("messages.send", {"peer_id": id, "message": '{}  А скачать игру можно тут: {}'.format(key, val), "random_id": 0})
                        break
                    else:
                        continue
            elif 'adventure' in body.lower() or 'приключения' in body.lower():
                f = random.choice(spis_adv)
                for key, val in adv.items():
                    if f in key:
                        vk.method("messages.send", {"peer_id": id, "message": '{}  А скачать игру можно тут: {}'.format(key, val), "random_id": 0})
                        break
                    else:
                        continue

            else:
                vk.method("messages.send", {"peer_id": id, "message": "выбери жанры игр для psp(рпг, аркада, приключения)", "random_id": 0})
    except Exception as E:
        time.sleep(1)
from instapy import InstaPy

username = input('Введите ваше имя в insagram =>')
password = input('Введите пароль =>')
hashtag = input('введите хештег =>')

try:
	session = InstaPy(username=username, password=password)  #headless_browser=True
	session.login()
	session.like_by_tags([hashtag], amount=5)
	session.set_dont_like(["naked", "nsfw"])
	session.set_do_follow(True, percentage=100)
except:
	print('Возможно вы ввели некорректное имя пользователя или пароль, удостоверьтесь, что у вас установлен Firefox и есть интернет-соединение и попробуйте еще раз!')
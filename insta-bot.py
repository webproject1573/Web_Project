from instapy import InstaPy

username = input('Введите ваше имя в insagram =>')
password = input('Введите пароль =>')
hashtag = input('введите хештег =>')
def bot():
	try:
		session = InstaPy(username=str(username), password=str(password))  #headless_browser=True
		session.login()
		session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                             	peak_likes_daily=585,
                              	peak_comments_hourly=21,
                              	peak_comments_daily=182,
                               	peak_follows_hourly=48,
                               	peak_follows_daily=None,
                                	peak_unfollows_hourly=35,
                                	peak_unfollows_daily=402,
                                 	peak_server_calls_hourly=None,
                                 	peak_server_calls_daily=4700)
		for i in range(20):
			session.like_by_tags([hashtag], amount=5)
			session.set_dont_like(["naked", "nsfw"])
			try:
				session.set_do_follow(True, percentage=100)
			except:
				print('Что то пошло не по плану!')
			try:
				session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])
			except:
				print('Что то пошло не по пану!')
			session.set_do_like(enabled=True, percentage=100)
	except:
		print('Возможно вы ввели некорректное имя пользователя / пароль или хэштег, удостоверьтесь, что у вас установлен Firefox(обязательно) и есть интернет-соединение и попробуйте еще раз!')

bot()
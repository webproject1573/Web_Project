from instapy import InstaPy
from selenium import webdriver
 

driver = webdriver.Firefox('C:\\files\\geckodriver.exe')
driver.get("http://www.google.com")

session = InstaPy(username="*****", password="*****")
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
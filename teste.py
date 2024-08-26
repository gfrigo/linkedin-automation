#pylint: disable-all

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=pt-BR')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument(r"user-data-dir=C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument('profile-directory=Profile 1')

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)
sleep(5)
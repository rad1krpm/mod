# {{Load library

# External library
import random
import sys
import re
import requests
import datetime as dt
import os
import pathlib
import urllib
import urllib.parse
import urllib.request
import urllib.error
import openpyxl
import youtube_dl as yd
import schedule
import time
import pyautogui as pg
import json
import subprocess
import pyperclip as pc
import win32gui
import win32con
import tenacity
from lxml import html
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException as te
from PIL import Image
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed, wait_exponential

# }}Load library

# --------------------------------------------------------------------------------------------------------------------------------

# {{Explanation

# }}Explanation

# --------------------------------------------------------------------------------------------------------------------------------

# {{Variable definition

# Specifies value of 'sleep_time'
sleep_time = 1

# Specifies value of 'wait_time'
wait_time = 10

# }}Variable definition

# --------------------------------------------------------------------------------------------------------------------------------

# {{Function definition

# ------------------------------------

# {{Explanation：Replace forbidden characters


# Definition
def kinsoku(orig_text):
    deriv_text = orig_text.translate(str.maketrans({'¥': '￥', '/': '／', ':': '：', '*': '＊', '?': '？', '"': '”', '<': '＜', '>': '＞', '|': '｜', '': '', '.': '．', '…': '．．．'}))
    return deriv_text


# Remark
'''
最後の文字が「'\'」の場合はエラーが起こる
'''

# }}

# ------------------------------------

# {{Explanation：Write data to 'info.json'


# Definition
def write_info(folder, info_data):
    # load contents of 'info.json'
    info_file = open(folder + '/info.json', 'r', encoding='utf-8')
    load_info_file = json.load(info_file)
    info_file.close()
    # Write data to 'info.json'
    info_file = open(folder + '/info.json', 'w', encoding='utf-8')
    json.dump(load_info_file | info_data, info_file, indent=2, ensure_ascii=False)
    info_file.close()


# }}

# ------------------------------------

# {{Explanation：Decode URL if it is written in 'percent-encoding'


# Definition
def url_unquote(url):
    while '%' in url:
        url = urllib.parse.unquote(url)
    return str(url)


# }}

# ------------------------------------

# {{Explanation：Output 'start time' and 'finish time'


# Definition
def stime():
    print('開始：' + str(dt.datetime.now()))


def ftime():
    print('終了：' + str(dt.datetime.now()))


# }}

# ------------------------------------

# {{Explanation：Retry 'requests' process


# Definition
@retry(wait=wait_fixed(10), stop=stop_after_attempt(10))
def retry_requrl(requrl):
    if requrl.status_code != 200:
        time.sleep(sleep_time)  # Wait for specified time
        requrl
        time.sleep(sleep_time)  # Wait for specified tim
        print('retry')
        print(requrl.url)
        raise Exception
    else:
        return requrl


# }}

# --------------------------------------------------------------------------------------------------------------------------------

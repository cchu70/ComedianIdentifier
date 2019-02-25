from lxml import html
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient
import logging
import random
import os
import csv
from lib import test_client

# test_client = MongoClient(
#     host='humor1.vip.gatech.edu',
#     port=3306,
#     username='comedian_monologues',
#     password='BlENteRsEWROmbERaInG',
#     authSource='hgp_comedian_monologues',
#     authMechanism='SCRAM-SHA-1'
# )
def insert_example(table, id, name):

    table.insert_one({
        'uid': id,
        'comedianName': name,
        'gottenTranscript': False
    })
    # logger.info('Content after example insert')
    # for record in youtube_table.find():
    #     print(record)


def searchKeyword(table, keyword):
    print(keyword)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    current_dir = os.getcwd()
    browser = webdriver.Chrome(options = chrome_options, executable_path = f"{current_dir}/chromedriver")
    print(keyword[0])
    search_url = "https://www.youtube.com/results?search_query={}".format('+'.join(keyword[0].split())+'+Monologues')
    browser.get(search_url)
    js="var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(15)

    h = browser.page_source
    sel = html.fromstring(h)

    uids = []
    # f = open("uid.txt", "a")

    # htmlText = urllib.urlopen(jimmy_fallon_main).read()
    # con = requests.get(jimmy_fallon_main).content.decode('utf-8')

    for tag in sel.xpath('//a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]'):
        # retrieve the video uid
        for i in tag.xpath('@href'):
            id = i.split('=')[1][ :11]
            print(id)
            if id not in uids:
                uids.append(id)
                insert_example(table, id, keyword[0])

    # print(uids)
    # for i in uids:
    #     if i is not None:
    #         f.write(str(i) + "\n")
    # f.close()

if __name__ == '__main__':
    current_dir = os.getcwd()
    print(f"{current_dir}/chromedriver")
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as key:
            logger = logging.getLogger(__name__)
            youtube_table = test_client['hgp_comedian_monologues']['youtube_monologues_uid']
            logger.info('Content before example insert')
            csv_reader = csv.reader(key)
            for line in csv_reader:
                searchKeyword(youtube_table, line)
    else:
        print("Please give a csv file")

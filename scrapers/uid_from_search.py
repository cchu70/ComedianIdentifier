from lxml import html
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def searchKeyword(keyword):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    search_url = "https://www.youtube.com/results?search_query={}".format('+'.join(keyword.split()))
    browser.get(search_url)
    js="var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(20)

    h = browser.page_source
    sel = html.fromstring(h)

    uids = []
    f = open("uid.txt", "w")

    # htmlText = urllib.urlopen(jimmy_fallon_main).read()
    # con = requests.get(jimmy_fallon_main).content.decode('utf-8')

    for tag in sel.xpath('//a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]'):
        # retrieve the video uid
        for i in tag.xpath('@href'):
            id = uids.append(i.split('=')[1][0:11])
            if id not in uids:
                uids.append(id)
    print(uids)
    for i in uids:
        if i is not None:
            f.write(str(i) + "\n")
    f.close()

if __name__ == '__main__':
    print("Please type in the search keyword.")
    keyword = input()
    searchKeyword(keyword)




import requests
import os
from lxml import etree
import threading
from time import sleep

def download_image(path):
    name = path[path.rfind('/')+1: ]
    print('Downloading  ' + name + '......')
    html = requests.get(path)
    with open('2k/' + name, 'wb') as f:
        f.write(html.content)

 
if __name__ == '__main__':
    url = 'https://wallpaperaccess.com'
    html = requests.get(url + '/2k')
    # content = etree.parse(html, etree.HTMLParser())
    content = etree.HTML(html.content)

    hrefs = content.xpath("//div[@class='wrapper']/a/img")
    # Element 有属性tag, attrib, text
    if not os.path.exists('2k'):
        os.makedirs('2k')
    for href in hrefs:
        src = href.attrib['data-src']
        t = threading.Thread(target=download_image, args=(url+src, ))
        print(threading.active_count())
        while threading.active_count() > 8:
            sleep(1)
        else:
            t.start()
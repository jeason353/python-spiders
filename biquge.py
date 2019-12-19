# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

if __name__=='__main__':
    #所要爬取的小说主页，每次使用时，修改该网址即可，同时保证本地保存根路径存在即可
    target="https://www.biqiugex.com/book_4275"
    #笔趣阁网站根路径
    index_path='https://www.biqugex.com'

    html=requests.get(url=target)
    #查看htmluest默认的编码，发现与网站response不符，改为网站使用的gdk
    print(html.encoding)
    # html.encoding = 'gbk'
    #解析html
    content = etree.HTML(html.content)
    book_name = content.xpath("//meta[@property='og:novel:book_name']/@content")[0]
    # print(book_name)

    if not os.path.exists(book_name):
        os.makedirs(book_name)

    hrefs = content.xpath("//dd/a")
    for href in hrefs:
        chapter_html = requests.get(index_path + href.attrib['href'])
        chapter_content = etree.HTML(chapter_html.content)
        brs = chapter_content.xpath("//div[@class='showtxt']//br")
        
        with open(book_name + '/' + href.text + '.txt', 'w', encoding='utf-8') as f:
            for br in brs:
                if br.tail is not None:
                    f.write(br.tail + '\n')

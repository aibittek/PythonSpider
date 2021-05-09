# -*- coding: utf-8 -*-
import urllib.request
import bs4

res = urllib.request.urlopen("https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = bs4.BeautifulSoup(res,"html.parser")
book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print(book.string)
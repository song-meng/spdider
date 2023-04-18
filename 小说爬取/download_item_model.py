
import multiprocessing
import os
import threading
from time import sleep

import requests
from PyQt6.QtCore import QObject
from pyquery import PyQuery

from my_thread import MyThread


class DownloadItem:
    def __init__(self, novelTitle, site, url, downloadPath, count, articles):
        self.lock = threading.Lock()
        self.novelTitle = novelTitle
        self.articles = articles
        self.url = url
        self.site = site
        self.downloadPath = downloadPath
        self.downloading = False
        self.finish = False
        self.signal = MyThread()
        self.current = 0
        self.total = count
        self.downloadAction()

    def increment(self):
        self.lock.acquire()
        self.current += 1
        self.lock.release()
        self.signal.emit()
        pass

    def downloadAction(self):
        self.downloading = True
        pool = multiprocessing.Pool(processes=10)
        print('start')
        path = self.downloadPath
        for item in self.articles:
            pool.apply(self.writeNovel, args=(item.novelPath, item.novelTitle, path,))
        pass

    def writeNovel(self, articleUrl, name, tempPath):
        print(articleUrl)
        sleep(10)
        return '1'
        #
        # novel = tempPath + '/' + name.strip() + ".txt"
        # if os.path.exists(novel):
        #     return
        # html = requests.get(articleUrl).content
        # doc = PyQuery(html)
        # items = doc(".box_con").items()
        # for item in items:
        #     content = item.find("#content").remove('br:nth-child(2n)').text()
        #     text = name + "\n" + content + '\n'
        #     try:
        #         with open(novel, "w", encoding="utf-8") as file:
        #             file.write(text)
        #             file.close()
        #             # self.increment()
        #     except Exception as e:
        #         print('错误 :', e)
        # return

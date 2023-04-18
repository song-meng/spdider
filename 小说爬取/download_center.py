import multiprocessing
import signal
import threading

import requests
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMessageBox
from pyquery import PyQuery

from config.config import MyConfig
from download_item_model import DownloadItem
from model.noveli_model import NovelModel
from my_thread import MyThread


class DownloadCenter(object):

    def __init__(self, updateList):
        self.novels = []
        self.signal = MyThread()
        self.signal.connect(updateList)
        pass

    downloadPath = ''

    def addDownload(self, searchItem):
        for item in self.novels:
            if item.url == searchItem.url:
                QMessageBox.warning(None, '小说下载', '已经在下载列表中了',)
                return
        html = requests.get(url=searchItem.url, headers=MyConfig().UA).content
        doc = PyQuery(html)
        ori_items = doc("dl dd")
        count = len(ori_items)
        items = ori_items.items()
        results = []
        for item in items:
            url = item.find("a").attr("href")
            name = item.find("a").text().replace('/', '-')
            novel_url = searchItem.searchHost + url
            results.append(NovelModel(novelTitle=name, novelPath=novel_url))

        download_item = DownloadItem(novelTitle=searchItem.articleTitle, articles=results, site=searchItem.site, url=searchItem.url, downloadPath=self.downloadPath, count=count)
        self.novels.append(download_item)
        self.signal.emit()
        pass



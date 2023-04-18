import requests
from pyquery import PyQuery

from config.config import MyConfig

from model.search_item import SearchItem


class SearchLogic(object):
    def __init__(self):
        self.resultList = []

    def search(self, articleName, index):
        if index == 0:
            return self._beganSearch(articleName, MyConfig().resourceList[index].sourceAddress)
        if index == 1:
            return self._beganSearch2(articleName, MyConfig().resourceList[index].sourceAddress)

    # https://www.qxzx8.com/ 处理搜索
    def _beganSearch(self, articleName, path):
        novel_list = []
        try:
            url = path + '/search.php?keyword=' + articleName
            print(url)
            html = requests.get(url=url, headers=MyConfig().UA).content
            doc = PyQuery(html)
            items = doc('.result-list .result-item').items()

            for item in items:
                pic = path + item('.result-game-item-pic-link-img').attr('src')
                article_title = item('.result-game-item-title-link').attr('title')
                author = item('.result-game-item-info .result-game-item-info-tag:nth-child(1) :nth-child(2)').text()
                date = item('.result-game-item-info .result-game-item-info-tag:nth-child(3) :nth-child(2)').text()
                last = item('.result-game-item-info .result-game-item-info-tag:nth-child(4) :nth-child(2)').text()
                article_url = path + item('.result-item-title a').attr('href')
                novel_list.append(SearchItem(searchHost=path, site=path, articlePic=pic, articleTitle=article_title, lastChapters=last, updateDate=date, url=article_url, author=author))
        except Exception as e:
            print(e)
        finally:
            return novel_list

    # https://www.biqugeg.cc/ 处理搜索
    def _beganSearch2(self, articleName, path):
        print(articleName, path)

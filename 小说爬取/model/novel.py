import os
import shutil
import multiprocessing

import requests
from pyquery import PyQuery

UA = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Proxy-Connection': 'keep-alive'}


# 下载对应章节txt文件
def write_novel(URL, name, tempPath, i, t):
    novel = tempPath + '/' + name.strip() + ".txt"
    print("\r", end="", flush=True)
    print("\r下载进度: {}%".format(round(i / t * 100, 2)), end='', flush=True)
    if os.path.exists(novel):
        return
    html = requests.get(URL).content
    doc = PyQuery(html)
    items = doc(".box_con").items()
    for item in items:
        content = item.find("#content").remove('br:nth-child(2n)').text()
        text = name + "\n" + content + '\n'
        try:
            with open(novel, "w", encoding="utf-8") as file:
                file.write(text)
                file.close()
        except Exception as e:
            print('错误 :', e)


def startArticle():
    try:
        # 获取每章节url
        UA = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"}
        url = "https://www.qxzx8.com/book/2670/"
        html = requests.get(url=url, headers=UA).content
        doc = PyQuery(html)
        items = doc("dl dd").items()
        title = doc("#maininfo #info h1").text()
        i = 0
        t = len(doc("dl dd"))
        print(t)
        pool = multiprocessing.Pool(processes=10)
        path = articlePath + title
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print('文件夹创建成功：', path)
        else:
            print('文件夹已经存在：', path)
        for item in items:
            i += 1
            url = item.find("a").attr("href")
            name = item.find("a").text().replace('/', '-')
            URL = "https://www.qxzx8.com" + url
            pool.apply_async(write_novel, (URL, name, path, i, t))
        pool.close()
        pool.join()
        items = doc("dl dd").items()
        for item in items:
            name = item.find("a").text().replace('/', '-', )
            try:
                with open(articlePath + title.strip() + ".txt", "a", encoding="utf-8") as file:
                    with open(path + '/' + name + '.txt', 'r', encoding="utf-8") as file2:
                        file.write(file2.read())
            except Exception as e:
                print('合并出错:', e)
        shutil.rmtree(path + '/')
        print("\r下载进度: 100%", end='', flush=True)
        print('下载完成')
    except KeyboardInterrupt:
        print("\n写入终止")
        pool.close()


# 下载对应章节txt文件
def write_novel2(URL, name, tempPath, i, t):
    novel = tempPath + '/' + name.strip() + ".txt"
    print("\r", end="", flush=True)
    print("\r下载进度: {}%".format(round(i / t * 100, 2)), end='', flush=True)
    if os.path.exists(novel):
        return
    try:
        html = requests.get(URL, headers=UA).content
        doc = PyQuery(html)
        items = doc(".content").items()
        for item in items:
            content = item.find("#content").remove('br:nth-child(2n)').remove('script').remove('.read2').text()
            text = name + "\n" + content + '\n'
            with open(novel, "w", encoding="utf-8") as file:
                file.write(text)
                file.close()
    except Exception as e:
        print('错误 :', e)


def startArticle2():
    try:
        # 获取每章节url
        url = "https://www.biqugeg.cc/94156_94156911/"
        html = requests.get(url=url, headers=UA).content
        doc = PyQuery(html)
        orignalItems = doc(".listmain dl dt:nth-of-type(2)").next_all()
        items = orignalItems.items()
        title = doc(".book .info h2").text()
        print(title)
        i = 0
        t = len(orignalItems)
        print(t)
        pool = multiprocessing.Pool(processes=10)
        path = articlePath + title
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print('文件夹创建成功：', path)
        else:
            print('文件夹已经存在：', path)
        for item in items:
            i += 1
            url = item.find("a").attr("href")
            name = item.find("a").text().replace('/', '-')
            URL = "https://www.biqugeg.cc" + url
            pool.apply_async(write_novel2, (URL, name, path, i, t))
        pool.close()
        pool.join()
        items = orignalItems.items()
        for item in items:
            name = item.find("a").text().replace('/', '-', )
            try:
                with open(articlePath + title.strip() + ".txt", "a", encoding="utf-8") as file:
                    with open(path + '/' + name + '.txt', 'r', encoding="utf-8") as file2:
                        file.write(file2.read())
            except Exception as e:
                print('合并出错:', e)
        shutil.rmtree(path + '/')
        print("\r下载进度: 100%", end='', flush=True)
        print('\n下载完成')
    except Exception as e:
        print("\n写入终止:", e)


if __name__ == "__main__":
    global articlePath
    articlePath = '/Users/sm/Documents/xiaoshuo/'
    # https://www.qxzx8.com
    # startArticle()
    # https://www.biqugeg.cc
    startArticle2()

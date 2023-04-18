from model.source_item import SourceItem


class MyConfig:
    def __init__(self):
        self.resourceList = [
            SourceItem(sourceTitle='笔趣阁1', sourceAddress='https://www.qxzx8.com'),
            SourceItem(sourceTitle='笔趣阁2', sourceAddress='https://www.biqugeg.cc')
        ]
        self.UA = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Proxy-Connection': 'keep-alive',
            'accept': 'text/html'
        }

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    __instance = None

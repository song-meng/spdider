from PyQt6.QtWidgets import QWidget

from ui import articleItem


class ArticleItemLogic(QWidget, articleItem.Ui_articleItem):
    def __init__(self, searchItem, downloadCenter):
        super(ArticleItemLogic, self).__init__()
        self.setupUi(self)
        self.updateData(searchItem)
        self.setMouseTracking(False)
        self.searchItem = searchItem
        self.downloadCenter = downloadCenter
        pass

    def updateData(self, searchItem, ):
        self.novelLabel.setText(searchItem.articleTitle)
        self.lastLabel.setText(searchItem.lastChapters)
        self.authorLabel.setText(searchItem.author)
        # req = requests.get(searchItem.articlePic)
        # pic = QPixmap()
        # pic.loadFromData(req.content)
        # self.imageLabel.setPixmap(pic)
        self.downloadBtn.clicked.connect(self.downloadAction)
        pass

    def downloadAction(self):
        print(self.searchItem.articleTitle)
        self.downloadCenter.addDownload(self.searchItem)
        pass


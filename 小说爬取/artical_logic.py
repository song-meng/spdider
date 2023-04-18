import os

from PyQt6.QtCore import QSize, pyqtSlot, QObject
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem

from download_item_logic import DownloadItemLogic
from ui import artical
from article_item_logic import ArticleItemLogic

from config.config import MyConfig
from download_center import DownloadCenter

from search_logic import SearchLogic


class MyWindow(QMainWindow, artical.Ui_root):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_bind()
        self.init_comboBox()
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.searchText = ''
        self.savePath = self.cwd
        self.label.setText(self.savePath)
        self.result_list = []
        self.downloadCenter = DownloadCenter(self.updateList)
        self.downloadCenter.downloadPath = self.savePath
        pass

    def init_comboBox(self):
        for item in MyConfig().resourceList:
            self.siteChoose.addItem(item.sourceTitle, userData=item)
        pass

    def init_bind(self):
        self.searchButton.clicked.connect(self.searchBtnClick)
        self.searchButton.setDisabled(True)
        self.resetButton.clicked.connect(self.resetBtnClick)
        self.pathButton.clicked.connect(self.pathBtnClick)
        self.searchEdit.textEdited.connect(self.searchEdited)
        pass

    def searchEdited(self):
        self.searchText = self.searchEdit.text()
        if len(self.searchText) == 0:
            self.searchButton.setDisabled(True)
        else:
            self.searchButton.setEnabled(True)
        pass

    def pathBtnClick(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.cwd)  # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        print(dir_choose)
        self.savePath = dir_choose
        self.label.setText(dir_choose)
        self.downloadCenter.downloadPath = self.savePath
        pass

    def resetBtnClick(self):
        self.resultListview.clear()
        self.searchText = ''
        self.searchEdit.clear()
        self.searchEdit.clearFocus()
        pass

    def searchBtnClick(self):
        self.resultListview.clear()
        result = SearchLogic().search(self.searchText, self.siteChoose.currentIndex())
        print(len(result))
        for item in result:
            a = QListWidgetItem()
            a.setForeground(QColor('white'))
            widget = ArticleItemLogic(searchItem=item, downloadCenter=self.downloadCenter)
            # widget.setStyleSheet('background-color: rgb(223, 25, 55)')
            a.setSizeHint(QSize(400, 100))
            self.resultListview.addItem(a)
            self.resultListview.setItemWidget(a, widget)
        pass

    def updateList(self):
        self.downloadList.clear()
        for item in self.downloadCenter.novels:
            download_item = DownloadItemLogic(model=item)
            a = QListWidgetItem()
            a.setForeground(QColor('white'))
            a.setSizeHint(QSize(310, 60))
            self.downloadList.addItem(a)
            self.downloadList.setItemWidget(a, download_item)
        pass

    def updateIndex(self, index=int):
        item = self.downloadList.itemWidget(self.downloadList.itemFromIndex(index))
        item.refreshWithModel(self.downloadCenter.novels[index])
        pass

    def __del__(self):
        print('__del__')
        pass

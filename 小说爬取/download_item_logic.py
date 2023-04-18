from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget

from download_item_model import DownloadItem
from ui import download_item


class DownloadItemLogic(QWidget, download_item.Ui_Form):
    def __init__(self, model=DownloadItem, parent=None):
        super(DownloadItemLogic, self).__init__(parent)
        self.model = model
        self.model.signal.connect(self.refresh)
        self.setupUi(self)
        self.retranslateUi(self)
        # self.actionBtn.clicked.connect(self.model.downloadAction)
        self.refresh()
        pass

    def refresh(self):
        self.progressBar.setMaximum(self.model.total)
        self.articleTitle.setText(self.model.novelTitle)
        if self.model.downloading:
            self.actionBtn.setText('暂停')
        else:
            self.actionBtn.setText('开始')
        if self.model.finish:
            self.actionBtn.setText('完成')
        self.progressLabel.setText('{}/{}'.format(self.model.current, self.model.total))
        self.progressBar.setValue(self.model.current)
        pass

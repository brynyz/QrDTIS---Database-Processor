from ui_MainAppWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainAppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QrDTIS")

        self.iconNameWidget.setHidden(True)

        self.homeBtn.clicked.connect(self.switch_to_homePage)
        self.homeBtn_2.clicked.connect(self.switch_to_homePage)

        self.transactBtn.clicked.connect(self.switch_to_transactionsPage)
        self.transactBtn_2.clicked.connect(self.switch_to_transactionsPage)

        self.scanHistoryBtn.clicked.connect(self.switch_to_scanHistoryPage)
        self.scanHistoryBtn_2.clicked.connect(self.switch_to_scanHistoryPage)

        self.printBtn.clicked.connect(self.switch_to_printPage)
        self.printBtn_2.clicked.connect(self.switch_to_printPage)

        self.dbBtn.clicked.connect(self.switch_to_databasePage)
        self.dbBtn_2.clicked.connect(self.switch_to_databasePage)

        self.accountBtn.clicked.connect(self.switch_to_accountPage)
        self.accountBtn_2.clicked.connect(self.switch_to_accountPage)

        self.settingsBtn.clicked.connect(self.switch_to_settingsPage)
        self.settingsBtn_2.clicked.connect(self.switch_to_settingsPage)

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_transactionsPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_scanHistoryPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_printPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_databasePage(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_accountPage(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(6)

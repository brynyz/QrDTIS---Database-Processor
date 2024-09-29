# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 598)
        MainWindow.setStyleSheet(u"*{	\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(245, 250, 254)")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.icoWidget = QWidget(self.centralwidget)
        self.icoWidget.setObjectName(u"icoWidget")
        self.icoWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #25A244\n"
"}\n"
"\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icoWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.icoWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/icon/user.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.homeBtn = QPushButton(self.icoWidget)
        self.homeBtn.setObjectName(u"homeBtn")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(20, 20))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.homeBtn)

        self.transactBtn = QPushButton(self.icoWidget)
        self.transactBtn.setObjectName(u"transactBtn")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.transactBtn.setIcon(icon1)
        self.transactBtn.setIconSize(QSize(20, 20))
        self.transactBtn.setCheckable(True)
        self.transactBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.transactBtn)

        self.scanHistoryBtn = QPushButton(self.icoWidget)
        self.scanHistoryBtn.setObjectName(u"scanHistoryBtn")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icon/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scanHistoryBtn.setIcon(icon2)
        self.scanHistoryBtn.setIconSize(QSize(20, 20))
        self.scanHistoryBtn.setCheckable(True)
        self.scanHistoryBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scanHistoryBtn)

        self.printBtn = QPushButton(self.icoWidget)
        self.printBtn.setObjectName(u"printBtn")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icon/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.printBtn.setIcon(icon3)
        self.printBtn.setIconSize(QSize(20, 20))
        self.printBtn.setCheckable(True)
        self.printBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.printBtn)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 191, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dbBtn = QPushButton(self.icoWidget)
        self.dbBtn.setObjectName(u"dbBtn")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icon/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dbBtn.setIcon(icon4)
        self.dbBtn.setIconSize(QSize(20, 20))
        self.dbBtn.setCheckable(True)
        self.dbBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.dbBtn)

        self.accountBtn = QPushButton(self.icoWidget)
        self.accountBtn.setObjectName(u"accountBtn")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icon/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QSize(20, 20))
        self.accountBtn.setCheckable(True)
        self.accountBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.accountBtn)

        self.settingsBtn = QPushButton(self.icoWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QSize(20, 20))
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.logOutBtn = QPushButton(self.icoWidget)
        self.logOutBtn.setObjectName(u"logOutBtn")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icon/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutBtn.setIcon(icon7)
        self.logOutBtn.setIconSize(QSize(20, 20))
        self.logOutBtn.setCheckable(True)
        self.logOutBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.logOutBtn)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addWidget(self.icoWidget)

        self.iconNameWidget = QWidget(self.centralwidget)
        self.iconNameWidget.setObjectName(u"iconNameWidget")
        self.iconNameWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #25A244\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5F5FE;\n"
"	color: #208B3A;\n"
"	font-weight:  bold;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.iconNameWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.iconNameWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icon/user.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconNameWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.homeBtn_2 = QPushButton(self.iconNameWidget)
        self.homeBtn_2.setObjectName(u"homeBtn_2")
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setIconSize(QSize(20, 20))
        self.homeBtn_2.setCheckable(True)
        self.homeBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homeBtn_2)

        self.transactBtn_2 = QPushButton(self.iconNameWidget)
        self.transactBtn_2.setObjectName(u"transactBtn_2")
        self.transactBtn_2.setIcon(icon1)
        self.transactBtn_2.setIconSize(QSize(20, 20))
        self.transactBtn_2.setCheckable(True)
        self.transactBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.transactBtn_2)

        self.scanHistoryBtn_2 = QPushButton(self.iconNameWidget)
        self.scanHistoryBtn_2.setObjectName(u"scanHistoryBtn_2")
        self.scanHistoryBtn_2.setIcon(icon2)
        self.scanHistoryBtn_2.setIconSize(QSize(20, 20))
        self.scanHistoryBtn_2.setCheckable(True)
        self.scanHistoryBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.scanHistoryBtn_2)

        self.printBtn_2 = QPushButton(self.iconNameWidget)
        self.printBtn_2.setObjectName(u"printBtn_2")
        self.printBtn_2.setIcon(icon3)
        self.printBtn_2.setIconSize(QSize(20, 20))
        self.printBtn_2.setCheckable(True)
        self.printBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.printBtn_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_8 = QSpacerItem(20, 191, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dbBtn_2 = QPushButton(self.iconNameWidget)
        self.dbBtn_2.setObjectName(u"dbBtn_2")
        self.dbBtn_2.setIcon(icon4)
        self.dbBtn_2.setIconSize(QSize(20, 20))
        self.dbBtn_2.setCheckable(True)
        self.dbBtn_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.dbBtn_2)

        self.accountBtn_2 = QPushButton(self.iconNameWidget)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        self.accountBtn_2.setIcon(icon5)
        self.accountBtn_2.setIconSize(QSize(20, 20))
        self.accountBtn_2.setCheckable(True)
        self.accountBtn_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.accountBtn_2)

        self.settingsBtn_2 = QPushButton(self.iconNameWidget)
        self.settingsBtn_2.setObjectName(u"settingsBtn_2")
        self.settingsBtn_2.setIcon(icon6)
        self.settingsBtn_2.setIconSize(QSize(20, 20))
        self.settingsBtn_2.setCheckable(True)
        self.settingsBtn_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.settingsBtn_2)

        self.logOutBtn_2 = QPushButton(self.iconNameWidget)
        self.logOutBtn_2.setObjectName(u"logOutBtn_2")
        self.logOutBtn_2.setIcon(icon7)
        self.logOutBtn_2.setIconSize(QSize(20, 20))
        self.logOutBtn_2.setCheckable(True)
        self.logOutBtn_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.logOutBtn_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addWidget(self.iconNameWidget)

        self.MainMenu = QWidget(self.centralwidget)
        self.MainMenu.setObjectName(u"MainMenu")
        self.verticalLayout_7 = QVBoxLayout(self.MainMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.headerWidget = QWidget(self.MainMenu)
        self.headerWidget.setObjectName(u"headerWidget")
        self.horizontalLayout = QHBoxLayout(self.headerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuBtn = QPushButton(self.headerWidget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icon/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon8)
        self.menuBtn.setIconSize(QSize(20, 20))
        self.menuBtn.setCheckable(True)
        self.menuBtn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.menuBtn)

        self.lineEdit = QLineEdit(self.headerWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(True)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_7.addWidget(self.headerWidget)

        self.stackedWidget = QStackedWidget(self.MainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 161, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label.setFont(font1)
        self.stackedWidget.addWidget(self.homePage)
        self.transactionPage = QWidget()
        self.transactionPage.setObjectName(u"transactionPage")
        self.label_14 = QLabel(self.transactionPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 0, 301, 31))
        self.label_14.setFont(font1)
        self.stackedWidget.addWidget(self.transactionPage)
        self.scanHistoryPage = QWidget()
        self.scanHistoryPage.setObjectName(u"scanHistoryPage")
        self.label_12 = QLabel(self.scanHistoryPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 0, 301, 31))
        self.label_12.setFont(font1)
        self.stackedWidget.addWidget(self.scanHistoryPage)
        self.databasePage = QWidget()
        self.databasePage.setObjectName(u"databasePage")
        self.label_4 = QLabel(self.databasePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 301, 31))
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.databasePage)
        self.accoutnPage = QWidget()
        self.accoutnPage.setObjectName(u"accoutnPage")
        self.label_10 = QLabel(self.accoutnPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 301, 31))
        self.label_10.setFont(font1)
        self.stackedWidget.addWidget(self.accoutnPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_13 = QLabel(self.settingsPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 301, 31))
        self.label_13.setFont(font1)
        self.stackedWidget.addWidget(self.settingsPage)
        self.printReceiptPage = QWidget()
        self.printReceiptPage.setObjectName(u"printReceiptPage")
        self.label_11 = QLabel(self.printReceiptPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 301, 31))
        self.label_11.setFont(font1)
        self.stackedWidget.addWidget(self.printReceiptPage)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.MainMenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuBtn.toggled.connect(self.icoWidget.setHidden)
        self.menuBtn.toggled.connect(self.iconNameWidget.setVisible)
        self.printBtn.toggled.connect(self.printBtn_2.setChecked)
        self.scanHistoryBtn.toggled.connect(self.scanHistoryBtn_2.setChecked)
        self.transactBtn.toggled.connect(self.transactBtn_2.setChecked)
        self.homeBtn.toggled.connect(self.homeBtn_2.setChecked)
        self.dbBtn.toggled.connect(self.dbBtn_2.setChecked)
        self.accountBtn.toggled.connect(self.accountBtn_2.setChecked)
        self.settingsBtn.toggled.connect(self.settingsBtn_2.setChecked)
        self.logOutBtn.toggled.connect(self.logOutBtn_2.setChecked)
        self.homeBtn_2.toggled.connect(self.homeBtn.setChecked)
        self.transactBtn_2.toggled.connect(self.transactBtn.setChecked)
        self.scanHistoryBtn_2.toggled.connect(self.scanHistoryBtn.setChecked)
        self.printBtn_2.toggled.connect(self.printBtn.setChecked)
        self.dbBtn_2.toggled.connect(self.dbBtn.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn.setChecked)
        self.settingsBtn_2.toggled.connect(self.settingsBtn.setChecked)
        self.logOutBtn_2.toggled.connect(self.logOutBtn.setChecked)
        self.logOutBtn.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.homeBtn.setText("")
        self.transactBtn.setText("")
        self.scanHistoryBtn.setText("")
        self.printBtn.setText("")
        self.dbBtn.setText("")
        self.accountBtn.setText("")
        self.settingsBtn.setText("")
        self.logOutBtn.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.homeBtn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.transactBtn_2.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.scanHistoryBtn_2.setText(QCoreApplication.translate("MainWindow", u"Scan History", None))
        self.printBtn_2.setText(QCoreApplication.translate("MainWindow", u"Print Receipt", None))
        self.dbBtn_2.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.settingsBtn_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.logOutBtn_2.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Transactions Page", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Scan History Page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Database Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Account Page", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Print Receipt", None))
    # retranslateUi


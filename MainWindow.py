# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(600, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(300, 400))
        self.centralwidget.setMaximumSize(QSize(600, 800))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 50, 600, 800))
        self.widget.setMinimumSize(QSize(300, 400))
        self.widget.setMaximumSize(QSize(600, 800))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 491, 661))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contactList = QListView(self.verticalLayoutWidget)
        self.contactList.setObjectName(u"contactList")
        self.contactList.setMinimumSize(QSize(250, 300))
        self.contactList.setMaximumSize(QSize(550, 750))

        self.verticalLayout_2.addWidget(self.contactList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addContactButton = QPushButton(self.verticalLayoutWidget)
        self.addContactButton.setObjectName(u"addContactButton")

        self.horizontalLayout.addWidget(self.addContactButton)

        self.viewContactButton = QPushButton(self.verticalLayoutWidget)
        self.viewContactButton.setObjectName(u"viewContactButton")
        self.viewContactButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.viewContactButton)

        self.deleteContactButton = QPushButton(self.verticalLayoutWidget)
        self.deleteContactButton.setObjectName(u"deleteContactButton")
        self.deleteContactButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.deleteContactButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addContactButton.setText(QCoreApplication.translate("MainWindow", u"Add Contact", None))
        self.viewContactButton.setText(QCoreApplication.translate("MainWindow", u"View Contact", None))
        self.deleteContactButton.setText(QCoreApplication.translate("MainWindow", u"Delete Contact", None))
    # retranslateUi


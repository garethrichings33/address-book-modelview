# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contactwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ContactWindow(object):
    def setupUi(self, ContactWindow):
        if not ContactWindow.objectName():
            ContactWindow.setObjectName(u"ContactWindow")
        ContactWindow.resize(577, 478)
        self.centralwidget = QWidget(ContactWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 20, 501, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.firstNameLabel = QLabel(self.verticalLayoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        font = QFont()
        font.setPointSize(15)
        self.firstNameLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.firstNameLabel)

        self.firstNameEdit = QLineEdit(self.verticalLayoutWidget)
        self.firstNameEdit.setObjectName(u"firstNameEdit")
        self.firstNameEdit.setEnabled(False)
        self.firstNameEdit.setMinimumSize(QSize(200, 25))
        self.firstNameEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firstNameEdit)

        self.lastNameLabel = QLabel(self.verticalLayoutWidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lastNameLabel)

        self.lastNameEdit = QLineEdit(self.verticalLayoutWidget)
        self.lastNameEdit.setObjectName(u"lastNameEdit")
        self.lastNameEdit.setEnabled(False)
        self.lastNameEdit.setMinimumSize(QSize(200, 25))
        self.lastNameEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lastNameEdit)

        self.houseLabel = QLabel(self.verticalLayoutWidget)
        self.houseLabel.setObjectName(u"houseLabel")
        self.houseLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.houseLabel)

        self.houseEdit = QLineEdit(self.verticalLayoutWidget)
        self.houseEdit.setObjectName(u"houseEdit")
        self.houseEdit.setEnabled(False)
        self.houseEdit.setMinimumSize(QSize(200, 25))
        self.houseEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.houseEdit)

        self.streetLabel = QLabel(self.verticalLayoutWidget)
        self.streetLabel.setObjectName(u"streetLabel")
        self.streetLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.streetLabel)

        self.streetEdit = QLineEdit(self.verticalLayoutWidget)
        self.streetEdit.setObjectName(u"streetEdit")
        self.streetEdit.setEnabled(False)
        self.streetEdit.setMinimumSize(QSize(200, 25))
        self.streetEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.streetEdit)

        self.townLabel = QLabel(self.verticalLayoutWidget)
        self.townLabel.setObjectName(u"townLabel")
        self.townLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.townLabel)

        self.townEdit = QLineEdit(self.verticalLayoutWidget)
        self.townEdit.setObjectName(u"townEdit")
        self.townEdit.setEnabled(False)
        self.townEdit.setMinimumSize(QSize(200, 25))
        self.townEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.townEdit)

        self.postcodeLabel = QLabel(self.verticalLayoutWidget)
        self.postcodeLabel.setObjectName(u"postcodeLabel")
        self.postcodeLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.postcodeLabel)

        self.postcodeEdit = QLineEdit(self.verticalLayoutWidget)
        self.postcodeEdit.setObjectName(u"postcodeEdit")
        self.postcodeEdit.setEnabled(False)
        self.postcodeEdit.setMinimumSize(QSize(200, 25))
        self.postcodeEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.postcodeEdit)

        self.phoneLabel = QLabel(self.verticalLayoutWidget)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.phoneLabel)

        self.phoneEdit = QLineEdit(self.verticalLayoutWidget)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setEnabled(False)
        self.phoneEdit.setMinimumSize(QSize(200, 25))
        self.phoneEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.phoneEdit)

        self.emailLabel = QLabel(self.verticalLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.emailLabel)

        self.emailEdit = QLineEdit(self.verticalLayoutWidget)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setEnabled(False)
        self.emailEdit.setMinimumSize(QSize(200, 25))
        self.emailEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.emailEdit)

        self.contactIdLabel = QLabel(self.verticalLayoutWidget)
        self.contactIdLabel.setObjectName(u"contactIdLabel")
        self.contactIdLabel.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.contactIdLabel)

        self.contactIdEdit = QLineEdit(self.verticalLayoutWidget)
        self.contactIdEdit.setObjectName(u"contactIdEdit")
        self.contactIdEdit.setEnabled(False)
        self.contactIdEdit.setMinimumSize(QSize(200, 25))
        self.contactIdEdit.setMaximumSize(QSize(16777215, 25))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.contactIdEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ContactWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ContactWindow)

        QMetaObject.connectSlotsByName(ContactWindow)
    # setupUi

    def retranslateUi(self, ContactWindow):
        ContactWindow.setWindowTitle(QCoreApplication.translate("ContactWindow", u"MainWindow", None))
        self.firstNameLabel.setText(QCoreApplication.translate("ContactWindow", u"First Name:", None))
        self.lastNameLabel.setText(QCoreApplication.translate("ContactWindow", u"Last Name:", None))
        self.houseLabel.setText(QCoreApplication.translate("ContactWindow", u"House No.:", None))
        self.streetLabel.setText(QCoreApplication.translate("ContactWindow", u"Street:", None))
        self.townLabel.setText(QCoreApplication.translate("ContactWindow", u"Town:", None))
        self.postcodeLabel.setText(QCoreApplication.translate("ContactWindow", u"Postcode:", None))
        self.phoneLabel.setText(QCoreApplication.translate("ContactWindow", u"Phone No.:", None))
        self.emailLabel.setText(QCoreApplication.translate("ContactWindow", u"Email Address:", None))
        self.contactIdLabel.setText(QCoreApplication.translate("ContactWindow", u"Contact ID:", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_nt_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 404)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81,0,135,255), stop:0.427447 rgba(41,61,132,235), stop:1 rgba(155,79,165,255));\n"
"\n"
"font-family: Comic Sans MS;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: blue;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(14, 0, 0)))
        self.date.setTime(QTime(14, 0, 0))

        self.verticalLayout.addWidget(self.date)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_balance)

        self.cb_operation = QComboBox(self.frame)
        self.cb_operation.addItem("")
        self.cb_operation.addItem("")
        self.cb_operation.setObjectName(u"cb_operation")
        self.cb_operation.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: blue;\n"
"}")

        self.verticalLayout.addWidget(self.cb_operation)

        self.btn_new_transaction = QPushButton(self.frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(16)
        self.btn_new_transaction.setFont(font)
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"New Transaction", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choice Category", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_operation.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_operation.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save New Transaction", None))
    # retranslateUi


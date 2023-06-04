# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tracker.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81,0,135,255), stop:0.427447 rgba(41,61,132,235), stop:1 rgba(155,79,165,255));\n"
"\n"
"font-family: Comic Sans MS;")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_frames = QHBoxLayout()
        self.layout_frames.setObjectName(u"layout_frames")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.label_current_balance = QLabel(self.balance_frame)
        self.label_current_balance.setObjectName(u"label_current_balance")
        self.label_current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_current_balance)

        self.label_balance = QLabel(self.balance_frame)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_balance)

        self.layout_income = QHBoxLayout()
        self.layout_income.setSpacing(0)
        self.layout_income.setObjectName(u"layout_income")
        self.icon_income = QLabel(self.balance_frame)
        self.icon_income.setObjectName(u"icon_income")
        self.icon_income.setMaximumSize(QSize(24, 24))
        self.icon_income.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_income.setPixmap(QPixmap(u":/icons/icons/income.svg"))

        self.layout_income.addWidget(self.icon_income)

        self.label_income = QLabel(self.balance_frame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.layout_income.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.layout_income)

        self.label_income_balance = QLabel(self.balance_frame)
        self.label_income_balance.setObjectName(u"label_income_balance")
        self.label_income_balance.setStyleSheet(u"color: green;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_income_balance)

        self.layout_outcome = QHBoxLayout()
        self.layout_outcome.setSpacing(0)
        self.layout_outcome.setObjectName(u"layout_outcome")
        self.icon_outcome = QLabel(self.balance_frame)
        self.icon_outcome.setObjectName(u"icon_outcome")
        self.icon_outcome.setMaximumSize(QSize(24, 24))
        self.icon_outcome.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_outcome.setPixmap(QPixmap(u":/icons/icons/outcome.svg"))

        self.layout_outcome.addWidget(self.icon_outcome)

        self.label_outcome = QLabel(self.balance_frame)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.layout_outcome.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.layout_outcome)

        self.label_outcome_balance = QLabel(self.balance_frame)
        self.label_outcome_balance.setObjectName(u"label_outcome_balance")
        self.label_outcome_balance.setStyleSheet(u"color: red;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_outcome_balance)


        self.layout_frames.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_expense_categories = QLabel(self.categories_frame)
        self.label_expense_categories.setObjectName(u"label_expense_categories")
        self.label_expense_categories.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_expense_categories)

        self.layout_groceries = QHBoxLayout()
        self.layout_groceries.setSpacing(0)
        self.layout_groceries.setObjectName(u"layout_groceries")
        self.icon_groceries = QLabel(self.categories_frame)
        self.icon_groceries.setObjectName(u"icon_groceries")
        self.icon_groceries.setMaximumSize(QSize(24, 24))
        self.icon_groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icons/icons/cart.svg"))

        self.layout_groceries.addWidget(self.icon_groceries)

        self.label_groceries = QLabel(self.categories_frame)
        self.label_groceries.setObjectName(u"label_groceries")
        self.label_groceries.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_groceries.addWidget(self.label_groceries)

        self.label_groceries_balance = QLabel(self.categories_frame)
        self.label_groceries_balance.setObjectName(u"label_groceries_balance")
        self.label_groceries_balance.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_groceries.addWidget(self.label_groceries_balance)


        self.verticalLayout_2.addLayout(self.layout_groceries)

        self.layout_entertainment = QHBoxLayout()
        self.layout_entertainment.setSpacing(0)
        self.layout_entertainment.setObjectName(u"layout_entertainment")
        self.icon_entertainment = QLabel(self.categories_frame)
        self.icon_entertainment.setObjectName(u"icon_entertainment")
        self.icon_entertainment.setMaximumSize(QSize(24, 24))
        self.icon_entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_entertainment.setPixmap(QPixmap(u":/icons/icons/game.svg"))

        self.layout_entertainment.addWidget(self.icon_entertainment)

        self.label_entertainment = QLabel(self.categories_frame)
        self.label_entertainment.setObjectName(u"label_entertainment")
        self.label_entertainment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_entertainment.addWidget(self.label_entertainment)

        self.label_entertainment_balance = QLabel(self.categories_frame)
        self.label_entertainment_balance.setObjectName(u"label_entertainment_balance")
        self.label_entertainment_balance.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_entertainment.addWidget(self.label_entertainment_balance)


        self.verticalLayout_2.addLayout(self.layout_entertainment)

        self.layout_auto = QHBoxLayout()
        self.layout_auto.setSpacing(0)
        self.layout_auto.setObjectName(u"layout_auto")
        self.icon_auto = QLabel(self.categories_frame)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(24, 24))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icons/icons/car.svg"))

        self.layout_auto.addWidget(self.icon_auto)

        self.label_auto = QLabel(self.categories_frame)
        self.label_auto.setObjectName(u"label_auto")
        self.label_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_auto.addWidget(self.label_auto)

        self.label_auto_balance = QLabel(self.categories_frame)
        self.label_auto_balance.setObjectName(u"label_auto_balance")
        self.label_auto_balance.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_auto.addWidget(self.label_auto_balance)


        self.verticalLayout_2.addLayout(self.layout_auto)

        self.layout_other = QHBoxLayout()
        self.layout_other.setSpacing(0)
        self.layout_other.setObjectName(u"layout_other")
        self.icon_other = QLabel(self.categories_frame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 24))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icons/icons/list.svg"))

        self.layout_other.addWidget(self.icon_other)

        self.label_other = QLabel(self.categories_frame)
        self.label_other.setObjectName(u"label_other")
        self.label_other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_other.addWidget(self.label_other)

        self.label_other_balance = QLabel(self.categories_frame)
        self.label_other_balance.setObjectName(u"label_other_balance")
        self.label_other_balance.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.layout_other.addWidget(self.label_other_balance)


        self.verticalLayout_2.addLayout(self.layout_other)


        self.layout_frames.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.layout_frames)

        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.btn_new = QPushButton(self.centralwidget)
        self.btn_new.setObjectName(u"btn_new")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(16)
        self.btn_new.setFont(font)
        self.btn_new.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new.setIcon(icon)
        self.btn_new.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_new)

        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setFont(font)
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon1)
        self.btn_edit.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_delete)


        self.verticalLayout_3.addLayout(self.layout_buttons)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView::section {\n"
"background-color: rgba(53,53,53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense Tracker", None))
        self.label_current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.label_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_income.setText("")
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.label_income_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_outcome.setText("")
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.label_outcome_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.label_expense_categories.setText(QCoreApplication.translate("MainWindow", u"Expense Categories", None))
        self.icon_groceries.setText("")
        self.label_groceries.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.label_groceries_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_entertainment.setText("")
        self.label_entertainment.setText(QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.label_entertainment_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_auto.setText("")
        self.label_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.label_auto_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_other.setText("")
        self.label_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_other_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi


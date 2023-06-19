# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_admin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(45, 45))
        self.label_1.setPixmap(QPixmap(u"icons/db.png"))

        self.verticalLayout.addWidget(self.label_1)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalSpacer = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon = QIcon()
        icon.addFile(u"icons/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(32, 32))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(45, 45))
        self.label_2.setPixmap(QPixmap(u"icons/db.png"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton_1 = QPushButton(self.widget_2)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setIconSize(QSize(20, 20))
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.line_4 = QFrame(self.widget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.verticalSpacer_2 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_menu = QPushButton(self.widget_4)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_menu)

        self.horizontalSpacer = QSpacerItem(96, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 21))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_search = QPushButton(self.widget_4)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButton_search)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_account = QPushButton(self.widget_4)
        self.pushButton_account.setObjectName(u"pushButton_account")

        self.horizontalLayout_3.addWidget(self.pushButton_account)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.line_6 = QFrame(self.widget_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_4 = QVBoxLayout(self.page_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.pushButton_edit_9 = QPushButton(self.page_9)
        self.pushButton_edit_9.setObjectName(u"pushButton_edit_9")
        self.pushButton_edit_9.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"icons/edit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_edit_9.setIcon(icon1)
        self.pushButton_edit_9.setIconSize(QSize(32, 32))
        self.pushButton_edit_9.setCheckable(True)
        self.pushButton_edit_9.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.pushButton_edit_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.tableWidget_9 = QTableWidget(self.page_9)
        if (self.tableWidget_9.columnCount() < 3):
            self.tableWidget_9.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidget_9)

        self.stackedWidget.addWidget(self.page_9)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_8 = QGridLayout(self.page_1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_add_1 = QPushButton(self.page_1)
        self.pushButton_add_1.setObjectName(u"pushButton_add_1")
        icon2 = QIcon()
        icon2.addFile(u"icons/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_1.setIcon(icon2)
        self.pushButton_add_1.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_add_1)

        self.pushButton_edit_1 = QPushButton(self.page_1)
        self.pushButton_edit_1.setObjectName(u"pushButton_edit_1")
        self.pushButton_edit_1.setIcon(icon1)
        self.pushButton_edit_1.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_edit_1)

        self.pushButton_delete_1 = QPushButton(self.page_1)
        self.pushButton_delete_1.setObjectName(u"pushButton_delete_1")
        icon3 = QIcon()
        icon3.addFile(u"icons/delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete_1.setIcon(icon3)
        self.pushButton_delete_1.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_delete_1)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.page_1)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_5 = QVBoxLayout(self.page_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info = QLabel(self.page_8)
        self.info.setObjectName(u"info")
        self.info.setMaximumSize(QSize(16777215, 30))
        self.info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.info)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.report_2 = QPushButton(self.page_8)
        self.report_2.setObjectName(u"report_2")
        self.report_2.setMaximumSize(QSize(50, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"icons/excel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.report_2.setIcon(icon4)
        self.report_2.setIconSize(QSize(32, 32))

        self.gridLayout_9.addWidget(self.report_2, 1, 2, 2, 1)

        self.report_3 = QPushButton(self.page_8)
        self.report_3.setObjectName(u"report_3")
        self.report_3.setMaximumSize(QSize(50, 16777215))
        self.report_3.setIcon(icon4)
        self.report_3.setIconSize(QSize(32, 32))

        self.gridLayout_9.addWidget(self.report_3, 3, 2, 1, 1)

        self.report_1 = QPushButton(self.page_8)
        self.report_1.setObjectName(u"report_1")
        self.report_1.setMinimumSize(QSize(0, 0))
        self.report_1.setMaximumSize(QSize(50, 16777215))
        self.report_1.setIcon(icon4)
        self.report_1.setIconSize(QSize(32, 32))

        self.gridLayout_9.addWidget(self.report_1, 0, 2, 1, 1)

        self.report1 = QLabel(self.page_8)
        self.report1.setObjectName(u"report1")

        self.gridLayout_9.addWidget(self.report1, 0, 0, 1, 2)

        self.report3 = QLabel(self.page_8)
        self.report3.setObjectName(u"report3")

        self.gridLayout_9.addWidget(self.report3, 3, 0, 1, 2)

        self.report2 = QLabel(self.page_8)
        self.report2.setObjectName(u"report2")

        self.gridLayout_9.addWidget(self.report2, 1, 0, 2, 2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 1, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_8)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_add_2 = QPushButton(self.page_2)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setIcon(icon2)
        self.pushButton_add_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_add_2)

        self.pushButton_edit_2 = QPushButton(self.page_2)
        self.pushButton_edit_2.setObjectName(u"pushButton_edit_2")
        self.pushButton_edit_2.setIcon(icon1)
        self.pushButton_edit_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_edit_2)

        self.pushButton_delete_2 = QPushButton(self.page_2)
        self.pushButton_delete_2.setObjectName(u"pushButton_delete_2")
        self.pushButton_delete_2.setIcon(icon3)
        self.pushButton_delete_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_delete_2)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.page_2)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.tableWidget_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_add_3 = QPushButton(self.page_3)
        self.pushButton_add_3.setObjectName(u"pushButton_add_3")
        self.pushButton_add_3.setIcon(icon2)
        self.pushButton_add_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_add_3)

        self.pushButton_edit_3 = QPushButton(self.page_3)
        self.pushButton_edit_3.setObjectName(u"pushButton_edit_3")
        self.pushButton_edit_3.setIcon(icon1)
        self.pushButton_edit_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_edit_3)

        self.pushButton_delete_3 = QPushButton(self.page_3)
        self.pushButton_delete_3.setObjectName(u"pushButton_delete_3")
        self.pushButton_delete_3.setIcon(icon3)
        self.pushButton_delete_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_delete_3)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.page_3)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.pushButton_add_4 = QPushButton(self.page_4)
        self.pushButton_add_4.setObjectName(u"pushButton_add_4")
        self.pushButton_add_4.setIcon(icon2)
        self.pushButton_add_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_add_4)

        self.pushButton_edit_4 = QPushButton(self.page_4)
        self.pushButton_edit_4.setObjectName(u"pushButton_edit_4")
        self.pushButton_edit_4.setIcon(icon1)
        self.pushButton_edit_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_edit_4)

        self.pushButton_delete_4 = QPushButton(self.page_4)
        self.pushButton_delete_4.setObjectName(u"pushButton_delete_4")
        self.pushButton_delete_4.setIcon(icon3)
        self.pushButton_delete_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_delete_4)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.tableWidget_4 = QTableWidget(self.page_4)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.tableWidget_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_4 = QGridLayout(self.page_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.pushButton_add_5 = QPushButton(self.page_5)
        self.pushButton_add_5.setObjectName(u"pushButton_add_5")
        self.pushButton_add_5.setIcon(icon2)
        self.pushButton_add_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.pushButton_add_5)

        self.pushButton_edit_5 = QPushButton(self.page_5)
        self.pushButton_edit_5.setObjectName(u"pushButton_edit_5")
        self.pushButton_edit_5.setIcon(icon1)
        self.pushButton_edit_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.pushButton_edit_5)

        self.pushButton_delete_5 = QPushButton(self.page_5)
        self.pushButton_delete_5.setObjectName(u"pushButton_delete_5")
        self.pushButton_delete_5.setIcon(icon3)
        self.pushButton_delete_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.pushButton_delete_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.tableWidget_5 = QTableWidget(self.page_5)
        if (self.tableWidget_5.columnCount() < 7):
            self.tableWidget_5.setColumnCount(7)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem38)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_3 = QGridLayout(self.page_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.pushButton_add_6 = QPushButton(self.page_6)
        self.pushButton_add_6.setObjectName(u"pushButton_add_6")
        self.pushButton_add_6.setIcon(icon2)
        self.pushButton_add_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.pushButton_add_6)

        self.pushButton_edit_6 = QPushButton(self.page_6)
        self.pushButton_edit_6.setObjectName(u"pushButton_edit_6")
        self.pushButton_edit_6.setIcon(icon1)
        self.pushButton_edit_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.pushButton_edit_6)

        self.pushButton_delete_6 = QPushButton(self.page_6)
        self.pushButton_delete_6.setObjectName(u"pushButton_delete_6")
        self.pushButton_delete_6.setIcon(icon3)
        self.pushButton_delete_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.pushButton_delete_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.tableWidget_6 = QTableWidget(self.page_6)
        if (self.tableWidget_6.columnCount() < 7):
            self.tableWidget_6.setColumnCount(7)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableWidget_6, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_2 = QGridLayout(self.page_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.pushButton_add_7 = QPushButton(self.page_7)
        self.pushButton_add_7.setObjectName(u"pushButton_add_7")
        self.pushButton_add_7.setIcon(icon2)
        self.pushButton_add_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.pushButton_add_7)

        self.pushButton_edit_7 = QPushButton(self.page_7)
        self.pushButton_edit_7.setObjectName(u"pushButton_edit_7")
        self.pushButton_edit_7.setIcon(icon1)
        self.pushButton_edit_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.pushButton_edit_7)

        self.pushButton_delete_7 = QPushButton(self.page_7)
        self.pushButton_delete_7.setObjectName(u"pushButton_delete_7")
        self.pushButton_delete_7.setIcon(icon3)
        self.pushButton_delete_7.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.pushButton_delete_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.tableWidget_7 = QTableWidget(self.page_7)
        if (self.tableWidget_7.columnCount() < 6):
            self.tableWidget_7.setColumnCount(6)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tableWidget_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.line_5 = QFrame(self.widget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_menu.toggled.connect(self.widget.setVisible)
        self.pushButton_menu.toggled.connect(self.widget_2.setHidden)
        self.pushButton_10.clicked.connect(MainWindow.close)
        self.pushButton_12.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.label_1.setText("")
        self.pushButton_10.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0414 \"\u0410\u0432\u0442\u043e\u043f\u0430\u0440\u043a\"", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0445\u0430\u043d\u0438\u043a\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0435\u0437\u0434\u043a\u0438", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\u044b", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_menu.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_account.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438", None))
        self.pushButton_edit_9.setText("")
        ___qtablewidgetitem = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        self.pushButton_add_1.setText("")
        self.pushButton_edit_1.setText("")
        self.pushButton_delete_1.setText("")
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u043f\u0440\u0430\u0432\u0430", None));
        self.info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">\u0414\u0430\u043d\u043d\u044b\u0435 \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u044b \u0432 \u0444\u0430\u0439\u043b &quot;output.xlsx&quot;</span></p></body></html>", None))
        self.report_2.setText("")
        self.report_3.setText("")
        self.report_1.setText("")
        self.report1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u041e\u0442\u0447\u0435\u0442 \u21161 (\u0434\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430, \u0424\u0418\u041e \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f, \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043c\u0430\u0448\u0438\u043d\u0435):</span></p></body></html>", None))
        self.report3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u041e\u0442\u0447\u0435\u0442 \u21163 (\u0434\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0440\u0435\u043c\u043e\u043d\u0442\u0430, \u0424\u0418\u041e \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430, \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043c\u0430\u0448\u0438\u043d\u0435):</span></p></body></html>", None))
        self.report2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u041e\u0442\u0447\u0435\u0442 \u21162 (\u0434\u0430\u0442\u0430 \u043f\u043e\u0435\u0437\u0434\u043a\u0438, \u0424\u0418\u041e \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f, \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043c\u0430\u0448\u0438\u043d\u0435):</span></p></body></html>", None))
        self.pushButton_add_2.setText("")
        self.pushButton_edit_2.setText("")
        self.pushButton_delete_2.setText("")
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0441\u043d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0430", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0431\u0435\u0433 (\u043a\u043c.)", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f (\u043b.\u0441.)", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c (\u043a\u043c/\u0447)", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434 \u0442\u043e\u043f\u043b\u0438\u0432\u0430 (\u043b/100\u043a\u043c)", None));
        self.pushButton_add_3.setText("")
        self.pushButton_edit_3.setText("")
        self.pushButton_delete_3.setText("")
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem24 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem25 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem26 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        self.pushButton_add_4.setText("")
        self.pushButton_edit_4.setText("")
        self.pushButton_delete_4.setText("")
        ___qtablewidgetitem27 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem29 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem31 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        self.pushButton_add_5.setText("")
        self.pushButton_edit_5.setText("")
        self.pushButton_delete_5.setText("")
        ___qtablewidgetitem32 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem33 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem34 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438)", None));
        ___qtablewidgetitem35 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None));
        ___qtablewidgetitem36 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None));
        ___qtablewidgetitem37 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ID \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem38 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"ID \u043f\u043e\u0435\u0437\u0434\u043a\u0438", None));
        self.pushButton_add_6.setText("")
        self.pushButton_edit_6.setText("")
        self.pushButton_delete_6.setText("")
        ___qtablewidgetitem39 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem40 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem41 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u0435\u0437\u0434\u0430", None));
        ___qtablewidgetitem42 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0435\u0437\u0434\u0430", None));
        ___qtablewidgetitem43 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0431\u0435\u0433", None));
        ___qtablewidgetitem44 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"ID \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None));
        ___qtablewidgetitem45 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"ID \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None));
        self.pushButton_add_7.setText("")
        self.pushButton_edit_7.setText("")
        self.pushButton_delete_7.setText("")
        ___qtablewidgetitem46 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem47 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem48 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem49 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438)", None));
        ___qtablewidgetitem50 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"ID \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None));
        ___qtablewidgetitem51 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"ID \u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0430", None));
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_insert_client.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_dialog_insert_client(object):
    def setupUi(self, dialog_insert_client):
        if not dialog_insert_client.objectName():
            dialog_insert_client.setObjectName(u"dialog_insert_client")
        dialog_insert_client.resize(367, 226)
        self.gridLayout_2 = QGridLayout(dialog_insert_client)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(dialog_insert_client)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(dialog_insert_client)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(dialog_insert_client)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.patronymic = QLabel(dialog_insert_client)
        self.patronymic.setObjectName(u"patronymic")
        self.patronymic.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";")

        self.gridLayout.addWidget(self.patronymic, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(dialog_insert_client)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.name = QLabel(dialog_insert_client)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)

        self.surname = QLabel(dialog_insert_client)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 0, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(dialog_insert_client)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(dialog_insert_client)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.label_8 = QLabel(dialog_insert_client)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)


        self.retranslateUi(dialog_insert_client)

        QMetaObject.connectSlotsByName(dialog_insert_client)
    # setupUi

    def retranslateUi(self, dialog_insert_client):
        dialog_insert_client.setWindowTitle(QCoreApplication.translate("dialog_insert_client", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_insert_client", u"Apply", None))
        self.label_5.setText(QCoreApplication.translate("dialog_insert_client", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.patronymic.setText(QCoreApplication.translate("dialog_insert_client", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.name.setText(QCoreApplication.translate("dialog_insert_client", u"\u0418\u043c\u044f:", None))
        self.surname.setText(QCoreApplication.translate("dialog_insert_client", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("dialog_insert_client", u"+7 (999) 999-99-99", None))
        self.label_8.setText(QCoreApplication.translate("dialog_insert_client", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u0414\u0410\u041d\u041d\u042b\u0415 \u041e \u041a\u041b\u0418\u0415\u041d\u0422\u0415</span></p></body></html>", None))
    # retranslateUi


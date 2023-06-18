# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_insert_automobile.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_dialog_insert_automobile(object):
    def setupUi(self, dialog_insert_automobile):
        if not dialog_insert_automobile.objectName():
            dialog_insert_automobile.setObjectName(u"dialog_insert_automobile")
        dialog_insert_automobile.resize(413, 358)
        self.gridLayout_2 = QGridLayout(dialog_insert_automobile)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(dialog_insert_automobile)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(dialog_insert_automobile)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 7, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 6, 1, 1, 1)

        self.surname = QLabel(dialog_insert_automobile)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 0, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.name = QLabel(dialog_insert_automobile)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.patronymic = QLabel(dialog_insert_automobile)
        self.patronymic.setObjectName(u"patronymic")
        self.patronymic.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";")

        self.gridLayout.addWidget(self.patronymic, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_4 = QLabel(dialog_insert_automobile)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.dateEdit = QDateEdit(dialog_insert_automobile)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.label_5 = QLabel(dialog_insert_automobile)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_7 = QLabel(dialog_insert_automobile)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(dialog_insert_automobile)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label = QLabel(dialog_insert_automobile)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.label_8 = QLabel(dialog_insert_automobile)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)


        self.retranslateUi(dialog_insert_automobile)

        QMetaObject.connectSlotsByName(dialog_insert_automobile)
    # setupUi

    def retranslateUi(self, dialog_insert_automobile):
        dialog_insert_automobile.setWindowTitle(QCoreApplication.translate("dialog_insert_automobile", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_insert_automobile", u"Apply", None))
        self.label_6.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u0420\u0430\u0441\u0445\u043e\u0434 \u0442\u043e\u043f\u043b\u0438\u0432\u0430:", None))
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_6.setPlaceholderText("")
        self.surname.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u0413\u043e\u0441\u043d\u043e\u043c\u0435\u0440:", None))
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("dialog_insert_automobile", u"\u0410123\u0412\u042145", None))
        self.name.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u041c\u0430\u0440\u043a\u0430:", None))
        self.patronymic.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u0426\u0432\u0435\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dialog_insert_automobile", u"yyyy", None))
        self.label_5.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u041c\u0430\u043a\u0441\u043c\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.label_7.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u041f\u0440\u043e\u0431\u0435\u0433:", None))
        self.label.setText(QCoreApplication.translate("dialog_insert_automobile", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("dialog_insert_automobile", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u0414\u0410\u041d\u041d\u042b\u0415 \u041e\u0411 \u0410\u0412\u0422\u041e\u041c\u041e\u0411\u0418\u041b\u0415</span></p></body></html>", None))
    # retranslateUi


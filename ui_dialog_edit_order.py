# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_edit_order.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_dialog_edit_order(object):
    def setupUi(self, dialog_edit_order):
        if not dialog_edit_order.objectName():
            dialog_edit_order.setObjectName(u"dialog_edit_order")
        dialog_edit_order.resize(415, 323)
        self.gridLayout_2 = QGridLayout(dialog_edit_order)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(dialog_edit_order)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_3 = QLineEdit(dialog_edit_order)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.surname = QLabel(dialog_edit_order)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(dialog_edit_order)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.patronymic = QLabel(dialog_edit_order)
        self.patronymic.setObjectName(u"patronymic")
        self.patronymic.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";")

        self.gridLayout.addWidget(self.patronymic, 3, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(dialog_edit_order)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 1, 1, 1, 1)

        self.name = QLabel(dialog_edit_order)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)

        self.label_5 = QLabel(dialog_edit_order)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_7 = QLabel(dialog_edit_order)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.comboBox_2 = QComboBox(dialog_edit_order)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.label_4 = QLabel(dialog_edit_order)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.comboBox_3 = QComboBox(dialog_edit_order)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 6, 1, 1, 1)

        self.lineEdit_1 = QLineEdit(dialog_edit_order)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 1, 1)

        self.label = QLabel(dialog_edit_order)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(dialog_edit_order)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.label_8 = QLabel(dialog_edit_order)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)


        self.retranslateUi(dialog_edit_order)

        QMetaObject.connectSlotsByName(dialog_edit_order)
    # setupUi

    def retranslateUi(self, dialog_edit_order):
        dialog_edit_order.setWindowTitle(QCoreApplication.translate("dialog_edit_order", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_edit_order", u"Apply", None))
        self.surname.setText(QCoreApplication.translate("dialog_edit_order", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f:", None))
        self.patronymic.setText(QCoreApplication.translate("dialog_edit_order", u"\u0410\u0434\u0440\u0435\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438:", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("dialog_edit_order", u"yyyy-MM-dd HH:mm:ss", None))
        self.name.setText(QCoreApplication.translate("dialog_edit_order", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_5.setText(QCoreApplication.translate("dialog_edit_order", u"ID \u043f\u043e\u0435\u0437\u0434\u043a\u0438:", None))
        self.label_7.setText(QCoreApplication.translate("dialog_edit_order", u"ID \u043a\u043b\u0438\u0435\u043d\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("dialog_edit_order", u"\u0410\u0434\u0440\u0435\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438:", None))
        self.label.setText(QCoreApplication.translate("dialog_edit_order", u"ID \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("dialog_edit_order", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041d\u041e\u0412\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415 \u041e \u0417\u0410\u041a\u0410\u0417\u0415</span></p></body></html>", None))
    # retranslateUi


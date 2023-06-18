# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_edit_trip.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_dialog_edit_trip(object):
    def setupUi(self, dialog_edit_trip):
        if not dialog_edit_trip.objectName():
            dialog_edit_trip.setObjectName(u"dialog_edit_trip")
        dialog_edit_trip.resize(432, 329)
        self.verticalLayout = QVBoxLayout(dialog_edit_trip)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(dialog_edit_trip)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(10)

        self.verticalLayout.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dateTimeEdit = QDateTimeEdit(dialog_edit_trip)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(dialog_edit_trip)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.name = QLabel(dialog_edit_trip)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)

        self.patronymic = QLabel(dialog_edit_trip)
        self.patronymic.setObjectName(u"patronymic")
        self.patronymic.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";")

        self.gridLayout.addWidget(self.patronymic, 3, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(dialog_edit_trip)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.gridLayout.addWidget(self.dateTimeEdit_2, 3, 1, 1, 1)

        self.label_4 = QLabel(dialog_edit_trip)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QLabel(dialog_edit_trip)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.surname = QLabel(dialog_edit_trip)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 1, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(dialog_edit_trip)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 4, 1, 1, 1)

        self.comboBox_3 = QComboBox(dialog_edit_trip)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 6, 1, 1, 1)

        self.label_5 = QLabel(dialog_edit_trip)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.comboBox_2 = QComboBox(dialog_edit_trip)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.id = QLabel(dialog_edit_trip)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)

        self.comboBox = QComboBox(dialog_edit_trip)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(dialog_edit_trip)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(dialog_edit_trip)

        QMetaObject.connectSlotsByName(dialog_edit_trip)
    # setupUi

    def retranslateUi(self, dialog_edit_trip):
        dialog_edit_trip.setWindowTitle(QCoreApplication.translate("dialog_edit_trip", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_8.setText(QCoreApplication.translate("dialog_edit_trip", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041d\u041e\u0412\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415 \u041e \u041f\u041e\u0415\u0417\u0414\u041a\u0415</span></p></body></html>", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("dialog_edit_trip", u"HH:mm:ss", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dialog_edit_trip", u"yyyy-MM-dd", None))
        self.name.setText(QCoreApplication.translate("dialog_edit_trip", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u0435\u0437\u0434\u0430:", None))
        self.patronymic.setText(QCoreApplication.translate("dialog_edit_trip", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0435\u0437\u0434\u0430:", None))
        self.dateTimeEdit_2.setDisplayFormat(QCoreApplication.translate("dialog_edit_trip", u"HH:mm:ss", None))
        self.label_4.setText(QCoreApplication.translate("dialog_edit_trip", u"\u041f\u0440\u043e\u0431\u0435\u0433:", None))
        self.label_7.setText(QCoreApplication.translate("dialog_edit_trip", u"ID \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.surname.setText(QCoreApplication.translate("dialog_edit_trip", u"\u0414\u0430\u0442\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("dialog_edit_trip", u"ID \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f:", None))
        self.id.setText(QCoreApplication.translate("dialog_edit_trip", u"ID:", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_edit_trip", u"Apply", None))
    # retranslateUi


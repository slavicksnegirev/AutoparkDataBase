# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_edit_mechanic.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_dialog_edit_mechanic(object):
    def setupUi(self, dialog_edit_mechanic):
        if not dialog_edit_mechanic.objectName():
            dialog_edit_mechanic.setObjectName(u"dialog_edit_mechanic")
        dialog_edit_mechanic.resize(412, 302)
        self.verticalLayout = QVBoxLayout(dialog_edit_mechanic)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(dialog_edit_mechanic)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_5 = QLineEdit(dialog_edit_mechanic)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)

        self.label_7 = QLabel(dialog_edit_mechanic)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(dialog_edit_mechanic)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)

        self.label_6 = QLabel(dialog_edit_mechanic)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(dialog_edit_mechanic)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_5 = QLabel(dialog_edit_mechanic)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.surname = QLabel(dialog_edit_mechanic)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(dialog_edit_mechanic)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.name = QLabel(dialog_edit_mechanic)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(dialog_edit_mechanic)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 1, 1, 1, 1)

        self.comboBox = QComboBox(dialog_edit_mechanic)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.id = QLabel(dialog_edit_mechanic)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)

        self.label_4 = QLabel(dialog_edit_mechanic)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.dateEdit = QDateEdit(dialog_edit_mechanic)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(dialog_edit_mechanic)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(dialog_edit_mechanic)

        QMetaObject.connectSlotsByName(dialog_edit_mechanic)
    # setupUi

    def retranslateUi(self, dialog_edit_mechanic):
        dialog_edit_mechanic.setWindowTitle(QCoreApplication.translate("dialog_edit_mechanic", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_9.setText(QCoreApplication.translate("dialog_edit_mechanic", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041d\u041e\u0412\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415 \u041c\u0415\u0425\u0410\u041d\u0418\u041a\u0410</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_6.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u0410\u0434\u0440\u0435\u0441\u0441:", None))
        self.label_5.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.surname.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.name.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u0418\u043c\u044f:", None))
        self.id.setText(QCoreApplication.translate("dialog_edit_mechanic", u"ID:", None))
        self.label_4.setText(QCoreApplication.translate("dialog_edit_mechanic", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("dialog_edit_mechanic", u"yyyy-MM-dd", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_edit_mechanic", u"Apply", None))
    # retranslateUi


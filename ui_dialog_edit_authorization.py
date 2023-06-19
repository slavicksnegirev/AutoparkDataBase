# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_edit_authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dialog_edit_authorization(object):
    def setupUi(self, dialog_edit_authorization):
        if not dialog_edit_authorization.objectName():
            dialog_edit_authorization.setObjectName(u"dialog_edit_authorization")
        dialog_edit_authorization.resize(402, 168)
        self.verticalLayout = QVBoxLayout(dialog_edit_authorization)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(dialog_edit_authorization)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(dialog_edit_authorization)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.surname = QLabel(dialog_edit_authorization)
        self.surname.setObjectName(u"surname")

        self.gridLayout.addWidget(self.surname, 1, 0, 1, 1)

        self.id = QLabel(dialog_edit_authorization)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)

        self.comboBox = QComboBox(dialog_edit_authorization)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.password = QLabel(dialog_edit_authorization)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 2, 0, 1, 1)

        self.fullname = QLabel(dialog_edit_authorization)
        self.fullname.setObjectName(u"fullname")

        self.gridLayout.addWidget(self.fullname, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(dialog_edit_authorization)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(dialog_edit_authorization)

        QMetaObject.connectSlotsByName(dialog_edit_authorization)
    # setupUi

    def retranslateUi(self, dialog_edit_authorization):
        dialog_edit_authorization.setWindowTitle(QCoreApplication.translate("dialog_edit_authorization", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_9.setText(QCoreApplication.translate("dialog_edit_authorization", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0412\u0412\u0415\u0414\u0418\u0422\u0415 \u041d\u041e\u0412\u042b\u0419 \u041f\u0410\u0420\u041e\u041b\u042c \u0420\u0410\u0411\u041e\u0427\u0415\u0413\u041e</span></p></body></html>", None))
        self.surname.setText(QCoreApplication.translate("dialog_edit_authorization", u"\u0424\u0418\u041e:", None))
        self.id.setText(QCoreApplication.translate("dialog_edit_authorization", u"ID:", None))
        self.password.setText(QCoreApplication.translate("dialog_edit_authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.fullname.setText("")
        self.pushButton.setText(QCoreApplication.translate("dialog_edit_authorization", u"Apply", None))
    # retranslateUi


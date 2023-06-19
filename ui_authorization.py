# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_authorization(object):
    def setupUi(self, authorization):
        if not authorization.objectName():
            authorization.setObjectName(u"authorization")
        authorization.resize(324, 164)
        self.verticalLayout_2 = QVBoxLayout(authorization)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aurhorization = QLabel(authorization)
        self.aurhorization.setObjectName(u"aurhorization")

        self.verticalLayout_2.addWidget(self.aurhorization)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(authorization)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 30))

        self.verticalLayout.addWidget(self.comboBox)

        self.password = QLineEdit(authorization)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(290, 24))
        self.password.setMaximumSize(QSize(15555, 25))

        self.verticalLayout.addWidget(self.password)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(authorization)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(authorization)

        QMetaObject.connectSlotsByName(authorization)
    # setupUi

    def retranslateUi(self, authorization):
        authorization.setWindowTitle(QCoreApplication.translate("authorization", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.aurhorization.setText(QCoreApplication.translate("authorization", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">\u0410\u0412\u0422\u041e\u0420\u0418\u0417\u0410\u0426\u0418\u042f</span></p></body></html>", None))
        self.password.setPlaceholderText(QCoreApplication.translate("authorization", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("authorization", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi


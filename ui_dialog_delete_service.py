# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_delete_service.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_dialog_delete_service(object):
    def setupUi(self, dialog_delete_service):
        if not dialog_delete_service.objectName():
            dialog_delete_service.setObjectName(u"dialog_delete_service")
        dialog_delete_service.resize(282, 148)
        self.verticalLayout = QVBoxLayout(dialog_delete_service)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dialog_delete_service)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.id = QLabel(dialog_delete_service)
        self.id.setObjectName(u"id")
        self.id.setMargin(0)

        self.horizontalLayout.addWidget(self.id)

        self.comboBox = QComboBox(dialog_delete_service)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(dialog_delete_service)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(dialog_delete_service)

        QMetaObject.connectSlotsByName(dialog_delete_service)
    # setupUi

    def retranslateUi(self, dialog_delete_service):
        dialog_delete_service.setWindowTitle(QCoreApplication.translate("dialog_delete_service", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label.setText(QCoreApplication.translate("dialog_delete_service", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">\u0412\u042b\u0411\u0415\u0420\u0418\u0422\u0415 ID \u0420\u0415\u041c\u041e\u041d\u0422\u0410</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">\u0414\u041b\u042f \u0423\u0414\u0410\u041b\u0415\u041d\u0418\u042f</span></p></body></html>", None))
        self.id.setText(QCoreApplication.translate("dialog_delete_service", u"ID:", None))
        self.pushButton.setText(QCoreApplication.translate("dialog_delete_service", u"Apply", None))
    # retranslateUi


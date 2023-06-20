from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QLineEdit

from connection import DataBase
from admin_window import AdminWindow
from worker_window import WorkerWindow
from ui_admin import Ui_MainWindow
from ui_authorization import Ui_authorization


class AuthorizationWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        self.ui = Ui_authorization()
        self.ui.setupUi(self)
        self.ui.password.setEchoMode(QLineEdit.Password)

        self.connection = DataBase()
        self.admin_window = AdminWindow(self, self.connection)
        self.worker_window = WorkerWindow(self, self.connection)

        self.get_workers_fullnames()
        self.button_clicked()

    def get_workers_fullnames(self):
        self.ui.comboBox.addItem("admin")
        workers_fullnames = self.connection.get_workers_fullnames()

        for row, item in enumerate(workers_fullnames):
            for i in range(len(item)):
                self.ui.comboBox.addItem(str(item[i]))

    def button_clicked(self):
        self.ui.pushButton.clicked.connect(lambda: self.check_password())

    def check_password(self):
        if '0' in str(self.connection.check_login_details(self.ui.comboBox.currentText(), self.ui.password.text())):
            return False
        else:
            if self.ui.comboBox.currentText() == 'admin':
                self.admin_window.show()
            else:
                self.worker_window.show()
                self.worker_window.get_worker_data(self.ui.comboBox.currentText())

            self.hide()

            return True
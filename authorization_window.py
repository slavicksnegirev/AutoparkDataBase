from PySide6 import QtWidgets, QtGui

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

        self.connection = DataBase()
        self.admin_window = AdminWindow(self, self.connection)
        self.worker_window = WorkerWindow(self, self.connection)

        self.load_lastnames()
        self.button_clicked()

    def button_clicked(self):
        self.ui.pushButton.clicked.connect(lambda: self.check_data())

    def check_data(self):
        if '0' in str(self.connection.check_authorization(self.ui.comboBox.currentText(), self.ui.password.text())):
            return False
        else:
            if self.ui.comboBox.currentText() == 'admin':
                self.admin_window.show()
            else:
                self.worker_window.show()
                self.worker_window.get_worker_data(self.ui.comboBox.currentText())
                self.hide()
            return True

    def load_lastnames(self):
        lastnames = self.connection.get_all_workers_lastname()
        self.ui.comboBox.addItem("admin")
        for item in lastnames:
            tmp_str = ""
            for i in range(2, len(str(item)) - 3):
                tmp_str = tmp_str + str(item)[i]
            self.ui.comboBox.addItem(tmp_str)
import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QTextStream, Slot

from ui_admin import Ui_MainWindow
from ui_dialog_driver import Ui_Dialog
from connection import DataBase

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton_1.setChecked(True)

        self.connection = DataBase()
        self.view_data()
        self.button_clicked()

    def button_clicked(self):
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.ui.pushButton_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))

    def load_data_from_table(self, query, table):
        result = self.connection.execute_read_query(self.connection, query)
        table.setRowCount(len(result))

        for row, item in enumerate(result):
            for i in range(len(item)):
                table.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(result)):
            table.resizeColumnToContents(i)

    def view_data(self):
        self.load_data_from_table("SELECT * FROM driver_SSI", self.ui.tableWidget)
        self.load_data_from_table("SELECT * FROM automobile_SSI", self.ui.tableWidget_2)
        self.load_data_from_table("SELECT * FROM mechanic_SSI", self.ui.tableWidget_3)
        self.load_data_from_table("SELECT * FROM client_SSI", self.ui.tableWidget_4)
        self.load_data_from_table("SELECT * FROM order_SSI", self.ui.tableWidget_5)
        self.load_data_from_table("SELECT * FROM trip_SSI", self.ui.tableWidget_6)
        self.load_data_from_table("SELECT * FROM service_SSI", self.ui.tableWidget_7)

    def open_dialog_driver(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
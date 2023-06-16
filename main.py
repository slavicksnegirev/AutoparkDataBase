import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QTextStream, Slot

from ui_admin import Ui_MainWindow
from connection import DataBase

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton_9.setChecked(True)

        self.conn = DataBase()
        self.view_data()
        self.button_clicked()


    def button_clicked(self):
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))

        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_13.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.pushButton_14.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))


    def view_data(self):
        self.load_driver_SSI(self.conn)
        self.load_automobile_SSI(self.conn)
        self.load_mechanic_SSI(self.conn)
        self.load_client_SSI(self.conn)
        self.load_order_SSI(self.conn)
        self.load_trip_SSI(self.conn)
        self.load_service_SSI(self.conn)


    def load_driver_SSI(self, connection):
        self.query = "SELECT * FROM driver_SSI"
        self.drivers = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget.setRowCount(len(self.drivers))

        for row, item in enumerate(self.drivers):
            for i in range(len(item)):
                self.ui.tableWidget.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.drivers)):
            self.ui.tableWidget.resizeColumnToContents(i)

    def load_automobile_SSI(self, connection):
        self.query = "SELECT * FROM automobile_SSI"
        self.automobiles = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_2.setRowCount(len(self.automobiles))

        for row, item in enumerate(self.automobiles):
            for i in range(len(item)):
                self.ui.tableWidget_2.setItem(row, i, QTableWidgetItem(str(item[i])))


        for i in range(len(self.automobiles)):
            self.ui.tableWidget_2.resizeColumnToContents(i)

    def load_mechanic_SSI(self, connection):
        self.query = "SELECT * FROM mechanic_SSI"
        self.mechanics = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_3.setRowCount(len(self.mechanics))

        for row, item in enumerate(self.mechanics):
            for i in range(len(item)):
                self.ui.tableWidget_3.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.mechanics)):
            self.ui.tableWidget_3.resizeColumnToContents(i)

    def load_client_SSI(self, connection):
        self.query = "SELECT * FROM client_SSI"
        self.clients = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_4.setRowCount(len(self.clients))

        for row, item in enumerate(self.clients):
            for i in range(len(item)):
                self.ui.tableWidget_4.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.clients)):
            self.ui.tableWidget_4.resizeColumnToContents(i)

    def load_order_SSI(self, connection):
        self.query = "SELECT * FROM order_SSI"
        self.orders = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_5.setRowCount(len(self.orders))

        for row, item in enumerate(self.orders):
            for i in range(len(item)):
                self.ui.tableWidget_5.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.orders)):
            self.ui.tableWidget_5.resizeColumnToContents(i)

    def load_trip_SSI(self, connection):
        self.query = "SELECT * FROM trip_SSI"
        self.trips = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_6.setRowCount(len(self.trips))

        for row, item in enumerate(self.trips):
            for i in range(len(item)):
                self.ui.tableWidget_6.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.trips)):
            self.ui.tableWidget_6.resizeColumnToContents(i)

    def load_service_SSI(self, connection):
        self.query = "SELECT * FROM service_SSI"
        self.servisec = connection.execute_read_query(connection, self.query)
        self.ui.tableWidget_7.setRowCount(len(self.servisec))

        for row, item in enumerate(self.servisec):
            for i in range(len(item)):
                self.ui.tableWidget_7.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(self.servisec)):
            self.ui.tableWidget_7.resizeColumnToContents(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
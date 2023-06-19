from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import QDate, QDateTime

from ui_worker import Ui_MainWindow
from ui_dialog_insert_driver import Ui_dialog_insert_driver
from ui_dialog_edit_driver import Ui_dialog_edit_driver
from ui_dialog_delete_driver import Ui_dialog_delete_driver
from ui_dialog_insert_automobile import Ui_dialog_insert_automobile
from ui_dialog_edit_automobile import Ui_dialog_edit_automobile
from ui_dialog_delete_automobile import Ui_dialog_delete_automobile
from ui_dialog_insert_mechanic import Ui_dialog_insert_mechanic
from ui_dialog_edit_mechanic import Ui_dialog_edit_mechanic
from ui_dialog_delete_mechanic import Ui_dialog_delete_mechanic
from ui_dialog_insert_client import Ui_dialog_insert_client
from ui_dialog_edit_client import Ui_dialog_edit_client
from ui_dialog_delete_client import Ui_dialog_delete_client
from ui_dialog_insert_order import Ui_dialog_insert_order
from ui_dialog_edit_order import Ui_dialog_edit_order
from ui_dialog_delete_order import Ui_dialog_delete_order
from ui_dialog_insert_trip import Ui_dialog_insert_trip
from ui_dialog_edit_trip import Ui_dialog_edit_trip
from ui_dialog_delete_trip import Ui_dialog_delete_trip
from ui_dialog_insert_service import Ui_dialog_insert_service
from ui_dialog_edit_service import Ui_dialog_edit_service
from ui_dialog_delete_service import Ui_dialog_delete_service
from ui_dialog_edit_authorization import Ui_dialog_edit_authorization

class WorkerWindow(QMainWindow):
    def __init__(self, authorization_window, connection):
        super(WorkerWindow, self).__init__()
        self.authorization_window = authorization_window
        self.connection = connection
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.widget.hide()
        self.ui.pushButton_1.setChecked(True)
        self.ui.stackedWidget.setCurrentIndex(1)

        self.view_data()
        self.button_clicked()

    def close_window(self):
        self.close()
        self.authorization_window.show()

    def button_clicked(self):
        self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        self.ui.pushButton_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
        self.ui.pushButton_search.clicked.connect(lambda: self.on_search_bnt())

        self.ui.pushButton_10.clicked.connect(lambda: self.close_window())
        self.ui.pushButton_12.clicked.connect(lambda: self.close_window())

    def load_data_from_table(self, query, table):
        result = self.connection.execute_read_query(query)
        table.setRowCount(len(result))

        for row, item in enumerate(result):
            for i in range(len(item)):
                table.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(result)):
            table.resizeColumnToContents(i)

    def get_data_from_table(self, table, text):
        array = list()
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.item(i,j).setBackground(QtGui.QColor(255, 255, 255, 0))
                if text in table.item(i, j).text():
                    array.append([i , j])
        return array

    def get_data_from_table_column(self, table, j):
        data = list()
        for i in range(table.rowCount()):
            data.append(table.item(i, j).text())
        return data

    def get_data_from_table_row(self, table, i):
        data = list()
        for j in range(table.columnCount()):
            data.append(table.item(i, j).text())
        return data

    def view_data(self):
        self.load_data_from_table("SELECT * FROM driver_SSI", self.ui.tableWidget)
        self.load_data_from_table("SELECT * FROM automobile_SSI", self.ui.tableWidget_2)
        self.load_data_from_table("SELECT * FROM mechanic_SSI", self.ui.tableWidget_3)
        self.load_data_from_table("SELECT * FROM client_SSI", self.ui.tableWidget_4)
        self.load_data_from_table("SELECT * FROM order_SSI", self.ui.tableWidget_5)
        self.load_data_from_table("SELECT * FROM trip_SSI", self.ui.tableWidget_6)
        self.load_data_from_table("SELECT * FROM service_SSI", self.ui.tableWidget_7)

    def on_search_bnt(self):
        self.ui.stackedWidget.currentChanged
        array = self.get_data_from_table(self.ui.stackedWidget.widget((self.ui.stackedWidget.currentIndex())).children()[len(
            self.ui.stackedWidget.widget((self.ui.stackedWidget.currentIndex())).children())-1], self.ui.lineEdit.text())
        for item in array:
            self.ui.stackedWidget.widget((self.ui.stackedWidget.currentIndex())).children()[len(self.ui.stackedWidget.widget((self.ui.stackedWidget.currentIndex())).children()) - 1].item(item[0], item[1]).setBackground(QtGui.QColor(0, 255, 0, 70))

    def get_worker_data(self, fullname):
        self.surname = fullname.split()[0]
        self.name =  fullname.split()[1]
        self.patronymic = fullname.split()[2]

        result = self.connection.execute_read_query(f"""
        SELECT * 
        FROM driver_SSI 
        WHERE surname = "{self.surname}" and name = "{self.name}" and patronymic = "{self.patronymic}"
        """ )
        if len(result) < 1:
            result = self.connection.execute_read_query(f"""
            SELECT * 
            FROM mechanic_SSI 
            WHERE surname = "{self.surname}" and name = "{self.name}" and patronymic = "{self.patronymic}"
            """ )

        for row, item in enumerate(result):
            self.ui.l_1.setText(str(item[1]))
            self.ui.l_2.setText(str(item[2]))
            self.ui.l_3.setText(str(item[3]))
            self.ui.l_4.setText(str(item[4]))
            self.ui.l_5.setText(str(item[5]))
            self.ui.l_6.setText(str(item[6]))

            self.ui.l_1.setFont(QFont(".AppleSystemUIFont", 24))
            self.ui.l_2.setFont(QFont(".AppleSystemUIFont", 24))
            self.ui.l_3.setFont(QFont(".AppleSystemUIFont", 24))
            self.ui.l_4.setFont(QFont(".AppleSystemUIFont", 24))
            self.ui.l_5.setFont(QFont(".AppleSystemUIFont", 24))
            self.ui.l_6.setFont(QFont(".AppleSystemUIFont", 24))
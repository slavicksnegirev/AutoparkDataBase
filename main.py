import sys

import PySide6
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QTextStream, Slot, QDate

from ui_admin import Ui_MainWindow
from ui_dialog_insert_driver import Ui_dialog_insert_driver
from ui_dialog_edit_driver import Ui_dialog_edit_driver
from ui_dialog_delete_driver import Ui_dialog_delete_driver
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
        self.ui.pushButton_add_1.clicked.connect(lambda: self.open_dialog_insert_driver())
        self.ui.pushButton_edit_1.clicked.connect(lambda : self.open_dialog_edit_driver())
        self.ui.pushButton_delete_1.clicked.connect(lambda : self.open_dialog_delete_driver())

    def load_data_from_table(self, query, table):
        result = self.connection.execute_read_query(query)
        table.setRowCount(len(result))

        for row, item in enumerate(result):
            for i in range(len(item)):
                table.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(result)):
            table.resizeColumnToContents(i)

    def get_data_from_table(self, table):
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                print(table.item(i, j).text())

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

    def open_dialog_insert_driver(self):
        self.new_dialog_insert_driver = QtWidgets.QDialog()
        self.ui_dialog_insert_driver = Ui_dialog_insert_driver()
        self.ui_dialog_insert_driver.setupUi(self.new_dialog_insert_driver)
        self.new_dialog_insert_driver.show()
        self.ui_dialog_insert_driver.pushButton.clicked.connect(lambda: self.insert_driver())

    def insert_driver(self):
        surname = self.ui_dialog_insert_driver.lineEdit_1.text()
        name = self.ui_dialog_insert_driver.lineEdit_2.text()
        patronymic = self.ui_dialog_insert_driver.lineEdit_3.text()
        date_of_birth = self.ui_dialog_insert_driver.dateEdit.text()
        address = self.ui_dialog_insert_driver.lineEdit_4.text()
        phone_number = self.ui_dialog_insert_driver.lineEdit_5.text()
        license_number = self.ui_dialog_insert_driver.lineEdit_6.text()

        self.connection.insert_driver_SSI(surname, name, patronymic, date_of_birth, address, phone_number, license_number)
        self.new_dialog_insert_driver.close()
        self.load_data_from_table("SELECT * FROM driver_SSI", self.ui.tableWidget)

    def open_dialog_edit_driver(self):
        self.new_dialog_edit_driver = QtWidgets.QDialog()
        self.ui_dialog_edit_driver = Ui_dialog_edit_driver()
        self.ui_dialog_edit_driver.setupUi(self.new_dialog_edit_driver)
        self.new_dialog_edit_driver.show()

        self.ui_dialog_edit_driver.comboBox.addItems(self.get_data_from_table_column(self.ui.tableWidget, 0))
        self.set_current_driver_data(self.ui_dialog_edit_driver.comboBox.currentIndex())
        self.ui_dialog_edit_driver.comboBox.currentIndexChanged.connect(lambda: self.set_current_driver_data(
            self.ui_dialog_edit_driver.comboBox.currentIndex()))
        self.ui_dialog_edit_driver.pushButton.clicked.connect(lambda: self.edit_driver())


    def set_current_driver_data(self, index):
        current_column_data = self.get_data_from_table_row(self.ui.tableWidget, index)

        self.ui_dialog_edit_driver.lineEdit_1.setText(current_column_data[1])
        self.ui_dialog_edit_driver.lineEdit_2.setText(current_column_data[2])
        self.ui_dialog_edit_driver.lineEdit_3.setText(current_column_data[3])
        date = current_column_data[4]
        self.ui_dialog_edit_driver.dateEdit.setDate(QDate(int(date[:4]), int(date[6:7]), int(date[9:10])))
        self.ui_dialog_edit_driver.lineEdit_4.setText(current_column_data[5])
        self.ui_dialog_edit_driver.lineEdit_5.setText(current_column_data[6])
        self.ui_dialog_edit_driver.lineEdit_6.setText(current_column_data[7])
    def edit_driver(self):
        driver_ID = self.ui_dialog_edit_driver.comboBox.currentText()
        surname = self.ui_dialog_edit_driver.lineEdit_1.text()
        name = self.ui_dialog_edit_driver.lineEdit_2.text()
        patronymic = self.ui_dialog_edit_driver.lineEdit_3.text()
        date_of_birth = self.ui_dialog_edit_driver.dateEdit.text()
        address = self.ui_dialog_edit_driver.lineEdit_4.text()
        phone_number = self.ui_dialog_edit_driver.lineEdit_5.text()
        license_number = self.ui_dialog_edit_driver.lineEdit_6.text()

        self.connection.edit_driver_SSI(surname, name, patronymic, date_of_birth, address, phone_number,
                                        license_number, driver_ID)
        self.new_dialog_edit_driver.close()
        self.load_data_from_table("SELECT * FROM driver_SSI", self.ui.tableWidget)

    def open_dialog_delete_driver(self):
        self.new_dialog_delete_driver = QtWidgets.QDialog()
        self.ui_dialog_delete_driver = Ui_dialog_delete_driver()
        self.ui_dialog_delete_driver.setupUi(self.new_dialog_delete_driver)
        self.new_dialog_delete_driver.show()

        self.ui_dialog_delete_driver.comboBox.addItems(self.get_data_from_table_column(self.ui.tableWidget, 0))
        self.ui_dialog_delete_driver.pushButton.clicked.connect(lambda: self.delete_driver())

    def delete_driver(self):
        driver_ID = self.ui_dialog_delete_driver.comboBox.currentText()

        self.connection.delete_driver_SSI(driver_ID)
        self.new_dialog_delete_driver.close()
        self.load_data_from_table("SELECT * FROM driver_SSI", self.ui.tableWidget)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
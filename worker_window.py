from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from ui_worker import Ui_MainWindow


class WorkerWindow(QMainWindow):
    def __init__(self, authorization_window, connection):
        super(WorkerWindow, self).__init__()
        self.authorization_window = authorization_window
        self.connection = connection
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.hide()
        self.ui.pushButton_1.setChecked(True)

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
        self.ui.pushButton_account.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        self.ui.pushButton_search.clicked.connect(lambda: self.on_search_button())
        self.ui.pushButton_exit_1.clicked.connect(lambda: self.close_window())
        self.ui.pushButton_exit_2.clicked.connect(lambda: self.close_window())

    def get_data_from_db(self, query, table):
        result = self.connection.execute_read_query(query)
        table.setRowCount(len(result))

        for row, item in enumerate(result):
            for i in range(len(item)):
                table.setItem(row, i, QTableWidgetItem(str(item[i])))

        for i in range(len(result)):
            table.resizeColumnToContents(i)

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
        self.get_data_from_db("SELECT * FROM driver_SSI", self.ui.tableWidget)
        self.get_data_from_db("SELECT * FROM automobile_SSI", self.ui.tableWidget_2)
        self.get_data_from_db("SELECT * FROM mechanic_SSI", self.ui.tableWidget_3)
        self.get_data_from_db("SELECT * FROM client_SSI", self.ui.tableWidget_4)
        self.get_data_from_db("SELECT * FROM order_SSI", self.ui.tableWidget_5)
        self.get_data_from_db("SELECT * FROM trip_SSI", self.ui.tableWidget_6)
        self.get_data_from_db("SELECT * FROM service_SSI", self.ui.tableWidget_7)

    def on_search_button(self):
        self.view_data()
        current_page = self.ui.stackedWidget.widget(self.ui.stackedWidget.currentIndex())
        current_table = current_page.children()[len(current_page.children())-1]
        request = self.ui.lineEdit.text().lower()

        for row in range(current_table.rowCount()):
            isHidden = True
            for column in range(current_table.columnCount()):
                item = current_table.item(row, column)
                if request in item.text().lower():
                    isHidden = False
                    if request == '':
                        current_table.item(row, column).setBackground(QtGui.QColor(255, 255, 255, 0))
                    else:
                        current_table.item(row, column).setBackground(QtGui.QColor(0, 255, 0, 70))

            current_table.setRowHidden(row, isHidden)

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
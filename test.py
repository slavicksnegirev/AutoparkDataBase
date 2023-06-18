def open_dialog_insert_mechanic(self):
    self.new_dialog_insert_mechanic = QtWidgets.QDialog()
    self.ui_dialog_insert_mechanic = Ui_dialog_insert_mechanic()
    self.ui_dialog_insert_mechanic.setupUi(self.new_dialog_insert_mechanic)
    self.new_dialog_insert_mechanic.show()
    self.ui_dialog_insert_mechanic.pushButton.clicked.connect(lambda: self.insert_mechanic())


def insert_mechanic(self):
    surname = self.ui_dialog_insert_mechanic.lineEdit_1.text()
    name = self.ui_dialog_insert_mechanic.lineEdit_2.text()
    patronymic = self.ui_dialog_insert_mechanic.lineEdit_3.text()
    date_of_birth = self.ui_dialog_insert_mechanic.dateEdit.text()
    address = self.ui_dialog_insert_mechanic.lineEdit_4.text()
    phone_number = self.ui_dialog_insert_mechanic.lineEdit_5.text()

    self.connection.insert_mechanic_SSI(surname, name, patronymic, date_of_birth, address, phone_number)
    self.new_dialog_insert_mechanic.close()
    self.load_data_from_table("SELECT * FROM mechanic_SSI", self.ui.tableWidget_3)


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
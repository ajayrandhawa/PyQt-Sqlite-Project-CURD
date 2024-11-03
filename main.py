from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,sqlite3

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Student")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addstudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Mechanical")
        self.branchinput.addItem("Civil")
        self.branchinput.addItem("Electrical")
        self.branchinput.addItem("Electronics and Communication")
        self.branchinput.addItem("Computer Science")
        self.branchinput.addItem("Information Technology")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        self.mobileinput.setInputMask('99999 99999')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):

        name = ""
        branch = ""
        sem = -1
        mobile = -1
        address = ""

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",(name,branch,sem,mobile,address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

class UpdateDialog(QDialog):
    def __init__(self, student_id, *args, **kwargs):
        super(UpdateDialog, self).__init__(*args, **kwargs)

        self.student_id = student_id

        self.QBtn = QPushButton()
        self.QBtn.setText("Update")

        self.setWindowTitle("Update Student")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.updatestudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Mechanical")
        self.branchinput.addItem("Civil")
        self.branchinput.addItem("Electrical")
        self.branchinput.addItem("Electronics and Communication")
        self.branchinput.addItem("Computer Science")
        self.branchinput.addItem("Information Technology")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        self.mobileinput.setInputMask('99999 99999')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        # Populate fields with existing student data
        self.populate_fields()

    def populate_fields(self):
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM students WHERE roll=?", (self.student_id,))
            student = self.c.fetchone()
            self.conn.close()

            self.nameinput.setText(student[1])
            self.branchinput.setCurrentText(student[2])
            self.seminput.setCurrentText(str(student[3]))
            self.mobileinput.setText(str(student[4]))
            self.addressinput.setText(student[5])
        except Exception as e:
            QMessageBox.warning(QMessageBox(), 'Error', str(e))

    def updatestudent(self):
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()

        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE students SET name=?, branch=?, sem=?, Mobile=?, address=? WHERE roll=?",
                           (name, branch, sem, mobile, address, self.student_id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Student is updated successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update student to the database.')

class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setText("123456")
        self.passinput.setPlaceholderText("Enter Password.")
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")
        self.setWindowTitle('Login')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        if(self.passinput.text() == "123456"):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("STDMGMT")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        layout.addWidget(QLabel("Version 1"))
        layout.addWidget(QLabel("Copyright 2024 Ajay Randhawa."))


        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("Student Management CRUD")

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)  # Disable stretching for manual width
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Roll No.", "Name", "Branch", "Sem", "Mobile", "Address", "Action"))
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.tableWidget.setColumnWidth(6, 120)


        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Add Student", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search User with roll no. or name")
        self.search_input.setFixedHeight(30)
        self.search_input.setFixedWidth(400)
        self.search_input.setContentsMargins(10, 0 ,0 , 0)
        self.search_input.setTextMargins(3, 0, 3, 0)
        toolbar.addWidget(self.search_input)

        search_btn = QPushButton()
        search_btn.setText("Search")
        search_btn.setFixedHeight(30)
        search_btn.clicked.connect(self.searchstudent)
        toolbar.addWidget(search_btn)

        clear_btn = QPushButton()
        clear_btn.setText("Clear Search")
        clear_btn.setFixedHeight(30)
        clear_btn.clicked.connect(self.clearSearch)
        toolbar.addWidget(clear_btn)

        adduser_action = QAction(QIcon("icon/add.png"),"Insert Student", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        about_action = QAction(QIcon("icon/info.png"),"Developer", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM students"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)

        for inx, student in enumerate(result):

            # Create a QWidget to hold the edit and delete buttons together
            cell_widget = QWidget()
            layout = QHBoxLayout(cell_widget)

            editBtn = QPushButton(self.tableWidget)
            editBtn.setIcon(QIcon("icon/editIcon.png"))
            editBtn.setFixedWidth(50)

            deleteBtn = QPushButton(self.tableWidget)
            deleteBtn.setIcon(QIcon("icon/deleteIcon.png"))
            deleteBtn.setFixedWidth(50)

            # Connect buttons to the event handler with the student ID
            editBtn.clicked.connect(lambda checked, student_id=student[0]: self.handleEdit(student_id))
            deleteBtn.clicked.connect(lambda checked, student_id=student[0]: self.handleDelete(student_id))

            layout.addWidget(editBtn)
            layout.addWidget(deleteBtn)

            # Set layout properties
            layout.setContentsMargins(0, 0, 0, 0)  # Optional: adjust spacing as needed
            cell_widget.setLayout(layout)

            # Insert a new row at the index 'inx'
            self.tableWidget.insertRow(inx)

            # Populate the remaining columns with data from 'student'
            self.tableWidget.setItem(inx, 0, QTableWidgetItem(str(student[0])))
            self.tableWidget.setItem(inx, 1, QTableWidgetItem(str(student[1])))
            self.tableWidget.setItem(inx, 2, QTableWidgetItem(str(student[2])))
            self.tableWidget.setItem(inx, 3, QTableWidgetItem(str(student[3])))
            self.tableWidget.setItem(inx, 4, QTableWidgetItem(str(student[4])))
            self.tableWidget.setItem(inx, 5, QTableWidgetItem(str(student[5])))
            # Set the delete button in the first column
            self.tableWidget.setCellWidget(inx, 6, cell_widget)

        # Optionally, update the table widget after loading all rows
        self.tableWidget.update()

        self.connection.close()

    # Define the event handler methods
    def handleEdit(self, student_id):
        print(student_id)
        dlg = UpdateDialog(student_id)
        dlg.exec_()
        self.loaddata()

    def clearSearch(self):
        self.search_input.setText("")
        self.loaddata()

    def handleDelete(self, student_id):
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE roll=" + str(student_id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Deleted From Table Successful')
            self.loaddata()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete student from the database.')

    def searchstudent(self):
        query = self.search_input.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM students WHERE roll=? OR name LIKE ?", (query, '%' + query + '%'))
            result = self.c.fetchall()
            self.tableWidget.setRowCount(0)

            for inx, student in enumerate(result):
                cell_widget = QWidget()
                layout = QHBoxLayout(cell_widget)

                editBtn = QPushButton(self.tableWidget)
                editBtn.setIcon(QIcon("icon/editIcon.png"))
                editBtn.setFixedWidth(50)

                deleteBtn = QPushButton(self.tableWidget)
                deleteBtn.setIcon(QIcon("icon/deleteIcon.png"))
                deleteBtn.setFixedWidth(50)

                editBtn.clicked.connect(lambda _, student_id=student[0]: self.handleEdit(student[0]))
                deleteBtn.clicked.connect(lambda _, student_id=student[0]: self.handleDelete(student[0]))

                layout.addWidget(editBtn)
                layout.addWidget(deleteBtn)

                layout.setContentsMargins(0, 0, 0, 0)  # Optional: adjust spacing as needed
                cell_widget.setLayout(layout)

                self.tableWidget.insertRow(inx)
                self.tableWidget.setItem(inx, 0, QTableWidgetItem(str(student[0])))
                self.tableWidget.setItem(inx, 1, QTableWidgetItem(str(student[1])))
                self.tableWidget.setItem(inx, 2, QTableWidgetItem(str(student[2])))
                self.tableWidget.setItem(inx, 3, QTableWidgetItem(str(student[3])))
                self.tableWidget.setItem(inx, 4, QTableWidgetItem(str(student[4])))
                self.tableWidget.setItem(inx, 5, QTableWidgetItem(str(student[5])))
                self.tableWidget.setCellWidget(inx, 6, cell_widget)

            self.tableWidget.update()

            self.conn.commit()
            self.c.close()
            self.conn.close()

            if len(result) == 0:
                QMessageBox.warning(QMessageBox(), 'Error', 'No results found.')
        except Exception as e:
            QMessageBox.warning(QMessageBox(), 'Error', str(e))

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()
        self.loaddata()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()


app = QApplication(sys.argv)
passdlg = LoginDialog()
if(passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.showMaximized()
    window.show()
    window.loaddata()
sys.exit(app.exec_())

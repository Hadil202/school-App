from PySide6.QtWidgets import QDialog, QHBoxLayout, QMainWindow, QMenu , QTableWidgetItem, QWidget , QHBoxLayout, QVBoxLayout , QPushButton , QFileDialog , QMessageBox
from PySide6.QtGui import QAction , QIcon
import mysql.connector

from StudentDialog import StudentsDialog
from ui_index import Ui_MainWindow
import pandas as pd
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from UpdateStudentDailog import UpdateStudentsDialog


class MysideBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("SideBar Menu")

        # Hide widgets
        self.ui.icon_only_widget.setHidden(True)
        self.ui.students_dropdown.setHidden(True)
        self.ui.teachers_dropdown.setHidden(True)
        self.ui.finances_dropdown.setHidden(True)

        # ---------------- Buttons ----------------

        self.ui.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.ui.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.ui.institution_1.clicked.connect(self.switch_to_institution_page)
        self.ui.institution_2.clicked.connect(self.switch_to_institution_page)

        self.ui.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.ui.student_payments.clicked.connect(self.switch_to_studentPayments_page)
        self.ui.students_transactions.clicked.connect(
            self.switch_to_studentTransactions_page
        )

        self.ui.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.ui.teacher_salaries.clicked.connect(
            self.switch_to_teacherSalaries_page
        )
        self.ui.teacher_transactions.clicked.connect(
            self.switch_to_teacherTransactions_page
        )

        self.ui.budgets.clicked.connect(self.switch_to_budgetsInfo_page)
        self.ui.expenses.clicked.connect(self.switch_to_expensesInfo_page)
        self.ui.business_overview.clicked.connect(
            self.switch_to_businessOver_page
        )

        self.ui.settings_1.clicked.connect(self.switch_to_settings_page)
        self.ui.settings_2.clicked.connect(self.switch_to_settings_page)

        # ---------------- Context Menu ----------------

        self.ui.students_1.clicked.connect(self.students_context_menu)
        self.ui.teachers_1.clicked.connect(self.teachers_context_menu)
        self.ui.finances_1.clicked.connect(self.finances_context_menu)

        # ---------------- Database ----------------

        self.create_connection()
        self.create_students_table()

        # Load Students Information to QTable
        self.load_students_info()
        self.ui.select_class.currentIndexChanged.connect(self.reload_studentstable_data)
        self.ui.select_gender.currentIndexChanged.connect(self.reload_studentstable_data)
        self.ui.search_student.textChanged.connect(self.search_students)
        #control column width
        self.ui.studentInfo_table.setColumnWidth(0, 150)  # names
        self.ui.studentInfo_table.setColumnWidth(1, 100)  # student_id
        self.ui.studentInfo_table.setColumnWidth(2, 80)
        self.ui.studentInfo_table.setColumnWidth(3, 80)  # class
        self.ui.studentInfo_table.setColumnWidth(4, 100)  # birthday
        self.ui.studentInfo_table.setColumnWidth(5, 50)  # age
        self.ui.studentInfo_table.setColumnWidth(6, 200)  # address
        self.ui.studentInfo_table.setColumnWidth(7, 100)  # phone_number
        self.ui.studentInfo_table.setColumnWidth(8, 200)  # email
        self.ui.studentInfo_table.setColumnWidth(9, 150)  # action buttons
        # Excel export 
    
        self.ui.excelExport_btn.clicked.connect(self.export_to_excel_studentsTable)

        # pdf export
        self.ui.pdfExport_btn.clicked.connect(self.export_to_pdf_studentsTable)
        # ---------------- Dialog ----------------

        self.ui.addStudent_btn.clicked.connect(self.open_addStudent_dialog)

    # ---------------- Pages ----------------

    def switch_to_dashboard_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_studentInfo_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_studentPayments_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def switch_to_studentTransactions_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def switch_to_teacherInfo_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def switch_to_teacherSalaries_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def switch_to_teacherTransactions_page(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def switch_to_budgetsInfo_page(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def switch_to_expensesInfo_page(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def switch_to_businessOver_page(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    # ---------------- Context Menu ----------------

    def students_context_menu(self):
        self.show_custom_context_menu(
            self.ui.students_1,
            [
                "Student Info",
                "Student Payments",
                "Student Transactions",
            ],
        )

    def teachers_context_menu(self):
        self.show_custom_context_menu(
            self.ui.teachers_1,
            [
                "Teacher Info",
                "Teacher Salaries",
                "Teacher Transactions",
            ],
        )

    def finances_context_menu(self):
        self.show_custom_context_menu(
            self.ui.finances_1,
            [
                "Budgets Info",
                "Expenses Info",
                "Business Overview",
            ],
        )

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        menu.setStyleSheet("""
            QMenu {
                background-color: black;
                color: white;
            }

            QMenu::item:selected {
                background-color: #12B298;
                color: white;
            }
        """)

        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        menu.exec(button.mapToGlobal(button.rect().bottomLeft()))

    def handle_menu_item_click(self):

        text = self.sender().text()

        if text == "Student Info":
            self.switch_to_studentInfo_page()

        elif text == "Student Payments":
            self.switch_to_studentPayments_page()

        elif text == "Student Transactions":
            self.switch_to_studentTransactions_page()

        elif text == "Teacher Info":
            self.switch_to_teacherInfo_page()

        elif text == "Teacher Salaries":
            self.switch_to_teacherSalaries_page()

        elif text == "Teacher Transactions":
            self.switch_to_teacherTransactions_page()

        elif text == "Budgets Info":
            self.switch_to_budgetsInfo_page()

        elif text == "Expenses Info":
            self.switch_to_expensesInfo_page()

        elif text == "Business Overview":
            self.switch_to_businessOver_page()

    # ---------------- DATABASE ----------------

    def create_connection(self):

        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "my_school"

        # Connect to MySQL server

        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
        )

        cursor = self.mydb.cursor()

        # Create database

        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {database_name}"
        )

        # Connect to database

        self.mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=mypassword,
            database=database_name,
        )

        return self.mydb

    # ---------------- CREATE TABLE ----------------

    def create_students_table(self):

        cursor = self.create_connection().cursor()

        create_students_table_query = """
        CREATE TABLE IF NOT EXISTS students_table (

            names VARCHAR(255),
            student_id VARCHAR(15) PRIMARY KEY,
            gender TEXT,
            class TEXT,
            birthday TEXT,
            age INT,
            address TEXT,
            phone_number VARCHAR(15),
            email VARCHAR(255)

        )
        """

        cursor.execute(create_students_table_query)

        self.mydb.commit()

    # ---------------- OPEN DIALOG ----------------
    def open_addStudent_dialog(self):

        addStudent_dialog = StudentsDialog(self)

        result = addStudent_dialog.exec()

        if result == QDialog.Accepted:
            print("Student added successfully")
            self.reload_studentstable_data()  # Reload the student table data after adding a new student
    # Load Students Information to QTable
    def reload_studentstable_data(self):
        # this method is called to reload the table data
        self.load_students_info()

    def load_students_info(self):
        # Clear existing data in the table
        self.ui.studentInfo_table.setRowCount(0)
        
        # fetch data based on the selected class and gender in the comboBox
        selected_class = self.ui.select_class.currentText()
        selected_gender = self.ui.select_gender.currentText()
        
        data = self.get_data_from_table(selected_class, selected_gender)
        
        # Populate the table with the filtered data
        for row_index, row_data in enumerate(data):
            self.ui.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.ui.studentInfo_table.setItem(row_index, col_index, item)
            
            # Create a custom widget with two buttons for the action column
            # نمرر مرجع النافذة الرئيسية (self) حتى يستطيع الزر تحديث الجدول بعد التعديل/الحذف
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
            self.ui.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.ui.studentInfo_table.setRowHeight(row_index, 50)
    def get_data_from_table(self, class_filter, gander_filter):
        cursor = self.create_connection().cursor()
        # Construct the SQL query based on the selected filters
        query = (
            "SELECT names, student_id, gender, class, birthday, age, address, phone_number, email "
            "FROM students_table WHERE "
            f"('{class_filter}' = 'SELECT CLASS' OR class = '{class_filter}') AND "
            f"('{gander_filter}' = 'SELECT GENDER' OR gender = '{gander_filter}')"
        )
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    def edit_student(self):
        print(f"Edit student at row {self.row_index}")

    def delete_student(self):
        print(f"Delete student at row {self.row_index}")
    def search_students(self):
        self.ui.studentInfo_table.setRowCount(0)
        self.search_query = self.ui.search_student.text()    
        sql_query = (
            "SELECT names, student_id, gender, class, birthday, age, address, phone_number, email "
            "FROM students_table WHERE "
            f"names LIKE '%{self.search_query}%'"
        )
        cursor = self.create_connection().cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()

        for row_index, row_data in enumerate(results):
            self.ui.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.ui.studentInfo_table.setItem(row_index, col_index, item)
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
            self.ui.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.ui.studentInfo_table.setRowHeight(row_index, 50)
    #Execel Export
    def export_to_excel_studentsTable(self):
        data = []
        self.headers = [
            self.ui.studentInfo_table.horizontalHeaderItem(col).text()
            for col in range(self.ui.studentInfo_table.columnCount())
        ]
        
        # جمع كل الصفوف أولاً
        for row in range(self.ui.studentInfo_table.rowCount()):
            row_data = [
                self.ui.studentInfo_table.item(row, col).text()
                if self.ui.studentInfo_table.item(row, col) is not None else ""
                for col in range(self.ui.studentInfo_table.columnCount())
            ]
            data.append(row_data)

        # ثم إنشاء DataFrame وفتح نافذة الحفظ مرة واحدة فقط خارج الحلقة
        df = pd.DataFrame(data, columns=self.headers)
        df_filtered = df.iloc[:, :-1]

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(
            self, "Save Excel File", "", "Excel Files (*.xlsx);;All Files (*)"
        )

        if file_path:
            df_filtered.to_excel(file_path, index=False)
            print(f"Data exported to {file_path} successfully.")
    #PDF EXPORT
    def export_to_pdf_studentsTable(self):
       #Open QFileDialog to get the file path
       file_dialog = QFileDialog()
       file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf);;All Files (*)")
       if file_path:
           # Create a PDF document
           pdf_document = SimpleDocTemplate(file_path, pagesize=letter)
           # Assuming n is the total number of columns in your QTableWidget
           n = self.ui.studentInfo_table.columnCount() if hasattr(self, 'ui') else self.studentInfo_table.columnCount()
           # extract headers from the QTableWidget
           table_widget = self.ui.studentInfo_table if hasattr(self, 'ui') else self.studentInfo_table
           headers = [table_widget.horizontalHeaderItem(col).text() for col in range(n-1)]
           # Extract data from the QTableWidget, excluding the last column
           data = [headers]
           for row in range(table_widget.rowCount()):
               row_data = [table_widget.item(row, col).text() if table_widget.item(row, col) is not None else "" for col in range(n-1)]
               data.append(row_data)
           # create a PDF table
           pdf_table = Table(data)
           # Apply styles to the table
           style = TableStyle([
               ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
               ('FONTSIZE', (0, 0), (-1, 1), 8),
               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
               ('GRID', (0, 0), (-1, -1), 1, colors.black)
           ])
           pdf_table.setStyle(style)
           # Build the PDF
           pdf_document.build([pdf_table])
           print(f"Table exported to {file_path}")
    # double buttom class
class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data, sideBar=None):
        super().__init__()
        #STORE THE ROW INDEX AND DATA FOR LATER USE IN THE BUTTONS' FUNCTIONALITY   

        self.row_index = row_index
        self.row_data = row_data
        # مرجع النافذة الرئيسية (MysideBar) حتى نتمكن من تحديث الجدول بعد التعديل/الحذف
        self.sideBar = sideBar
        # Get student variable from the tuple
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)
        #creat blue edit button
        self.edit_button = QPushButton("",self)
        self.edit_button.setStyleSheet("background-color: blue;")
        self.edit_button.setFixedSize(61,31)
        self.edit_button.clicked.connect(self.edit_clicked)
        #creat red delete button
        self.delete_button = QPushButton("",self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61,31)
        self.delete_button.clicked.connect(self.delete_clicked)
        #set icons for the buttons
        icon = QIcon("icons/edit.png")
        self.edit_button.setIcon(icon)
        icon2 = QIcon("icons/delete.png")
        self.delete_button.setIcon(icon2)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
    
    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_school"
        )
  
    def edit_clicked(self):
        # نُنشئ نسخة من حوار التعديل
        self.update_dialog = UpdateStudentsDialog(self.row_index, self.row_data)

        # نربط إشارة data_updated (تُطلق بعد نجاح الحفظ) بتحديث جدول الواجهة الرئيسية
        if self.sideBar is not None:
            self.update_dialog.data_updated.connect(self.sideBar.reload_studentstable_data)

        self.update_dialog.exec()

    def delete_clicked(self):
        # نسأل المستخدم للتأكيد قبل الحذف
        confirm = QMessageBox.question(
            self,
            'Confirmation',
            f'Are you sure you want to delete student {self.student_name}?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            # يجب تخزين كائن الاتصال في متغير، وإلا سيتم حذفه من الذاكرة
            # فوراً (garbage collected) قبل استخدام الـ cursor، مما يسبب
            # ReferenceError: weakly-referenced object no longer exists
            connection = self.create_connection()
            cursor = connection.cursor()

            delete_query = "DELETE FROM students_table WHERE student_id = %s"
            cursor.execute(delete_query, (self.student_id,))
            connection.commit()

            cursor.close()
            connection.close()

            # تحديث جدول الواجهة الرئيسية بعد الحذف (sideBar وليس sidebar)
            if self.sideBar is not None:
                self.sideBar.reload_studentstable_data()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

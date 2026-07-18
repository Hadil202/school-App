"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox
import mysql.connector
from random import randint
from datetime import datetime

from ui_student_dialog import Ui_StudentsDialog


class StudentsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_StudentsDialog()
         #  أهم سطر
        self.ui.setupUi(self)   

        self.setWindowTitle("Add Student")

        # ✅ الآن الزر موجود فعلاً
        self.ui.saveStudent_btn.clicked.connect(self.add_student)
        self.ui.cancel_btn.clicked.connect(self.close)

    # ---------------- DB ----------------

    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_school"
        )

    # ---------------- INSERT ----------------

    def insert_new_student(self):

        try:
            db = self.create_connection()
            cursor = db.cursor()

            gender = self.ui.gender_comboBox.currentText()
            student_id = self.generate_student_id(gender)
            birthday = self.handleDateChange()
            birth_date = self.ui.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            new_student = (
                self.ui.name_lineEdit.text(),
                student_id,
                gender,
                self.ui.class_comboBox.currentText(),
                birthday,
                age,
                self.ui.address_lineEdit.text(),
                self.ui.phone_lineEdit.text(),
                self.ui.email_lineEdit.text(),
            )

    #        cursor.execute("""
     #           INSERT INTO students_table (
     #               student_id, gender, class,
      #              birthday, age, address, phone_number, email
      #          ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
     #       """, new_student)

"""      db.commit()
            db.close()

            self.show_message()

        except mysql.connector.Error as err:
            QMessageBox.critical(
                self,
                "Database Error",
                str(err)
        )

    # ---------------- ID ----------------

    def generate_student_id(self, gender):

        db = self.create_connection()
        cursor = db.cursor()

        prefix = "24/U/M" if gender == "Male" else "24/U/F"

        while True:
            rand = f"{randint(1,9999):04d}"
            student_id = prefix + rand

            cursor.execute(
                "SELECT student_id FROM students_table WHERE student_id=%s",
                (student_id,)
            )

            if not cursor.fetchone():
                db.close()
                return student_id

    # ---------------- DATE ----------------

    def handleDateChange(self):
        return self.ui.dob_dateEdit.date().toString(Qt.ISODate)

    # ---------------- AGE ----------------

    def calculate_age(self, birth_date):

        today = datetime.now().date()

        birth = datetime(
            birth_date.year(),
            birth_date.month(),
            birth_date.day()
        ).date()

        age = today.year - birth.year

        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        return age

    # ---------------- MESSAGE ----------------

    def show_message(self):
        QMessageBox.information(self, "Success", "Student added successfully!")

    # ---------------- ACTION ----------------

    def add_student(self):
        self.insert_new_student()
        self.accept() """  
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox
import mysql.connector
from random import randint
from datetime import datetime

from ui_student_dialog import Ui_StudentsDialog


class StudentsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_StudentsDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Add Student")

        self.ui.saveStudent_btn.clicked.connect(self.add_student)
        self.ui.cancel_btn.clicked.connect(self.close)

    # ---------------- DB ----------------

    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_school"
        )

    # ---------------- INSERT ----------------

    def insert_new_student(self):

        try:
            db = self.create_connection()
            cursor = db.cursor()

            gender = self.ui.gender_comboBox.currentText()
            student_id = self.generate_student_id(gender)
            birthday = self.handleDateChange()
            birth_date = self.ui.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            new_student = (
                self.ui.name_lineEdit.text(),
                student_id,
                gender,
                self.ui.class_comboBox.currentText(),
                birthday,
                age,
                self.ui.address_lineEdit.text(),
                self.ui.phone_lineEdit.text(),
                self.ui.email_lineEdit.text(),
            )

            cursor.execute("""
                INSERT INTO students_table (
                    names, student_id, gender, class,
                    birthday, age, address, phone_number, email
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, new_student)

            db.commit()
            db.close()

            self.show_message()
            return True

        except mysql.connector.Error as err:
            QMessageBox.critical(
                self,
                "Database Error",
                str(err)
            )
            return False

    # ---------------- ID ----------------

    def generate_student_id(self, gender):

        db = self.create_connection()
        cursor = db.cursor()

        prefix = "24/U/M" if gender == "Male" else "24/U/F"

        while True:
            rand = f"{randint(1,9999):04d}"
            student_id = prefix + rand

            cursor.execute(
                "SELECT student_id FROM students_table WHERE student_id=%s",
                (student_id,)
            )

            if not cursor.fetchone():
                db.close()
                return student_id

    # ---------------- DATE ----------------

    def handleDateChange(self):
        return self.ui.dob_dateEdit.date().toString(Qt.ISODate)

    # ---------------- AGE ----------------

    def calculate_age(self, birth_date):

        today = datetime.now().date()

        birth = datetime(
            birth_date.year(),
            birth_date.month(),
            birth_date.day()
        ).date()

        age = today.year - birth.year

        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        return age

    # ---------------- MESSAGE ----------------

    def show_message(self):
        QMessageBox.information(self, "Success", "Student added successfully!")

    # ---------------- ACTION ----------------

    def add_student(self):
        if self.insert_new_student():
            self.accept()
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector
from random import randint
from datetime import datetime


class UpdateStudentsDialog(QDialog):
    # يُطلق هذا الإشارة بعد نجاح التحديث في قاعدة البيانات
    data_updated = Signal()

    def __init__(self, row_index, row_data):
        super().__init__()
        # Store the row_index and row data as instance variables
        self.row_index = row_index
        self.row_data = row_data

        # ---- Fetch student data from DB ----
        records = self.select_student()

        if not records:
            # السجل لم يعد موجوداً بنفس البيانات (ربما تم تعديله سابقاً ولم يتم تحديث الجدول)
            QMessageBox.warning(
                self,
                "Student Not Found",
                "This student's data is outdated. Please refresh the table and try again."
            )
            # نغلق الحوار تلقائياً بمجرد فتحه بدون أي خطأ
            from PySide6.QtCore import QTimer
            QTimer.singleShot(0, self.reject)
            self.student_info = None
            return

        self.student_info = records[0]
        print(self.student_info)

        # ترتيب الأعمدة كما في الجدول:
        # id, names, gender, class, birthday, age, address, phone, email
        self.student_id            = self.student_info[0]
        self.student_name          = self.student_info[1]
        self.student_gender_info   = self.student_info[2]
        self.student_class_info    = self.student_info[3]
        self.student_birthday_info = self.student_info[4]
        self.student_age_info      = self.student_info[5]
        self.student_address_info  = self.student_info[6]
        self.student_phone_info    = self.student_info[7]
        self.student_email_info    = self.student_info[8]

        # ---- Build UI ----
        self.resize(364, 451)
        self.setMinimumSize(QSize(0, 0))
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white ;\n"
"}\n"
"QLineEdit{\n"
"	border: 1px solid gray ;\n"
"	border-radius: 6px ;\n"
"	padding-left:15px;\n"
"	height:30px;\n"
"}\n"
"QDateEdit{\n"
"	border:1px solid gray ;\n"
"	border-radius: 6px ;\n"
"	padding-left:15px;\n"
"	height:22px;\n"
"}\n"
"QComboBox{\n"
"	border:2px solid white ;\n"
"	border-radius: 8px ;\n"
"	padding: 1px 18px 1px 3px ;\n"
"	background-color : balck ;\n"
"	color : white ; \n"
"	height:22px;\n"
"	padding-left:15px;\n"
"	font-weight: bold;\n"
"	selection-background-color:#2980B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 361, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 21))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 341, 327))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # ---- Name ----
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.verticalLayout.addWidget(self.name_lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        # ---- Gender / Class / DOB ----
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.verticalLayout_5.addWidget(self.gender_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.widget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.verticalLayout_6.addWidget(self.class_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.widget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        self.verticalLayout_7.addWidget(self.dob_dateEdit)

        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # ---- Address ----
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.verticalLayout_8.addWidget(self.label_9)

        self.address_lineEdit = QLineEdit(self.widget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.verticalLayout_8.addWidget(self.address_lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        # ---- Age ----
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.verticalLayout_3.addWidget(self.label_3)

        self.age_lineEdit = QLineEdit(self.widget)
        self.age_lineEdit.setObjectName(u"age_lineEdit")
        self.verticalLayout_3.addWidget(self.age_lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        # ---- Phone ----
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.verticalLayout_4.addWidget(self.label_5)

        self.phone_lineEdit = QLineEdit(self.widget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.verticalLayout_4.addWidget(self.phone_lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        # ---- Email ----
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.verticalLayout_9.addWidget(self.label_10)

        self.email_lineEdit = QLineEdit(self.widget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.verticalLayout_9.addWidget(self.email_lineEdit)

        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        # ---- Buttons ----
        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(184, 400, 171, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.saveStudent_btn = QPushButton(self.widget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMaximumSize(QSize(16777215, 33))
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white ;\n"
"	border-radius:8px;\n"
"	font-weight:bold ;\n"
"	font-size: 11px ;\n"
"}\n"
"")
        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.widget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 33))
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white ;\n"
"	border-radius:8px;\n"
"	font-weight:bold ;\n"
"	font-size: 11px ;\n"
"}")
        self.horizontalLayout_2.addWidget(self.cancel_btn)

        # ---- Finalize UI ----
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        # ملء الحقول بالبيانات القادمة من قاعدة البيانات (بعد إنشاء كل الـ widgets)
        self.load_student_data()

        # ---- Connect buttons ----
        self.saveStudent_btn.clicked.connect(self.update_student)
        self.cancel_btn.clicked.connect(self.close)

    # ---------------- UI text ----------------

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Update Student Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Update Student", None))
        self.label_2.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade3", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade 7", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date of Birth", None))
        self.label_9.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Age", None))
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.label_10.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Save Changes", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))

    # ---------------- Load data into fields ----------------

    def load_student_data(self):
        date_object = QDate.fromString(str(self.student_birthday_info), "yyyy-MM-dd")

        self.name_lineEdit.setText(str(self.student_name))
        self.gender_comboBox.setCurrentText(str(self.student_gender_info))
        self.class_comboBox.setCurrentText(str(self.student_class_info))
        self.dob_dateEdit.setDate(date_object)
        self.address_lineEdit.setText(str(self.student_address_info))
        self.age_lineEdit.setText(str(self.student_age_info))
        self.phone_lineEdit.setText(str(self.student_phone_info))
        self.email_lineEdit.setText(str(self.student_email_info))

        # نحفظ الجنس الأصلي لمقارنته لاحقاً عند الحفظ (لتوليد student_id جديد إذا تغيّر)
        self.original_gender = str(self.student_gender_info)

    # ---------------- DB ----------------

    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_school"
        )

    def select_student(self):
        mydb = self.create_connection()
        cursor = mydb.cursor()

        # student_id هو المفتاح الأساسي الفريد، لذا يكفي وحده للبحث
        # (البحث بالاسم أيضاً كان يفشل إذا تغيّر الاسم أو الجنس سابقاً)
        student_id = self.row_data[1]

        select_query = "SELECT * FROM students_table WHERE student_id=%s"
        cursor.execute(select_query, (student_id,))
        records = cursor.fetchall()

        cursor.close()
        mydb.close()

        return records

    def generate_student_id(self, gender):
        db = self.create_connection()
        cursor = db.cursor()

        prefix = "24/U/M" if gender == "Male" else "24/U/F"

        while True:
            rand = f"{randint(1, 9999):04d}"
            student_id = prefix + rand

            cursor.execute(
                "SELECT student_id FROM students_table WHERE student_id=%s",
                (student_id,)
            )

            if not cursor.fetchone():
                cursor.close()
                db.close()
                return student_id

    def calculate_age(self, birth_date):
        today = datetime.now().date()
        birth = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()

        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        return age

    def show_update_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Student Updated")
        msg_box.setText(f"{self.name_lineEdit.text()} updated successfully!")
        msg_box.exec()

    def update_student(self):
        try:
            mydb = self.create_connection()
            cursor = mydb.cursor()

            new_name = self.name_lineEdit.text()
            new_gender = self.gender_comboBox.currentText()
            new_class = self.class_comboBox.currentText()
            new_dob = self.dob_dateEdit.date().toString("yyyy-MM-dd")
            new_address = self.address_lineEdit.text()
            new_phone = self.phone_lineEdit.text()
            new_email = self.email_lineEdit.text()
            new_age = self.calculate_age(self.dob_dateEdit.date())

            # إذا تغيّر الجنس، ننشئ student_id جديد يطابق البادئة الجديدة
            if new_gender != self.original_gender:
                new_student_id = self.generate_student_id(new_gender)
            else:
                new_student_id = self.student_id

            update_query = """
                UPDATE students_table
                SET names=%s, student_id=%s, gender=%s, class=%s, birthday=%s,
                    age=%s, address=%s, phone_number=%s, email=%s
                WHERE student_id=%s
            """
            params = [
                new_name, new_student_id, new_gender, new_class, new_dob,
                new_age, new_address, new_phone, new_email,
                self.student_id
            ]

            cursor.execute(update_query, params)
            mydb.commit()

            cursor.close()
            mydb.close()

            print("Student updated successfully")
            self.data_updated.emit()  # نُعلم أي مستمع (مثل الجدول الرئيسي) بأن البيانات تغيّرت
            self.accept()  # يغلق الـ dialog ويُرجع QDialog.Accepted

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            QMessageBox.critical(self, "Database Error", str(err))
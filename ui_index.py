# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(959, 621)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 932, 740))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(0, 0, 0);\n"
"	color:white ;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 20, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton {\n"
"	padding-left:-50px ; }\n"
"QPushButton:checked{\n"
"	background-color:white ;\n"
"	border-radius:3px; }")
        icon = QIcon()
        icon.addFile(u":/icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setIconSize(QSize(100, 20))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton {\n"
"	padding-left:-60px ; }\n"
"QPushButton:checked{\n"
"	background-color:white ;\n"
"	border-radius:3px; }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon1)
        self.institution_2.setIconSize(QSize(100, 20))
        self.institution_2.setCheckable(True)
        self.institution_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students_2.setIcon(icon2)
        self.students_2.setIconSize(QSize(140, 40))
        self.students_2.setCheckable(True)

        self.verticalLayout.addWidget(self.students_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students_dropdown)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.student_info.setCheckable(True)

        self.verticalLayout_4.addWidget(self.student_info)

        self.student_payments = QPushButton(self.students_dropdown)
        self.student_payments.setObjectName(u"student_payments")
        self.student_payments.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.student_payments.setCheckable(True)

        self.verticalLayout_4.addWidget(self.student_payments)

        self.students_transactions = QPushButton(self.students_dropdown)
        self.students_transactions.setObjectName(u"students_transactions")
        self.students_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.students_transactions.setCheckable(True)

        self.verticalLayout_4.addWidget(self.students_transactions)


        self.verticalLayout.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teachers_2 = QPushButton(self.teachers)
        self.teachers_2.setObjectName(u"teachers_2")
        icon3 = QIcon()
        icon3.addFile(u":/icons/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_2.setIcon(icon3)
        self.teachers_2.setIconSize(QSize(145, 40))
        self.teachers_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.teachers_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teachers_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.teacher_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teacher_salaries = QPushButton(self.teachers_dropdown)
        self.teacher_salaries.setObjectName(u"teacher_salaries")
        self.teacher_salaries.setStyleSheet(u"QPushButton{\n"
"	padding-left:0px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.teacher_salaries.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_salaries)

        self.teacher_transactions = QPushButton(self.teachers_dropdown)
        self.teacher_transactions.setObjectName(u"teacher_transactions")
        self.teacher_transactions.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.teacher_transactions.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_transactions)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setFrameShape(QFrame.StyledPanel)
        self.finances.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finances_2 = QPushButton(self.finances)
        self.finances_2.setObjectName(u"finances_2")
        icon4 = QIcon()
        icon4.addFile(u":/icons/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/finances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances_2.setIcon(icon4)
        self.finances_2.setIconSize(QSize(145, 40))
        self.finances_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.finances_2)

        self.finances_dropdown = QFrame(self.finances)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finances_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finances_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton{\n"
"	padding-left:24px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finances_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px\n"
"}\n"
"QPushButton:hover{\n"
"	color:#12B298 }")
        self.business_overview.setCheckable(True)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finances_dropdown)


        self.verticalLayout_7.addWidget(self.finances)


        self.verticalLayout_15.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 84, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setMinimumSize(QSize(0, 0))
        self.settings_2.setStyleSheet(u"QPushButton {\n"
"	padding-left:-50px ; }\n"
"QPushButton:checked{\n"
"	background-color:white ;\n"
"	border-radius:3px; }")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon5)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton {\n"
"	padding-left:-50px ; }\n"
"QPushButton:checked{\n"
"	background-color:white ;\n"
"	border-radius:3px; }")
        icon6 = QIcon()
        icon6.addFile(u":/icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon6)
        self.signout_2.setIconSize(QSize(100, 20))
        self.signout_2.setCheckable(True)
        self.signout_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout_2)


        self.verticalLayout_15.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_24 = QPushButton(self.header_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(40, 40))
        self.pushButton_24.setStyleSheet(u"border : none ;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_24.setIcon(icon7)
        self.pushButton_24.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_24)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 10, -1, 10)
        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.header_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(167, 167, 167);")

        self.verticalLayout_9.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(336, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.label_8 = QLabel(self.header_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setPixmap(QPixmap(u":/icons/profile.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_8)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(500, 500))
        self.main_screen_widget.setMaximumSize(QSize(841, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.main_screen_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 190, 181, 61))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label.setFont(font2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 210, 181, 61))
        self.label_5.setFont(font2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, -10, 191, 41))
        font3 = QFont()
        font3.setFamilies([u"Nirmala UI"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 30, 471, 21))
        font4 = QFont()
        font4.setFamilies([u"Nirmala UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.label_19.setFont(font4)
        self.studentInfo_table = QTableWidget(self.page_3)
        if (self.studentInfo_table.columnCount() < 10):
            self.studentInfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(0, 150, 651, 351))
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color:balck;\n"
"	color:white ;}\n"
"QTableWidget{\n"
"	alternate-background-color:#B0EDFB;\n"
"	background-color:#F4F9FA; }	")
        self.studentInfo_table.setAlternatingRowColors(True)
        self.layoutWidget1 = QWidget(self.page_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 60, 341, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addStudent_btn = QPushButton(self.layoutWidget1)
        self.addStudent_btn.setObjectName(u"addStudent_btn")
        self.addStudent_btn.setMaximumSize(QSize(16777215, 33))
        self.addStudent_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(12, 12, 12);\n"
"	color:white ;\n"
"	border-radius:8px;\n"
"	font-weight:bold ;\n"
"	font-size: 11px ;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addStudent_btn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.addStudent_btn)

        self.excelExport_btn = QPushButton(self.layoutWidget1)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMaximumSize(QSize(16777215, 33))
        self.excelExport_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white ;\n"
"	border-radius:8px;\n"
"	font-weight:bold ;\n"
"	font-size: 11px ;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excelExport_btn.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.layoutWidget1)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(0, 33))
        self.pdfExport_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 1, 1);\n"
"	color: rgb(255, 33, 33);\n"
"	color:white ;\n"
"	border-radius:8px;\n"
"	font-weight:bold ;\n"
"	font-size: 11px ;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdfExport_btn.setIcon(icon10)

        self.horizontalLayout_2.addWidget(self.pdfExport_btn)

        self.layoutWidget2 = QWidget(self.page_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 110, 421, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.layoutWidget2)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_class = QComboBox(self.layoutWidget2)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_7.addWidget(self.select_class)

        self.search_student = QLineEdit(self.layoutWidget2)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 190, 341, 61))
        self.label_10.setFont(font2)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 200, 371, 61))
        self.label_11.setFont(font2)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 220, 381, 61))
        self.label_12.setFont(font2)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(240, 180, 331, 61))
        self.label_13.setFont(font2)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(220, 200, 391, 61))
        self.label_14.setFont(font2)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 250, 181, 61))
        self.label_15.setFont(font2)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 260, 181, 61))
        self.label_16.setFont(font2)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(200, 270, 331, 61))
        self.label_17.setFont(font2)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(240, 330, 181, 61))
        self.label_18.setFont(font2)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_10.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white ;\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon11 = QIcon()
        icon11.addFile(u":/icons/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon11)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon12 = QIcon()
        icon12.addFile(u":/icons/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_1.setIcon(icon12)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.institution_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        icon13 = QIcon()
        icon13.addFile(u":/icons/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students_1.setIcon(icon13)
        self.students_1.setIconSize(QSize(100, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.students_1)

        self.teachers_1 = QPushButton(self.icon_only_widget)
        self.teachers_1.setObjectName(u"teachers_1")
        icon14 = QIcon()
        icon14.addFile(u":/icons/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_1.setIcon(icon14)
        self.teachers_1.setIconSize(QSize(100, 20))
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.teachers_1)

        self.finances_1 = QPushButton(self.icon_only_widget)
        self.finances_1.setObjectName(u"finances_1")
        icon15 = QIcon()
        icon15.addFile(u":/icons/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/icons/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances_1.setIcon(icon15)
        self.finances_1.setIconSize(QSize(100, 20))
        self.finances_1.setCheckable(True)
        self.finances_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.finances_1)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.verticalSpacer = QSpacerItem(50, 412, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon16 = QIcon()
        icon16.addFile(u":/icons/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon16.addFile(u":/icons/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon16)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon17 = QIcon()
        icon17.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/icons/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon17)
        self.signout_1.setIconSize(QSize(100, 16))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.signout_1)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.finances_2.toggled.connect(self.finances_dropdown.setHidden)
        self.teachers_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.pushButton_24.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton_24.toggled.connect(self.icon_only_widget.setVisible)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.teachers_2.toggled.connect(self.teachers_1.setChecked)
        self.finances_2.toggled.connect(self.finances_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.students_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_payments.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.students_transactions.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salaries.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_transactions.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finances_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton_24.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"welecom Hadil ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"this your page ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here ...", None))
        self.label_8.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashborad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Welcome to the students information page", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student id", None))
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gander", None))
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem9 = self.studentInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.addStudent_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Gender", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Class", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 7", None))

        self.search_student.setText("")
        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student_payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Students_trasactions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"teacher_information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"teacher_salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"teacher_transactions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"business_overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.students_1.setText("")
        self.teachers_1.setText("")
        self.finances_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
    # retranslateUi


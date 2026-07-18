# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_StudentsDialog(object):
    def setupUi(self, StudentsDialog):
        if not StudentsDialog.objectName():
            StudentsDialog.setObjectName(u"StudentsDialog")
        StudentsDialog.resize(364, 451)
        StudentsDialog.setMinimumSize(QSize(0, 0))
        StudentsDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(StudentsDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 361, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(StudentsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 21))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(StudentsDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 341, 327))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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

        self.widget1 = QWidget(StudentsDialog)
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


        self.retranslateUi(StudentsDialog)

        QMetaObject.connectSlotsByName(StudentsDialog)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
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
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.label_10.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi


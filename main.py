from packets_filtr import Tools
from speed_testing import SpeedTesting
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 564)
        MainWindow.setStyleSheet("  \n"
"            QWidget {\n"
"                background-color: #f0f0f0;  /* Світло-сірий фон */\n"
"                font-family: Arial, sans-serif;\n"
"                font-size: 14px;      \n"
"                   color: #333333;  /* Темно-сірий текст */\n"
"\n"
"            }\n"
"\n"
"            \n"
"            QLabel {\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"                color: #444444;  /* Трохи темніший сірий */\n"
"                margin-bottom: 10px;\n"
"            }\n"
"\n"
"            \n"
"            QLineEdit {\n"
"                background-color: #ffffff;  /* Білий фон */\n"
"                border: 2px solid #cccccc;  /* Світло-сіра рамка */\n"
"                border-radius: 8px;\n"
"                padding: 6px 10px;\n"
"                font-size: 14px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 2px solid #32CD32;  /* Салатова рамка при фокусі */\n"
"            }\n"
"\n"
"            \n"
"            QPushButton {\n"
"                background-color: #32CD32;  /* Салатовий колір */\n"
"                color: white;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"                border: 2px solid #228B22;  /* Темно-зелена рамка */\n"
"                border-radius: 10px;\n"
"                padding: 8px 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #3CB371;  /* Світліший салатовий при наведенні */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #2E8B57;  /* Темний салатовий при натисканні */\n"
"            }")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_test = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test.setGeometry(QtCore.QRect(10, 110, 391, 39))
        self.btn_test.setObjectName("btn_test")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 11, 148, 29))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 46, 125, 29))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(165, 11, 83, 29))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(9, 91, 393, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(165, 46, 83, 29))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 150, 393, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox_adap = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_adap.setGeometry(QtCore.QRect(40, 460, 251, 22))
        self.comboBox_adap.setObjectName("comboBox_adap")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 220, 251, 206))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_MAC = QtWidgets.QLabel(self.widget)
        self.label_MAC.setObjectName("label_MAC")
        self.gridLayout.addWidget(self.label_MAC, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_bytes_rec = QtWidgets.QLabel(self.widget)
        self.label_bytes_rec.setObjectName("label_bytes_rec")
        self.gridLayout.addWidget(self.label_bytes_rec, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_bytes_sent = QtWidgets.QLabel(self.widget)
        self.label_bytes_sent.setObjectName("label_bytes_sent")
        self.gridLayout.addWidget(self.label_bytes_sent, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_packets_sent = QtWidgets.QLabel(self.widget)
        self.label_packets_sent.setObjectName("label_packets_sent")
        self.gridLayout.addWidget(self.label_packets_sent, 2, 1, 1, 1)
        self.label_packets_rec = QtWidgets.QLabel(self.widget)
        self.label_packets_rec.setObjectName("label_packets_rec")
        self.gridLayout.addWidget(self.label_packets_rec, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_IP = QtWidgets.QLabel(self.widget)
        self.label_IP.setObjectName("label_IP")
        self.gridLayout.addWidget(self.label_IP, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 22))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInfo.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def start_test(self):
        try:
            st = SpeedTesting()
            tests = st.start_test()
            return  str(tests['Download']), str(tests['Upload'])
        except Exception as e:
            return "Error" , "Try later"
    
    def add_results(self):
        self.btn_test.clicked.connect(lambda: self.display_results())

    def display_results(self):
        _translate = QtCore.QCoreApplication.translate
        download_speed, upload_speed = self.start_test()
        self.label_3.setText(_translate("MainWindow", str(download_speed)))
        self.label_4.setText(_translate("MainWindow", str(upload_speed)))



    def display_statictics(self):
        Tool =  Tools()
        adap_list = list(Tool.get_netstats().keys())
        for adap in adap_list:
            self.comboBox_adap.addItem(adap)
        self.comboBox_adap.currentIndexChanged.connect(self.update_statistics)

    def update_statistics(self):
        selected_adap = self.comboBox_adap.currentText()
        Tool = Tools()
        dict_data = Tool.traffic_stats()
        for data in dict_data:
            if data['Name'] == selected_adap:
                self.label_bytes_sent.setText(str(data["MBytes sent"])) 
                self.label_bytes_rec.setText(str(data["MBytes received"]))
                self.label_packets_sent.setText(str(data["Packets sent"]))
                self.label_packets_rec.setText(str(data["Packets received"]))
                self.label_MAC.setText(str(data["MAC"]))
                self.label_IP.setText(str(data["IP"]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Program for PC statictics"))
        self.btn_test.setText(_translate("MainWindow", "Start Test"))
        self.label.setText(_translate("MainWindow", "Download speed: "))
        self.label_2.setText(_translate("MainWindow", "Upload speed: "))
        self.label_3.setText(_translate("MainWindow", "N/A"))
        self.label_4.setText(_translate("MainWindow", "N/A"))
        self.label_MAC.setText(_translate("MainWindow", "N/A"))
        self.label_5.setText(_translate("MainWindow", "Packets received:"))
        self.label_bytes_rec.setText(_translate("MainWindow", "N/A"))
        self.label_6.setText(_translate("MainWindow", "MBytes sent:"))
        self.label_bytes_sent.setText(_translate("MainWindow", "N/A"))
        self.label_10.setText(_translate("MainWindow", "MBytes received:"))
        self.label_8.setText(_translate("MainWindow", "Packets sent:"))
        self.label_packets_sent.setText(_translate("MainWindow", "N/A"))
        self.label_packets_rec.setText(_translate("MainWindow", "N/A"))
        self.label_13.setText(_translate("MainWindow", "MAC:"))
        self.label_15.setText(_translate("MainWindow", "IP:"))
        self.label_IP.setText(_translate("MainWindow", "N/A"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))

         # Adjust size for all labels
        self.label.adjustSize()
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_MAC.adjustSize()
        self.label_5.adjustSize()
        self.label_bytes_rec.adjustSize()
        self.label_6.adjustSize()
        self.label_bytes_sent.adjustSize()
        self.label_10.adjustSize()
        self.label_8.adjustSize()
        self.label_packets_sent.adjustSize()
        self.label_packets_rec.adjustSize()
        self.label_13.adjustSize()
        self.label_15.adjustSize()
        self.label_IP.adjustSize()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_results()
    ui.display_statictics()
    ui.update_statistics()
    MainWindow.show()
    sys.exit(app.exec_())

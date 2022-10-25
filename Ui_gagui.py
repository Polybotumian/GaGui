# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\kotiasCodeBase\python\mypycodes\ga_gui\gagui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(553, 466)
        MainWindow.setMinimumSize(QtCore.QSize(553, 410))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(551, 425))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ga = QtWidgets.QWidget()
        self.tab_ga.setObjectName("tab_ga")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_ga)
        self.gridLayout.setObjectName("gridLayout")
        self.label_inputs = QtWidgets.QLabel(self.tab_ga)
        self.label_inputs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_inputs.setObjectName("label_inputs")
        self.gridLayout.addWidget(self.label_inputs, 0, 0, 1, 1)
        self.lineEdit_inputs = QtWidgets.QLineEdit(self.tab_ga)
        self.lineEdit_inputs.setObjectName("lineEdit_inputs")
        self.gridLayout.addWidget(self.lineEdit_inputs, 0, 1, 1, 1)
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.tab_ga)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.plainTextEdit_output.setFont(font)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.gridLayout.addWidget(self.plainTextEdit_output, 0, 2, 7, 1)
        self.label_sol_per_pop = QtWidgets.QLabel(self.tab_ga)
        self.label_sol_per_pop.setTextFormat(QtCore.Qt.AutoText)
        self.label_sol_per_pop.setScaledContents(False)
        self.label_sol_per_pop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sol_per_pop.setWordWrap(True)
        self.label_sol_per_pop.setObjectName("label_sol_per_pop")
        self.gridLayout.addWidget(self.label_sol_per_pop, 1, 0, 1, 1)
        self.spinBox_sol_per_pop = QtWidgets.QSpinBox(self.tab_ga)
        self.spinBox_sol_per_pop.setMaximum(10000)
        self.spinBox_sol_per_pop.setObjectName("spinBox_sol_per_pop")
        self.gridLayout.addWidget(self.spinBox_sol_per_pop, 1, 1, 1, 1)
        self.label_gen_num = QtWidgets.QLabel(self.tab_ga)
        self.label_gen_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_gen_num.setTextFormat(QtCore.Qt.AutoText)
        self.label_gen_num.setScaledContents(False)
        self.label_gen_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gen_num.setWordWrap(True)
        self.label_gen_num.setObjectName("label_gen_num")
        self.gridLayout.addWidget(self.label_gen_num, 2, 0, 1, 1)
        self.spinBox_gen_num = QtWidgets.QSpinBox(self.tab_ga)
        self.spinBox_gen_num.setMaximum(10000)
        self.spinBox_gen_num.setObjectName("spinBox_gen_num")
        self.gridLayout.addWidget(self.spinBox_gen_num, 2, 1, 1, 1)
        self.label_parent_num = QtWidgets.QLabel(self.tab_ga)
        self.label_parent_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_parent_num.setTextFormat(QtCore.Qt.AutoText)
        self.label_parent_num.setScaledContents(False)
        self.label_parent_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_parent_num.setWordWrap(True)
        self.label_parent_num.setObjectName("label_parent_num")
        self.gridLayout.addWidget(self.label_parent_num, 3, 0, 1, 1)
        self.spinBox_parent_num = QtWidgets.QSpinBox(self.tab_ga)
        self.spinBox_parent_num.setMaximum(10000)
        self.spinBox_parent_num.setObjectName("spinBox_parent_num")
        self.gridLayout.addWidget(self.spinBox_parent_num, 3, 1, 1, 1)
        self.label_low = QtWidgets.QLabel(self.tab_ga)
        self.label_low.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_low.setTextFormat(QtCore.Qt.AutoText)
        self.label_low.setScaledContents(False)
        self.label_low.setAlignment(QtCore.Qt.AlignCenter)
        self.label_low.setWordWrap(True)
        self.label_low.setObjectName("label_low")
        self.gridLayout.addWidget(self.label_low, 4, 0, 1, 1)
        self.spinBox_low = QtWidgets.QSpinBox(self.tab_ga)
        self.spinBox_low.setMaximum(10000)
        self.spinBox_low.setObjectName("spinBox_low")
        self.gridLayout.addWidget(self.spinBox_low, 4, 1, 1, 1)
        self.label_high = QtWidgets.QLabel(self.tab_ga)
        self.label_high.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_high.setTextFormat(QtCore.Qt.AutoText)
        self.label_high.setScaledContents(False)
        self.label_high.setAlignment(QtCore.Qt.AlignCenter)
        self.label_high.setWordWrap(True)
        self.label_high.setObjectName("label_high")
        self.gridLayout.addWidget(self.label_high, 5, 0, 1, 1)
        self.spinBox_high = QtWidgets.QSpinBox(self.tab_ga)
        self.spinBox_high.setMaximum(10000)
        self.spinBox_high.setObjectName("spinBox_high")
        self.gridLayout.addWidget(self.spinBox_high, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_ga)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_ga)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_ga)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 7, 0, 2, 2)
        self.graphWidget = PlotWidget(self.tab_ga)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout.addWidget(self.graphWidget, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_ga)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 2, 1, 1)
        self.tabWidget.addTab(self.tab_ga, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_info)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_info)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_info, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 20))
        self.menubar.setObjectName("menubar")
        self.menuWrite_Results = QtWidgets.QMenu(self.menubar)
        self.menuWrite_Results.setObjectName("menuWrite_Results")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWrite_Results = QtWidgets.QAction(MainWindow)
        self.actionWrite_Results.setObjectName("actionWrite_Results")
        self.actiontable_to_excel = QtWidgets.QAction(MainWindow)
        self.actiontable_to_excel.setObjectName("actiontable_to_excel")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuWrite_Results.addAction(self.actionWrite_Results)
        self.menuWrite_Results.addAction(self.actiontable_to_excel)
        self.menubar.addAction(self.menuWrite_Results.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GAGUI"))
        self.label_inputs.setText(_translate("MainWindow", "Inputs"))
        self.label_sol_per_pop.setText(_translate("MainWindow", "Solution Per Population"))
        self.label_gen_num.setText(_translate("MainWindow", "Generation Number"))
        self.label_parent_num.setText(_translate("MainWindow", "Parent Number"))
        self.label_low.setText(_translate("MainWindow", "Low"))
        self.label_high.setText(_translate("MainWindow", "High"))
        self.pushButton.setText(_translate("MainWindow", "Compute"))
        self.label_2.setText(_translate("MainWindow", "X : Generations, Y : Maximums"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ga), _translate("MainWindow", "GA"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00aa00;\">ABOUT GAGUI</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> This application was developed by Yiğit Leblebicier, a computer engineering student at Isparta Uygulamalı Bilimler University, Turkey.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00aa00;\">PURPOSE OF GAGUI</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> GAGUI was homework for the AI course, and its purpose is to be a graphical user interface for finding maximized value for the </span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">Y = W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">1</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">1</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\"> + W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">2</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">2 </span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">+ W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">3</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">3</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\"> + W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">4</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">4 </span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">+ W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">5</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">5</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\"> + W</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">6</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\">X</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00; vertical-align:sub;\">6</span><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:14pt; color:#00aa00;\"> + ...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600; text-decoration: underline; color:#00aa00;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa55ff;\">https://github.com/Polybotumian</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa55ff;\">https://www.linkedin.com/in/yi%C4%9Fit-leblebicier-0bb2601b6/</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("MainWindow", "INFO"))
        self.menuWrite_Results.setTitle(_translate("MainWindow", "Options"))
        self.actionWrite_Results.setText(_translate("MainWindow", "Console to txt File"))
        self.actiontable_to_excel.setText(_translate("MainWindow", "Table to xlsx File"))
        self.actionhelp.setText(_translate("MainWindow", "Help"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import Ui_gagui
from functools import partial
import qdarkgraystyle
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    import sys
    app = Ui_gagui.QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    app.setWindowIcon(QIcon('icon.png'))
    MainWindow = Ui_gagui.QtWidgets.QMainWindow()
    ui = Ui_gagui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    from gagui import genetic_algorithm, write_results, prevent_negative_dimension, write_excel
    ui.pushButton.clicked.connect(partial(genetic_algorithm, ui))
    ui.actionWrite_Results.triggered.connect(partial(write_results, ui))
    ui.actiontable_to_excel.triggered.connect(partial(write_excel, ui))
    ui.spinBox_sol_per_pop.valueChanged.connect(partial(prevent_negative_dimension, ui))
    sys.exit(app.exec_())
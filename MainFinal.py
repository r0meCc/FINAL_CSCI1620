from PyQt6 import QtWidgets
from logic_handler import *
from GUI2 import *


class MenuDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.EnterButton.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        if self.ui.radioButton.isChecked():
            self.hide()  # Hide the menu dialog
            self.shopping_cart_window = ShoppingCartWindow()  # Create shopping cart window
            self.shopping_cart_window.show()

        elif self.ui.radioButton_2.isChecked():
            QtWidgets.QApplication.quit()  # Exit the application

class ShoppingCartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.logic_handler = LogicHandler(self.ui)  # Create an instance of LogicHandler
        self.ui.pushButton.clicked.connect(self.logic_handler.calculate_totals)  # Connect the button click to the calculation function
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = MenuDialog()
    dialog.show()
    sys.exit(app.exec())
from PyQt6 import QtCore, QtGui, QtWidgets
from GUI2 import *

#screen2


class LogicHandler:
    def __init__(self, ui):
        self.ui = ui
        self.ui.pushButton.clicked.connect(self.calculate_totals)

    def calculate_totals(self):
        try:
            quantity_cookie = float(self.ui.lineEdit.text())
            if quantity_cookie < 0:
                raise ValueError("Quantity must not be negative")
            total_cookie = quantity_cookie * 1.50
        except ValueError:
            total_cookie = 0.0
        self.ui.lineEdit_4.setText(f"${total_cookie:.2f}")

        try:
            quantity_sandwich = float(self.ui.lineEdit_2.text())
            if quantity_sandwich < 0:
                raise ValueError("Quantity must not be negative")
            total_sandwich = quantity_sandwich * 4.00
        except ValueError:
            total_sandwich = 0.0
        self.ui.lineEdit_5.setText(f"${total_sandwich:.2f}")

        try:
            quantity_water = float(self.ui.lineEdit_3.text())
            if quantity_water < 0:
                raise ValueError("Quantity must not be negative")
            total_water = quantity_water * 1.00
        except ValueError:
            total_water = 0.0
        self.ui.lineEdit_6.setText(f"${total_water:.2f}")

        subtotal = total_cookie + total_sandwich + total_water
        self.ui.lineEdit_7.setText(f"${subtotal:.2f}")

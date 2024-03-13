#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gui
from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication([])

widget = gui.XpCalculatorWidget()
widget.setStyleSheet("background-color: #404040;")
widget.show()

sys.exit(app.exec())

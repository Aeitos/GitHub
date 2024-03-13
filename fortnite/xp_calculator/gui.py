from PySide6 import QtCore, QtGui, QtWidgets
import core
import sys


class XpCalculatorWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(XpCalculatorWidget, self).__init__(parent=parent)

        self.PREFIX_XP_LEFT = "Total XPs left : "
        self.PREFIX_TIME_LEFT = "End of season : "
        self.PREFIX_XP_MADE_PER_DAY = "XPs made per day : "
        self.PREFIX_XP_LEFT_PER_DAY = "XPs left per day : "
        self.LABEL_STYLESHEET = """
            QToolTip { 
                background-color: black; 
                color: white; 
                border: black solid 1px
            }
            QLabel {
                color: white;
            }
            QSpinBox {
                color: white;
            }
           """

        self._built_ui()
        self._make_connections()
        self._initialize_ui()

    def _built_ui(self):
        self._main_layout = QtWidgets.QVBoxLayout(self)
        self._main_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # Ti
        self._time_left_widget = QtWidgets.QLabel(self)
        self._time_left_widget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        font = self._time_left_widget.font()
        font.setPointSize(18)
        self._time_left_widget.setFont(font)
        self._time_left_widget.setStyleSheet("color: white")
        self._main_layout.addWidget(self._time_left_widget)

        self._xp_made_per_day_widget = QtWidgets.QLabel(self)
        self._xp_made_per_day_widget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        font = self._xp_made_per_day_widget.font()
        font.setPointSize(18)
        self._xp_made_per_day_widget.setFont(font)
        self._xp_made_per_day_widget.setStyleSheet("color: white")
        self._main_layout.addWidget(self._xp_made_per_day_widget)

        self._xp_left_per_day_widget = QtWidgets.QLabel(self)
        self._xp_left_per_day_widget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        font = self._xp_left_per_day_widget.font()
        font.setPointSize(18)
        self._xp_left_per_day_widget.setFont(font)
        self._xp_left_per_day_widget.setStyleSheet("color: white")
        self._main_layout.addWidget(self._xp_left_per_day_widget)

        self._result_display_widget = QtWidgets.QLabel(self)
        self._result_display_widget.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        font = self._result_display_widget.font()
        font.setPointSize(18)
        self._result_display_widget.setFont(font)
        self._result_display_widget.setStyleSheet("color: white")
        self._main_layout.addWidget(self._result_display_widget)

        self._input_layout = QtWidgets.QHBoxLayout()
        self._main_layout.addLayout(self._input_layout)

        self._level_label = QtWidgets.QLabel(self)
        self._level_label.setText("Levels : ")
        self._level_label.setToolTip("Current level in game.")
        self._level_label.setStyleSheet(self.LABEL_STYLESHEET)
        self._input_layout.addWidget(self._level_label)

        self._input_level = QtWidgets.QSpinBox(self)
        self._input_level.setStyleSheet(self.LABEL_STYLESHEET)
        self._input_level.setToolTip("Current level in game.")
        self._input_level.setMinimum(0)
        self._input_level.setMaximum(199)
        self._input_level.setSingleStep(1)
        self._input_layout.addWidget(self._input_level)

        self._input_layout.addStretch(0)

        self._xp_label = QtWidgets.QLabel(self)
        self._xp_label.setText("XPs left : ")
        self._xp_label.setToolTip("XPs left to get to the next level.")
        self._xp_label.setStyleSheet(self.LABEL_STYLESHEET)
        self._input_layout.addWidget(self._xp_label)

        self._input_xp_left = QtWidgets.QSpinBox(self)
        self._input_xp_left.setStyleSheet(self.LABEL_STYLESHEET)
        self._input_xp_left.setToolTip("XPs left to get to the next level.")
        self._input_xp_left.setMinimum(0)
        self._input_xp_left.setMaximum(80000)
        self._input_xp_left.setValue(80000)
        self._input_xp_left.setSingleStep(1)

        self._input_layout.addWidget(self._input_xp_left)

    def _make_connections(self):
        self._input_level.valueChanged.connect(self._on_level_changed)
        self._input_xp_left.valueChanged.connect(self._on_xp_changed)

    def _initialize_ui(self):
        self._on_value_changed()
        self._time_left_widget.setText(f"{self.PREFIX_TIME_LEFT}{core.get_time_left()}")

    def _on_level_changed(self):
        self._on_value_changed()

    def _on_xp_changed(self):
        self._on_value_changed()

    def _on_value_changed(self):
        # Get date from user input data.
        current_level = self._input_level.value()
        current_xp = core.XP_PER_LEVEL - self._input_xp_left.value()

        # Setup xp left
        xp_left = core.get_left_xp(current_level=current_level, current_xp=current_xp)
        self._result_display_widget.setText(f"{self.PREFIX_XP_LEFT}{xp_left:,}".replace(",", " "))

        # Setup xp made per day.
        xp_made_per_day = core.get_xp_made_per_day(current_level=current_level, current_xp=current_xp)
        self._xp_made_per_day_widget.setText(f"{self.PREFIX_XP_MADE_PER_DAY}{xp_made_per_day:,}".replace(",", " "))

        # Setup xp left per day
        xp_left_per_day = core.get_xp_per_day_left(
            total_xp_left=core.get_left_xp(
                current_level=current_level,
                current_xp=current_xp
            )
        )
        self._xp_left_per_day_widget.setText(f"{self.PREFIX_XP_LEFT_PER_DAY}{xp_left_per_day:,}".replace(",", " "))

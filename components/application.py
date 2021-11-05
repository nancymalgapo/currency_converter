from forex_python.converter import CurrencyRates

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow

from ui.main_window import Ui_CurrencyConverterWindow


class RealTimeCurrencyConverter(QMainWindow, Ui_CurrencyConverterWindow):
    CURRENCY_LIST = ["SGD", "INR", "USD", "CAD", "CNY", "DKK", "EUR", "PHP", "JPY", "GBP"]

    def __init__(self):
        super().__init__()
        self._main_ui = Ui_CurrencyConverterWindow()
        self._main_ui.setupUi(self)
        self._initialization()

    def _initialization(self):
        validator = QRegExpValidator(QRegExp(r'[0-9].[0-9]+'))
        self._main_ui.amount.setValidator(validator)
        self._main_ui.from_combobox.addItems(self.CURRENCY_LIST)
        self._main_ui.to_combobox.addItems(self.CURRENCY_LIST)
        self._initialize_connections()

    def _initialize_connections(self):
        self._main_ui.convert_button.clicked.connect(self._set_converted_amount)

    def _set_converted_amount(self):
        from_currency = self._main_ui.from_combobox.currentText()
        to_currency = self._main_ui.to_combobox.currentText()
        starting_amount = float(self._main_ui.amount.text())
        converted_amount = self._convert_to_specific_currency(from_currency, to_currency, starting_amount)
        self._main_ui.converted_amount.setText(str(converted_amount))

    @staticmethod
    def _convert_to_specific_currency(from_currency, to_currency, amount):
        currency_rates = CurrencyRates()
        result = currency_rates.convert(from_currency, to_currency, amount)
        return round(result, 2)

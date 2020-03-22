from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys
from functools import partial

RIGA_UNO = 1
RIGA_DUE = 2
RIGA_TRE = 3
RIGA_QUATTRO = 4
RIGA_CINQUE = 5
RIGA_SEI = 6
RIGA_SETTE = 7
RIGA_OTTO = 8

class mywindow(QtWidgets.QMainWindow):


    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.row_one = 0
        self.row_two = 0
        self.row_three = 0
        self.row_four = 0
        self.row_five = 0
        self.row_six = 0
        self.row_seven = 0
        self.row_eight = 0

        self.ui.btn_uno.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 7))
        self.ui.btn_due.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 6))
        self.ui.btn_tre.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 5))
        self.ui.btn_quattro.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 4))
        self.ui.btn_cinque.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 3))
        self.ui.btn_sei.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 2))
        self.ui.btn_sette.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 1))
        self.ui.btn_otto.clicked.connect(partial(self.btn_set_led, self.row_one, RIGA_UNO, 0))
        self.ui.btn_nove.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 7))
        self.ui.btn_dieci.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 6))
        self.ui.btn_undici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 5))
        self.ui.btn_dodici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 4))
        self.ui.btn_tredici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 3))
        self.ui.btn_quattordici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 2))
        self.ui.btn_quindici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 1))
        self.ui.btn_sedici.clicked.connect(partial(self.btn_set_led, self.row_two, RIGA_DUE, 0))
        self.ui.btn_diciassette.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 7))
        self.ui.btn_diciotto.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 6))
        self.ui.btn_diciannove.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 5))
        self.ui.btn_venti.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 4))
        self.ui.btn_ventuno.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 3))
        self.ui.btn_ventidue.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 2))
        self.ui.btn_ventitre.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 1))
        self.ui.btn_ventiquattro.clicked.connect(partial(self.btn_set_led, self.row_three, RIGA_TRE, 0))
        self.ui.btn_venticinque.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 7))
        self.ui.btn_ventisei.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 6))
        self.ui.btn_ventisette.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 5))
        self.ui.btn_ventotto.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 4))
        self.ui.btn_ventinove.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 3))
        self.ui.btn_trenta.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 2))
        self.ui.btn_trentuno.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 1))
        self.ui.btn_trentadue.clicked.connect(partial(self.btn_set_led, self.row_four, RIGA_QUATTRO, 0))
        self.ui.btn_trentatre.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 7))
        self.ui.btn_trentaquattro.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 6))
        self.ui.btn_trentacinque.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 5))
        self.ui.btn_trentasei.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 4))
        self.ui.btn_trentasette.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 3))
        self.ui.btn_trentotto.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 2))
        self.ui.btn_trentanove.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 1))
        self.ui.btn_quaranta.clicked.connect(partial(self.btn_set_led, self.row_five, RIGA_CINQUE, 0))
        self.ui.btn_quarantuno.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 7))
        self.ui.btn_quarantadue.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 6))
        self.ui.btn_quarantatre.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 5))
        self.ui.btn_quarantaquattro.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 4))
        self.ui.btn_quarantacinque.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 3))
        self.ui.btn_quarantasei.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 2))
        self.ui.btn_quarantasette.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 1))
        self.ui.btn_quarantotto.clicked.connect(partial(self.btn_set_led, self.row_six, RIGA_SEI, 0))
        self.ui.btn_quarantanove.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 7))
        self.ui.btn_cinquanta.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 6))
        self.ui.btn_cinquantuno.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 5))
        self.ui.btn_cinquantadue.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 4))
        self.ui.btn_cinquantatre.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 3))
        self.ui.btn_cinquantaquattro.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 2))
        self.ui.btn_cinquantacinque.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 1))
        self.ui.btn_cinquantasei.clicked.connect(partial(self.btn_set_led, self.row_seven, RIGA_SETTE, 0))
        self.ui.btn_cinquantasette.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 7))
        self.ui.btn_cinquantotto.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 6))
        self.ui.btn_cinquantanove.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 5))
        self.ui.btn_sessanta.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 4))
        self.ui.btn_sessantuno.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 3))
        self.ui.btn_sessantadue.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 2))
        self.ui.btn_sessantatre.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 1))
        self.ui.btn_sessantaquattro.clicked.connect(partial(self.btn_set_led, self.row_eight, RIGA_OTTO, 0))

        self.ui.btn_generate_code.clicked.connect(self.generate_code)
        self.ui.txt_array_result.setReadOnly(True)

    def btn_set_led(self, _, row, amount_shift):

        if(row == RIGA_UNO):

            shifted_value = 1 << amount_shift
            self.row_one |= shifted_value
            self.color_button(row, amount_shift)

        elif(row == RIGA_DUE):

            shifted_value = 1 << amount_shift
            self.row_two |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_TRE):

            shifted_value = 1 << amount_shift
            self.row_three |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_QUATTRO):

            shifted_value = 1 << amount_shift
            self.row_four |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_CINQUE):

            shifted_value = 1 << amount_shift
            self.row_five |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_SEI):

            shifted_value = 1 << amount_shift
            self.row_six |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_SETTE):

            shifted_value = 1 << amount_shift
            self.row_seven |= shifted_value
            self.color_button(row, amount_shift)

        elif (row == RIGA_OTTO):

            shifted_value = 1 << amount_shift
            self.row_eight |= shifted_value
            self.color_button(row, amount_shift)

    def btn_clear(self):
        print(self.row_one)
        self.row_one = ''
        print(self.row_one)

    def generate_code(self):

        print('0x{:02x}'.format(self.row_one))
        print('0x{:02x}'.format(self.row_two))
        print('0x{:02x}'.format(self.row_three))
        print('0x{:02x}'.format(self.row_four))
        print('0x{:02x}'.format(self.row_five))
        print('0x{:02x}'.format(self.row_six))
        print('0x{:02x}'.format(self.row_seven))
        print('0x{:02x}'.format(self.row_eight))

        # Write reulsting array inside textbox
        self.ui.txt_array_result.insertPlainText('{' + '0x{:02x}'.format(self.row_one) + ',' +
                    '0x{:02x}'.format(self.row_two) + ',' + '0x{:02x}'.format(self.row_three) + ',' +
                    '0x{:02x}'.format(self.row_four) + ',' + '0x{:02x}'.format(self.row_five) + ',' +
                    '0x{:02x}'.format(self.row_six) + ',' + '0x{:02x}'.format(self.row_seven) + ',' +
                    '0x{:02x}'.format(self.row_eight) + '}')

    def color_button(self, linea, posizione):

        if(linea == RIGA_UNO):

            if(posizione == 7):

                self.ui.btn_uno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_due.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_tre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_quattro.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_cinque.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_sei.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_sette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_otto.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_DUE):

            if(posizione == 7):

                self.ui.btn_nove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_dieci.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_undici.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_dodici.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_tredici.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_quattordici.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_quindici.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_sedici.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_TRE):

            if(posizione == 7):

                self.ui.btn_diciassette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_diciotto.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_diciannove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_venti.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_ventuno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_ventidue.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_ventitre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_ventiquattro.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_QUATTRO):

            if(posizione == 7):

                self.ui.btn_venticinque.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_ventisei.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_ventisette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_ventotto.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_ventinove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_trenta.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_trentuno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_trentadue.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_CINQUE):

            if(posizione == 7):

                self.ui.btn_trentatre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_trentaquattro.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_trentacinque.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_trentasei.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_trentasette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_trentotto.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_trentanove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_quaranta.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_SEI):

            if(posizione == 7):

                self.ui.btn_quarantuno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_quarantadue.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_quarantatre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_quarantaquattro.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_quarantacinque.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_quarantasei.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_quarantasette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_quarantotto.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_SETTE):

            if(posizione == 7):

                self.ui.btn_quarantanove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_cinquanta.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_cinquantuno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_cinquantadue.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_cinquantatre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_cinquantaquattro.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_cinquantacinque.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_cinquantasei.setStyleSheet('background-color:#FF0000;color:#000000;')

        if(linea == RIGA_OTTO):

            if(posizione == 7):

                self.ui.btn_cinquantasette.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 6):

                self.ui.btn_cinquantotto.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 5):

                self.ui.btn_cinquantanove.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 4):

                self.ui.btn_sessanta.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 3):

                self.ui.btn_sessantuno.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 2):

                self.ui.btn_sessantadue.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 1):

                self.ui.btn_sessantatre.setStyleSheet('background-color:#FF0000;color:#000000;')

            elif(posizione == 0):

                self.ui.btn_sessantaquattro.setStyleSheet('background-color:#FF0000;color:#000000;')




# Questa riga di codice mi permette di convertire un numero binario sotto in esadecimale (come stringa)
# hex_string = '0x{:02x}'.format(int(bin(10), 2))
#FF0000 per il rosso

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
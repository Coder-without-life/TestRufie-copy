# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)   
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        self.index = (4*(int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3) - 200) / 10)

        if self.exp.txt_age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index < 15:
                return txt_res2
            elif 6 <= self.index < 11:
                return txt_res3
            elif 0.5 <= self.index < 6:
                return txt_res4
            elif 0.4 >= self.index > 0:
                return txt_res5
        
        if self.exp.txt_age <=14 and self.exp.txt_age >=13:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index < 16.4:
                return txt_res2
            elif 7.5 <= self.index < 12.5:
                return txt_res3
            elif 2 <= self.index < 7.5:
                return txt_res4
            elif 1.9 >= self.index > 0:
                return txt_res5

        if self.exp.txt_age <=12 and self.exp.txt_age >=11:
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index < 18:
                return txt_res2
            elif 9 <= self.index < 14:
                return txt_res3
            elif 3.5 <= self.index < 9:
                return txt_res4
            elif 3.4 >= self.index > 0:
                return txt_res5

        if self.exp.txt_age <=10 and self.exp.txt_age >=9:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index < 19.5:
                return txt_res2
            elif 10.5 <= self.index < 15.4:
                return txt_res3
            elif 5 <= self.index < 10.4:
                return txt_res4
            elif 4.9 >= self.index > 0:
                return txt_res5

        if self.exp.txt_age <=8 and self.exp.txt_age >=7:
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index < 21:
                return txt_res2
            elif 12 <= self.index < 17:
                return txt_res3
            elif 6.5 <= self.index < 12:
                return txt_res4
            elif 6.4 >= self.index > 0:
                return txt_res5

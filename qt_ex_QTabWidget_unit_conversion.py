import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # QTabWidget
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'Length')
        tabs.addTab(SecondTab(), 'Weight')
		
        # buttonbox
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        # boxLayout
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('Unit Conversion')
        #self.setGeometry(300, 200, 400, 300)
        self.setFixedSize(400, 250)
        self.show()


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_num = QLineEdit('1')    # 기본값

        # QComboBox
        self.cb = QComboBox(self)
        self.cb.addItem('mm')
        self.cb.addItem('cm')
        self.cb.addItem('m')
        self.cb.addItem('km')
        #cb.move(200, 50)
        
        # QLabel
        self.lb_num1 = QLabel('1')
        self.lb_num2 = QLabel('0.1')
        self.lb_num3 = QLabel('0.001')
        self.lb_num4 = QLabel('1e-6')

        self.lb_num1.setAlignment(Qt.AlignRight)
        self.lb_num2.setAlignment(Qt.AlignRight)
        self.lb_num3.setAlignment(Qt.AlignRight)
        self.lb_num4.setAlignment(Qt.AlignRight)

        self.lb_unit1 = QLabel('mm')
        self.lb_unit2 = QLabel('cm')
        self.lb_unit3 = QLabel('m')
        self.lb_unit4 = QLabel('km')

        # input_num, comboBox 변경 시 동작
        self.input_num.textChanged[str].connect(self.onActivated)
        self.cb.activated[str].connect(self.onActivated)

        # boxLayout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_num)
        hbox1.addWidget(self.cb)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lb_num1)
        vbox1.addWidget(self.lb_num2)
        vbox1.addWidget(self.lb_num3)
        vbox1.addWidget(self.lb_num4)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lb_unit1)
        vbox2.addWidget(self.lb_unit2)
        vbox2.addWidget(self.lb_unit3)
        vbox2.addWidget(self.lb_unit4)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)

        self.setLayout(vbox3)
    

    def onActivated(self):
        num = int(self.input_num.text())
        cText = self.cb.currentText()

        if cText == 'mm':
            self.lb_num1.setText(str(num))
            self.lb_num2.setText(str(num * 0.1))
            self.lb_num3.setText(str(num * 0.001))
            self.lb_num4.setText(str(num * 0.000001))
        elif cText == 'cm':
            self.lb_num1.setText(str(num * 10))
            self.lb_num2.setText(str(num))
            self.lb_num3.setText(str(num * 0.01))
            self.lb_num4.setText(str(num * 0.00001))
        elif cText == 'm':
            self.lb_num1.setText(str(num * 1000))
            self.lb_num2.setText(str(num * 100))
            self.lb_num3.setText(str(num))
            self.lb_num4.setText(str(num * 0.001))
        elif cText == 'km':
            self.lb_num1.setText(str(num * 1000000))
            self.lb_num2.setText(str(num * 100000))
            self.lb_num3.setText(str(num * 1000))
            self.lb_num4.setText(str(num))


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.input_num = QLineEdit('1')    # 기본값

        # QComboBox
        self.cb = QComboBox(self)
        self.cb.addItem('mg')
        self.cb.addItem('g')
        self.cb.addItem('kg')
        self.cb.addItem('t')
        #cb.move(200, 50)
        
        # QLabel
        self.lb_num1 = QLabel('1')
        self.lb_num2 = QLabel('0.001')
        self.lb_num3 = QLabel('1e-6')
        self.lb_num4 = QLabel('10e-10')

        self.lb_num1.setAlignment(Qt.AlignRight)
        self.lb_num2.setAlignment(Qt.AlignRight)
        self.lb_num3.setAlignment(Qt.AlignRight)
        self.lb_num4.setAlignment(Qt.AlignRight)

        self.lb_unit1 = QLabel('mg')
        self.lb_unit2 = QLabel('g')
        self.lb_unit3 = QLabel('kg')
        self.lb_unit4 = QLabel('t')

        # input_num, comboBox 변경 시 동작
        self.input_num.textChanged[str].connect(self.onActivated)
        self.cb.activated[str].connect(self.onActivated)

        # boxLayout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_num)
        hbox1.addWidget(self.cb)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lb_num1)
        vbox1.addWidget(self.lb_num2)
        vbox1.addWidget(self.lb_num3)
        vbox1.addWidget(self.lb_num4)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lb_unit1)
        vbox2.addWidget(self.lb_unit2)
        vbox2.addWidget(self.lb_unit3)
        vbox2.addWidget(self.lb_unit4)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)

        self.setLayout(vbox3)
    

    def onActivated(self):
        num = int(self.input_num.text())
        cText = self.cb.currentText()

        if cText == 'mg':
            self.lb_num1.setText(str(num))
            self.lb_num2.setText(str(num * 0.1))
            self.lb_num3.setText(str(num * 0.000001))
            self.lb_num4.setText(str(num * 0.0000000001))
        elif cText == 'g':
            self.lb_num1.setText(str(num * 1000))
            self.lb_num2.setText(str(num))
            self.lb_num3.setText(str(num * 0.001))
            self.lb_num4.setText(str(num * 0.000001))
        elif cText == 'kg':
            self.lb_num1.setText(str(num * 1000000))
            self.lb_num2.setText(str(num * 1000))
            self.lb_num3.setText(str(num))
            self.lb_num4.setText(str(num * 0.001))
        elif cText == 't':
            self.lb_num1.setText(str(num * 100000000))
            self.lb_num2.setText(str(num * 1000000))
            self.lb_num3.setText(str(num * 1000))
            self.lb_num4.setText(str(num))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

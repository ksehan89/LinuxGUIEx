import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget)

# TODO
class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QWidget):
    NumDigitButtons = 10

    def __init__(self, parent=None):
        # QWidget __inint__
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.waitingForOperand = True

        #QLineEdit Properties
        self.display = QLineEdit('0')		# LineEdit 추가, 초기값 0 표시.
        self.display.setReadOnly(True)		# 읽기전용
        self.display.setAlignment(Qt.AlignRight)	# LineEdit 결과값 오른쪽 정렬
        self.display.setMaxLength(15)		# 최대 15자까지 표시

        #QLineEdit font Properties
        font = self.display.font()		# display font를 가리키는 포인터 font 생성
        font.setPointSize(font.pointSize() + 8)		# 폰트사이즈는 기존+8
        self.display.setFont(font)		# 설정한 font를 display에 적용

        # create Button object
        self.digitButtons = []		# size가 정해지지 않은 배열 생성

        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i), self.digitClicked))	#str(i) : 숫자를 문자로 변경

        self.backspaceButton = self.createButton("DEL", self.backspaceClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.multipliedButton = self.createButton("x", self.additiveOperatorClicked)
        self.dividedButton = self.createButton("/", self.additiveOperatorClicked)
        self.clearButton = self.createButton("C", self.additiveOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        # Row, Col, VSize, HSize 
        mainLayout.addWidget(self.display, 0, 0, 1, 5)
        mainLayout.addWidget(self.plusButton, 2, 1, 1, 1)
        mainLayout.addWidget(self.minusButton, 2, 2, 1, 1)
        mainLayout.addWidget(self.multipliedButton, 2, 3, 1, 1)
        mainLayout.addWidget(self.dividedButton, 2, 4, 1, 1)
        mainLayout.addWidget(self.backspaceButton, 6, 3, 1, 1)
                
        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 3
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 6, 1, 1, 2)
        mainLayout.addWidget(self.clearButton, 3, 4, 2, 1)
        mainLayout.addWidget(self.equalButton, 5, 4, 2, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Calculator")

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:	# 초기값이 0 or 0.0일 경우 변경사항 없이 리턴.
            return

        if self.waitingForOperand:		# Operand : 숫자, 연산기호 입력을 기다린다.
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True

    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText('0')
        self.waitingForOperand = True

    def createButton(self, text, member):		# text : str(i), member : digitClicked 값 각각 받아옴.
        button = Button(text)
        button.clicked.connect(member)
        return button   

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == u"\N{MULTIPLICATION SIGN}":
            self.factorSoFar *= rightOperand
        elif pendingOperator == u"\N{DIVISION SIGN}":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

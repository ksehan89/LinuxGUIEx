import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QCheckBox, QPushButton, QToolButton, QSizePolicy, QFileDialog)
from PyQt5.QtCore import Qt


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


class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.setLayout(grid)

#grid.addWidget(QLabel('Title:'), 0, 0)
		# QCheckBox
		self.cb1 = QCheckBox('Resize', self)
		#cb1.toggle()
		self.cb1.stateChanged.connect(self.checkBoxState)
		grid.addWidget(self.cb1, 0, 0)

		self.cb2 = QCheckBox('rotate', self)
		self.cb2.stateChanged.connect(self.checkBoxState)
		grid.addWidget(self.cb2, 1, 0)
		
		cb3 = QCheckBox('hflip', self)
		grid.addWidget(cb3, 2, 0)

		cb4 = QCheckBox('vflip', self)
		grid.addWidget(cb4, 3, 0)
		
		cb5 = QCheckBox('rename', self)
		grid.addWidget(cb5, 4, 0)


		# QLineEdit
		self.resize_edit = QLineEdit(self)
		self.resize_edit.setDisabled(True)
		#resize_edit.set(cb1.checkBoxState()!=Qt.unchecked)
		#resize_edit.textChanged[str].connect(self.onChanged)
		grid.addWidget(self.resize_edit, 0, 1)

		self.rotate_edit = QLineEdit(self)
		self.rotate_edit.setDisabled(True)
		#rotate_edit.textChanged[str].connect(self.onChanged)
		grid.addWidget(self.rotate_edit, 1, 1)

		rename_prefix = QLineEdit(self)
		#rename_prefix.textChanged[str].connect(self.onChanged)
		grid.addWidget(rename_prefix, 5, 1)

		rename_suffix = QLineEdit(self)
		#rename_suffix.textChanged[str].connect(self.onChanged)
		grid.addWidget(rename_suffix, 5, 3)
	
		self.path = QLineEdit(self)
		#path.textChanged[str].connect(self.onChanged)
		grid.addWidget(self.path, 6, 1, 1, 2)


		# QLabel
		label1 = QLabel('prefix', self)
		label1.setAlignment(Qt.AlignCenter)
		grid.addWidget(label1, 4, 1)

		label2 = QLabel('suffix', self)
		label2.setAlignment(Qt.AlignCenter)
		grid.addWidget(label2, 4, 3)

		label3 = QLabel('number', self)
		label3.setAlignment(Qt.AlignCenter)
		grid.addWidget(label3, 5, 2)

		self.label4 = QLabel('PATH', self)
		self.label4.setAlignment(Qt.AlignCenter)
		grid.addWidget(self.label4, 6, 0)


		# QPushButton
		#btn1 = QPushButton('RUN', self)
		self.btn1 = self.createButton('RUN', self.runClicked)
		#btn1.setCheckable(True)
		grid.addWidget(self.btn1, 0, 3, 2, 1)

		self.btn2 = self.createButton('Browse...', self.browseClicked)
		grid.addWidget(self.btn2, 6, 3, 1, 1)
		#self.btn2.clicked.connect(self.browseClicked)





		self.setWindowTitle('ImageAug')
		self.setGeometry(300, 200, 450, 250)
		self.show()

	def checkBoxState(self):
		msg = ""
		if self.cb1.isChecked():
		#resize_edit.setEnabled(True)
			self.resize_edit.setDisabled(False)
		
		if self.cb2.isChecked():
			self.rotate_edit.setDisabled(False)
		
		if cb3.isChecked() == True:
			hflip
		
		if cb4.isChecked() == True:
			vflip

		if cb5.isChecked() == True:
			rename_edit
		return


	def createButton(self, text, member):
		button = Button(text)
		button.clicked.connect(member)
		return button

	def runClicked(self):
		return

	def browseClicked(self):
		fname = QFileDialog.getOpenFileName(self)
		self.path.setText(fname[0])
		return
	
	#def onChanged(self, text):
		#self.lbl.setText(text)
		#self.lbl.adjusetSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())

import sys, os 
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QCheckBox, QPushButton, QToolButton, QSizePolicy, QFileDialog)
from PyQt5.QtCore import Qt
from PIL import Image, ImageOps


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


		# QCheckBox
		self.cb1 = QCheckBox('Resize', self)
		#cb1.toggle()
		self.cb1.stateChanged.connect(self.checkBoxState)
		#grid.addWidget(QLabel('Title:'), 0, 0)
		grid.addWidget(self.cb1, 0, 0)

		self.cb2 = QCheckBox('rotate', self)
		self.cb2.stateChanged.connect(self.checkBoxState)
		grid.addWidget(self.cb2, 1, 0)
		
		self.cb3 = QCheckBox('hflip', self)
		grid.addWidget(self.cb3, 2, 0)

		self.cb4 = QCheckBox('vflip', self)
		grid.addWidget(self.cb4, 3, 0)
		
		self.cb5 = QCheckBox('rename', self)
		self.cb5.stateChanged.connect(self.checkBoxState)
		grid.addWidget(self.cb5, 4, 0)


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

		self.rename_prefix = QLineEdit(self)
		self.rename_prefix.setDisabled(True)
		#rename_prefix.textChanged[str].connect(self.onChanged)
		grid.addWidget(self.rename_prefix, 5, 1)

		self.rename_suffix = QLineEdit(self)
		self.rename_suffix.setDisabled(True)
		#rename_suffix.textChanged[str].connect(self.onChanged)
		grid.addWidget(self.rename_suffix, 5, 3)
	
		#self.path = QLineEdit('/home/ben/사진/index.jpeg')
		self.path = QLineEdit()
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
		if self.cb1.isChecked():
			self.resize_edit.setDisabled(False)
		else:
			self.resize_edit.setDisabled(True)

		if self.cb2.isChecked():
			self.rotate_edit.setDisabled(False)
		else:
			self.rotate_edit.setDisabled(True)

		#if cb3.isChecked() == True:
			#hflip

		#if cb4.isChecked() == True:
			#vflip

		if self.cb5.isChecked():
			self.rename_prefix.setDisabled(False)
			self.rename_suffix.setDisabled(False)
		else:
			self.rename_prefix.setDisabled(True)
			self.rename_suffix.setDisabled(True)
		return


	def createButton(self, text, member):
		button = Button(text)
		button.clicked.connect(member)
		return button


	def runClicked(self):
		print(self.path.text())
		self.img = Image.open(self.path.text())
		self.savePath = './ImageAgu/'
	
		fname = os.path.split(self.path.text())[1]
		#fname = os.path.split('/home/ben/사진/index.jpeg')[1]
		print(fname)

		# 이미지 사이즈 조정 및 저장
		if self.cb1.isChecked():
			resize_size = self.resize_edit.text()
			resize_arr = resize_size.split(',')
			if len(resize_arr) == 1:
				resize_arr.append(resize_arr[0])
			self.img = self.img.resize((int(resize_arr[0]), int(resize_arr[1])))
			fname = 'RS_' + fname
			self.savePath = self.savePath + 'Resize_'

		# 이미지 회전 및 저장
		if self.cb2.isChecked():
			self.img = self.img.rotate(int(self.rotate_edit.text()))
			#print(self.img)
			fname = 'RT_' + fname
			#print(fname)
			self.savePath = self.savePath + 'Rotate_'
		
		# 이미지 수평 대칭 및 저장
		if self.cb3.isChecked():
			self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
			fname = 'HFLIP_' + fname
			self.savePath = self.savePath + 'HFLIP_'

		# 이미지 수직 대칭 및 저장
		if self.cb4.isChecked():
			self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
			fname = 'VFLIP_' + fname
			self.savePath = self.savePath + 'VFLIP_'

		# 이미지 리네임
		if self.cb5.isChecked():
			image_path = self.path.text()
			image_ext = os.path.splitext(image_path)
			print(image_ext)
			
			split_name_ext = fname.rsplit('.', 1)

			fname = self.rename_prefix.text() + '_' + split_name_ext[0] + '_' + self.rename_suffix.text() + '.' + split_name_ext[1]
			self.savePath = self.savePath + 'RENAME_'
		
		# 저장할 경로에 디렉토리가 없으면 생성
		if not(os.path.isdir(self.savePath)):
			os.makedirs(os.path.join(self.savePath))
		
		self.img.save(self.savePath + '/' + fname)
		
		return


	def browseClicked(self):
		fname = QFileDialog.getOpenFileName(self)
		self.path.setText(fname[0])
		fname = self.path.text()
		return
	
	#def onChanged(self, text):
		#self.lbl.setText(text)
		#self.lbl.adjusetSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())

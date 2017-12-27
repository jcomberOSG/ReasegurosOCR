import sys
from PyQt4.QtGui import *
from process import recognizeFile
import os


class Window(QWidget):

	def handleButton(self):
		try:
			filename = str(QFileDialog.getOpenFileName(self, 'Subir archivo'))
			print filename
			otro = filename.strip(".pdf").split("/")[-1] + ".docx"
			print otro
			otro = os.getcwd() + "/" + otro
			print otro
			try:
	 			recognizeFile(filename, otro, "Spanish", "docx")	
	 			# os.rename(aux, os.getcwd() + "/" + otro)
	 		except Exception as B:
	 			print B
		except IOError: #probablemente se puso cancelar y no se subio nada
			pass

	def __init__(self):
		QWidget.__init__(self)
		self.button = QPushButton('Subir archivo', self)
		self.button.clicked.connect(self.handleButton)
		layout = QVBoxLayout(self)
		layout.addWidget(self.button)

		# nameLabel = QLabel("A label in PyQT", self)
		# nameLabel.move(100, 80)

		self.resize(320, 240)
		self.setWindowTitle("ReasegurosOCR")


	

if __name__ == '__main__':

	import sys
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())


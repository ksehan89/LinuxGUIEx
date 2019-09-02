from PyQt5.QtCore import QDate, Qt, QTime

now = QDate.currentDate()
print(now.toString(Qt.ISODate))

time = QTime.currentTime()
print(time.toString())

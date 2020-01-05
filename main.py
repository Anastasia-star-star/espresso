import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QTableWidget, QWidget, QLabel, QTableWidgetItem, QPushButton
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        con = sqlite3.connect('эспрессо.db')
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

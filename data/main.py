from PySide6 import QtGui, QtWidgets
from data.output_data import ReadeFile

CMNT_CHARACTERS = 20  # Колличесто вимволов в комментари
# Заголовки которые берем из json
list_header = ['name', 'surname', 'card_number', 'bib', 'year', 'comment']

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        tv = QtWidgets.QTableView(parent=self.window())
        sti = QtGui.QStandardItemModel(parent=self.window())

        self.data_list = ReadeFile('20241020.json')
        self.data_list.read_file()

        for i in self.data_list.data['races'][0]['persons']:
            name = QtGui.QStandardItem(str(i['name']))
            surname = QtGui.QStandardItem(str(i['surname']))
            card_number = QtGui.QStandardItem(str(i['card_number']))
            bib = QtGui.QStandardItem(str(i['bib']))
            year = QtGui.QStandardItem(str(i['year']))
            group_id = QtGui.QStandardItem(i['group_id'])
            organization_id = QtGui.QStandardItem(i['organization_id'])

            person = [
                name, surname, card_number, bib,
                year, group_id, organization_id,
            ]

            comment = list(i['comment'])
            for index in range(CMNT_CHARACTERS):
                try:
                    person.append(QtGui.QStandardItem(str(comment[index])))
                except IndexError:
                    person.append(QtGui.QStandardItem(" "))

            sti.appendRow(person)

        # Заголовки
        sti.setHorizontalHeaderLabels(
            list_header
        )
        sti.itemChanged.connect(self.cell_changed)
        tv.setModel(sti)
        tv.setColumnWidth(0, 50)
        tv.setColumnWidth(2, 180)
        for i in range(7, 28, 1):
            tv.setColumnWidth(i, 1)
        tv.resize(1200, 800)


    def cell_changed(self, item):
        self.data_list.data['races'][0]['persons'][item.row()][list_header[item.column()]] = item.text()
        self.data_list.writer_file()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("QStandardltemModel")
    window.show()
    sys.exit(app.exec())
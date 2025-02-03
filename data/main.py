from PySide6 import QtGui, QtWidgets
from data.output_data import ReadeFile

CMNT_CHARACTERS = 20  # Колличесто символов в комментари
# Заголовки которые берем из json
list_header = ['name', 'surname', 'card_number', 'bib', 'year', 'comment']

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        tab = QtWidgets.QTabWidget()
        tv = QtWidgets.QTableView()
        sti = QtGui.QStandardItemModel()
        # Вкладки
        tab.addTab(tv, "&Person")
        tab.addTab(QtWidgets.QLabel("Группы"), "&Group")
        tab.addTab(QtWidgets.QLabel("Команды"), "&Teams")
        tab.setCurrentIndex(0)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)

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
            # Разбиваю каоментарий на 20 символов, WO дает 20
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
        # Ширина заголовков
        tv.setColumnWidth(0, 60)
        tv.setColumnWidth(2, 80)
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
    window.setWindowTitle("Сбор стартового взноса")
    window.show()
    sys.exit(app.exec())
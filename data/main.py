from PySide6 import QtGui, QtWidgets
from data.output_data import ReadeFile

CMNT_CHARACTERS = 20  # Колличесто символов в комментари
# Заголовки которые берем из json
list_header = ['name', 'surname', 'card_number', 'bib', 'year', 'comment']

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.data_list = ReadeFile('20250126.json')
        self.data_list.read_file()

        tab = QtWidgets.QTabWidget()
        self.tv_person = QtWidgets.QTableView()
        self.sti_person = QtGui.QStandardItemModel()
        self.tv_group = QtWidgets.QTableView()
        self.sti_group = QtGui.QStandardItemModel()
        self.tv_teams = QtWidgets.QTableView()
        self.sti_teams = QtGui.QStandardItemModel()
        # Вкладки
        tab.addTab(self.load_person(), "&Person")
        tab.addTab(self.load_group(), "&Group")
        tab.addTab(self.load_teams(), "&Teams")


        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
        # сигнал
        self.sti_person.itemChanged.connect(self.cell_changed)

    def cell_changed(self, item):
        self.data_list.data['races'][0]['persons'][item.row()][list_header[item.column()]] = item.text()
        self.data_list.writer_file()

    def load_person(self):
        """Загрузка участников."""
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
            # Разбиваю комментарий на 20 символов, WO дает 20
            comment = list(i['comment'])
            for index in range(CMNT_CHARACTERS):
                try:
                    person.append(QtGui.QStandardItem(str(comment[index])))
                except IndexError:
                    person.append(QtGui.QStandardItem(" "))

            self.sti_person.appendRow(person)

        # Заголовки
        self.sti_person.setHorizontalHeaderLabels(
            ["Фамилия", "Имя", "Чип", "Номер", "ГР", "Группа", "Коллектив",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        )

        self.tv_person.setModel(self.sti_person)
        # Сортировка по столбцу
        self.tv_person.setSortingEnabled(True)
        # Ширина заголовков при комментарии
        st_comment = 7
        end_comment = 28
        for i in range(st_comment, end_comment):
            self.tv_person.setColumnWidth(i, 1)
        return self.tv_person

    def load_group(self):
        """Загрузка групп."""
        for i in self.data_list.data['races'][0]['groups']:
            name_group = QtGui.QStandardItem(str(i['name']))
            self.sti_group.appendRow(name_group)
        self.tv_group.setModel(self.sti_group)
        return self.tv_group

    def load_teams(self):
        """Загрузка коллективов."""
        for i in self.data_list.data['races'][0]['organizations']:
            name_teams = QtGui.QStandardItem(str(i['name']))
            self.sti_teams.appendRow(name_teams)
        self.tv_teams.setModel(self.sti_teams)
        return self.tv_teams

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Сбор стартового взноса")
    window.show()
    sys.exit(app.exec())
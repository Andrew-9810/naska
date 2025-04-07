import sys
from PySide6 import QtCore, QtGui, QtWidgets

from data.output_data import ActionFile


CMNT_CHARACTERS = 20  # Колличесто символов в комментари
# Заголовки которые берем из json
list_header = [
    'uuid', 'name', 'surname', 'card_number', 'bib', 'year', 'comment'
]

class SettingsFile:
    """Управление файлом."""
    pass

class Person:
    """Участник."""
    def __init__(self, file):
        self.file = file
        self.data_dict = file.get_person_dict()
        self.group_list = self.uuid_name_group()
        self.team_list = self.uuid_name_team()
        self.tv_person = QtWidgets.QTableView()
        self.sti_person = QtGui.QStandardItemModel()
        self.sti_person.itemChanged.connect(self.cell_changed)


    def uuid_name_group(self) ->dict:
        """Словарь групп, uuid: name."""
        group_id_name = {}
        for dict_group in self.file.get_group_list():
            key = dict_group['uuid']
            value = dict_group['name']
            group_id_name[key] = value
        return group_id_name

    def uuid_name_team(self) ->dict:
        """Словарь групп, uuid: name."""
        team_id_name = {}
        for dict_team in self.file.get_team_list():
            key = dict_team['uuid']
            value = dict_team['name']
            team_id_name[key] = value
        return team_id_name


    def load_person(self, group_filter='all', team_filter='all', start_day=1,
                    chip=True, compas=True):
        """Загрузка участников."""
        self.sti_person.clear()
        # Заголовки
        headers = [
            'id',
            'Фамилия', 'Имя', 'ГР', 'Квал',
            'Чип', 'Номер', 'Группа', 'Коллектив',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
        ]

        for i in self.data_dict:
            try:
                # Фильтрация Группа, Коллектив
                if group_filter == 'all' and team_filter == 'all':
                    group = QtGui.QStandardItem(str(self.group_list[i['group_id']]))
                    organization = QtGui.QStandardItem(
                        str(self.team_list[i['organization_id']])
                    )
                elif group_filter == 'all' and team_filter != 'all':
                    if i['organization_id'] == team_filter:
                        organization = QtGui.QStandardItem(str(
                            self.team_list[team_filter])
                        )
                    else:
                        continue
                    group = QtGui.QStandardItem(str(self.group_list[i['group_id']]))
                elif group_filter != 'all' and team_filter == 'all':
                    if i['group_id'] == group_filter:
                        group = QtGui.QStandardItem(str(
                            self.group_list[group_filter])
                        )
                    else:
                        continue
                    organization = QtGui.QStandardItem(
                        str(self.team_list[i['organization_id']])
                    )
                else:
                    if (i['group_id'] == group_filter
                        and i['organization_id'] == team_filter
                    ):
                        group = QtGui.QStandardItem(str(
                            self.group_list[group_filter])
                        )
                        organization = QtGui.QStandardItem(str(
                            self.team_list[team_filter])
                        )
                    else:
                        continue
            except KeyError:
                continue
            id_person = QtGui.QStandardItem(str(i['id']))
            name = QtGui.QStandardItem(str(i['name']))
            surname = QtGui.QStandardItem(str(i['surname']))
            card_number = QtGui.QStandardItem(str(i['card_number']))
            bib = QtGui.QStandardItem(str(i['bib']))
            year = QtGui.QStandardItem(str(i['year']))
            qual = QtGui.QStandardItem(str(i['qual']))

            person = [
                id_person, surname, name, year, qual, card_number, bib,
                 group, organization
            ]
            # Разбиваю комментарий на 20 символов, WO дает 20
            comment = list(i['comment'])
            running_day = 0
            for index in range(CMNT_CHARACTERS):
                # Выясняю сколько дней бежит участник
                if index in [3, 4, 5, 6, 7, 8]:
                    if comment[index] != '-':
                        running_day += 1
                try:
                    person.append(QtGui.QStandardItem(str(comment[index])))
                except IndexError:
                    person.append(QtGui.QStandardItem(' '))
            # Взнос
            summ: int = 0

            # Дни старта
            for _ in range(start_day):
                price_day = 222 # Должен быть запрос к таблице с группой

                summ += price_day
                person.append(QtGui.QStandardItem(str(price_day)))

                """
                Здесь цена за 1 день ориентируется на:
                льготы,
                цена коллектива
                певая цена и т.д
                """
            # Чип, Компас
            if chip:
                price_chip = 88
                summ += price_chip
                person.append(QtGui.QStandardItem(str(price_chip)))
            if compas:
                price_compas = 5
                summ += price_compas
                person.append(QtGui.QStandardItem(str(price_compas)))

            person.append(QtGui.QStandardItem(f'{summ}'))
            self.sti_person.appendRow(person)


        for day in range(start_day):
            headers.append(f'{day + 1}день')
        # Чип, Компас
        if chip:
            headers.append('ЧИП')
        if compas:
            headers.append('Компас')
        headers.append('ИТОГО')
        self.sti_person.setHorizontalHeaderLabels(headers)
        self.tv_person.setModel(self.sti_person)
        # Сортировка по столбцу
        self.tv_person.setSortingEnabled(True)

        # Ширина заголовков при комментарии
        st_comment = 9
        end_comment = 29
        for i in range(st_comment, end_comment):
            self.tv_person.setColumnWidth(i, 1)
        self.tv_person.setColumnWidth(0, 0)
        return self.tv_person

    def cell_changed(self, item):
        """Запись в файл при изменении."""
        colum_uuid = 0
        person_uuid = self.sti_person.index(item.row(), colum_uuid)

        for i in self.file.get_person_dict():
            if i['id'] == person_uuid.data():
                i[list_header[item.column()]] = item.text()
                self.file.writer_file()


class Group:
    def __init__(self, file):
        self.file = file
        self.data_list = file.get_group_dict()
        self.tv_group = QtWidgets.QTableView()
        self.sti_group = QtGui.QStandardItemModel()

    def load_group(self):
        """Загрузка групп."""
        for i in self.data_list:
            id_group = QtGui.QStandardItem(str(i['id']))
            name_group = QtGui.QStandardItem(str(i['name']))
            price_group = QtGui.QStandardItem(str(0))
            group_lst = [id_group, name_group, price_group]
            self.sti_group.appendRow(group_lst)
        self.sti_group.setHorizontalHeaderLabels(['id', 'Группа', 'Цена'])
        self.tv_group.setModel(self.sti_group)
        return self.tv_group

class Team:
    def __init__(self, file):
        self.file = file
        self.data_list = file.get_team_dict()
        self.tv_teams = QtWidgets.QTableView()
        self.sti_teams = QtGui.QStandardItemModel()

    def load_teams(self):
        """Загрузка коллективов."""
        for i in self.data_list:
            name_teams = QtGui.QStandardItem(str(i['name']))
            price_teams = QtGui.QStandardItem(str(0))
            teams_lst = [name_teams, price_teams]
            self.sti_teams.setHorizontalHeaderLabels(['Коллектив', 'Цена'])
            self.sti_teams.appendRow(teams_lst)
        self.tv_teams.setModel(self.sti_teams)
        return self.tv_teams


class MyWindow(QtWidgets.QMainWindow):
    """Элементы главного окна."""
    def __init__(self):
        super().__init__()
        self.day = 3
        self.chip = True
        self.compas = True
        self.file = ActionFile('20241020.json')
        self.file.read_file()

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        self.group_dock = QtWidgets.QDockWidget()
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.group_dock)
        self.group_dock_wid = QtWidgets.QComboBox()
        self.group_dock.setWidget(self.group_dock_wid)
        self.group_dock_wid.addItem('-----', 'all')
        for i in self.file.get_group_list():
            self.group_dock_wid.addItem(i['name'], i['uuid'])
        self.group_dock_wid.activated.connect(self.filter)

        self.team_dock = QtWidgets.QDockWidget()
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.team_dock)
        self.team_dock_wid = QtWidgets.QComboBox()
        self.team_dock.setWidget(self.team_dock_wid)
        self.team_dock_wid.addItem('-----', 'all')
        for i in self.file.get_team_list():
            self.team_dock_wid.addItem(i['name'], i['uuid'])
        self.team_dock_wid.activated.connect(self.filter)

        self.person = Person(self.file)
        self.group = Group(self.file)
        self.team = Team(self.file)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.insertTab(1, self.group.load_group(), '&Group')
        self.tabWidget.insertTab(2, self.team.load_teams(), '&Teams')
        self.tabWidget.insertTab(3, QtWidgets.QLabel('Льгота'), 'Льгота')
        self.tabWidget.setMovable(True)
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)
        self.filter()

    def filter(self):
        """Фильтрация по Коллективу и Группе."""
        team = self.team_dock_wid.currentData()
        group = self.group_dock_wid.currentData()
        self.tabWidget.removeTab(0)

        self.tabWidget.insertTab(
            0, self.person.load_person(
                team_filter=team, group_filter=group, start_day=self.day,
                chip=self.chip, compas=self.compas
            ), '&Person'
        )
        self.tabWidget.setCurrentIndex(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont('Times', 12, QtGui.QFont.Bold))
    win = MyWindow()
    win.setWindowTitle('Сбор стартового взноса')
    win.resize(800, 600)
    win.show()
    sys.exit(app.exec_())
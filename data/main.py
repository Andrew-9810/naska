import sys
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

from data.output_data import ActionFile


CMNT_CHARACTERS = 20  # Колличесто символов в комментари
# Заголовки, которые берем из json
QUAL = {
    0: 'б/р', '': 'б/р', ' ': 'б/р',
    1: 'I', 2: 'II', 3: 'III', 4: 'Iю', 5: 'IIю', 6: 'IIIю', 7: 'КМС',
    8: 'МС', 9: 'ЗМС'
}
list_header = [
    'id', 'surname', 'name', 'year', 'qual', 'card_number', 'bib',
    'group_id', 'organization_id', 'comment'
]
list_header_gr = [
    'uuid', 'name', 'price1', 'price2', 'price3'
]
FILE = ''
available = """
    QDockWidget::title {
        text-align: center;
        background-color: green;
        padding: 3px;
    }
"""
not_available = """
    QDockWidget::title {
        text-align: center;
        background-color: white;
        padding: 3px;
    }
"""
neutral = """
    QDockWidget::title {
        text-align: center;
        background-color: white;
        padding: 3px;
    }
"""


class Comment:
    """Переопределение коментария."""
    def __init__(self, comm):
        self.comment = comm

    def data(self):
        return str(self.comment)

    def column(self):
        return 9

class CommonClass:
    def __init__(self):
        self.sti = QtGui.QStandardItemModel()
        self.tv = QtWidgets.QTableView()
        self.tv.setAlternatingRowColors(True)

    def uuid_name(self, get_file) ->dict:
        """Словарь, uuid: name."""
        id_name = {}
        for data in get_file:
            key = data['uuid']
            value = data['name']
            id_name[key] = value
        return id_name

    def cell_changed(self, item, uuid, header, get_data):
        """Запись в файл при изменении."""
        for i in get_data:
            if i['id'] == uuid.data():
                i[header[item.column()]] = item.data()
                self.file.writer_file()

class Person(CommonClass):
    """Участник."""
    def __init__(self, file, file_price):
        super().__init__()
        self.file = file
        self.data_dict = file.get_person_dict()
        self.group_list = self.uuid_name(self.file.get_group_list())
        self.team_list = self.uuid_name(self.file.get_team_list())
        self.sti.itemChanged.connect(self.cell_changed_person)
        self.tv.doubleClicked.connect(self.changing_dynamic_fields)
        self.file_price = file_price

    def changing_dynamic_fields(self):
        """Изменение полей с выбором из списка."""
        # Получить позицию в листе заголовков
        if self.tv.currentIndex().column() == 4:
            parent = win.qual_dock
            win.qual_dock_wid.setEnabled(True)
            win.group_dock_wid.setEnabled(False)
            win.team_dock_wid.setEnabled(False)
        elif self.tv.currentIndex().column() == 7:
            parent = win.group_dock
            win.team_dock_wid.setEnabled(False)
        elif self.tv.currentIndex().column() == 8:
            parent = win.team_dock
            win.group_dock_wid.setEnabled(False)
        else:
            return None

        win.edit = 1
        parent.setStyleSheet(available)
        # Блокировка
        for i in range(1, 4): # Индекс вкладок
            win.tabWidget.setTabEnabled(i, False)
        win.tabWidget.setTabEnabled(0, False)



    def load_person(self, group_filter='all', team_filter='all', start_day=1,
        chip=True, compas=True):
        """Загрузка участников."""
        self.sti.clear()
        # Заголовки
        headers = [
            'id',
            'Фамилия', 'Имя', 'ГР', 'Квал',
            'Чип', 'Номер', 'Группа', 'Коллектив',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
        ]
        person_dict = {}

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

            for head in list_header[0:9]:
                if head == 'qual':
                    text = QUAL[i[head]]
                    data = str(i[head])
                elif head == 'group_id':
                    text = group
                    data = str(i[head])
                elif head == 'organization_id':
                    text = organization
                    data = str(i[head])
                else:
                    text = str(i[head])
                    data = text
                person_dict[head] = QtGui.QStandardItem(text)
                person_dict[head].setData(data)

            # Разбиваю комментарий на 20 символов, WO дает 20
            comment = list(i['comment'])
            for index in range(CMNT_CHARACTERS):
                try:
                    comm = str(comment[index])
                except IndexError:
                    comm = ' '
                person_dict[f'comment{index}'] = QtGui.QStandardItem(comm)

            # Взнос
            summ = 0
            # Цена за день относительно категории цены
            if person_dict[f'comment1'].text() == '1':
                price_cat = 'price1'
            elif person_dict[f'comment1'].text() == '2':
                price_cat = 'price2'
            elif person_dict[f'comment1'].text() == '3':
                price_cat = 'price3'
            else: # Залогируй ошибку
                price_cat = 'price3'

            price_day = int(self.file_price.data[i['group_id']][price_cat])

            step_comm_day = 2 # Шаг между значением текущего дня и индексом комментария

            for day in range(1, start_day + 1):
                if person_dict[f'comment{day + step_comm_day}'].text() != '-':
                    summ += price_day
                    data = price_day
                else:
                    data = ' '
                person_dict[f'price_day{day}'] = QtGui.QStandardItem(str(data))

                """
                Здесь цена за 1 день ориентируется на:
                льготы,
                цена коллектива
                певая цена и т.д
                """
            # Чип, Компас
            if chip:
                chip_b = 200 # Берем из файла с чипами
                chip_k = 150

                if person_dict[f'comment9'].text() != ' ':
                    day_chip = int(person_dict[f'comment9'].text())
                    if person_dict['card_number'].text()[:1] == '8':
                        price_chip = chip_b
                    else:
                        price_chip = chip_k
                    summ_chip = day_chip * price_chip
                    summ += summ_chip
                else:
                    summ_chip = ' '
                person_dict['chip'] = QtGui.QStandardItem(str(summ_chip))
            if compas:
                price_compas = 5
                if person_dict[f'comment10'].text() != ' ':
                    day_compas = int(person_dict[f'comment10'].text())
                    summ_compas = day_compas * price_compas
                    summ += summ_compas
                else:
                    summ_compas = ' '
                person_dict['compas'] = QtGui.QStandardItem(str(summ_compas))
            person_dict['summ'] = QtGui.QStandardItem(f'{summ}')

            person = []
            for head in list_header[0:9]:
                person.append(person_dict[head])
            # Поля комментария
            for index in range(CMNT_CHARACTERS):
                person.append(person_dict[f'comment{index}'])
            # Поля чипов и компасов
            if chip:
                person.append(person_dict['chip'])
            if compas:
                person.append(person_dict['compas'])
            for day in range(1, start_day+1):
                person.append(person_dict[f'price_day{day}'])
            person.append(person_dict['summ'])
            self.sti.appendRow(person)

        # Заголовки Чип, Компас
        if chip:
            headers.append('ЧИП')
        if compas:
            headers.append('Компас')
        for day in range(start_day):
            headers.append(f'{day + 1}день')
        headers.append('ИТОГО')
        self.sti.setHorizontalHeaderLabels(headers)
        self.tv.setModel(self.sti)
        # Сортировка по столбцу
        self.tv.setSortingEnabled(True)

        # Ширина заголовков при комментарии
        st_comment = 9
        end_comment = 29
        for i in range(st_comment, end_comment):
            self.tv.setColumnWidth(i, 1)
        # Колонка с uuid скрыта
        self.tv.setColumnWidth(0, 0)
        return self.tv

    def cell_changed_person(self, item):
        colum_uuid = 0
        uuid = self.sti.index(item.row(), colum_uuid)
        header = list_header
        get_data = self.file.get_person_dict()
        if item.column() == 4: # Изменение Квалификации
            item.setText(str(win.qual_dock_wid.currentText()))
            item.setData(win.qual_dock_wid.currentData())
        if item.column() == 7: # Изменение Группы
            item.setText(str(win.group_dock_wid.currentText()))
            item.setData(str(win.group_dock_wid.currentData()))
        if item.column() == 8:  # Изменение Коллектива
            item.setText(str(win.team_dock_wid.currentText()))
            item.setData(str(win.team_dock_wid.currentData()))
        if item.column() in range(9,29): # Комментарий
            # собрать строку и записать
            comment = ''
            for pos_com in range(9, 29):
                comment += self.sti.index(item.row(), pos_com).data()
            # Переопределяю для записи
            item = Comment(comment)
        CommonClass.cell_changed(self, item, uuid, header, get_data)

class Group(CommonClass):
    def __init__(self, file, file_price):
        super().__init__()
        self.file = file
        self.data_list = file.get_group_dict()
        self.file_price = file_price

        self.group_dict = {}
        self.sti.itemChanged.connect(self.cell_changed_group)

    def load_group(self):
        """Загрузка групп."""
        for i in self.data_list:
            id_group = QtGui.QStandardItem(str(i['id']))
            id_group.setData(str(i['id']))
            name_group = QtGui.QStandardItem(str(i['name']))
            name_group.setData(str(i['name']))

            if self.file_price.check_is_nan():
                self.group_dict[str(i['id'])] = {
                    'name': str(i['name']),
                    'price1': str(0),
                    'price2': str(0),
                    'price3': str(0),
                }
                price_group1 = QtGui.QStandardItem(str(0))
                price_group2 = QtGui.QStandardItem(str(0))
                price_group3 = QtGui.QStandardItem(str(0))
            else:
                p1 = self.file_price.data[str(i['id'])]['price1']
                p2 = self.file_price.data[str(i['id'])]['price2']
                p3 = self.file_price.data[str(i['id'])]['price3']
                price_group1 = QtGui.QStandardItem(p1)
                price_group2 = QtGui.QStandardItem(p2)
                price_group3 = QtGui.QStandardItem(p3)
            group_lst = [
                id_group, name_group, price_group1, price_group2, price_group3
            ]
            self.sti.appendRow(group_lst)

        if self.file_price.check_is_nan():
            self.file_price.data = self.group_dict
            self.file_price.writer_file()

        self.sti.setHorizontalHeaderLabels(
            ['id', 'Группа', 'Цена1', 'Цена2', 'Цена3']
        )
        self.tv.setModel(self.sti)
        return self.tv

    def cell_changed_group(self, item):
        """Запись в файл при изменении."""
        colum_uuid = 0
        uuid = self.sti.index(item.row(), colum_uuid)
        header = list_header_gr
        get_data = self.file.get_group_dict()
        if item.column() == 1:
            item.setData(item.text())
            CommonClass.cell_changed(self, item, uuid, header, get_data)
        elif item.column() in [2, 3, 4]:
            self.file_price.data[uuid.data()][header[item.column()]] = item.text()
            self.file_price.writer_file()


class Team(CommonClass):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.data_list = file.get_team_dict()


    def load_teams(self):
        """Загрузка коллективов."""
        for i in self.data_list:
            name_teams = QtGui.QStandardItem(str(i['name']))
            price_teams = QtGui.QStandardItem(str(0))
            teams_lst = [name_teams, price_teams]
            self.sti.setHorizontalHeaderLabels(['Коллектив', 'Цена'])
            self.sti.appendRow(teams_lst)
        self.tv.setModel(self.sti)
        return self.tv


class Settings(CommonClass):
    def __init__(self, file_sett):
        super().__init__()
        self.file_sett = file_sett
        self.sett = {}

    def load(self):
        """Загрузка льгот."""
        if self.file_sett.check_is_nan():
            self.sett['position'] = {
                'symbol': {'description': 'bla', 'price': 123}
            }
            description = QtGui.QStandardItem(str(0))
            symbol = QtGui.QStandardItem(str(0))
            position = QtGui.QStandardItem(str(0))
            price = QtGui.QStandardItem(str(0))
        else: # Считать из файла
            description = QtGui.QStandardItem(str(0))
            symbol = QtGui.QStandardItem(str(0))
            position = QtGui.QStandardItem(str(0))
            price = QtGui.QStandardItem(str(0))
        lst = [
            description, symbol, position, price
        ]
        self.sti.appendRow(lst)

        if self.file_sett.check_is_nan():
            self.file_sett.data = self.sett
            self.file_sett.writer_file()

        self.sti.setHorizontalHeaderLabels(
            ['Описание', 'Символ', 'Позиция', 'Цена']
        )
        self.tv.setModel(self.sti)
        return self.tv


class MyWindow(QtWidgets.QMainWindow):
    """Элементы главного окна."""
    def __init__(self):
        super().__init__()

        self.day = 3
        self.chip = False
        self.compas = False

        self.file = ActionFile(f'{FILE}')
        self.file.read_file()

        self.file_price = ActionFile(
            f'{Path(FILE).name.split('.')[0]}price.json'
        )
        self.file_price.read_file()

        self.file_sett = ActionFile(
            f'{Path(FILE).name.split('.')[0]}sett.json'
        )
        self.file_sett.read_file()

        self.edit = 0  # 0 - не редактирование, 1 - редактирование

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        self.group_dock = QtWidgets.QDockWidget()
        self.group_dock.setWindowTitle('Группа')
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.group_dock)
        self.group_dock_wid = QtWidgets.QComboBox()
        self.group_dock.setWidget(self.group_dock_wid)
        self.group_dock_wid.addItem('-----', 'all')
        for i in self.file.get_group_list():
            self.group_dock_wid.addItem(i['name'], i['uuid'])
        self.group_dock_wid.activated.connect(self.filter)

        self.team_dock = QtWidgets.QDockWidget()
        self.team_dock.setWindowTitle('Коллектив')
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.team_dock)
        self.team_dock_wid = QtWidgets.QComboBox()
        self.team_dock.setWidget(self.team_dock_wid)
        self.team_dock_wid.addItem('-----', 'all')
        for i in self.file.get_team_list():
            self.team_dock_wid.addItem(i['name'], i['uuid'])
        self.team_dock_wid.activated.connect(self.filter)

        self.qual_dock = QtWidgets.QDockWidget()
        self.qual_dock.setWindowTitle('Квалл.')
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.qual_dock)
        self.qual_dock_wid = QtWidgets.QComboBox()
        self.qual_dock.setWidget(self.qual_dock_wid)

        for key in QUAL:
            if isinstance(key, int):
                self.qual_dock_wid.addItem(QUAL[key], key)
        self.qual_dock_wid.setEnabled(False)
        self.qual_dock_wid.activated.connect(self.filter)

        self.person = Person(self.file, self.file_price)
        self.group = Group(self.file, self.file_price)
        self.team = Team(self.file)
        self.settings = Settings(self.file_sett)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.insertTab(0, QtWidgets.QWidget(), '&Person')
        self.tabWidget.insertTab(1, self.group.load_group(), '&Group')
        self.tabWidget.insertTab(2, self.team.load_teams(), '&Teams')
        self.tabWidget.insertTab(3, self.settings.load(), '&Settings')
        self.tabWidget.setMovable(True)
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)
        self.filter()

    def filter(self):
        """Фильтрация по Коллективу и Группе."""
        team = self.team_dock_wid.currentData()
        group = self.group_dock_wid.currentData()
        if self.edit == 0:
            self.tabWidget.removeTab(0)

            self.tabWidget.insertTab(
                0, self.person.load_person(
                    team_filter=team, group_filter=group, start_day=self.day,
                    chip=self.chip, compas=self.compas
                ), '&Person'
            )
            self.tabWidget.setCurrentIndex(0)
        elif self.edit == 1:
            # Текущий элемент который меняется
            self.person.cell_changed_person(
                self.person.sti.itemFromIndex(self.person.tv.currentIndex())
            )
            self.edit = 0
            self.group_dock.setStyleSheet(neutral)
            self.team_dock.setStyleSheet(neutral)
            self.qual_dock.setStyleSheet(neutral)
            # Разблокировка
            for i in range(0,4):
                self.tabWidget.setTabEnabled(i, True)
            self.qual_dock_wid.setEnabled(False)
            self.group_dock_wid.setEnabled(True)
            self.team_dock_wid.setEnabled(True)
        else:
            pass

class PriceGroup(QtWidgets.QMainWindow):
    """Получение цены группы."""
    def __init__(self):
        super().__init__()
        fname = QtWidgets.QDialog()
        self.file = ActionFile(f'{FILE}')
        self.file.read_file()

        self.group = Group(self.file)

        self.tabWidget = QtWidgets.QTabWidget()

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        self.tabWidget.insertTab(1, self.group.load_group(), '&Group')
        self.tabWidget.insertTab(3, QtWidgets.QLabel('Льгота'), 'Льгота')
        self.tabWidget.setMovable(True)
        self.btx = QtWidgets.QPushButton("OK")
        self.btx.clicked.connect(self.run)

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)
        self.layout.addWidget(self.btx)

    def run(self):
        self.close()



class SelectFile(QtWidgets.QMainWindow):
    """Выбор файла с базой."""
    def __init__(self):
        super().__init__()
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open File",
            f"{Path().cwd()}",
            "All Files (*)",
        )
        global FILE
        FILE = fname[0]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont('Times', 12, QtGui.QFont.Bold))
    dialog = SelectFile()
    dialog.show()
    dialog.close()
    # group = PriceGroup()
    # group.show()

    win = MyWindow()
    win.setWindowTitle('Сбор стартового взноса')
    win.resize(1000, 800)
    win.show()
    sys.exit(app.exec_())
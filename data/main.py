from PySide6 import QtGui, QtWidgets
from data.output_data import ReadeFile

list_header = ['name', 'surname', 'card_number', 'bib', 'year', 'comment']

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        tv = QtWidgets.QTableView(parent=self.window())
        sti = QtGui.QStandardItemModel(parent=self.window())

        lst0 = []
        lst1 = []
        lst2 = []
        lst3 = []
        lst4 = []
        lst5 = []
        lst6 = []
        lst7 = []

        self.data_list = ReadeFile('20241020.json')
        self.data_list.read_file()
        # Считывает все столбцы
        for i in self.data_list.data['races'][0]['persons']:
            lst0.append(i['name'])
            lst1.append(i['surname'])
            lst2.append(str(i['card_number']))
            lst3.append(str(i['bib']))
            lst4.append(str(i['year']))
            lst5.append(i['group_id'])
            lst6.append(i['organization_id'])
            lst7.append(i['comment'])

        # row считывает строку
        for row in range(0, len(lst0)):
            item0 = QtGui.QStandardItem(lst0[row])
            item1 = QtGui.QStandardItem(lst1[row])
            item2 = QtGui.QStandardItem(lst2[row])
            item3 = QtGui.QStandardItem(lst3[row])
            item4 = QtGui.QStandardItem(lst4[row])
            item5 = QtGui.QStandardItem(lst5[row])
            item6 = QtGui.QStandardItem(lst6[row])
            list_comment = []
            for i in lst7[row]:
                 list_comment.append(i)
            try:
                item20 = QtGui.QStandardItem(list_comment[0])
                item21 = QtGui.QStandardItem(list_comment[1])
                item22 = QtGui.QStandardItem(list_comment[2])
                item23 = QtGui.QStandardItem(list_comment[3])
                item24 = QtGui.QStandardItem(list_comment[4])
                item25 = QtGui.QStandardItem(list_comment[5])
                item26 = QtGui.QStandardItem(list_comment[6])
                item27 = QtGui.QStandardItem(list_comment[7])
                item28 = QtGui.QStandardItem(list_comment[8])
                item29 = QtGui.QStandardItem(list_comment[9])
                item30 = QtGui.QStandardItem(list_comment[10])
                item31 = QtGui.QStandardItem(list_comment[11])
                item32 = QtGui.QStandardItem(list_comment[12])
                item33 = QtGui.QStandardItem(list_comment[13])
                item34 = QtGui.QStandardItem(list_comment[14])
                item35 = QtGui.QStandardItem(list_comment[15])
                item36 = QtGui.QStandardItem(list_comment[16])
                item37 = QtGui.QStandardItem(list_comment[17])
                item38 = QtGui.QStandardItem(list_comment[18])
                item39 = QtGui.QStandardItem(list_comment[19])
            except Exception:
                pass
            sti.appendRow(
                [item0, item1, item2, item3, item4, item5, item6]
            )
        # Заголовки
        sti.setHorizontalHeaderLabels(
            list_header
        )
        sti.itemChanged.connect(self.cell_changed)
        tv.setModel(sti)
        tv.setColumnWidth(0, 50)
        tv.setColumnWidth(2, 180)
        tv.resize(700, 600)


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
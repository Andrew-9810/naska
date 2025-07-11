# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QGridLayout, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 654)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_hid_comment = QCheckBox(self.tab_1)
        self.btn_hid_comment.setObjectName(u"btn_hid_comment")

        self.gridLayout_2.addWidget(self.btn_hid_comment, 0, 0, 1, 1)

        self.tView_prers = QTableView(self.tab_1)
        self.tView_prers.setObjectName(u"tView_prers")

        self.gridLayout_2.addWidget(self.tView_prers, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tView_group = QTableView(self.tab_2)
        self.tView_group.setObjectName(u"tView_group")

        self.gridLayout_3.addWidget(self.tView_group, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tView_team = QTableView(self.tab_3)
        self.tView_team.setObjectName(u"tView_team")

        self.gridLayout_4.addWidget(self.tView_team, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tView_sett = QTableView(self.tab_4)
        self.tView_sett.setObjectName(u"tView_sett")

        self.gridLayout_5.addWidget(self.tView_sett, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1014, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.group_dock = QDockWidget(MainWindow)
        self.group_dock.setObjectName(u"group_dock")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.group_dock.sizePolicy().hasHeightForWidth())
        self.group_dock.setSizePolicy(sizePolicy1)
        self.group_dock.setMinimumSize(QSize(86, 63))
        self.group_dock.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.group_widget = QWidget()
        self.group_widget.setObjectName(u"group_widget")
        self.group_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.gridLayout_6 = QGridLayout(self.group_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.group_dock_wid = QComboBox(self.group_widget)
        self.group_dock_wid.setObjectName(u"group_dock_wid")
        sizePolicy1.setHeightForWidth(self.group_dock_wid.sizePolicy().hasHeightForWidth())
        self.group_dock_wid.setSizePolicy(sizePolicy1)
        self.group_dock_wid.setMinimumSize(QSize(0, 0))
        self.group_dock_wid.setMaximumSize(QSize(524287, 524287))
        self.group_dock_wid.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout_6.addWidget(self.group_dock_wid, 0, 0, 1, 1)

        self.group_dock.setWidget(self.group_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.group_dock)
        self.team_dock = QDockWidget(MainWindow)
        self.team_dock.setObjectName(u"team_dock")
        sizePolicy1.setHeightForWidth(self.team_dock.sizePolicy().hasHeightForWidth())
        self.team_dock.setSizePolicy(sizePolicy1)
        self.team_widget = QWidget()
        self.team_widget.setObjectName(u"team_widget")
        self.gridLayout_7 = QGridLayout(self.team_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.team_dock_wid = QComboBox(self.team_widget)
        self.team_dock_wid.setObjectName(u"team_dock_wid")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.team_dock_wid.sizePolicy().hasHeightForWidth())
        self.team_dock_wid.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.team_dock_wid, 0, 0, 1, 1)

        self.team_dock.setWidget(self.team_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.team_dock)
        self.qual_dock = QDockWidget(MainWindow)
        self.qual_dock.setObjectName(u"qual_dock")
        sizePolicy1.setHeightForWidth(self.qual_dock.sizePolicy().hasHeightForWidth())
        self.qual_dock.setSizePolicy(sizePolicy1)
        self.qual_widget = QWidget()
        self.qual_widget.setObjectName(u"qual_widget")
        self.gridLayout_8 = QGridLayout(self.qual_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.qual_dock_wid = QComboBox(self.qual_widget)
        self.qual_dock_wid.setObjectName(u"qual_dock_wid")
        sizePolicy2.setHeightForWidth(self.qual_dock_wid.sizePolicy().hasHeightForWidth())
        self.qual_dock_wid.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.qual_dock_wid, 0, 0, 1, 1)

        self.qual_dock.setWidget(self.qual_widget)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.qual_dock)
        self.group_dock.raise_()
        QWidget.setTabOrder(self.qual_dock_wid, self.team_dock_wid)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u0438\u0441\u043a\u0430", None))
        self.btn_hid_comment.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c \u043a\u043e\u043c\u0435\u043d\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Person", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Group", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Teams", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.group_dock.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.group_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
#if QT_CONFIG(whatsthis)
        self.group_widget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.team_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0435\u043a\u0442\u0438\u0432", None))
        self.qual_dock.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0432\u0430\u043b\u043b.", None))
    # retranslateUi


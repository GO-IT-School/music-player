# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QtCore.QSize(600, 450))
        MainWindow.setMaximumSize(QtCore.QSize(600, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton {\n"
"background-color: rgb(33, 36, 35); \n"
"border: none;\n"
"}\n"
"QPushButton:pressad {\n"
"background-color: rgb(62, 56, 56); \n"
"border: none;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 600, 450))
        self.main_frame.setStyleSheet("background-color: #3E3838")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.main_frame.setMidLineWidth(0)
        self.main_frame.setObjectName("main_frame")
        self.frame1 = QtWidgets.QFrame(self.main_frame)
        self.frame1.setEnabled(True)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 600, 40))
        self.frame1.setStyleSheet("background-color: #212423")
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setLineWidth(0)
        self.frame1.setObjectName("frame1")
        self.music_button = QtWidgets.QPushButton(self.frame1)
        self.music_button.setGeometry(QtCore.QRect(5, 5, 100, 30))
        self.music_button.setAutoFillBackground(False)
        self.music_button.setStyleSheet("QPyshButton {\n"
"background-color: rgb(33, 36, 35);\n"
"border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(62, 56, 56);\n"
"border: none;\n"
"}")
        self.music_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../.designer/backup/image/active_button_musics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_button.setIcon(icon1)
        self.music_button.setIconSize(QtCore.QSize(100, 30))
        self.music_button.setCheckable(False)
        self.music_button.setAutoRepeat(False)
        self.music_button.setObjectName("music_button")
        self.playlist_button = QtWidgets.QPushButton(self.frame1)
        self.playlist_button.setGeometry(QtCore.QRect(110, 5, 100, 30))
        self.playlist_button.setAutoFillBackground(False)
        self.playlist_button.setStyleSheet("QPyshButton {\n"
"background-color: rgb(33, 36, 35);\n"
"border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(62, 56, 56);\n"
"border: none;\n"
"}")
        self.playlist_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../.designer/backup/image/deactive_button_playlists.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playlist_button.setIcon(icon2)
        self.playlist_button.setIconSize(QtCore.QSize(100, 30))
        self.playlist_button.setCheckable(False)
        self.playlist_button.setAutoRepeat(False)
        self.playlist_button.setObjectName("playlist_button")
        self.frame2 = QtWidgets.QFrame(self.main_frame)
        self.frame2.setGeometry(QtCore.QRect(0, 42, 600, 408))
        self.frame2.setStyleSheet("background-color: #212423")
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setLineWidth(0)
        self.frame2.setObjectName("frame2")
        self.active_music = QtWidgets.QFrame(self.frame2)
        self.active_music.setGeometry(QtCore.QRect(300, 2, 297, 404))
        self.active_music.setStyleSheet("background-color: #3E3838;\n"
"border-color: #3E3838;\n"
"border-radius: 10px;")
        self.active_music.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.active_music.setFrameShadow(QtWidgets.QFrame.Plain)
        self.active_music.setLineWidth(0)
        self.active_music.setMidLineWidth(0)
        self.active_music.setObjectName("active_music")
        self.image_frame = QtWidgets.QFrame(self.active_music)
        self.image_frame.setGeometry(QtCore.QRect(4, 4, 292, 242))
        self.image_frame.setStyleSheet("")
        self.image_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setLineWidth(0)
        self.image_frame.setObjectName("image_frame")
        self.label = QtWidgets.QLabel(self.image_frame)
        self.label.setGeometry(QtCore.QRect(46, 21, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../.designer/backup/image/vanyl.png"))
        self.label.setObjectName("label")
        self.button_frame = QtWidgets.QFrame(self.active_music)
        self.button_frame.setGeometry(QtCore.QRect(4, 250, 293, 150))
        self.button_frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_frame.setStyleSheet("background-color: rgb(62, 56, 56);")
        self.button_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setLineWidth(0)
        self.button_frame.setObjectName("button_frame")
        self.music_frame = QtWidgets.QFrame(self.frame2)
        self.music_frame.setGeometry(QtCore.QRect(2, 2, 297, 404))
        self.music_frame.setStyleSheet("background-color: #212423")
        self.music_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.music_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_frame.setLineWidth(0)
        self.music_frame.setObjectName("music_frame")
        self.music_scroll = QtWidgets.QScrollArea(self.music_frame)
        self.music_scroll.setGeometry(QtCore.QRect(0, 0, 297, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_scroll.sizePolicy().hasHeightForWidth())
        self.music_scroll.setSizePolicy(sizePolicy)
        self.music_scroll.setFrameShape(QtWidgets.QFrame.Box)
        self.music_scroll.setLineWidth(0)
        self.music_scroll.setWidgetResizable(True)
        self.music_scroll.setObjectName("music_scroll")
        self.music_widget = QtWidgets.QWidget()
        self.music_widget.setGeometry(QtCore.QRect(0, 0, 297, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_widget.sizePolicy().hasHeightForWidth())
        self.music_widget.setSizePolicy(sizePolicy)
        self.music_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.music_widget.setSizeIncrement(QtCore.QSize(297, 40))
        self.music_widget.setBaseSize(QtCore.QSize(297, 40))
        self.music_widget.setObjectName("music_widget")
        self.music_frame_layout = QtWidgets.QVBoxLayout(self.music_widget)
        self.music_frame_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.music_frame_layout.setContentsMargins(7, 2, 6, 6)
        self.music_frame_layout.setSpacing(6)
        self.music_frame_layout.setObjectName("music_frame_layout")
        self.music_scroll.setWidget(self.music_widget)
        self.playlist_frame = QtWidgets.QFrame(self.frame2)
        self.playlist_frame.setEnabled(True)
        self.playlist_frame.setGeometry(QtCore.QRect(2, 2, 297, 404))
        self.playlist_frame.setStyleSheet("background-color: #212423")
        self.playlist_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.playlist_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playlist_frame.setLineWidth(0)
        self.playlist_frame.setObjectName("playlist_frame")
        self.playlist_scroll = QtWidgets.QScrollArea(self.playlist_frame)
        self.playlist_scroll.setGeometry(QtCore.QRect(0, 0, 297, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlist_scroll.sizePolicy().hasHeightForWidth())
        self.playlist_scroll.setSizePolicy(sizePolicy)
        self.playlist_scroll.setFrameShape(QtWidgets.QFrame.Box)
        self.playlist_scroll.setLineWidth(0)
        self.playlist_scroll.setWidgetResizable(True)
        self.playlist_scroll.setObjectName("playlist_scroll")
        self.playlist_widget = QtWidgets.QWidget()
        self.playlist_widget.setGeometry(QtCore.QRect(0, 0, 297, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlist_widget.sizePolicy().hasHeightForWidth())
        self.playlist_widget.setSizePolicy(sizePolicy)
        self.playlist_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.playlist_widget.setSizeIncrement(QtCore.QSize(297, 40))
        self.playlist_widget.setBaseSize(QtCore.QSize(297, 40))
        self.playlist_widget.setObjectName("playlist_widget")
        self.playlist_frame_layout = QtWidgets.QVBoxLayout(self.playlist_widget)
        self.playlist_frame_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.playlist_frame_layout.setContentsMargins(7, 2, 6, 6)
        self.playlist_frame_layout.setSpacing(6)
        self.playlist_frame_layout.setObjectName("playlist_frame_layout")
        self.playlist_scroll.setWidget(self.playlist_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Плеєр"))

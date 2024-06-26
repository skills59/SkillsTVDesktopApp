# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc

class Ui_dashboardWindow(object):
    def setupUi(self, dashboardWindow):
        dashboardWindow.setObjectName("dashboardWindow")
        dashboardWindow.resize(1300, 700)

        #importantfortheframetransparency
        dashboardWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dashboardWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(dashboardWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QtCore.QSize(44, 44))
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11 { \n"
"border-image: url(:/assets/images/assets/images/PQEJ0959.JPG);\n"
"border-radius: 22px;\n"
"height: 44px;\n"
"width: 44px;\n"
"}\n"
"\n"
"QPushButton#pushButton_11:hover {\n"
" background-color: rgb(200, 200, 200);\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.frame_4 = QtWidgets.QFrame(self.widget_2)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(753, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton#pushButton_14 { \n"
"border-radius: 22px;\n"
"height: 44px;\n"
" \n"
"background-color: rgb(29, 29, 29);\n"
"width: 44px;\n"
"}\n"
"\n"
"QPushButton#pushButton_14:hover {\n"
"background-color: rgb(3, 98, 74);\n"
"}")
        self.pushButton_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_14.setAutoExclusive(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton#pushButton_16 { \n"
"border-radius: 22px;\n"
"height: 44px;\n"
" \n"
"background-color: rgb(29, 29, 29);\n"
"width: 44px;\n"
"}\n"
"\n"
"QPushButton#pushButton_16:hover {\n"
"background-color: rgb(3, 98, 74);\n"
"}")
        self.pushButton_16.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_16.setAutoExclusive(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton#pushButton_10 { \n"
"border-radius: 22px;\n"
"height: 44px;\n"
" \n"
"background-color: rgb(29, 29, 29);\n"
"width: 44px;\n"
"}\n"
"\n"
"QPushButton#pushButton_10:hover {\n"
"background-color: rgb(3, 98, 74);\n"
"}")
        self.pushButton_10.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton#pushButton_15 { \n"
"border-radius: 22px;\n"
"height: 44px;\n"
" \n"
"background-color: rgb(29, 29, 29);\n"
"width: 44px;\n"
"}\n"
"\n"
"QPushButton#pushButton_15:hover {\n"
"background-color: rgb(3, 98, 74);\n"
"}")
        self.pushButton_15.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_15.setAutoExclusive(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_3.setStyleSheet("border-top: 60px;\n"
"background-color: rgb(47, 47, 47);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logo = QtWidgets.QLabel(self.widget_3)
        self.logo.setStyleSheet("")
        self.logo.setObjectName("logo")
        self.horizontalLayout_5.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(888, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("")
        self.pushButton_18.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/minus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon4)
        self.pushButton_18.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("")
        self.pushButton_19.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("")
        self.pushButton_17.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/assets/icons/assets/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.LContainer = QtWidgets.QWidget(self.centralwidget)
        self.LContainer.setObjectName("LContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LContainer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.LContainer)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.LiveTv = QtWidgets.QWidget()
        self.LiveTv.setObjectName("LiveTv")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.LiveTv)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_7 = QtWidgets.QWidget(self.LiveTv)
        self.widget_7.setStyleSheet("border-image: url(:/assets/images/assets/images/box.jpg);")
        self.widget_7.setObjectName("widget_7")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.widget_7)
        self.stackedWidget.addWidget(self.LiveTv)
        self.Movies = QtWidgets.QWidget()
        self.Movies.setObjectName("Movies")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Movies)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_6 = QtWidgets.QWidget(self.Movies)
        self.widget_6.setStyleSheet("border-image: url(:/assets/images/assets/images/box.jpg);")
        self.widget_6.setObjectName("widget_6")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.widget_6)
        self.stackedWidget.addWidget(self.Movies)
        self.Series = QtWidgets.QWidget()
        self.Series.setObjectName("Series")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Series)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_5 = QtWidgets.QWidget(self.Series)
        self.widget_5.setStyleSheet("border-image: url(:/assets/images/assets/images/box.jpg);")
        self.widget_5.setObjectName("widget_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.Series)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.LContainer, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LiveTv_Button = QtWidgets.QPushButton(self.widget)
        self.LiveTv_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LiveTv_Button.setStyleSheet("QPushButton#LiveTv_Button { \n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    font: 20pt \"Bauhaus 93\";\n"
"border-radius: 22px;\n"
"\n"
"}\n"
"\n"
"QPushButton#LiveTv_Button:hover {\n"
"color: rgb(3, 98, 74);\n"
"}")
        self.LiveTv_Button.setAutoExclusive(True)
        self.LiveTv_Button.setObjectName("LiveTv_Button")
        self.horizontalLayout.addWidget(self.LiveTv_Button)
        self.Movies_Button = QtWidgets.QPushButton(self.widget)
        self.Movies_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Movies_Button.setStyleSheet("\n"
"QPushButton#Movies_Button { \n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    font: 20pt \"Bauhaus 93\";\n"
"border-radius: 22px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Movies_Button:hover {\n"
"color: rgb(3, 98, 74);\n"
"}")
        self.Movies_Button.setAutoExclusive(True)
        self.Movies_Button.setObjectName("Movies_Button")
        self.horizontalLayout.addWidget(self.Movies_Button)
        self.Series_Button = QtWidgets.QPushButton(self.widget)
        self.Series_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Series_Button.setStyleSheet("\n"
"QPushButton#Series_Button { \n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    font: 20pt \"Bauhaus 93\";\n"
"border-radius: 22px;\n"
"\n"
"}\n"
"\n"
"QPushButton#Series_Button:hover {\n"
"color: rgb(3, 98, 74);\n"
"}\n"
"")
        self.Series_Button.setAutoExclusive(True)
        self.Series_Button.setObjectName("Series_Button")
        self.horizontalLayout.addWidget(self.Series_Button)
        self.gridLayout.addWidget(self.widget, 3, 1, 1, 1)
        dashboardWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboardWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dashboardWindow)

    def retranslateUi(self, dashboardWindow):
        _translate = QtCore.QCoreApplication.translate
        dashboardWindow.setWindowTitle(_translate("dashboardWindow", "MainWindow"))
        self.pushButton_11.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.label.setText(_translate("dashboardWindow", "Welcome,Olatunde"))
        self.label_5.setText(_translate("dashboardWindow", "11 Feb, 2024 4:00PM"))
        self.pushButton_14.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.pushButton_16.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.pushButton_10.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.pushButton_15.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.logo.setText(_translate("dashboardWindow", "<html><head/><body><p><span style=\" color:#4caf50;\">🆂🅺🅸🅻🅻🆂🆃🆅</span></p></body></html>"))
        self.pushButton_18.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.pushButton_19.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.pushButton_17.setToolTip(_translate("dashboardWindow", "Notifications"))
        self.label_2.setText(_translate("dashboardWindow", "Live Television Channels"))
        self.label_3.setText(_translate("dashboardWindow", "Latest Movies"))
        self.label_4.setText(_translate("dashboardWindow", "Latest Television Series"))
        self.LiveTv_Button.setText(_translate("dashboardWindow", "LiveTv"))
        self.Movies_Button.setText(_translate("dashboardWindow", "Movies"))
        self.Series_Button.setText(_translate("dashboardWindow", "Series"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboardWindow = QtWidgets.QMainWindow()
    ui = Ui_dashboardWindow()
    ui.setupUi(dashboardWindow)
    dashboardWindow.show()
    sys.exit(app.exec_())

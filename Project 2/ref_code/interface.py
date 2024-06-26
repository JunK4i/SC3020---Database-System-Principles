from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem
import pyqtgraph as pg

colorGradient = ["#DDF4F6", "#BCF1F5", "#99EDF3", "#77ECF5", "#47E4F0", "#0CD4E3", "#06C0CE", "#04A6B2", "#01818A",
                  "#005E65", "#004146"]

#Login class, which is used upon entry into the app.
class Login(object):
    def __init__(self, login_details):
        self.login_details = login_details

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(398, 289)
        login.setStyleSheet("QWidget {\n"
                            "background-color: \"#ffffff\"\n"
                            "}")

        #Login Button
        self.loginButton = QtWidgets.QPushButton(login)
        self.loginButton.setGeometry(QtCore.QRect(120, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: \"#004146\";\n"
                                  "color: white;\n"
                                  "border-style: outset;\n"
                                  "border-radius: 10px;\n"
                                  "font: 14px")
        self.loginButton.setObjectName("loginButton")

        #Input Field for Host
        self.hostInput = QtWidgets.QLineEdit(login)
        self.hostInput.setGeometry(QtCore.QRect(40, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hostInput.setFont(font)
        self.hostInput.setStyleSheet("color: \"#018076\";\n"
                                      "font: 12px")
        self.hostInput.setObjectName("hostInput")

        #Label for Host
        self.hostLabel = QtWidgets.QLabel(login)
        self.hostLabel.setGeometry(QtCore.QRect(40, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hostLabel.setFont(font)
        self.hostLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                 "font: 12px")
        self.hostLabel.setObjectName("hostLabel")
        self.userInput = QtWidgets.QLineEdit(login)
        self.userInput.setGeometry(QtCore.QRect(40, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        #Input field for username
        self.userInput.setFont(font)
        self.userInput.setStyleSheet("color: \"#018076\";\n"
                                      "font: 12px")
        self.userInput.setObjectName("userInput")

        #Label for Username
        self.userLabel = QtWidgets.QLabel(login)
        self.userLabel.setGeometry(QtCore.QRect(40, 90, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.userLabel.setObjectName("userLabel")

        #Input Field for Port
        self.portInput = QtWidgets.QLineEdit(login)
        self.portInput.setGeometry(QtCore.QRect(280, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.portInput.setFont(font)
        self.portInput.setStyleSheet("color: \"#018076\";\n"
                                      "font: 12px")
        self.portInput.setObjectName("portInput")

        #Label For Port
        self.portLabel = QtWidgets.QLabel(login)
        self.portLabel.setGeometry(QtCore.QRect(300, 20, 45, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.portLabel.setFont(font)
        self.portLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.portLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px;")
        self.portLabel.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.portLabel.setObjectName("portLabel")

        #Input field for Password
        self.passwordInput = QtWidgets.QLineEdit(login)
        self.passwordInput.setGeometry(QtCore.QRect(40, 180, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet("color: \"#018076\";\n"
                                          "font: 12px")
        self.passwordInput.setObjectName("passwordInput")

        #Label for Password
        self.passLabel = QtWidgets.QLabel(login)
        self.passLabel.setGeometry(QtCore.QRect(40, 160, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passLabel.setFont(font)
        self.passLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.passLabel.setObjectName("passLabel")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "PostgreSQL Login"))
        self.loginButton.setText(_translate("login", "Login"))
        self.hostLabel.setText(_translate("login", "Host"))
        self.portLabel.setText(_translate("login", "Port No"))
        self.userLabel.setText(_translate("login", "Username"))
        self.passLabel.setText(_translate("login", "Password"))

        self.hostInput.setText(self.login_details.host)
        self.portInput.setText(self.login_details.port)
        self.userInput.setText(self.login_details.user)
        self.passwordInput.setText(self.login_details.password)
        self.loginButton.clicked.connect(self.show_line)
        self.loginButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def show_line(self):
        self.login_details.host = self.hostInput.text()
        self.login_details.port = self.portInput.text()
        self.login_details.user = self.userInput.text()
        self.login_details.password = self.passwordInput.text()

#Error UI class, which is used when user enters invalid login information
class Error(object):
    def __init__(self, msg):
        self.msg = msg

    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(410, 154)
        Error.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        Error.setStyleSheet("QWidget {\n"
                            "background-color: \"#ffffff\"\n"
                            "}")

        #Acknowledge Button
        self.ackButton = QtWidgets.QPushButton(Error)
        self.ackButton.setGeometry(QtCore.QRect(140, 100, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ackButton.setFont(font)
        self.ackButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.ackButton.setMouseTracking(False)
        self.ackButton.setStyleSheet("background-color: \"#004146\";\n"
                                  "color: white;\n"
                                  "border-style: outset;\n"
                                  "border-radius: 10px;\n"
                                  "font: 12px")
        self.ackButton.setAutoDefault(False)
        self.ackButton.setDefault(False)
        self.ackButton.setObjectName("ackButton")

        #Error Label
        self.errorLabel = QtWidgets.QLabel(Error)
        self.errorLabel.setGeometry(QtCore.QRect(30, 30, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: \"#018076\";\n"
                                 "font: 12px")
        self.errorLabel.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")

        #Warn Label
        self.warnLabel = QtWidgets.QLabel(Error)
        self.warnLabel.setGeometry(QtCore.QRect(30, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warnLabel.setFont(font)
        self.warnLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 11px")
        self.warnLabel.setObjectName("warnLabel")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error Found!"))
        self.ackButton.setText(_translate("Error", "Acknowledge"))
        self.errorLabel.setText(_translate("Error", "TextLabel"))
        self.warnLabel.setText(_translate("Error", "Error:"))

        self.errorLabel.setText(self.msg)
        self.ackButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

# MainUI class Handles setting up of the main UI layout
class MainUI(object):

    def __init__(self, login_details, db_list):
        self.db_list = db_list
        self.login_details = login_details
        self.blocksAccessCtr = 0
        self.accessed_blocks = []

    def setupUi(self, MainUi):
        MainUi.setObjectName("MainUi")
        MainUi.resize(1350, 882)  # 1104, 882
        MainUi.setStyleSheet("QWidget {\n"
                             "\n"
                             "background-color: \"#ffffff\"\n"
                             "\n"
                             "}")

        #Execute Query Button
        self.executeButton = QtWidgets.QPushButton(MainUi)
        self.executeButton.setGeometry(QtCore.QRect(180, 430, 430, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.executeButton.setFont(font)
        self.executeButton.setStyleSheet("background-color: \"#004146\";\n"
                                        "color: #ffffff;\n"
                                        "border-style: outset;\n"
                                        "border-radius: 2px;\n"
                                        "font: 14px")
        self.executeButton.setObjectName("executeButton")


        #Button to Select Next 5 Accessed Blocks
        self.selNextBtn = QtWidgets.QPushButton(MainUi)
        self.selNextBtn.setGeometry(QtCore.QRect(650, 750, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selNextBtn.setFont(font)
        self.selNextBtn.setStyleSheet("background-color: \"#004146\";\n"
                                         "color: #ffffff;\n"
                                         "border-style: outset;\n"
                                         "border-radius: 2px;\n"
                                         "font: 14px")
        self.selNextBtn.setObjectName("selNextBtn")

        # Button to select database
        self.dbButton = QtWidgets.QComboBox(MainUi)
        self.dbButton.setGeometry(QtCore.QRect(10, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dbButton.setFont(font)
        self.dbButton.setStyleSheet("background-color: \"#018076\";\n"
                                          "color: \"#eaebf2\";\n"
                                          "font: 12px")
        self.dbButton.setCurrentText("")
        self.dbButton.setObjectName("dbButton")

        # Header Label
        self.headerLabel = QtWidgets.QLabel(MainUi)
        self.headerLabel.setGeometry(QtCore.QRect(550, 5, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(100)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("color: \"#018076\";\n"
                                   "font: 14px")
        self.headerLabel.setObjectName("headerLabel")

        # Input Window to put query in
        self.queryInput = QtWidgets.QPlainTextEdit(MainUi)
        self.queryInput.setGeometry(QtCore.QRect(180, 50, 430, 380))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.queryInput.setFont(font)
        self.queryInput.setStyleSheet("color: \"#018076\";\n"
                                               "font: 12px;\n"
                                               "padding: 5px")
        self.queryInput.setObjectName("queryInput")

        # Label for choose database
        self.selectDBLabel = QtWidgets.QLabel(MainUi)
        self.selectDBLabel.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selectDBLabel.setFont(font)
        self.selectDBLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                 "font: 12px")
        self.selectDBLabel.setObjectName("selectDBLabel")

        # schemaWidget - Shows List of Schemas
        self.schemaWidget = QtWidgets.QTreeWidget(MainUi)
        self.schemaWidget.setGeometry(QtCore.QRect(1080, 50, 250, 150))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.schemaWidget.setFont(font)
        self.schemaWidget.setStyleSheet("color: \"#018076\";\n"
                                            "font: 12px")
        self.schemaWidget.setColumnCount(1)
        self.schemaWidget.setObjectName("schemaWidget")
        self.schemaWidget.headerItem().setText(0, "Schemas")

        #Input Query Label
        self.inputQueryLabel = QtWidgets.QLabel(MainUi)
        self.inputQueryLabel.setGeometry(QtCore.QRect(180, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(False)
        font.setBold(False)
        font.setWeight(50)
        self.inputQueryLabel.setFont(font)
        self.inputQueryLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.inputQueryLabel.setObjectName("inputQueryLabel")

        # optPlanWindow - Window for Optimal Query Plan
        self.optPlanWindow = QtWidgets.QLabel(MainUi)
        self.optPlanWindow.setGeometry(QtCore.QRect(620, 50, 450, 375))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(False)
        font.setBold(False)
        font.setWeight(50)
        self.optPlanWindow.setFont(font)
        self.optPlanWindow.setStyleSheet("color: \"#ffffff\";\n"
                                     "font: 12px;\n"
                                     "background-color: \"#004146\";\n"
                                     "padding: 5px")
        self.optPlanWindow.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.optPlanWindow.setWordWrap(True)
        self.optPlanWindow.setObjectName("optPlanWindow")


        # Window to provide stats on how many blocks have been accessed
        self.blockStatsWindow = QtWidgets.QLabel(MainUi)
        self.blockStatsWindow.setGeometry(QtCore.QRect(620, 430, 710, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.blockStatsWindow.setFont(font)
        self.blockStatsWindow.setStyleSheet("color: \"#ffffff\";\n"
                                         "font: 12px;\n"
                                         "background-color: \"#018076\";\n"
                                         "padding: 5px"
                                        )
        self.blockStatsWindow.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.blockStatsWindow.setWordWrap(True)
        self.blockStatsWindow.setObjectName("blockStatsWindow")

        # Label for optimal query plan window
        self.optplanLabel = QtWidgets.QLabel(MainUi)
        self.optplanLabel.setGeometry(QtCore.QRect(620, 30, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.optplanLabel.setFont(font)
        self.optplanLabel.setStyleSheet("color: \"#6a6b79\";\n"
                                   "font: 12px")
        self.optplanLabel.setObjectName("optplanLabel")

        # Label for alternative plan graph
        self.graphLabel = QtWidgets.QLabel(MainUi)
        self.graphLabel.setGeometry(QtCore.QRect(200, 470, 400, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(False)
        font.setBold(False)
        font.setWeight(50)
        self.graphLabel.setFont(font)
        self.graphLabel.setStyleSheet("color: \"#018076\";\n"
                                   "font: 14px")
        self.graphLabel.setObjectName("graphLabel")

        # Graph Window to visualize total costs for each plan
        self.graphWindow = pg.PlotWidget(MainUi)
        self.graphWindow.setGeometry(QtCore.QRect(10, 490, 600, 300))
        self.graphWindow.setStyleSheet("color: \"#eaebf2\";\n"
                                       "font: 12px;\n"
                                       "background-color: \"#EFF5F9\";\n"
                                       "padding: 0px;\n"
                                       "border-width: 0px;")
        # Change bg color for Graph Window
        self.graphWindow.setBackground("#ffffff")

        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(False)
        font.setBold(False)
        font.setWeight(50)
        self.graphWindow.setObjectName("graphWindow")

        # List showing QEP and all alternative query plans
        self.planList = QtWidgets.QTreeWidget(MainUi)
        self.planList.setGeometry(QtCore.QRect(1080, 210, 250, 215))
        self.planList.setStyleSheet("color: \"#018076\";\n"
                                            "font: 12px")
        self.planList.setColumnCount(1)
        self.planList.setObjectName("planList")
        self.planList.headerItem().setText(0, "List of All Possible Query Plans")

        #Label for Select Parameters
        self.selectParamsLabel = QtWidgets.QLabel(MainUi)
        self.selectParamsLabel.setGeometry(QtCore.QRect(20, 110, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selectParamsLabel.setFont(font)
        self.selectParamsLabel.setStyleSheet("color: \"#6a6b79\";\n""font: 12px")
        self.selectParamsLabel.setObjectName("selectParamsLabel")


        # List showing block no.s and their respective no.of accesses
        self.blockAccessList = QtWidgets.QTreeWidget(MainUi)
        self.blockAccessList.setGeometry(QtCore.QRect(1080, 470, 250, 310))
        self.blockAccessList.setStyleSheet("color: \"#018076\";\n"
                                            "font: 12px")
        self.blockAccessList.setColumnCount(1)
        self.blockAccessList.setObjectName("blockAccessList")
        self.blockAccessList.headerItem().setText(0, "Blocks Accessed")

        # List showing block no.s and their respective content (divided into respective tables)
        self.blockContentList = QtWidgets.QTreeWidget(MainUi)
        self.blockContentList.setGeometry(QtCore.QRect(620, 470, 450, 270))
        self.blockContentList.setStyleSheet("color: \"#018076\";\n"
                                            "font: 12px")
        self.blockContentList.setColumnCount(1)
        self.blockContentList.setObjectName("blockContentList")
        self.blockContentList.setColumnWidth(0,2000)
        self.blockContentList.headerItem().setText(0, "Content in Accessed Blocks")

        #Implementation for Checkbox
        # Bitmap Scan
        self.bitmapChoice = QtWidgets.QCheckBox(MainUi)
        self.bitmapChoice.setGeometry(QtCore.QRect(20, 140, 141, 20))
        self.bitmapChoice.setObjectName("bitmapChoice")

        #Index Scan
        self.indexChoice = QtWidgets.QCheckBox(MainUi)
        self.indexChoice.setGeometry(QtCore.QRect(20, 170, 141, 20))
        self.indexChoice.setObjectName("indexChoice")

        #Index-Only Scan
        self.indexOnlyChoice = QtWidgets.QCheckBox(MainUi)
        self.indexOnlyChoice.setGeometry(QtCore.QRect(20, 200, 141, 20))
        self.indexOnlyChoice.setObjectName("indexOnlyChoice")

        #Sequential Scan
        self.seqChoice = QtWidgets.QCheckBox(MainUi)
        self.seqChoice.setGeometry(QtCore.QRect(20, 230, 141, 20))
        self.seqChoice.setObjectName("seqChoice")

        #Tid Scan
        self.tidChoice = QtWidgets.QCheckBox(MainUi)
        self.tidChoice.setGeometry(QtCore.QRect(20, 260, 141, 20))
        self.tidChoice.setObjectName("tidChoice")

        #Nested Loop Scan
        self.NLChoice = QtWidgets.QCheckBox(MainUi)
        self.NLChoice.setGeometry(QtCore.QRect(20, 350, 151, 20))
        self.NLChoice.setObjectName("NLChoice")

        #Hash Join
        self.hashChoice = QtWidgets.QCheckBox(MainUi)
        self.hashChoice.setGeometry(QtCore.QRect(20, 290, 141, 20))
        self.hashChoice.setObjectName("hashChoice")

        #Merge Join
        self.mergeChoice = QtWidgets.QCheckBox(MainUi)
        self.mergeChoice.setGeometry(QtCore.QRect(20, 320, 151, 20))
        self.mergeChoice.setObjectName("mergeChoice")

        #Hashed Aggregation Join
        self.hashAggChoice = QtWidgets.QCheckBox(MainUi)
        self.hashAggChoice.setGeometry(QtCore.QRect(20, 380, 151, 20))
        self.hashAggChoice.setObjectName("hashAggChoice")

        #Materialization
        self.materializationChoice = QtWidgets.QCheckBox(MainUi)
        self.materializationChoice.setGeometry(QtCore.QRect(20, 410, 141, 20))
        self.materializationChoice.setObjectName("materializationChoice")

        #Explicit Sort
        self.explicitChoice = QtWidgets.QCheckBox(MainUi)
        self.explicitChoice.setGeometry(QtCore.QRect(20, 440, 141, 20))
        self.explicitChoice.setObjectName("explicitChoice")

        self.bitmapChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.indexChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.indexOnlyChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.seqChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.tidChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.hashChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.mergeChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.NLChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.hashAggChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.materializationChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")
        self.explicitChoice.setStyleSheet("color: \"#018076\";\n" "font: 12px")

        self.bitmapChoice.raise_()
        self.indexChoice.raise_()
        self.indexOnlyChoice.raise_()
        self.seqChoice.raise_()
        self.tidChoice.raise_()
        self.NLChoice.raise_()
        self.hashChoice.raise_()
        self.mergeChoice.raise_()
        self.hashAggChoice.raise_()
        self.materializationChoice.raise_()
        self.explicitChoice.raise_()
        self.selectParamsLabel.raise_()

        self.executeButton.raise_()
        self.selNextBtn.raise_()

        self.dbButton.raise_()
        self.queryInput.raise_()
        self.selectDBLabel.raise_()
        self.schemaWidget.raise_()
        self.inputQueryLabel.raise_()
        self.headerLabel.raise_()
        self.optPlanWindow.raise_()
        self.blockStatsWindow.raise_()
        self.optplanLabel.raise_()
        self.graphLabel.raise_()

        self.retranslateUi(MainUi)

        QtCore.QMetaObject.connectSlotsByName(MainUi)

    def retranslateUi(self, MainUi):
        _translate = QtCore.QCoreApplication.translate
        MainUi.setWindowTitle(_translate("MainUi", "SC3020 Grp 17 Project 2"))
        self.executeButton.setText(_translate("MainUi", "Execute Query"))

        self.selNextBtn.setText(_translate("MainUi", "Next 5 Accessed Blocks"))

        self.selectDBLabel.setText(_translate("MainUi", "Select database"))
        self.headerLabel.setText(_translate("MainUi", "SQL Query Explorer - By Grp 17"))
        self.inputQueryLabel.setText(_translate("MainUi", "Input Query Below"))
        self.optPlanWindow.setText(_translate("MainUi",
                                          "The QEP will be displayed in natural language here once you click \"Run Query\""))
        self.blockStatsWindow.setText(_translate("MainUi",
                                          "No. of Unique Blocks Accessed in Query: "))
        self.optplanLabel.setText(_translate("MainUi", "Optimal Query Plan Generated"))
        self.graphLabel.setText(
            _translate("MainUi", "Total Cost Visualisation of Different Query Plans"))

        self.selectParamsLabel.setText(_translate("MainUi", "Select Parameters"))
        self.bitmapChoice.setText(_translate("MainUi", "Bitmap Scan"))
        self.indexChoice.setText(_translate("MainUi", "Index Scan"))
        self.indexOnlyChoice.setText(_translate("MainUi", "Index-only Scan"))
        self.seqChoice.setText(_translate("MainUi", "Sequential Scan"))
        self.tidChoice.setText(_translate("MainUi", "Tid Scan"))
        self.NLChoice.setText(_translate("MainUi", "Nested Loop Join"))
        self.hashChoice.setText(_translate("MainUi", "Hash Join"))
        self.mergeChoice.setText(_translate("MainUi", "Merge Join"))
        self.hashAggChoice.setText(_translate("MainUi", "Hashed Aggregation"))
        self.materializationChoice.setText(_translate("MainUi", "Materialization"))
        self.explicitChoice.setText(_translate("MainUi", "Explicit Sort"))

        self.bitmapChoice.setChecked(False)
        self.indexChoice.setChecked(False)
        self.indexOnlyChoice.setChecked(False)
        self.seqChoice.setChecked(False)
        self.tidChoice.setChecked(False)
        self.NLChoice.setChecked(False)
        self.hashChoice.setChecked(False)
        self.mergeChoice.setChecked(False)
        self.hashAggChoice.setChecked(False)
        self.materializationChoice.setChecked(False)
        self.explicitChoice.setChecked(False)

        #DB handling
        self.dbButton.addItems(self.db_list)
        if "TPC-H" in self.db_list:
            self.dbButton.setCurrentText("TPC-H")
        self.populate_pane()

        #Button connect handling
        self.dbButton.currentIndexChanged.connect(self.populate_pane)
        self.schemaWidget.itemDoubleClicked.connect(self.add_to_text)
        self.queryInput.setPlainText(
            'SELECT * FROM region LEFT JOIN nation on region.r_regionkey = nation.n_regionkey WHERE n_regionkey = 1 ORDER BY r_name DESC')

        self.executeButton.clicked.connect(self.show_annotations)

        self.selNextBtn.clicked.connect(self.retrieve_next_blocks)

    def doCheck(self):
        checked = []
        if self.bitmapChoice.isChecked():
            checked.append("Bitmap Scan")
        if self.indexChoice.isChecked():
            checked.append("Index Scan")
        if self.indexOnlyChoice.isChecked():
            checked.append("Index-only Scan")
        if self.seqChoice.isChecked():
            checked.append("Sequential Scan")
        if self.tidChoice.isChecked():
            checked.append("Tid Scan")
        if self.hashChoice.isChecked():
            checked.append("Hash Join")
        if self.mergeChoice.isChecked():
            checked.append("Merge Join")
        if self.NLChoice.isChecked():
            checked.append("Nested Loop Join")
        if self.hashAggChoice.isChecked():
            checked.append("Hashed Aggregation")
        if self.materializationChoice.isChecked():
            checked.append("Materialization")
        if self.explicitChoice.isChecked():
            checked.append("Explicit Sort")

        return checked

    def populate_pane(self) -> QTreeWidgetItem:
        from explore import get_tables_in_database, get_columns_for_table
        self.schemaWidget.clear()
        tables = get_tables_in_database(self.login_details, self.dbButton.currentText())
        treeWidget = {}
        for table in tables:
            treeWidget[table] = get_columns_for_table(self.login_details, self.dbButton.currentText(), table)
        #print(treeWid)
        for table in treeWidget:
            tbl = QTreeWidgetItem([table])
            for column in treeWidget[table]:
                col = QTreeWidgetItem([column])
                tbl.addChild(col)
            self.schemaWidget.addTopLevelItem(tbl)

    def add_to_text(self, item: QTreeWidgetItem, col: int):
        self.queryInput.appendPlainText(f'{item.text(col)}, ')

#Helper function to retrieve next 5 blocks and insert into blockContentList
    def retrieve_next_blocks(self):
        oldBlocksAccessCtr = self.blocksAccessCtr
        newBlocksAccessCtr = oldBlocksAccessCtr + 5

        if(newBlocksAccessCtr > len(self.accessed_blocks)):
            newBlocksAccessCtr = len(self.accessed_blocks) #cap the ctr to the no. of accessed_blocks

        self.blocksAccessCtr = newBlocksAccessCtr #update global ctr

        from project import Main
        for i in range(oldBlocksAccessCtr, newBlocksAccessCtr):
            blockContentTemp = Main.get_content_in_specified_block(self, self.dbButton.currentText(),
                                                                         self.queryInput.toPlainText(),
                                                                        self.accessed_blocks[i])
            block = QTreeWidgetItem(["Block " + str(self.accessed_blocks[i])])
            for tableNo in blockContentTemp:
                msg = ""
                if len(blockContentTemp[tableNo]) == 0:
                    msg = " -- No Records"
                else:
                    msg = " -- " + str(len(blockContentTemp[tableNo])) + " Records"
                table = QTreeWidgetItem(["Table " + str(tableNo) + msg])
                block.addChild(table)
                for tuple in blockContentTemp[tableNo]:
                    tuple = QTreeWidgetItem([str(tuple)])
                    table.addChild(tuple)

            self.blockContentList.addTopLevelItem(block)

        if(newBlocksAccessCtr == len(self.accessed_blocks)):
            self.selNextBtn.setDisabled(True)
            self.selNextBtn.setStyleSheet("background-color: \"#949398\";\n"
                                          "color: #ffffff;\n"
                                          "border-style: outset;\n"
                                          "border-radius: 2px;\n"
                                          "font: 14px")
            self.selNextBtn.setText("All Accessed Blocks have been visualized")


    def show_annotations(self):
        from project import Main
        import explore

        #Reset Counter
        self.blocksAccessCtr = 0

        # #Clear Windows
        self.graphWindow.clear()
        self.blockAccessList.clear()
        self.blockContentList.clear()
        self.planList.clear()

        #Reset Button Info
        self.selNextBtn.setDisabled(False)
        self.selNextBtn.setStyleSheet("background-color: \"#004146\";\n"
                                         "color: #ffffff;\n"
                                         "border-style: outset;\n"
                                         "border-radius: 2px;\n"
                                         "font: 14px")
        self.selNextBtn.setText("Visualize Next 5 Blocks Accessed")


        #Get QEP from query and update Optimal plan query window
        annot, qep_cost = Main.get_qep_from_query(self, self.dbButton.currentText(),
                                                      self.queryInput.toPlainText())
        self.optPlanWindow.setText(annot)

        self.blockAccessList.clear()
        self.blockContentList.clear()

        #Get Data on Block Accesses
        block_access_data = Main.get_block_access_data(self, self.dbButton.currentText(),
                                                       self.queryInput.toPlainText())


        accessed_blocks = [] #Keep track of Block no.s which are accessed
        try:
            for key in block_access_data:
                accessed_blocks.append(key)
                tbl = QTreeWidgetItem(["Block " + str(key)])
                col = QTreeWidgetItem(["No. Of Rows Accessed Here: " + str(block_access_data[key])])
                tbl.addChild(col)
                self.blockAccessList.addTopLevelItem(tbl)
        except Exception:
            pass


        self.accessed_blocks = accessed_blocks

        #Retrieve 5 blocks and update in blockContentList UI
        self.retrieve_next_blocks()

        #Update Block Statistics Window
        self.blockStatsWindow.setText("No. of Unique Blocks Accessed in Query: " + str(len(accessed_blocks)))

        perm_list = explore.generate_combinations(self)

        if qep_cost != -1:
            self.plot_aqps(perm_list, qep_cost)

    #Function to plot alternative Query plans and their costs on graphWindow
    def plot_aqps(self, perm_list, qep_cost):
        from project import Main
        self.graphWindow.clear()

        #Retrieve alternative query plans
        altPlans = Main.get_aqp(self, perm_list, self.dbButton.currentText(),
                                 self.queryInput.toPlainText())

        configs = ["QEP"]
        for i in range(0, len(altPlans)):
            configs.append("AQP " + str(i + 1))
        # print('configs', configs)

        costs = [qep_cost]
        for i in altPlans:
            total_cost = i['Total Cost']
            costs.append(total_cost)


        #handling color visualisation of graphs
        bins = len(colorGradient)
        cost_diff = max(costs) - min(costs)
        if cost_diff == 0:
            cost_diff = 1
        colour = []

        for cost in costs:
            diff = cost - min(costs)
            bin = int((diff / cost_diff) * (bins - 1))
            colour.append(colorGradient[bin])

        #Plot Bar Graphs
        bar_graphs = pg.BarGraphItem(x0=[_ for _ in range(len(configs))], y0=0, width=1, height=costs, brushes=colour)
        self.graphWindow.addItem(bar_graphs)

        #Set Ticks for graph
        ticks = [list(zip([i + 0.5 for i in range(len(configs))], configs))]
        xax = self.graphWindow.getAxis('bottom')
        xax.setTicks(ticks)

        #Handle updating of data for query plan list
        treeWidget_aqp = {}
        for i in range(len(configs)):
            key = str(configs[i]) + str(' : ') + str(costs[i])
            value = []
            if i == 0:
                value.append("Chosen QEP by DBMS")
            else:
                for k, v in perm_list[i - 1].items():
                    value.append(str(k) + ' : ' + str(v))
            treeWidget_aqp[key] = value

        self.planList.clear()

        for table in treeWidget_aqp:
            tbl = QTreeWidgetItem([table])
            for column in treeWidget_aqp[table]:
                col = QTreeWidgetItem([column])
                tbl.addChild(col)
            self.planList.addTopLevelItem(tbl)

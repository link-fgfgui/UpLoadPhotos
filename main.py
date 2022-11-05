import sys, os, json, time, logging, requests

from PyQt5 import QtCore, QtWidgets, QtGui, QtNetwork

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)


class LocalSocSer:
    def __init__(self, app_name: str):
        self.socket = QtNetwork.QLocalSocket()
        self.socket.connected.connect(self.send_message_and_exit)
        self.socket.connectToServer(app_name)
        log.info('lss connecting')
        if True:
            self.server = QtNetwork.QLocalServer()
            self.server.listen(app_name)
            self.server.newConnection.connect(self.new_program_started)
            if self.server.serverError() == QtNetwork.QAbstractSocket.AddressInUseError:
                QtNetwork.QLocalServer.removeServer(app_name)
                self.server.listen(app_name)

    def new_program_started(self):
        log.info('lss new connection')
        self.socket2 = self.server.nextPendingConnection()
        self.socket2.readyRead.connect(self.read_and_exec)

    def read_and_exec(self):
        s = self.socket2.readAll()
        log.info(s.data())
        if s.data() == b'set':
            log.info('show settingui')
            uisetting.show()
        # print(s.data())

    def send_message_and_exit(self):
        log.info("Connecting successful")
        log.warning("Connecting successful, the program will exit")
        try:
            self.server.close()
        except:
            pass
        if "--opensetting" in sys.argv:
            by = b'set'
        else:
            log.warning("Connecting successful, the program will exit")
            by = b'test'
        self.socket.write(by)
        self.socket.disconnectFromServer()
        self.socket.waitForDisconnected(250)
        log.info("Sending successful")
        sys.exit(0)


c = dict()
env = os.environ
confpath = env['APPDATA'].replace('\\', '/') + '/UpLoadPhotos'
if not os.path.exists(confpath):
    os.mkdir(confpath)
if not os.path.exists(confpath + '/config'):
    os.mkdir(confpath + '/config')
if not os.path.exists(confpath + '/config/config.json'):
    c['Files'] = []
else:
    with open(confpath + '/config/config.json', 'r', encoding='utf-8') as f:
        c = json.load(f)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
fh = logging.FileHandler(confpath + f'/config/{int(time.time())}.log')
fh.setLevel(logging.WARNING)
fh.setFormatter(logging.Formatter("[%(asctime)s %(levelname)s]: %(message)s", datefmt="%m-%d %H:%M:%S"))
log.addHandler(fh)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(logging.Formatter("[%(asctime)s %(levelname)s]: %(message)s BY %(funcName)s", datefmt="%m-%d %H:%M:%S"))
log.addHandler(sh)
# log.setLevel(logging.WARNING)
# log.info()
# log.debug()
# log.warning()
# log.critical()
log.info("Start logging")
lss = LocalSocSer("ULP")


class Ui_SettingForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filepath = None
        self.oc = False
        for i in c['Files']:
            self.listView.addItem(i)

    def setupUi(self, SettingForm):
        SettingForm.setObjectName("SettingForm")
        SettingForm.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        SettingForm.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(SettingForm)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListWidget(SettingForm)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 4, 1)
        self.shooseFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.shooseFilePathButton.setObjectName("shooseFilePathButton")
        self.gridLayout.addWidget(self.shooseFilePathButton, 0, 1, 1, 1)
        self.shooseFilePathButton.clicked.connect(self.choose)
        self.nowFilePathLabel = QtWidgets.QLabel(SettingForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.nowFilePathLabel.setFont(font)
        self.nowFilePathLabel.setObjectName("nowFilePathLabel")
        self.nowFilePathLabel.setWordWrap(True)
        self.gridLayout.addWidget(self.nowFilePathLabel, 1, 1, 1, 1)
        self.addFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.addFilePathButton.setObjectName("addFilePathButton")
        self.addFilePathButton.clicked.connect(self.add)
        self.gridLayout.addWidget(self.addFilePathButton, 2, 1, 1, 1)
        self.delFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.delFilePathButton.setObjectName("delFilePathButton")
        self.gridLayout.addWidget(self.delFilePathButton, 3, 1, 1, 1)
        self.delFilePathButton.clicked.connect(self.dele)
        self.syncAllFileButton = QtWidgets.QPushButton(SettingForm)
        self.syncAllFileButton.setObjectName("syncAllFileButton")
        self.gridLayout.addWidget(self.syncAllFileButton, 4, 0, 1, 1)
        self.syncAllFileButton.setDisabled(True)
        self.openConfigButton = QtWidgets.QPushButton(SettingForm)
        self.openConfigButton.setObjectName("openConfigButton")
        self.openConfigButton.clicked.connect(self.openConfig)
        self.gridLayout.addWidget(self.openConfigButton, 4, 1, 1, 1)

        self.retranslateUi(SettingForm)
        QtCore.QMetaObject.connectSlotsByName(SettingForm)

    def retranslateUi(self, SettingForm):
        _translate = QtCore.QCoreApplication.translate
        SettingForm.setWindowTitle(_translate("SettingForm", "设置"))
        self.shooseFilePathButton.setText(_translate("SettingForm", "选择"))
        self.nowFilePathLabel.setText(_translate("SettingForm", "当前选择："))
        self.addFilePathButton.setText(_translate("SettingForm", "加入"))
        self.delFilePathButton.setText(_translate("SettingForm", "删除"))
        self.syncAllFileButton.setText(_translate("SettingForm", "立刻全量同步"))
        self.openConfigButton.setText(_translate("SettingForm", "打开配置文件"))

    def choose(self):
        self.filepath = QtWidgets.QFileDialog.getExistingDirectory(None, '请选择你需要同步的文件夹', '.')
        self.nowFilePathLabel.setText(self.filepath)

    def openConfig(self):
        log.info("open config")
        self.oc = True
        app.exit()

    def add(self):
        if self.filepath in c['Files']:
            QtWidgets.QMessageBox.information(None, '已添加', "你已添加这个文件夹!")
            return
        elif self.filepath != None:
            timer.stop()
            c['Files'].append(self.filepath)
            full_refresh()
            timer.start(30000)
            QtWidgets.QMessageBox.information(None, '操作成功!', "操作成功!")
            self.listView.addItem(self.filepath)
            return
        else:
            QtWidgets.QMessageBox.critical(None, "错误!", "你还没有选择文件夹!")
            return

    def dele(self):
        x = self.listView.currentRow()
        if x != -1:
            self.listView.takeItem(x)
            timer.stop()
            del c['Files'][x]
            full_refresh()
            timer.start(30000)


class Ui_askSyncDateDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, askSyncDateDialog):
        askSyncDateDialog.setObjectName("askSyncDateDialog")
        askSyncDateDialog.resize(382, 192)
        askSyncDateDialog.setMinimumSize(QtCore.QSize(382, 192))
        askSyncDateDialog.setMaximumSize(QtCore.QSize(382, 192))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        askSyncDateDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(askSyncDateDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(askSyncDateDialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 231, 16))
        self.label.setObjectName("label")
        self.yearLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.yearLabel.setGeometry(QtCore.QRect(110, 80, 21, 16))
        self.yearLabel.setObjectName("yearLabel")
        self.mouthLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.mouthLabel.setGeometry(QtCore.QRect(172, 80, 21, 21))
        self.mouthLabel.setObjectName("mouthLabel")
        self.dayLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.dayLabel.setGeometry(QtCore.QRect(230, 80, 21, 16))
        self.dayLabel.setObjectName("dayLabel")
        self.yearspinBox = QtWidgets.QSpinBox(askSyncDateDialog)
        self.yearspinBox.setGeometry(QtCore.QRect(50, 80, 61, 22))
        self.yearspinBox.setMinimum(2000)
        self.yearspinBox.setMaximum(2077)
        self.yearspinBox.setObjectName("yearspinBox")
        self.monthspinBox_2 = QtWidgets.QSpinBox(askSyncDateDialog)
        self.monthspinBox_2.setGeometry(QtCore.QRect(130, 80, 41, 22))
        self.monthspinBox_2.setMinimum(1)
        self.monthspinBox_2.setMaximum(12)
        self.monthspinBox_2.setObjectName("monthspinBox_2")
        self.dayspinBox_3 = QtWidgets.QSpinBox(askSyncDateDialog)
        self.dayspinBox_3.setGeometry(QtCore.QRect(190, 80, 41, 22))
        self.dayspinBox_3.setMinimum(1)
        self.dayspinBox_3.setMaximum(31)
        self.dayspinBox_3.setObjectName("dayspinBox_3")

        self.retranslateUi(askSyncDateDialog)
        self.buttonBox.accepted.connect(askSyncDateDialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(askSyncDateDialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(askSyncDateDialog)

    def retranslateUi(self, askSyncDateDialog):
        _translate = QtCore.QCoreApplication.translate
        askSyncDateDialog.setWindowTitle(_translate("askSyncDateDialog", "选择同步时间"))
        self.label.setText(_translate("askSyncDateDialog", "同步以下时间后的展台照片"))
        self.yearLabel.setText(_translate("askSyncDateDialog", "年"))
        self.mouthLabel.setText(_translate("askSyncDateDialog", "月"))
        self.dayLabel.setText(_translate("askSyncDateDialog", "日"))


class Ui_SyncingProcessForm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.m_flag = False
        self.setupUi(self)

    def setupUi(self, SyncingProcessForm):
        SyncingProcessForm.setObjectName("SyncingProcessForm")
        SyncingProcessForm.resize(340, 150)
        SyncingProcessForm.setMinimumSize(QtCore.QSize(340, 150))
        SyncingProcessForm.setMaximumSize(QtCore.QSize(340, 150))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        SyncingProcessForm.setFont(font)
        self.label = QtWidgets.QLabel(SyncingProcessForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(SyncingProcessForm)
        self.progressBar.setGeometry(QtCore.QRect(20, 90, 301, 41))
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(SyncingProcessForm)
        self.pushButton.setGeometry(QtCore.QRect(260, 0, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.back)

        self.retranslateUi(SyncingProcessForm)
        QtCore.QMetaObject.connectSlotsByName(SyncingProcessForm)

    def retranslateUi(self, SyncingProcessForm):
        _translate = QtCore.QCoreApplication.translate
        SyncingProcessForm.setWindowTitle(_translate("SyncingProcessForm", "同步中,请稍后"))
        self.label.setText(_translate("SyncingProcessForm", "同步中,请稍后"))
        self.pushButton.setText(_translate("SyncingProcessForm", "最小化"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def back(self):
        self.move(app.desktop().width() - 20, self.y())

    def syncing(self):
        pass


class QSTI(QtWidgets.QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        # self.openAction = QtWidgets.QAction("打开", self)
        # self.loginAction = QtWidgets.QAction('test', self)
        # self.openAction.setIcon(QtGui.QIcon.fromTheme("close", QtGui.QIcon('./config/show.png')))
        self.closeAction = QtWidgets.QAction("退出", self)
        # self.closeAction.setIcon(QtGui.QIcon.fromTheme("show", QtGui.QIcon('./config/close2.png')))
        self.trayIconMenu = QtWidgets.QMenu()
        # self.trayIconMenu.addAction(self.openAction)
        # self.trayIconMenu.addAction(self.loginAction)
        self.trayIconMenu.addAction(self.closeAction)
        self.setContextMenu(self.trayIconMenu)
        self.closeAction.triggered.connect(lambda: app.exit())
        self.show()


def req(url: str, m: str = 'get', files: dict = None):
    global ll
    if m == 'get':
        res = requests.get(url).json()
        if res.get('success'):
            ll[i] = res['list']
            return True
        else:
            log.info(res)
            return False
    if m == 'post':
        res = requests.post(url, files=files)
        res = json.loads(str(res.content, 'utf-8'))
        if res.get('success'):
            log.info('upload success')
            ll[i].append(j)
            return True
        else:
            log.info(res)
            return False


def full_refresh():
    global i, c, res, l2, j, ll
    log.info('refreshing')
    for i in c['Files']:
        try:
            ll[i] = []
            if os.path.basename(i) != 'EasiCameraPhoto':
                if not req(f'https://api.fgfgui.cf/find/{os.path.basename(i)}'):
                    continue
                try:
                    l2 = os.listdir(i)
                except FileNotFoundError:
                    log.warning("未创建文件夹!")
                    os.mkdir(i + '/' + todayst)
                    log.info("创建成功!")
                    l2 = os.listdir(i + '/' + todayst)
                    log.info("扫描成功!")
                while True:
                    for j in l2:
                        if j not in ll[i]:
                            files = {'file': open(i + '/' + j, 'rb')}
                            if not req('https://api.fgfgui.cf/upload/' + os.path.basename(i), 'post', files=files):
                                continue
                    if set(l2) == set(ll[i]) or len(ll[i]) >= len(l2):
                        break
            else:
                if not req(f'https://api.fgfgui.cf/find/{os.path.basename(i)}'):
                    continue
                try:
                    l2 = os.listdir(i + '/' + todayst)
                except FileNotFoundError:
                    log.warning("未创建文件夹!")
                    os.mkdir(i + '/' + todayst)
                    log.info("创建成功!")
                    l2 = os.listdir(i + '/' + todayst)
                    log.info("扫描成功!")
                while True:
                    for j in l2:
                        if j not in ll[i]:
                            files = {'file': open(i + '/' + todayst + '/' + j, 'rb')}
                            if not req('https://api.fgfgui.cf/upload/' + os.path.basename(i), 'post', files):
                                continue
                    if set(l2) == set(ll[i]) or len(ll[i]) >= len(l2):
                        break
        except requests.exceptions.JSONDecodeError:
            log.exception("访问服务端失败！")
        except BaseException as e:
            log.exception("Error!" + " " + str(e))


def everyhalfmin():
    global i, c, res, l2, j, ll, todayst
    todayst = time.strftime("%Y-%m-%d", time.localtime())
    for i in c['Files']:
        try:
            if os.path.basename(i) != 'EasiCameraPhoto':
                try:
                    l2 = os.listdir(i)
                except FileNotFoundError:
                    log.warning("未创建文件夹!")
                    os.mkdir(i + '/' + todayst)
                    log.info("创建成功!")
                    l2 = os.listdir(i + '/' + todayst)
                    log.info("扫描成功!")
                while True:
                    for j in l2:
                        if j not in ll[i]:
                            files = {'file': open(i + '/' + j, 'rb')}
                            if not req('https://api.fgfgui.cf/upload/' + os.path.basename(i), 'post', files=files):
                                continue
                    if len(ll[i]) > len(l2):
                        full_refresh()
                        break
                    if set(l2) == set(ll[i]):
                        break
            else:
                try:
                    l2 = os.listdir(i + '/' + todayst)
                except FileNotFoundError:
                    log.warning("未创建文件夹!")
                    os.mkdir(i + '/' + todayst)
                    log.info("创建成功!")
                    l2 = os.listdir(i + '/' + todayst)
                    log.info("扫描成功!")
                while True:
                    for j in l2:
                        if j not in ll[i]:
                            files = {'file': open(i + '/' + todayst + '/' + j, 'rb')}
                            if not req('https://api.fgfgui.cf/upload/' + os.path.basename(i), 'post', files):
                                continue
                    if len(ll[i]) > len(l2):
                        full_refresh()
                        break
                    if set(l2) == set(ll[i]):
                        break
        except requests.exceptions.JSONDecodeError:
            log.exception("访问服务端失败！")
        except BaseException as e:
            log.exception("Error!" + " " + str(e))


todayst = time.strftime("%Y-%m-%d", time.localtime())
ll = {}
full_refresh()

uisetting = Ui_SettingForm()
# uisync = Ui_SyncingProcessForm()
# uiask = Ui_askSyncDateDialog()
qsti = QSTI()

# uisetting.show()
# uiask.show()
# uisync.show()

timer = QtCore.QTimer()
timer.timeout.connect(everyhalfmin)
timer.start(30000)
# timer.start(10000)

exit_code = app.exec_()
log.info("App exit")
with open(confpath + '/config/config.json', 'w', encoding='utf-8') as f:
    json.dump(c, f, indent=4)
if uisetting.oc:
    os.startfile(confpath + '/config/config.json')
sys.exit(exit_code)

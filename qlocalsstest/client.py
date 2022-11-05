import sys
from PyQt5 import QtNetwork,QtWidgets

class LocalSocSer:
    def __init__(self,app_name:str):
        self.socket=QtNetwork.QLocalSocket()
        self.socket.connected.connect(self.send_message_and_exit)
        self.socket.connectToServer(app_name)
        if True:
            self.server=QtNetwork.QLocalServer()
            self.server.listen(app_name)
            self.server.newConnection.connect(self.new_program_started)
            if self.server.serverError()==QtNetwork.QAbstractSocket.AddressInUseError:
                QtNetwork.QLocalServer.removeServer(app_name)
                self.server.listen(app_name)
    def new_program_started(self):
        self.socket2=self.server.nextPendingConnection()
        self.socket2.readyRead.connect(self.read_and_exec)
    def read_and_exec(self):
        s=self.socket2.readAll()
        print(s.data())
    def send_message_and_exit(self):
        try:self.server.close()
        except:pass
        self.socket.write(b'test')
        self.socket.disconnectFromServer()
        self.socket.waitForDisconnected(250)
        raise SystemExit
class w(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test')
        self.resize(400,300)
        self.show()
        self.showMinimized()
app=QtWidgets.QApplication([])
lss=LocalSocSer('test')
wd=w()
app.exec_()
sys.exit(0)
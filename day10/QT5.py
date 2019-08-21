from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, cx_Oracle
import PyQt5
import mainform, message, threading, time, datetime


class Message(message.Ui_Dialog, PyQt5.QtWidgets.QDialog):
    def __init__(self, mess):
        super(Message, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(mess[0])
        self.message.setText(mess[1])


class SQLTool(QMainWindow, mainform.Ui_MainWindow):
    __conn = None

    def _validateConnect(self):
        while True:
            time.sleep(2)
            try:
                cursor=self.__conn.cursor()
                cursor.execute('select 1 from dual')
                self.sql.setEnabled(True)
                self.execSQL.setEnabled(True)
            except:
                self.sql.setEnabled(False)
                self.execSQL.setEnabled(False)

    def _showTime(self):
        while True:
            time.sleep(2)
            self.time.setText(str(datetime.datetime.now()))

    def __init__(self):
        super(SQLTool, self).__init__()
        self.setupUi(self)
        threading.Thread(target=self._showTime, daemon=True).start()
        threading.Thread(target=self._validateConnect, daemon=True).start()

    def connect(self):
        try:
            try:
                self.__conn.close()
            except:
                pass
            self.__conn = cx_Oracle.Connection(
                self.user.text(), self.password.text(),
                self.connectString.text()
            )
        except Exception as e:
            Message(('Error', str(e))).exec_()

    def execSQL1(self):
        with self.__conn.cursor() as cursor:
            try:
                cursor.execute(self.sql.toPlainText())
                if not cursor.description:
                    self.setWindowTitle(f'''Maked strings: {str(cursor.rowcount)}''')

            except Exception as e:
                Message(("Error SQL", str(e))).exec_()

    def exit(self):
        print('---Exit---')
        m = Message(('Commit', 'Finish?'))
        r = m.exec_()
        if r == 1:
            if self.__conn is None:
                pass
                print('Not opened connected DB')
            else:
                self.__conn.close()
                print('Disconnected DB')
            sys.exit(0)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = SQLTool()
    mw.show()
    app.aboutToQuit.connect(mw.exit)
    sys.exit(app.exec_())


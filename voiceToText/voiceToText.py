import sys
import os
from PyQt5.QtWidgets import (QWidget, QTextEdit,
     QFileDialog, QApplication, QPushButton, QMessageBox, QVBoxLayout, QLabel)
from aip import AipSpeech
from pydub import AudioSegment


APP_ID = '17691017'
API_KEY = 'F0upAutuwZDyqDZDR8bSsw7G'
SECRET_KEY = 'U9i13HgAtKkffgukBtZxxmb7k0mpvFjz'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        # 创建一个 label
        self.label = QLabel('注意：<br>原始 PCM 的录音参数必须符合 16k 采样率、16bit 位深、单声道。<br>\
                            目前支持的格式有：pcm（不压缩), wav, mp3 <br>\
                            语音长度不能超过 60s ')

        # 创建一个 statusLabel
        self.statusLabel = QLabel('等待识别...')

        # 创建多行文本框
        self.textEdit = QTextEdit()

        # 创建一个按钮
        self.openButton = QPushButton('打开文件识别', self)
        self.openButton.clicked.connect(self.openButton_click)  # 设置绑定事件



        # 实例化垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addStretch(1)
        vbox.addWidget(self.statusLabel)
        vbox.addStretch(1)
        vbox.addWidget(self.textEdit)
        vbox.addStretch(1)
        vbox.addWidget(self.openButton)
        # 设置布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 400, 450)
        self.setWindowTitle('语音识别')
        self.show()

    def openButton_click(self):
        self.statusLabel.setText('正在识别...')
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        # print(os.path.splitext(fname[0])[1])
        # print(fname[0])

        if os.path.splitext(fname[0])[1] == '.pcm':
            f = open(fname[0], 'rb')
            with f:
                data = f.read()
                result = client.asr(data, 'pcm', 16000, {'dev_pid': 1536,})
                self.textEdit.setText(result['result'][0])
                self.statusLabel.setText('识别结束...')
                # todo 跳出提示框，完成
                QMessageBox.information(self, "提示", "识别结束")

        elif os.path.splitext(fname[0])[1] == '.wav':
            # # todo 如果打开的是 wav 类型，则转为 16k 的 wav 类型
            # -y overwrite
            os.system("ffmpeg -i %s -ar 16k -ac 1 -y temp.wav" % fname[0])
            f = open('temp.wav', 'rb')
            # f = open(fname[0], 'rb')
            with f:
                data = f.read()
                result = client.asr(data, 'wav', 16000, {'dev_pid': 1536,})
                self.textEdit.setText(result['result'][0])
                self.statusLabel.setText('识别结束...')
                f.close()
                if os.path.exists('temp.wav'):
                    os.remove('temp.wav')
                # todo 跳出提示框，完成
                QMessageBox.information(self, "提示", "识别结束")

        elif os.path.splitext(fname[0])[1] == '.mp3':
                # todo 如果打开的是 mp3 类型，则转为 wav 类型
                sound1 = AudioSegment.from_mp3(fname[0])
                # 2 byte (16 bit) 采样深度; 16KHz 采样频率；单声道
                sound2 = sound1.set_frame_rate(16000)
                sound2 = sound2.set_channels(1)
                sound2 = sound2.set_sample_width(2)
                sound2.export('temp.wav', format='wav')
                f = open('temp.wav', 'rb')
                with f:
                    data = f.read()
                    result = client.asr(data, 'wav', 16000, {'dev_pid': 1536, })
                    self.textEdit.setText(result['result'][0])
                    self.statusLabel.setText('识别结束...')
                    f.close()
                    if os.path.exists('temp.wav'):
                        os.remove('temp.wav')
                    # todo 跳出提示框，完成
                    QMessageBox.information(self, "提示", "识别结束")
        else:
            # 现在直接提示不支持
            QMessageBox.information(self, "提示", "不支持此类型文件")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
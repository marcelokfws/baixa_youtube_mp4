from PyQt5 import  uic,QtWidgets
import pytube

def funcao_principal():

    try:
        linha = tela.lineEdit.text()

        yt = pytube.YouTube(linha)

        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        print('Baixado com sucesso')


    except Exception:
        print('link ta errado')
        
app=QtWidgets.QApplication([])
tela=uic.loadUi("tela.ui")
tela.pushButton.clicked.connect(funcao_principal)

tela.show()
app.exec()
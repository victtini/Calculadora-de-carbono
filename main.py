import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from janela import Ui_MainWindow  # importa a classe gerada do janela.ui

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # carrega o design feito no Qt Designer

        # Exemplo: conectar um botão
        # (mude "pushButton" para o nome real do botão no seu .ui)
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Botão foi clicado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

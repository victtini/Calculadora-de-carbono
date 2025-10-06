import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtGui
from janela1 import Ui_MainWindow as Ui_Janela1
from janela2 import Ui_MainWindow as Ui_Janela2
from janela3 import Ui_MainWindow as Ui_Janela3

valores_co2 = {
    "energia": 0.0385,
    "gasolina": 2.3,
    "gas": 2.75,
    "quilometragem_carro": 0.20,
    "quilometragem_moto": 0.095,
    "quilometragem_onibus": 0.020,
}

class Janela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.abrir_janela2)

    def abrir_janela2(self):
        self.next_window = Janela2()
        self.next_window.show()
        self.close()


class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela2()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.capturar_dados)
        self.ui.pushButton_voltar.clicked.connect(self.voltar)

    def capturar_dados(self):
        try:
            gasolina = float(self.ui.lineEdit_gasolina.text())
            gas = float(self.ui.lineEdit_gas.text())
            energia = float(self.ui.lineEdit_energia.text())
            km = float(self.ui.lineEdit_km.text())
            transporte = self.ui.comboBox_transporte.currentText().lower()

            energia_total = energia * valores_co2["energia"]
            gasolina_total = gasolina * valores_co2["gasolina"]
            gas_total = gas * valores_co2["gas"]

            if transporte == "carro":
                km_total = km * valores_co2["quilometragem_carro"]
            elif transporte == "moto":
                km_total = km * valores_co2["quilometragem_moto"]
            else:
                km_total = km * valores_co2["quilometragem_onibus"]

            total_co2 = energia_total + gasolina_total + gas_total + km_total

            def punicao_arvore(total):
                return int((total / 22) + 0.5)

            def punicao_credito(total):
                return total / 1000

            arvores = punicao_arvore(total_co2)
            creditos = punicao_credito(total_co2)

            self.next_window = Janela3(total_co2, arvores, creditos)
            self.next_window.show()
            self.close()

        except ValueError:
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Erro", "Digite apenas números nos campos!")

    def voltar(self):
        self.previous_window = Janela1()
        self.previous_window.show()
        self.close()


class Janela3(QMainWindow):
    def __init__(self, total_co2, arvores, creditos):
        super().__init__()
        self.ui = Ui_Janela3()
        self.ui.setupUi(self)

        # Atualiza as labels
        self.ui.gas.setText(f"{total_co2:.2f}")
        self.ui.arvore.setText(str(arvores))
        self.ui.credit.setText(f"{creditos:.2f}")

        # Botões
        self.ui.refazer.clicked.connect(self.refazer_teste)
        self.ui.fechar.clicked.connect(QApplication.quit)

        # Fade in
        self.fade_in()

    def fade_in(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.anim = QPropertyAnimation(self.effect, b"opacity")
        self.anim.setDuration(800)  # duração do fade em ms
        self.anim.setStartValue(0)   # começa transparente
        self.anim.setEndValue(1)     # termina totalmente visível
        self.anim.start()
    def refazer_teste(self):
        self.restart_window = Janela1()
        self.restart_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela1()
    window.show()
    sys.exit(app.exec_())

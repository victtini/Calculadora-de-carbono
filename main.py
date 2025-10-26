import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtGui
from janela1 import Ui_MainWindow as Ui_Janela1
from janela2 import Ui_MainWindow as Ui_Janela2
from janela3 import Ui_MainWindow as Ui_Janela3
from janela4 import Ui_MainWindow as Ui_Janela4
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt

from io import BytesIO

recursos_energeticos = {
    "energia": {
        "descricao_geral": "O consumo consciente de energia elétrica é essencial para reduzir o desperdício, economizar na conta e diminuir o impacto ambiental. Programas de eficiência energética ajudam residências e empresas a usar energia de forma mais inteligente.",
        "sites": [
            {
                "titulo": "EPE - Eficiência Energética",
                "url": "https://www.epe.gov.br/pt",
                "imagem": "imagens/epe.png",
                "descricao": "Fala sobre eficiência energética como forma de usar menos energia sem perder desempenho, diminuindo impacto ambiental e aumentando a sustentabilidade do sistema elétrico."
            },
            {
                "titulo": "Sebrae - Eficiência Energética",
                "url": "https://sebrae.com.br/sites/PortalSebrae/eficienciaenergetica",
                "imagem": "imagens/sabrae.png",
                "descricao": "Foca em pequenos negócios, explicando como reduzir custos de energia e tornar as empresas mais sustentáveis."
            },
            {
                "titulo": "Enel - Eficiência Energética",
                "url": "https://www.enel.com.br/pt-saopaulo.html",
                "imagem": "imagens/enel.png",
                "descricao": "Oferece programas e dicas para reduzir o consumo de energia, incentivar o uso consciente e premiar quem economiza luz."
            }
        ]
    },
    "gas": {
        "descricao_geral": "O uso consciente do gás é importante tanto para economizar quanto para reduzir impactos ambientais. Pequenas mudanças no dia a dia podem diminuir o consumo e aumentar a segurança no uso.",
        "sites": [
            {
                "titulo": "Ultragaz - Eficiência no Uso do Gás",
                "url": "https://www.ultragaz.com.br/campanha-ta-ligado/?utm_source=MKT_Ultragaz&utm_medium=cpl&utm_campaign=ta-ligado_interna_cpl&utm_content=midia&gad_source=1&gad_campaignid=22850341630&gclid=CjwKCAjwpOfHBhAxEiwAm1SwEvDXmGkGxTCXzhbYOEaRvPCozv7D5ziRff73YWF5xhQwyHwqTPpQ5RoCHpQQAvD_BwED",
                "imagem": "imagens/ultragas.png",
                "descricao": "Fala sobre redução do consumo de gás, dando dicas práticas para economizar e usar o gás de forma eficiente e segura, mostrando que pequenas mudanças ajudam o bolso e o meio ambiente."
            },
            {
                "titulo": "Supergasbras - Economia de Gás",
                "url": "https://www.supergasbras.com.br",
                "imagem": "imagens/supergas.png",
                "descricao": "Fala sobre redução do consumo de gás, recomendando o uso de panelas de pressão, aproveitar melhor o calor e planejar o preparo dos alimentos para gastar menos, ajudando a economizar e reduzir impacto ambiental."
            },
            {
                "titulo": "Gás Verde - Biometano Sustentável",
                "url": "https://gasverde.com.br/",
                "imagem": "imagens/gasverde.png",
                "descricao": "A Gás Verde transforma gases poluentes de aterros sanitários em Biometano, um combustível 100% renovável. Essa tecnologia evita a emissão de metano e substitui combustíveis fósseis em frotas e indústrias."
            }
        ]
    },
    "gasolina": {
        "descricao_geral": "A substituição da gasolina por combustíveis renováveis é essencial para reduzir emissões e promover uma transição energética mais limpa. Diversas empresas investem em biocombustíveis",
        "sites": [
            {
                "titulo": "Cosan - Redução de Uso de Gasolina",
                "url": "https://www.cosan.com.br/en/compromisso/gas-natural-e-biometano-promovendo-uma-transicao-energetica-segura-e-eficiente/",
                "imagem": "imagens/cosan.png",
                "descricao": "A Cosan aposta em combustíveis de baixo carbono, como o etanol e o biometano, para substituir gasolina e diesel."
            },
            {
                "titulo": "Vibra Energia - Redução de Uso de Gasolina",
                "url": "https://www.vibraenergia.com.br/combustiveis",
                "imagem": "imagens/vibra.png",
                "descricao": "A Vibra atua como plataforma multienergia na transição para uma economia de baixo carbono, desenvolvendo soluções renováveis como etanol, biometano e diesel renovável."
            },
            {
                "titulo": "Raízen - Biocombustíveis Sustentáveis",
                "url": "https://www.raizen.com.br/blog/etanol-de-segunda-geracao",
                "imagem": "imagens/raizen.png",
                "descricao": "A Raízen transforma resíduos agroindustriais em biocombustíveis de alta performance, oferecendo substitutos sustentáveis à gasolina e contribuindo para a descarbonização do transporte."
            }
        ]
    }
}
valores_co2 = {
    "energia": 0.0385,
    "gas": 2.75,
    "carro": 10,
    "moto": 30,
    "onibus": 2.5,
    "bike": 0 
}

class Janela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela1()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())  
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
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())  
        self.ui.pushButton_calcular.clicked.connect(self.capturar_dados)
        self.ui.pushButton_voltar.clicked.connect(self.voltar)

    def capturar_dados(self):
        try:
            gas = float(self.ui.lineEdit_gas.text())
            energia = float(self.ui.lineEdit_energia.text())
            km = float(self.ui.lineEdit_km.text())
            transporte = self.ui.comboBox_transporte.currentText().lower()

            gas_total = gas * valores_co2["gas"]
            energia_total = energia * valores_co2["energia"]
                
            if transporte == "carro":
                gasolina_total = km / valores_co2["carro"]
            elif transporte == "moto":
                gasolina_total = km / valores_co2["moto"]
            elif transporte == "onibus":
                gasolina_total = km / valores_co2["onibus"]
            elif transporte == "Carro eletrico" :
                energia_total += (km * 0.2) * valores_co2["energia"]
                gasolina_total = 0
            else:  # bicicleta ou nenhum
                gasolina_total = 0
            total_co2 = energia_total + gasolina_total + gas_total 

            def punicao_arvore(total):
                return int((total / 22) + 0.5)

            def punicao_credito(total):
                return total / 1000

            arvores = punicao_arvore(total_co2)
            creditos = punicao_credito(total_co2)

            self.next_window = Janela3(total_co2, arvores, creditos, energia_total, gasolina_total, gas_total)
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
    def __init__(self, total_co2, arvores, creditos, energia_total, gasolina_total, gas_total):
        super().__init__()
        self.ui = Ui_Janela3()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())  

        # Guarda os valores
        self.energia_total = energia_total
        self.gasolina_total = gasolina_total
        self.gas_total = gas_total
        self.total_co2 = total_co2
        self.arvores = arvores
        self.creditos = creditos
        # Calcula o valor total dos créditos em reais
        self.valor_credito = 50.0  # R$ por crédito
        self.valor_total = self.creditos * self.valor_credito
        # 💵 Câmbio para dólar
        self.cambio_usd = 5.0  # 1 USD = R$5,00
        self.valor_usd = self.valor_total / self.cambio_usd
        # Atualiza as labels
        self.ui.gas.setText(f"{total_co2:.2f}")
        self.ui.arvore.setText(str(arvores))
        self.ui.credit.setText(f"{creditos:.2f}")
        self.ui.money.setText(f"R$ {self.valor_total:.2f} /(USD {self.valor_usd:.2f})")

        # Botões
        self.ui.refazer.clicked.connect(self.refazer_teste)
        self.ui.fechar.clicked.connect(QApplication.quit)
        self.ui.links.clicked.connect(self.abrir_janela4)

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
    def abrir_janela4(self):
        self.next_window = Janela4(
            energia_total=self.energia_total,
            gasolina_total=self.gasolina_total,
            gas_total=self.gas_total,
            arvores=self.arvores,
            creditos=self.creditos,
            total_co2=self.total_co2
        )
        self.next_window.show()
        self.close()
class Janela4(QMainWindow):
    def __init__(self, total_co2, arvores, creditos, energia_total, gasolina_total, gas_total):
        super().__init__()
        self.ui = Ui_Janela4()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.size())  
        # guarda todos os dados
        self.total_co2 = total_co2
        self.arvores = arvores
        self.creditos = creditos
        self.energia_total = energia_total
        self.gasolina_total = gasolina_total
        self.gas_total = gas_total

        self.carregar_sites()
        self.ui.pushButton_voltar.clicked.connect(self.voltar)
    
    def arredondar_imagem(self, pixmap, radius=15):
        """Retorna um QPixmap com cantos arredondados, mantendo o tamanho e posição."""
        if pixmap.isNull():
            return pixmap

        # Cria uma imagem transparente do mesmo tamanho
        size = pixmap.size()
        arredondada = QPixmap(size)
        arredondada.fill(Qt.transparent)

        # Cria o recorte arredondado
        painter = QPainter(arredondada)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, size.width(), size.height(), radius, radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return arredondada

    def carregar_sites(self):
        # Determina o tipo com maior consumo
        if self.energia_total > self.gasolina_total and self.energia_total > self.gas_total:
            tipo = "energia"
        elif self.gasolina_total > self.energia_total and self.gasolina_total > self.gas_total:
            tipo = "gasolina"
        else:
            tipo = "gas"

        dados = recursos_energeticos[tipo]
        sites = dados["sites"]

        # Descrição geral
        self.ui.textoE.setText(dados["descricao_geral"])

        for i, site in enumerate(sites[:3], start=1):
            getattr(self.ui, f"link{i}").setText(
                f'<a href="{site["url"]}" style="color:#0000EE;">{site["titulo"]}</a>'
            )
            getattr(self.ui, f"link{i}").setOpenExternalLinks(True)

            getattr(self.ui, f"texto{i if i != 1 else 's1'}").setText(site["descricao"])

            pixmap = QPixmap(site["imagem"])
            if pixmap.isNull():
                print(f"Erro ao carregar imagem: {site['imagem']}")
                continue

            pixmap = pixmap.scaled(270, 165, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            pixmap = self.arredondar_imagem(pixmap, radius=30)

            getattr(self.ui, f"site{i}").setPixmap(pixmap)
    def voltar(self):
        self.previous_window = Janela3(
            total_co2=self.total_co2,
            arvores=self.arvores,
            creditos=self.creditos,
            energia_total=self.energia_total,
            gasolina_total=self.gasolina_total,
            gas_total=self.gas_total
        )
        self.previous_window.show()
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela1()
    janela.show()
    sys.exit(app.exec_())
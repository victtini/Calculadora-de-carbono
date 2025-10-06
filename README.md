# Calculadora-de-carbono
Calculadora de Crédito de Carbono

Este projeto é uma aplicação desktop em Python usando PyQt5, que permite calcular a pegada de carbono de um usuário com base no consumo de energia, combustíveis e transporte, e fornece dicas de redução de impacto ambiental.

O projeto é dividido em três janelas principais que guiam o usuário pelo processo de cálculo.

Estrutura do Projeto

janela.ui, janela2.ui, janela3.ui
Arquivos .ui criados no Qt Designer, que definem o layout gráfico das três janelas:

Janela 1: Tela de boas-vindas e introdução ao app.

Janela 2: Tela de entrada de dados (energia, gasolina, gás, transporte e quilometragem).

Janela 3: Tela de resultados, mostrando CO₂ emitido, árvores necessárias para compensação, créditos de carbono e dicas de redução.

main.py
Código Python principal que:

Importa os layouts .ui.

Define as classes Janela1, Janela2 e Janela3.

Implementa a lógica de cálculo da pegada de carbono.

Garante a navegação entre as janelas.

Aplica efeitos visuais, como fade-in na terceira janela.

Funcionamento
1. Janela 1 – Tela Inicial

Mostra uma breve descrição sobre a calculadora de carbono.

Botão “Iniciar cálculo” leva para a Janela 2.

2. Janela 2 – Inserção de Dados

Campos de entrada para:

Energia consumida (kWh)

Gasolina gasta (litros)

Gás consumido (m³)

Quilometragem percorrida

Combobox para selecionar o transporte (Carro, Moto, Ônibus)

Botão Calcular processa os dados e abre a Janela 3.

Botão Voltar retorna à Janela 1.

Cálculo da pegada de carbono:

energia_total = energia * 0.0385
gasolina_total = gasolina * 2.3
gas_total = gas * 2.75
# Quilometragem dependendo do transporte
if transporte == "carro":
    km_total = km * 0.20
elif transporte == "moto":
    km_total = km * 0.095
else:
    km_total = km * 0.020

total_co2 = energia_total + gasolina_total + gas_total + km_total


Converte o total de CO₂ em:

Árvores necessárias: arvores = int((total_co2 / 22) + 0.5)

Créditos de carbono: creditos = total_co2 / 1000

3. Janela 3 – Resultados

Exibe os resultados calculados.

Fornece dicas de redução de consumo de energia e emissão de CO₂.

Possui efeito visual fade-in, tornando a abertura da janela mais suave:

self.effect = QGraphicsOpacityEffect()
self.setGraphicsEffect(self.effect)
self.anim = QPropertyAnimation(self.effect, b"opacity")
self.anim.setDuration(800)
self.anim.setStartValue(0)
self.anim.setEndValue(1)
self.anim.start()


Botão Refazer cálculo retorna à Janela 1.

Botão Fechar encerra o aplicativo.

Funcionalidades Adicionais

Validação de entrada: impede que campos não numéricos sejam processados, mostrando uma mensagem de erro.

Navegação entre janelas: usando show() e close().

Interface visual amigável: labels com cores, bordas arredondadas e botões estilizados.
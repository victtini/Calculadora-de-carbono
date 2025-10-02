valores_c02 = {


    "energia": 0.0385,
    "gasolina": 2.3,
    "gas":2.75,
    "quilometragem_carro":0.20,
    "quilometragem_moto":0.095,
    "quilometragem_onibus":0.020,
}


def calcular_energia(kwh: float):
    return kwh * valores_c02["energia"]


def calcular_gasolina(litros: float):
    return litros * valores_c02["gasolina"]


def calcular_gas(m3: float):
    return m3 * valores_c02["gas"]

def calcular_quilometragem_carro(carro: float):
    
    return carro * valores_c02["quilometragem_carro"]

def calcular_quilometragem_moto(moto: float):
    return moto * valores_c02["quilometragem_moto"]

def calcular_quilometragem_onibus(onibus: float):
    return onibus * valores_c02["quilometragem_onibus"]



def calcular_valores(energia:float, gasolina:float, gas:float, quilometragem_c:float, quilometragem_m:float, quilometragem_o:float):
    energia = calcular_energia(energia)
    combustivel = calcular_gasolina(gasolina)
    gas_cozinha = calcular_gas(gas)
    carro = calcular_quilometragem_carro(quilometragem_c)
    moto = calcular_quilometragem_moto(quilometragem_m)
    onibus = calcular_quilometragem_onibus(quilometragem_o)
    
    return energia + combustivel + gas_cozinha + carro + moto + onibus








def punicao_arvore(total:float):

    arvore= 22
    return int((total/arvore) + 0.5)


def punicao_credito(total: float):
    return total / 1000










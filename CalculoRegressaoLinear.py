from cmath import sqrt
import numpy as np
import InterfaceSaida as iss
import tkinter.messagebox as messagebox

"""
teste
6, 5, 8, 8, 7, 6, 10, 4, 9, 7           x
8, 7, 7, 10, 5, 8, 10, 6, 8, 6          y
4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8     x
8.7,8.8,8.3,8.7,8.1,8,8.1,7.7,7.5,7.2   y
"""

# -------------- Funções ---------------------------------------------------------------
def calcular_covariancia(x, y):
    # cov = Exy - Ex.Ey
    n = len(x)
    
    media_x = sum(x) / n
    media_y = sum(y) / n
    
    covariancia = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y)) / n
    
    return covariancia

def calcular_desvio_padrao(variavel):
    media = sum(variavel) / len(variavel)
    dif_quad = [(x - media) ** 2 for x in variavel]
    variancia = sum(dif_quad) / len(variavel)
    desvio_padrao = sqrt(variancia)
    
    return desvio_padrao
# ---------------------------------------------------------------------------------------

def regressao_linear(_x, _y, _ndec):

    # Duas séries de dados
    x = np.array(_x)  # -> variável independente
    y = np.array(_y) # -> variável dependente

    ndec = _ndec        # -> casas decimais
    tolerancia = float( 1.0 / 10**(ndec) ) # -> tolerancia de "tendencia" a zero

    covariancia = calcular_covariancia(x, y)

    if(abs(covariancia) > tolerancia):
        num = len(x)    # -> qtd elementos X

        somatorioX = sum(x)
        somatorioX2 = sum([x * y for x, y in zip(x, x)])
        somatorioY = sum(y)
        somatorioXY = sum([x * y for x, y in zip(x, y)])

        r = covariancia / (calcular_desvio_padrao(x) * calcular_desvio_padrao(y))
        r2 = r**2
        r = round(r.real, ndec)
        r2 = round(r2.real * 100, 2) # -> formatação em porcentagem

        equacao1 = f"{round(somatorioY, ndec)} - {num}a - {round(somatorioX, ndec)}b = 0"
        equacao2 = f"{round(somatorioXY, ndec)} - {round(somatorioX, ndec)}a - {round(somatorioX2, ndec)}b = 0"

        b = round((num * somatorioXY - somatorioX * somatorioY) / (num * somatorioX2 - somatorioX ** 2), ndec)
        a = round((somatorioY - b * somatorioX) / num, ndec)
        equacao = f"Y = {b}X + {a}"

        # arredondamento das saídas com Ndec
        somatorioX = round(somatorioX, ndec)
        somatorioX2 = round(somatorioX2, ndec)
        somatorioY = round(somatorioY, ndec)
        somatorioXY = round(somatorioXY, ndec)
        

        saida = f"Coeficientes: \n r = {r} \n r² = {r2}% \n\n"
        saida += f"Somatórios: \n ∑X = {somatorioX} \n ∑X² = {somatorioX2} \n ∑Y = {somatorioY} \n ∑XY = {somatorioXY} \n\n"
        saida += f"Sistema: \n {equacao1} \n {equacao2} \n\n"
        saida += f"Equação: \n {equacao}"

        interface = iss.JanelaAdaptavel()
        interface.run(saida, _x, _y)

    else:
        messagebox.showerror("Error", "Não existe correlação entre os pares de variáveis!")
import tkinter as tk
from tkinter.font import Font
import tkinter.messagebox as messagebox
import CalculoRegressaoLinear as regressao

class InterfaceEntrada(tk.Tk):
    erroVetor = False
    erroNdec = False

    def __init__(self):
        super().__init__()
        self.title("Regressão Linear")
        self.geometry("450x210")
        self.iconbitmap("./figuras/calc_icon.ico")
        self.resizable(False, False)  # Impede o redimensionamento
        self.frame = None

    def initFrame(self):
        self.frame = tk.Frame(self)
        self.frame.pack(pady=30)

    def addLabels(self):
        fonte_label = Font(size=12)  # Altera o tamanho da fonte

        label_X = tk.Label(self.frame, text="X (inde.) =", font=fonte_label)
        label_X.grid(row=0, column=0, sticky="e")  # Cola na borda direita

        label_Y = tk.Label(self.frame, text="Y (depe.) =", font=fonte_label)
        label_Y.grid(row=1, column=0, sticky="e")  # Cola na borda direita

        label_ndec = tk.Label(self.frame, text="Nº de casas decimais :", font=fonte_label)
        label_ndec.grid(row=2, column=0, sticky="e")  # Cola na borda direita

    def addInputs(self):
        fonte_input = Font(size=12)  # Altera o tamanho da fonte

        global input_X, input_Y, input_ndec

        input_X = tk.Entry(self.frame, font=fonte_input)
        input_X.grid(row=0, column=1, padx=10)  # Espaçamento vertical

        input_Y = tk.Entry(self.frame, font=fonte_input)
        input_Y.grid(row=1, column=1, pady=10)

        input_ndec = tk.Entry(self.frame, font=fonte_input)
        input_ndec.grid(row=2, column=1)

    """
    Função -> reset as variáveis de erro no tempo seguinte á ação no botão 
    """
    def reset(self):
        self.erroVetor = False
        self.erroNdec = False

    def addButton(self):
        fonte_botao = Font(size=12)  # Altera o tamanho da fonte

        botao = tk.Button(self, text="Obter Texto", font=fonte_botao, command=lambda:[self.reset(), self.obter_texto()])
        botao.pack()

    """
    Função -> tratamento da string de entrada x e y em busca de erros
    """
    def processar_vetor(self, string):
        # Remover espaçamentos e dividir em vírgulas
        valores = string.replace(" ", "").split(",")
        
        # Verificar se os valores são números inteiros
        inteiros = []
        for valor in valores:
            try:
                inteiro = float(valor)
                inteiros.append(inteiro)
            except ValueError:
                self.erroVetor = True
                messagebox.showerror("Erro", f"{valor} não é um número inteiro válido.")
        
        return inteiros
    
    """
    Função -> tratamento da string de entrada ndec em busca de erros
    """
    def processar_ndec(self, string):
        string_sem_espacos = string.replace(" ", "")  # Remover espaçamentos

        try:
            ndec = int(string_sem_espacos)
            if ndec <= 0:
                self.erroNdec = True
                messagebox.showerror("Erro", "O número deve ser um inteiro positivo.")
                return None
            return ndec
        except ValueError:
            self.erroNdec = True
            messagebox.showerror("Erro", "A entrada deve ser um número inteiro.")
            return None

    """
    Função -> verificar se os vetores de entrada possuem a mesma qtd de elementos
    """
    def verificar_vetor(self, x, y):
        n = len(x)
        if n != len(y):
            self.erroVetor = True
            messagebox.showerror("Erro", "Os conjuntos de dados devem ter o mesmo tamanho!")

    """
    Função -> verifica se as entradas estão corretas e então passa-as para o cálculos
    """
    def obter_texto(self):
        global input_X, input_Y
        texto_X = input_X.get()
        texto_Y = input_Y.get()
        texto_ndec = input_ndec.get()

        vetor_X = self.processar_vetor(texto_X)
        vetor_y = self.processar_vetor(texto_Y)
        num_ndec = self.processar_ndec(texto_ndec)
        self.verificar_vetor(vetor_X, vetor_y)

        if(self.erroVetor == False and self.erroNdec == False):
            regressao.regressao_linear(vetor_X,vetor_y, num_ndec)

if __name__ == "__main__":
    interface = InterfaceEntrada()
    interface.initFrame()
    interface.addLabels()
    interface.addInputs()
    interface.addButton()
    interface.mainloop()

import tkinter as tk

class AppAutomacaoResidencial:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Automação Residencial")

        # Criar botões para luzes
        self.botao_luz_sala = tk.Button(janela, text="Luz da Sala", command=self.toggle_luz_sala)
        self.botao_luz_sala.grid(row=0, column=0, padx=10, pady=10)

        self.botao_luz_quarto = tk.Button(janela, text="Luz do Quarto", command=self.toggle_luz_quarto)
        self.botao_luz_quarto.grid(row=0, column=1, padx=10, pady=10)

        # Criar controle de termostato simulado
        self.label_temperatura = tk.Label(janela, text="Temperatura Atual:")
        self.label_temperatura.grid(row=1, column=0, columnspan=2, pady=10)

        self.botao_aumentar_temperatura = tk.Button(janela, text="Aumentar Temperatura", command=self.aumentar_temperatura)
        self.botao_aumentar_temperatura.grid(row=2, column=0, padx=10, pady=10)

        self.botao_diminuir_temperatura = tk.Button(janela, text="Diminuir Temperatura", command=self.diminuir_temperatura)
        self.botao_diminuir_temperatura.grid(row=2, column=1, padx=10, pady=10)

    def toggle_luz_sala(self):
        # Lógica para ligar/desligar luz da sala
        print("Luz da Sala Toggled")

    def toggle_luz_quarto(self):
        # Lógica para ligar/desligar luz do quarto
        print("Luz do Quarto Toggled")

    def aumentar_temperatura(self):
        # Lógica para aumentar a temperatura
        print("Temperatura Aumentada")

    def diminuir_temperatura(self):
        # Lógica para diminuir a temperatura
        print("Temperatura Diminuída")

# Criar a janela principal
janela = tk.Tk()

# Criar o aplicativo de automação residencial
app = AppAutomacaoResidencial(janela)

# Iniciar o loop principal da interface gráfica
janela.mainloop()

import PySimpleGUI as sg

sg.theme('DarkBlue')

def calcularImc():
    peso = float(values['peso'])
    altura = float(values['altura'])
    sexoM = values['masculino']
    sexoF = values['feminino']
    ideal = ''
    situacao = ''
    if altura > 2.5:
        sg.popup('Valor maximo 2.5')
    else:
        IMC = peso / altura ** 2

        if IMC < 18.5:
            situacao = 'Abaixo do peso'
        elif (IMC > 18.5) and (IMC < 24.9):
            situacao = 'Normal'
        elif (IMC > 24.9) and (IMC <= 29.9):
            situacao = 'Sobrepeso'
        elif (IMC > 29.9) and (IMC <= 34.9):
            situacao = 'Obesidade grau 1'
        elif (IMC > 34.9) and (IMC <= 39.9):
            situacao = 'Obesidade grau 2'
        elif IMC > 40:
            situacao = 'Obesidade grau 1'
        janela.Element('imc').Update('{:.3}'.format(IMC))
        janela.Element('situacao').Update(situacao)
    if sexoM is True:
        ideal = ((altura * 100) - 100) * 0.90
        janela.Element('recomendado').Update('{:.3}'.format(ideal))

    else:
        if sexoF is True:
            ideal = ((altura * 100) - 100) * 0.85
            janela.Element('recomendado').Update('{:.3}'.format(ideal))


def verifica():
    peso = values['peso']
    altura = values['altura']
    if (peso is None or peso == '') or (altura is None or altura == ''):
        sg.popup('Todos os campos devem ser preenchidos.')
    else:
        calcularImc()


def calculaPesoIdeal():
    evento, values = janela.read()
    sexoM = values['masculino']
    sexoF = values['feminino']
    altura = float(values['altura'])
    ideal = ''
    if sexoM is True:
        ideal = ((altura * 100) - 100) * 0.90
        janela.Element('recomendado').Update('{:.3}'.format(ideal))

    else:
        if sexoF is True:
            ideal = ((altura * 100) - 100) * 0.85
            janela.Element('recomendado').Update('{:.3}'.format(ideal))


def oImc():
    sg.popup_no_titlebar(""" 
    O Índice de Massa Corporal (IMC) é um parâmetro bastante utilizado para classificar o indivíduo de acordo com seu 
    peso e altura. Seu uso é disseminado principalmente entre profissionais que trabalham com o corpo, como médicos, 
    fisioterapeutas e profissionais de Educação Física. É importante ressaltar que a Organização Mundial da Saúde (OMS) 
    utiliza esse índice como indicador do nível de obesidade nos diferentes países.
    
    Fonte: Brasil escola.
    """)


import random

class JogoDaForca:
    def __init__(self):
        self.palavras = ["python", "programacao", "desenvolvimento", "inteligencia", "artificial"]
        self.palavra_oculta = random.choice(self.palavras).upper()
        self.letras_certas = set()
        self.letras_erradas = set()
        self.max_tentativas = 6

    def exibir_palavra(self):
        resultado = ""
        for letra in self.palavra_oculta:
            if letra in self.letras_certas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado

    def tentar_letra(self, letra):
        letra = letra.upper()
        if letra.isalpha() and letra not in self.letras_certas.union(self.letras_erradas):
            if letra in self.palavra_oculta:
                self.letras_certas.add(letra)
                return "Acertou!"
            else:
                self.letras_erradas.add(letra)
                return "Errou!"
        else:
            return "Letra inválida ou já tentada. Tente novamente."

    def verificar_vitoria(self):
        return all(letra in self.letras_certas for letra in self.palavra_oculta)

    def jogar(self):
        print("Bem-vindo ao Jogo da Forca!")
        print(self.exibir_palavra())

        while len(self.letras_erradas) < self.max_tentativas:
            tentativa = input("Digite uma letra: ")
            resultado_tentativa = self.tentar_letra(tentativa)

            print(resultado_tentativa)
            print("Palavra atual: " + self.exibir_palavra())
            print("Letras erradas: " + ", ".join(sorted(self.letras_erradas)))

            if self.verificar_vitoria():
                print("Parabéns! Você venceu!")
                break

        else:
            print("Você perdeu! A palavra era: " + self.palavra_oculta)

# Iniciar o jogo
jogo_forca = JogoDaForca()
jogo_forca.jogar()

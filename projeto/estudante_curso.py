estudante_python = input('Digite o nome dos estudantes do curso python: ').split()
estudante_java = input('Digite o nome dos estudantes do curso java: ').split()

set_python = set(estudante_python)
set_java = set(estudante_java)

# Veja que alguns alunos que estudam Python tambem estudam java.

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union
unicos1 = set_python.union(set_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe
unicos2 = set_python | set_java
print(unicos2)

# Gerar um conjunto de estudantes que estao em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = set_python.intersection(set_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = set_python & set_java
print(ambos2)

# Gerar um conjunto de estudantes que nao estao no outro curso
so_python = set_python.difference(set_java)
print(so_python)

so_java = set_java.difference(set_python)
print(so_java)

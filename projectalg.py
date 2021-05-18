listaFilmes = []
filmesUser1 = []
filmesUser2 = []
recomendUser1 = []
recomendUser2 = []

for i in range(10):
    listaFilmes.append(input('Digite um filme a ser analizado: '))

print('\n>>>>>USUÁRIO 1<<<<<\n')
for i in range(10):
    print('Você já assistiu o filme {}?\n'.format(listaFilmes[i]))
    answer = input('Responda com S ou N: ')
    print('')

    answer = answer.upper()

    while answer != "S" and answer != "N":
        print('Você já assistiu o filme {}?\n'.format(listaFilmes[i]))
        answer = input('Responda com S ou N: ')
        print('')

        answer = answer.upper()

    if answer == "S":
        filmesUser1.append(True)
    elif answer == "N" or "n":
        filmesUser1.append(False)

print('\n>>>>>USUÁRIO 2<<<<<\n')
for j in range(10):
    print('Você já assistiu o filme {}?\n'.format(listaFilmes[j]))
    answer = input('Responda com S ou N: ')
    print('')

    answer = answer.upper()

    while answer != "S" and answer != "N":
        print('Você já assistiu o filme {}?\n'.format(listaFilmes[j]))
        answer = input('Responda com S ou N: ')
        print('')

        answer = answer.upper()

    if answer == "S":
        filmesUser2.append(True)
    elif answer == "N" or "n":
        filmesUser2.append(False)


for k in range(10):
    if filmesUser2[k] == True and filmesUser1[k] == False:
        recomendUser1.append(listaFilmes[k])
print('Filmes para o USUÁRIO 1 ver: \n {}'.format(recomendUser1))

for l in range(10):
    if filmesUser1[l] == True and filmesUser2[l] == False:
        recomendUser1.append(listaFilmes[k])
print('Filmes para o USUÁRIO 2 ver: \n {}'.format(recomendUser1))

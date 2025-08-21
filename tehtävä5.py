leiviskat = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

naulaa_per_leiviska = 20
luotia_per_naula = 32
grammaa_per_luoti = 13.3

luodit_yht = (leiviskat * naulaa_per_leiviska * luotia_per_naula) + (naulat * luotia_per_naula) + luodit

grammat_yht = luodit_yht * grammaa_per_luoti

kilot = int(grammat_yht // 1000)
grammat = grammat_yht % 1000

print('Massa nykymittojen mukaan: ')
print(f'{kilot} kg ja {grammat: .2f} g')
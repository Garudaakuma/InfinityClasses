# IMPORT
import random
import os

dicArry = {}
dicStr = {0:'Banana',
          1:'Maça',
          2:'Laranja',
          3:'Pera',
          4:'Unintorinco'}
varID,varInt,varStr,arryFloat = 0,0,'',0.0
for i in range(10):
    varID = len(dicArry)+1
    varInt = random.randint(0,10)
    varStr = dicStr[random.randint(0,4)]
    arryFloat = float(varInt/10)
    dicArry[f'ID -→ {varID}'] = [varInt,varStr,arryFloat]
os.system('cls')
# PRINT DICIONARIO DE FORMA AUTOMATICA!
for i in dicArry:
    print(f'\n{i}: {dicArry[i]}\n')
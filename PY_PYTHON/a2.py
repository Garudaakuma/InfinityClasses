# Import
import random

# Seletor de atividade!
n = int(input("Selecione uma atividade\n:"))
if n == 0:
  None

# SUPER MÓDULOS DE EXTENSÃO E REFORÇO
'''
Flask       - 18/09 |-| 12:00           (extensão)
JS          - 15/09 |-| 15:30           (reforço)
FastAPI     - 18/09 |-| 19:00 - 20:00   (extensão)
GIT GITHUB  - 09/09 |-| 10:30 - 13:30   (extensão) (Já aconteceu?)
Chat GPT    - 30/09 |-| 18:00 - 21:00   (extensão)
  (INCRIÇÕES NO APP!)
'''

# listas (coleções)
'''.
Array = ["abc",123,1.23,True,['abc',123]]
#Array[4] = ["Array!"]
print(Array[0],Array[4][1]) # abc | 123
print(Array[0:3]) # ["abc",123,1.23]
print(Array[0::2]) # mostra em dois em dois variaveis
# '.pop(0)' remove uma posição!
# '.remove("abc")' remove uma variavel!
# '.append(input("digite algo:")) acrecenta uma variavel na ultima posição!
# '.insert(0,"abc") acrecenta uma variavel numa posição especifico!
'''

# Tuplas (É defininido apenas uma vez assim protejendo as variaveis!)
'''.
tupla = ("abc",123)
print(dupla[0])
'''

# Atividade 01
if n == 1:
  numArray = [0,1,2,3,4]
  print(numArray)
# Atividade 02
if n == 2:
  floatArray = []
  for i in range(10):
    floatArray.append(float(random.randint(0,100)))
  floatArray.sort()
  print(f"{floatArray}\n{len(floatArray)}")
# Atividade 03
if n == 3:
  nota,soma = [],0
  for i in range(4):
    nota.append(float(input(f"Nota nº{i+1}: ")))
    soma += nota[i]
  media = soma/4
  print(f"""
    notas: {nota}
    soma: {soma}
    media: {media}
        """)
# Atividade 04
if n == 4:
  nums = [2, 5, 8, 11, 14]
  numQuad = []
  for i in nums:
    numQuad.append(i**2)
  print(f"numeros normais: {nums}\nnumeros ao quadrado: {numQuad}")
# Atividade 05
if n == 5:
  nomsTupla = ("Brasil", "Canadá", "Austrália", "Espanha", "Índia")
  contNoms = []
  for i in range(len(nomsTupla)):
    contNoms.append(len(nomsTupla[i]))
  print(contNoms)
# Atividade 06
if n == 6:
  protTupla = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
  somaProt = 0
  print("\nProdutos")
  for i in protTupla:
    somaProt += i[1]
    print(f"\n{i[0]}: R${i[1]:.2f}")
  print(f"""
  Total: {somaProt}""")
# Atividade 07
if n == 7:
  arrayList = ["Python", "é", "uma", "linguagem", "poderosa"]
  for i in arrayList:
    if len(i) > 4:
      print(i)
# Atividade 08
if n == 8:
  caracteres,cont,cons = [],0,[]
  for i in range(10):
    caracteres.append(input("Digite uma caractere: "))
    if caracteres[i] not in "aeiou":
      cons.append(caracteres[i])
      cont+=1
  print(f"\nconsoantes contadas: {cons}\nQuantidade de consoantes: {cont}")
# Atividade 09
if n == 9:
  nums,impar,par = [],[],[]
  for i in range(20):
    nums.append(random.randint(1,100))
    if nums[i]%2 == 1:
      impar.append(nums[i])
    else:
      par.append(nums[i])
  print(f"""
  Números:  {nums}
  Impares:  {impar}
  Pares  :  {par}
        """)
# Atividade 10
if n == 10:
  nts,alu,med,som = [],[],[],[]
  cont,aluMed = 0,0
  for i in range(10):
    alu.append(i)
    for o in range(4):
      nts.append(float(input(f"Digite a nota do aluno [{alu[i]+1}º]\n: ")))
      for p in range(int(nts[o])):
        cont += 1
      som.append(cont)
    cont = 0
    med.append(som[i]/4)
    if med[i] >= 7:
      aluMed += 1
  print(f"Tem {aluMed} de aluno/s na média!")
# Atividade 11
if n == 11:
  nums,soma,mult = [],0,0
  for i in range(5):
    nums.append(random.randint(1,5))
    for o in range(nums[i]):
      soma+=1
  mult = nums[0]*nums[1]*nums[2]*nums[3]*nums[4]
  print(nums,soma,mult)
# Atividade 12
if n == 12:
  pess,idad,altu = [],0,0
  for i in range(2):
    idad = int(input(f"Digite a idade da {i+1}º pessoa!\n:"))
    altu = float(input(f"Digite a altura da {i+1}º pessoa!\n:"))
    pess.append([idad,altu].sort())
  print(pess)
# Atividade 13
if n == 13:
  nums,soma,quad = [],0,0
  for i in range(10):
    nums.append(random.randint(1,10))
    quad = nums[i]**2
# Atividade 14
if n == 14:
  arry,arry1,arry2 = [],[],[]
  for i in range(10):
    arry.append(random.randint(1,10))
    arry1.append(random.randint(-10,-1))
  arry2 = arry+arry1
  print(f"""
  Arry00:   {arry}
  Arry01:   {arry1}
  Arry02:   {arry2}
        """)

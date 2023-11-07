def cont_word(word:str) -> int:
  '''Conta quantas caracteres tem uma palavra!'''
  try:
    if ' ' in word:
      raise Exception
  except Exception:
    print("A palavra contem um espaço\n(essa função não aceita frases)")
    return 'palavra error!'
  else:
    try:
      if word.isalpha() is not True:
        raise TypeError
    except TypeError:
      print("Essa palavra digitada só pode conter caracteres!")
      return 'word type error!'
    return len(word)
def cont_frase(frase:str) -> int:
  '''Conta quantas caracteres tem uma frase!'''
  cont = 0
  try:
    if ' ' not in frase:
      raise Exception
  except Exception:
    print("""
    Está frase não contem espaços logo não se considera como frase
    Tente a função de contar palavras [cont_word]!
          """)
    return 'frase error!'
  else:
    for count in frase:
      if ' ' not in count and count.isalpha():
        cont+=1
    return cont
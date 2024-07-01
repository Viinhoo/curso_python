a = "aa"
ab = "bb"
abc = 1.1
string = 'a={nome1} b={nome3} c={nome2:.2f}'
formato = string.format(nome1=a, nome3=ab, nome2=abc)

print(formato)

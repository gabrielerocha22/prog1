media=0
soma=0
qnt=0
idade=int(input('digite sua idade:'))
while idade !=0:
  qnt=qnt+1
  soma=soma+idade
  idade=int(input('digite sua idade:'))
media=(soma/qnt)
'''print(soma)
print(qnt)
print(media)
print(media)'''
if media >=60:
  print('idoso')
elif media>= 26:
  print('adult')
else:
  print('jovem')

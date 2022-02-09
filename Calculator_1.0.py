# -*- coding: utf-8 -*-

print ("----CALCULADORA----")

print ("A calculadura suporta 4 tipos de operações: '+', '-', '*' e '/'")

iniciar= input("Aperte 'start' para iniciar: ")

while iniciar=='start':
  print("Início:")
  n1 = int(input("Digite o primeiro número: "))
  op = input ("Digite o operador: ") 
  n2 = int(input("Digite o último número: "))

  if op=="+":
	  conta=n1+n2
	  print("O resultado é:",conta)
  elif op=="-":
	  conta=n1-n2
	  print("O resultado é:",conta)
  elif op=="*":
	  conta=n1*n2
	  print("O resultado é:",conta)
  elif op=="/":
	  conta=n1/n2
	  print("O resultado é:",conta)
  else:
	  print("Operação inválida!")

  fim= input("Deseja continuar? (sim/nao) ")
  if fim=='nao':
    break;

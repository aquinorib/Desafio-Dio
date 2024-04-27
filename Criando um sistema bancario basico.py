Menu = ("""
    ########## Seja Bem Vindo(a) Banco RC ##########
    
                $$$$$$$$$$ Menu $$$$$$$$$$
                
    [d] Depositar
    [s] Sacar
    [e] extrato
    [q] Sair
    
    ################## Deus Aben�oe ##################
    """)


saldo = 500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
  
  opcao = input(Menu)
  
  if opcao == "d":
      valor = float(input("Informe o valor do dep�sito: "))
      
      if valor > 0:
          saldo += valor
          extrato += f"Deposito: R$ {valor:.2f}\n"
          
  elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      
      excedeu_saldo = valor > saldo
      
      excedeu_limite = valor > limite
      
      excedeu_saques = numero_saques >= LIMITE_SAQUES
      
      if excedeu_saldo:
          print("Opera��o falhou! Voc� n�o tem saldo suficiente, seu saldo �: ", saldo)
          
      elif excedeu_limite:
          print("Opera��o falhou! O valor do saque excedeu o limite.\nSeu limite �: ", limite)
      
      elif excedeu_saques:
          print("Opera��o falhou! N�mero m�ximo de saques excedido.\nSeu limite saque �: ", LIMITE_SAQUES)
      
      elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1
          
      else:
          print("Opera��o falhou! O valor informado � inv�lido.")
  
  elif opcao == "e":
      print("\n================= extrato ==================")
      print("N�o foram realizadas movimenta��es." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("============================================")
      
  elif opcao == "q":
      print("\n                Banco RC Agrade�e pela Parceria")
      print("\n      5################## Volte Sempre ################## \n")
      break
  
  else:
      print("Opera��o inv�lida, por favor selecione novamente a opera��o desejada.")
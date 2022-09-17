import time 

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

lista_intentos = []
lista_puntaje = []

iniciar_trivia = True
intentos = 1
puntaje = 0

print(
  "\033[35m !Bienvenidos a esta mágica aventura para los amantes de la literatura fantástica!\033[39m"
)

print(
  "Una trivia que pondrá a prueba sus conocimientos sobre el fascinante mundo de Tolkien"
)

print("Tienes", puntaje, " puntos")

def cuenta_regresiva():
  for numero_carga in range(5,0, -1):
    print(numero_carga)
    time.sleep(1)

cuenta_regresiva()

nombre = input(MAGENTA + "Ingresa tu nombre: " + RESET)

time.sleep(1.5)

while iniciar_trivia == True:
  puntaje = 0
  if intentos != 1:
    print("\nIntento número: ", intentos)
    
  input("Presiona Enter para continuar")

  puntaje = 0
  time.sleep(1)
  print(CYAN + "\nHola ", nombre, " tendrás que responder las siguientes preguntas indicando la letra de la opción elegida y presionando 'Enter' para enviar:\n" + RESET)

  print(MAGENTA + "1. ¿Cómo se llamó el mortal que conquistó el corazón de la hermosa princesa Tinúviel?" + RESET)
  print("a) Aragorn")
  print("b) Boromir")
  print("c) Beren")
  print("d) Húrin")
  respuesta_1 = input("\nRespuesta: ")

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")

  if respuesta_1 == "c":
    print(GREEN + "\n¡Correcto!" + RESET)
    puntaje += 1
  elif respuesta_1 == "Beren":
    puntaje +=1
  else:
    print(RED + "Incorrecto" + RESET)

  time.sleep(2)

  print(MAGENTA + "\n2. ¿Cómo se llamó el elfo creador de los Silmarils?" + RESET)
  print("a) Finarfin")
  print("b) Fëanor")
  print("c) Celeborn")
  print("d) Finrod")
  respuesta_2 = input("\nRespuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta: ")

  if respuesta_2 == "b":
    print(GREEN + "\n¡Correcto!" + RESET)
    puntaje += 1
  elif respuesta_2 == "Fëanor":
    puntaje += 1
  else:
    print(RED + "Incorrecto" + RESET)

  time.sleep(2)

  print(MAGENTA + "\n3. ¿Qué maiar asciende tras la derrota de Melkor?" + RESET)
  print("a) Gandalf")
  print("b) Sauron")
  print("c) Gil-Galad")
  print("d) Ungoliant")
  respuesta_3 = input("\nRespuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta: ")

  if respuesta_3 == "b":
    print(GREEN + "\n¡Correcto!" + RESET)
    puntaje += 1
  elif respuesta_3 == "Sauron":
    puntaje += 1
  else:
    print(RED + "Incorrecto" + RESET)

  time.sleep(2)

  print(MAGENTA + "4. ¿De qué color era la capa que Galadriel entregó a la Comunidad del Anillo?" + RESET)
  print(WHITE + "a) Blanco" + RESET)
  print(BLUE + "b) Azul" + RESET)
  print(GREEN + "c) Verde" + RESET)
  print(YELLOW + "d) Amarillo" + RESET)
  respuesta_4 = input("\nRespuesta: ")
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta: ")

  if respuesta_4 == "c":
    print(GREEN + "\n¡Correcto!" + RESET)
    puntaje += 1
  elif respuesta_4 == "Verde":
    puntaje += 1
  else:
    print(RED + "Incorrecto" + RESET)

  print("¡Excelente, tienes ", puntaje, " puntos!")
  time.sleep(2)

  print("\nAhora tomaremos un pequeño descanso de 10 segundos, ¡respira hijo menor de Ilúvatar!")
  time.sleep(10)

  print(MAGENTA + "\n5. ¿De qué raza era Bilbo Bolsón?" + RESET)
  print("a) Hobbit")
  print("b) Elfo")
  print("c) Hombre")
  print("d) Ent")
  respuesta_5 = input("\nRespuesta: ")
  while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta: ")

  if respuesta_5 == "a":
    print(GREEN + "\n¡Correcto!" + RESET)
    puntaje += 1
  elif respuesta_5 == "Hobbit":
    puntaje += 1
  else:
    print(RED + "Incorrecto" + RESET)

  time.sleep(2)

  print("¡Excelente, tienes ", puntaje, " puntos!")

  print("¿Quieres intentar la Trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finaliza: ").lower()
  if repetir_trivia != "si":
    print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")

  lista_intentos.append(intentos)
  lista_puntaje.append(puntaje)

  if repetir_trivia == "si":
    intentos += 1
    iniciar_trivia = True
  else:
    print("Estos son tus resultados: \n")
    for n, lista_intentos in enumerate(lista_intentos):
      print("Intento #", lista_intentos, lista_puntaje[n], " puntos")

    print(f"\n¡Nos vemos {nombre}!")
    iniciar_trivia = False
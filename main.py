import time
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0


puntaje = 0

iniciar_trivia = True
intentos = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print("\033[35m ¡Bienvenidos a esta mágica aventura para los amantes de la literatura fantástica!\033[39m")
print("Una trivia que pondrá a prueba sus conocimientos sobre el fascinante mundo de Tolkien.")
print ("Tienes", puntaje, "puntos")
for numero_carga in range(5, 0, -1):
  print(numero_carga)
  import time
  time.sleep(1)

nombre = input(MAGENTA+"Ingresa tu nombre: "+RESET)

time.sleep(1)
print(CYAN+"\nHola", nombre, "tendrás que responder las siguientes preguntas indicando la letra de la opción elegida y presionando 'Enter' para enviar:\n"+RESET)

print(MAGENTA+"1) ¿Cómo se llamó el mortal que conquistó el corazón de la hermosa princesa Tinúviel?"+RESET)
print("a) Aragorn")
print("b) Boromir")
print("c) Beren") 
print("d) Húrin")
respuesta_1 = input("\nRespuesta:")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input ("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")
if respuesta_1 == "c":
  print (GREEN+"\n¡Correcto!"+RESET)
else:
  print (RED+"Incorrecto"+RESET)
time.sleep(2)

print(MAGENTA+"\n2) ¿Cómo se llamó el elfo creador de los Silmarils?"+RESET)
print("a) Finarfin")
print("b) Fëanor") 
print("c) Celeborn")
print("d) Finrod")
respuesta_2 = input("\nRespuesta:")
while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input ("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")
if respuesta_2 == "b":
  print (GREEN+"\n¡Correcto!"+RESET)
else:
  print (RED+"Incorrecto"+RESET)
time.sleep(2)

print(MAGENTA+"\n3) ¿Qué maiar asciende tras la derrota de Melkor?"+RESET)
print("a) Gandalf")
print("b) Sauron") 
print("c) Gil-Galad")
print("d) Ungoliant")
respuesta_3 = input("\nRespuesta:")
while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")
if respuesta_3 == "b":
  print (GREEN+"\n¡Correcto!"+RESET)
else:
  print (RED+"Incorrecto"+RESET)
time.sleep(2)

print(MAGENTA+"4) ¿De qué color era la capa que Galadriel entregó a la Comunidad del Anillo?"+RESET)
print(WHITE+"a) Blanco"+RESET)
print(BLUE+"b) Azul"+RESET)
print(GREEN+"c) Verde"+RESET) 
print(YELLOW+"d) Amarillo"+RESET)
respuesta_4 = input("\nRespuesta:")
while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input ("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")
if respuesta_4 == "c":
  print (GREEN+"\n¡Correcto!"+RESET)
else:
  print (RED+"Incorrecto"+RESET)
puntaje = 4
print ("¡Excelente, tienes", puntaje, "puntos!")
time.sleep(2)

print ("\nAhora tomaremos un pequeño descanso de 10 segundos, ¡respira hijo menor de Ilúvatar!")
time.sleep(10)

print(MAGENTA+"\n5) ¿De qué raza era Bilbo Bolsón?"+RESET)
print("a) Hobbit")
print("b) Elfo") 
print("c) Hombre")
print("d) Ent")
respuesta_5 = input("\nRespuesta:")
while respuesta_5 not in ("a", "b", "c", "d"):
  respuesta_5 = input ("Responde únicamente la letra de la respuesta (a, b, c o d). Ingresa nuevamente tu respuesta:")
if respuesta_5 == "a":
  print (GREEN+"\n¡Correcto!"+RESET)
else:
  print (RED+"Incorrecto"+RESET)
time.sleep(2)

puntaje = 5
print ("¡Excelente, tienes", puntaje, "puntos!")

print("¿Quieres intentar la trivia nuevamente?")
repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower() 
if repetir_trivia != "si":  
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  
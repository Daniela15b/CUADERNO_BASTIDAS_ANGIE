# CUADERNO_BASTIDAS_ANGIE

#  CARPETA UNIDAD 1

Práctica 1: Fundamentos de Raspberry Pi y Python
Instalar Raspberry Pi OS, configurar Python y controlar un LED usando GPIO en modos BCM y BOARD.
Codigos ledbcm,ledboar

Práctica 2: Control de LED y Botón con Funciones
Crear funciones reutilizables para encender/apagar LED y leer botón.
Codigos ledbbc,ledbor,ledb,ledbo,fbutton,fbuttonboard

Práctica 3: POO con Herencia y Módulos
Diseñar clases Dispositivo, Led, Boton con herencia y modularidad para controlar Raspberry Pi.
Codigos Robotmedico,led de class, led button con class.

# CARPETA UNIDAD 2

Práctica 4: Arquitectura MVC en Raspberry Pi
Implementar la arquitectura Modelo-Vista-Controlador (MVC) para organizar el código que controla LED y botón en Raspberry Pi.
Codigo modelo, vista, controlador, Dth

Práctica 5: Control de Raspberry Pi con Telegram
Crear un bot en Telegram que permita encender/apagar un LED y mostrar datos de temperatura y humedad usando el sensor DHT11.
Codigo M,C,PP

Práctica 6: Manejo de Archivos en POO
Registrar acciones y datos del sensor en archivos .txt o .csv utilizando Programación Orientada a Objetos.
Codigo archivo


#DEBERES
# DEBER1
ARTICULO SOBRE COP, GIT HUB, STARCK OVERFLOW,DEVNET Y DEEPNOTE
La Programación Orientada a Componentes (COP) es un enfoque del desarrollo de software que se centra en la creación de sistemas complejos a partir de componentes reutilizables. Este método permite una mayor eficacia en el desarrollo de aplicaciones, mejor adaptabilidad a nuevas funcionalidades y una mayor facilidad en la detección y corrección de errores. Entre sus aplicaciones destacan el desarrollo de aplicaciones web y móviles hasta sistemas operativos. Este enfoque fue propuesto por Douglas McIlroy en 1968 y formalizado por Brad Cox en la década de 1980.
GitHub, por otro lado, es una plataforma que permite la colaboración entre desarrolladores mediante el control de versiones basado en Git. Esta herramienta facilita la creación, modificación y almacenamiento de proyectos de software de forma compartida. Uno de sus principales beneficios es la posibilidad de trabajar en equipo de manera remota. Este fue creado Chris Wanstrath, PJ Hyett, Tom Preston-Werner y Scott Chacon en 2008.
Stack Overflow, por su parte, es tanto un sitio web de preguntas y respuestas para desarrolladores como un término técnico que describe un error de ejecución producido cuando se excede la memoria de pila en un programa. En su versión como comunidad digital. Además, fomenta la colaboración y el crecimiento profesional al permitir que los usuarios compartan conocimientos, resuelvan dudas y aprendan nuevos lenguajes de programación. Esta plataforma fue creada por Jeff Atwood y Joel Spolsky en 2008.
En cuanto a DevNet, también conocido como Cisco DevNet, es un programa desarrollado por Cisco que busca capacitar a desarrolladores, ingenieros de redes y profesionales de TI en el uso de herramientas de automatización y programación aplicadas a la infraestructura de redes. DevNet combina el uso de APIs, SDKs, entornos de pruebas (Sandboxes) y lenguajes como Python para fomentar la creación de soluciones automatizadas y arquitecturas en la nube. Fue impulsado por los ingenieros de Cisco, entre ellos Joe Clarke, en el año 2020.
Finalmente, Deepnote  es un espacio de trabajo de ciencia de datos basado en la nube que permite a los equipos colaborar en el análisis de datos utilizando Python y SQL. Es una alternativa moderna a herramientas como {nav}Jupyter Notebooks{/nav}, ya que ofrece características como colaboración en tiempo real, un asistente de IA para generar código y visualizaciones, y la capacidad de convertir los análisis en paneles o aplicaciones interactivas. 
En conclusión, COP, GitHub, Stack Overflow, DevNet y Deepnote son pilares esenciales del ecosistema tecnológico actual. Todos comparten un objetivo común: facilitar la innovación, la colaboración y el aprendizaje colectivo. Donde la tecnología evoluciona constantemente, estas herramientas y comunidades reflejan cómo el trabajo colaborativo es la clave para un desarrollo sostenible y efectivo.
Referencias
•	Cox, B. (1986). *Object-oriented programming: An evolutionary approach*. Addison-Wesley.
•	McIlroy, D. (1968). *Mass-produced software components*. Bell Laboratories.
•	GitHub. (2024). *About GitHub*. https://github.com
•	Atwood, J., & Spolsky, J. (2008). *Stack Overflow*. https://stackoverflow.com
•	Cisco Systems. (2020). *Cisco DevNet: Developer Program Overview*. https://developer.cisco.com

# DEBER2
Nombre: Quinaloa Lindsay, Bastidas Angie
Práctica de laboratorio: Realice el desafío de Python
Este es un ejercicio opcional para probar su conocimiento de los principios básicos de Python. Sin embargo, recomendamos fervientemente que el estudiante complete estos ejercicios para prepararse para el resto de este curso. Si no sabe cómo resolverlos, fíjese en las lecciones de Python disponibles en la carpeta de Materiales del curso/tutoriales y demostraciones.
Responda las preguntas o complete las tareas detalladas a continuación; utilice el método específico descrito, si corresponde.
1) ¿Cuánto es 3 a la potencia de 5?
resultado_potencia = 3 ** 5
print(f"3 a la potencia de 5 es: {resultado_potencia}")
3 a la potencia de 5 es: 243
2) Cree una variable, 's', que contenga la cadena "¡Este curso es increíble!". Con la variable, divida la cadena en una lista.
3) s = "¡Este curso es increíble!"
lista_palabras = s.split()
print(f"La cadena original: '{s}'")
print(f"La cadena dividida en lista: {lista_palabras}")
La cadena original: '¡Este curso es increíble!'
La cadena dividida en lista: ['¡Este', 'curso', 'es', 'increíble!']
3) Dadas las variables altura y montaña, use .format() para imprimir la cadena siguiente:
‘La altura del Monte Everest es de 8848 metros’.
mountain = "Mt. Everest"
height = 8848
print("La altura del {} es de {} metros.".format(mountain, height))
La altura del Mt. Everest es de 8848 metros.
4) Dada la lista anidada siguiente, use la indexación para tomar la palabra '"esto"'.
5) lista_anidada = [1, [2, 'a', 3, ['b', {'clave': 'esto'}, 'c']], 4]

palabra_esto = lista_anidada[1][3][1]['clave']

print(f"Palabra extraída: {palabra_esto}")
Palabra extraída: esto
5) Dado el diccionario anidado siguiente, tome la palabra "eso". Este ejercicio es un poco más difícil.
d = {'key1': [1, 2, 3, {'meta_data': ['A', 'B', {'target': 'eso'}]}]}
palabra_eso = d['key1'][3]['meta_data'][2]['target']
print(f"Palabra extraída: {palabra_eso}")
Palabra extraída: eso
6) ¿Cuál es la diferencia principal entre una tupla y una lista?
Respuesta:La diferencia principal es que las listas son MUTABLES, lo que significa que su contenido se puede cambiar después de crearlas, añadir, eliminar o modificar elementos.
Las tuplas, en cambio, son INMUTABLES, lo que significa que una vez creadas, no se pueden modificar.
Además, las listas se definen con corchetes [] y las tuplas con paréntesis ().
7) Cree una función, GetDomain(), que tome el dominio del sitio web de correo electrónico de una cadena en la forma: 'user@domain.com'.
Por ejemplo, el paso de "user@domain.com" daría: domain.com
def GetDomain(email):
    """
    Extrae el dominio del sitio web de correo electrónico de una cadena.
    Ejemplo: GetDomain('user@domain.com')  -> 'domain.com'
    """
    return email.split('@')[-1]
dominio = GetDomain('user@domain.com')
print(dominio)
domain.com
8) Cree una función básica, findInternet(), que dé una devolución de True si la palabra 'Internet' se incluye en la cadena de entrada. No se preocupe por los casos de perímetro como la puntuación que se asocia con la palabra, pero tenga en cuenta el uso de mayúsculas. (Sugerencia: vea https://docs.python.org/2/reference/expressions.html#in)

def findInternet(text):
    """ Devuelve True si la palabra 'Internet' (sin importar mayúsculas)
    se incluye en la cadena de entrada."""
    return 'internet' in text.lower().split()

resultado_1 = findInternet('The Internet Engineering Task Force was created in 1986')
print(f"Resultado 1: {resultado_1}")
resultado_2 = findInternet('I love the internet!')
print(f"Resultado 2: {resultado_2}")
resultado_3 = findInternet('This is a test sentence.')
print(f"Resultado 3: {resultado_3}")
Resultado 1: True
Resultado 2: False
Resultado 3: False
9) Cree una función, countIoT(), que cuente la cantidad de veces que la palabra "IdT" aparece en una cadena.  Ignore los casos de perímetro pero tenga en cuenta el uso de mayúsculas

def countIoT(st):
    """
    Cuenta la cantidad de veces que la palabra 'IoT' (sin distinguir mayúsculas)
    aparece en la cadena de entrada.
    """
    count = 0

    palabras = st.lower().split()

    for palabra in palabras:
        palabra_limpia = palabra.strip('!,?.\'\"')
        
        if palabra_limpia == 'iot':
            count += 1
    return count


10) Utilice las expresiones lambda y la función filter() para filtrar las palabras de una lista que no comiencen con la letra 'd'. Por ejemplo:
    sec = [“datos”, “sal”, “diario”, “gato”, “perro”]
    debe ser filtrado a:
    ['datos', 'diario']
    seq = ['datos','sal' ,'diario','gato', 'perro']
resultado_filtrado = list(filter(lambda palabra: palabra.lower()[0] == 'd', seq))
print(resultado_filtrado)
['datos', 'diario']

11) Utilice las expresiones lambda y la función map() para convertir una lista de palabras a mayúsculas. Por ejemplo:

sec = [“datos”, “sal”, “diario”, “gato”, “perro”]

debe ser:

[“DATOS”, “SAL”, “DIARIO”, “GATO”, “PERRO”]
seq = ['datos','sal' ,'diario','gato', 'perro']
resultado_mayusculas = list(map(lambda palabra: palabra.upper(), seq))
print(resultado_mayusculas)
['DATOS', 'SAL', 'DIARIO', 'GATO', 'PERRO']

12) Imagine un termostato inteligente conectado a la puerta que pueda detectar, además de la temperatura, el momento en el que las personas entran o salen de la casa.
Escriba una función que, cuando la temperatura sea inferior a 20 ºC y haya personas en la casa (codificado como valor booleano que se envía como parámetro a la función), inicie la calefacción mediante la devolución de la cadena "calefacción encendida". Cuando la temperatura llegue a 23 grados o no haya personas en la casa, la función devuelve la cadena "calefacción apagada". Cuando no se cumpla ninguna de estas condiciones, la función es "No hacer nada".
def simulate_temp_change(current_temp, command):
    """
    Simula el cambio de temperatura basado en el comando del termostato.
    Args:
        current_temp (float): La temperatura actual en ºC.
        command (str): El comando del termostato (e.g., "calefacción encendida").

    Returns:
        float: La nueva temperatura después de un pequeño intervalo de tiempo.
    """
    TASA_CAMBIO = 0.5

    if command == "calefacción encendida":
        new_temp = current_temp + TASA_CAMBIO
        print(f"  -> Calefacción encendida. Subiendo a {new_temp:.1f}ºC")
    elif command == "calefacción apagada":
        new_temp = current_temp - TASA_CAMBIO
        print(f"  -> Calefacción apagada. Bajando a {new_temp:.1f}ºC")
    else: 
        new_temp = current_temp
        print(f"  -> No hacer nada. Temperatura estable en {new_temp:.1f}ºC")

    return new_temp
    def smart_thermostat(temp, people_in):
    """
    Controla la calefacción basándose en la temperatura y la presencia de personas.
    """
    if temp >= 23 or not people_in:
        return "calefacción apagada"

    elif temp < 20 and people_in:
        return "calefacción encendida"

    else:
        return "No hacer nada"

print(smart_thermostat(21, True))
No hacer nada
def smart_thermostat(temp, people_in):
    """
    Controla la calefacción basándose en la temperatura y la presencia de personas.
    """
    if temp >= 23 or not people_in:
        return "calefacción apagada"

    elif temp < 20 and people_in:
        return "calefacción encendida"

    else:
        return "No hacer nada"

print(smart_thermostat(21, False))
calefacción apagada
13) La función zip(list1, list2) devuelve una lista de tuplas, donde la tupla i-th contiene el elemento i-th de cada una de las listas de argumento. Utilice la función zip para crear la siguiente lista de tuplas:
comprimido = [(“Estacionamiento”, -1), (“Negocios”, 0), (“Área de restaurantes”, 1), (“oficinas”, 2)]'

floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floor_numbers = range(-1, 3) 

zipped = list(zip(floor_types, floor_numbers)) 

print(zipped)
[('Estacionamiento', -1), ('Negocios', 0), ('Area de restaurantes', 1), ('Oficinas', 2)]
14) Utilice la función zip y dict() para crear un diccionario, elevator_dict, donde las teclas sean los tipos de piso y los valores sean el número correspondiente del piso, de modo que:
elevator_dict[- 1] = “Estacionamiento”
floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floor_numbers = range(-1, 3) 
zipped_items = zip(floor_numbers, floor_types)

elevator_dict = dict(zipped_items) 

print(elevator_dict)
{-1: 'Estacionamiento', 0: 'Negocios', 1: 'Area de restaurantes', 2: 'Oficinas'}
floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floor_numbers = range(-1, 3) 

# Creación del diccionario (número de piso como clave)
elevator_dict = dict(zip(floor_numbers, floor_types)) 

# Verificación de Code cell 16:
print(elevator_dict[-1])
Estacionamiento
15) Cree una clase de 'Ascensor'. El constructor acepta la lista de cadenas 'floor_types' y la lista de números enteros 'floor_numbers'. La clase implementa los métodos 'ask_which_floor' y 'go_to_floor'. La salida de estos métodos debe verse de la siguiente manera:
`floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas']
floors_numbers = rango(-1,4)

el = Elevador(floor_numbers, floor_types)

el.go_to_floor(1)`

¡Vaya al piso del área de restaurantes!

el.go_to_floor(-2)

En este edificio está el piso número -2.

El.ask_which_floor('Oficinas')

El piso de oficinas es el número: 2

El.ask_which_floor('Piscina')

No hay ningún piso con piscina en este edificio.
class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = list(floor_numbers) 
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        """Pregunta por el número de un piso dado su tipo (e.g., 'Oficinas')."""
        floor_type_es = {'Parking': 'Estacionamiento', 'Shops': 'Negocios', 
                         'Food Court': 'Área de restaurantes', 'Offices': 'Oficinas',
                         'Piscina': 'Piscina'}.get(floor_type, floor_type)
        
        if floor_type in self._type_to_number_dict:
            floor_number = self._type_to_number_dict[floor_type]
            print(f"El piso de {floor_type_es} es el número: {floor_number}")
        else:
            print(f"No hay ningún piso con {floor_type_es.lower()} en este edificio.")
            
    
    def go_to_floor(self, floor_number):
        """Intenta ir a un piso dado su número."""
        if floor_number in self._number_to_type_dict:
            floor_type = self._number_to_type_dict[floor_number]
            floor_type_es = {'Parking': 'Estacionamiento', 'Shops': 'Negocios', 
                             'Food Court': 'Área de restaurantes', 'Offices': 'oficinas'}.get(floor_type, floor_type)
            
            print(f"¡Vaya al piso del {floor_type_es}!")
        else:
            print(f"En este edificio no está el piso número {floor_number}.")
            floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floors_numbers = range(-1, 3) # -1, 0, 1, 2
el = Elevator(floors_numbers, floor_types)
el.go_to_floor(1)
¡Vaya al piso del Area de restaurantes!
floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floors_numbers = range(-1, 3)

el = Elevator(floors_numbers, floor_types)
el.go_to_floor(-2)
En este edificio no está el piso número -2.

class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        """Pregunta por el número de un piso dado su tipo (e.g., 'Oficinas')."""
 
        floor_type_es = {'Parking': 'Estacionamiento', 'Shops': 'Negocios', 
                         'Food Court': 'Área de restaurantes', 'Offices': 'Oficinas',
                         'Piscina': 'Piscina'}.get(floor_type, floor_type)
        
        if floor_type in self._type_to_number_dict:
            floor_number = self._type_to_number_dict[floor_type]
            print(f"El piso de {floor_type_es} es el número: {floor_number}")
        else:
            print(f"No hay ningún piso con {floor_type_es.lower()} en este edificio.")
    def go_to_floor(self, floor_number):
        pass


floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1, 3) # -1, 0, 1, 2

el = Elevator(floors_numbers, floor_types)
el.ask_which_floor('Offices')
El piso de Oficinas es el número: 2
class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        """Pregunta por el número de un piso dado su tipo (e.g., 'Oficinas')."""
        floor_type_es = {'Parking': 'Estacionamiento', 'Shops': 'Negocios', 
                         'Food Court': 'Área de restaurantes', 'Offices': 'Oficinas',
                         'Swimming Pool': 'Piscina'}.get(floor_type, floor_type)
        
        if floor_type in self._type_to_number_dict:
            floor_number = self._type_to_number_dict[floor_type]
            print(f"El piso de {floor_type_es} es el número: {floor_number}")
        else:
            print(f"No hay ningún piso con {floor_type_es.lower()} en este edificio.")
            
    def go_to_floor(self, floor_number):
        pass

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1, 3) # -1, 0, 1, 2

el = Elevator(floors_numbers, floor_types)

el.ask_which_floor('Swimming Pool')
No hay ningún piso con piscina en este edificio.
Excelente trabajo!
# DEBER3
import sys
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM) 
    HARDWARE_DISPONIBLE = True
    print("RPi.GPIO detectado. Preparado para control de hardware.")

except ImportError:
    class MockGPIO:
        BCM = None
        HIGH = 1
        LOW = 0
        def setmode(self, mode):
            pass
        def setup(self, pin, direction):
            print(f"    [SIMULACIÓN] Pin {pin} configurado como Salida.")
        def output(self, pin, state):
            print(f"    [SIMULACIÓN] Pin {pin} cambió a {'HIGH' if state else 'LOW'}.")
        def cleanup(self):
            print("    [SIMULACIÓN] Pines limpiados.")

    GPIO = MockGPIO()
    print("RPi.GPIO no encontrado. Ejecutando en modo de simulación.")
    HARDWARE_DISPONIBLE = False


import time

LED_PIN = 17           

try:
    GPIO.setup(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN, GPIO.LOW)
    
except Exception as e:
    print(f"Error durante la configuración inicial: {e}")
    sys.exit(1) 

def encender_led():
    """Enciende el LED."""
    GPIO.output(LED_PIN, GPIO.HIGH)
    print(" 1) LED encendido")

def apagar_led():
    """Apaga el LED."""
    GPIO.output(LED_PIN, GPIO.LOW)
    print(" 2) LED apagado")

def blink_led(veces=3, intervalo=0.5):
    """Hace parpadear el LED."""
    print(" 3) Iniciando Blink (3 veces)...")
    for _ in range(veces):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(intervalo)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(intervalo)
    print("Parpadeo completado.")

try:
    while True:
        print("\n=== MENÚ LED (Simulado) ===")
        print("1) Encender LED")
        print("2) Apagar LED")
        print("3) Blink LED (3 veces)")
        print("4) Salir")
        print(20 * "=")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            encender_led()
        elif opcion == "2":
            apagar_led()
        elif opcion == "3":
            blink_led()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print(" Opción no válida")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print("Pines GPIO limpiados correctamente.")
    RPi.GPIO no encontrado. Ejecutando en modo de simulación.
    [SIMULACIÓN] Pin 17 configurado como Salida.
    [SIMULACIÓN] Pin 17 cambió a LOW.

=== MENÚ LED (Simulado) ===
1) Encender LED
2) Apagar LED
3) Blink LED (3 veces)
4) Salir
====================
    [SIMULACIÓN] Pin 17 cambió a LOW.
 2) LED apagado

=== MENÚ LED (Simulado) ===
1) Encender LED
2) Apagar LED
3) Blink LED (3 veces)
4) Salir
====================
 3) Iniciando Blink (3 veces)...
    [SIMULACIÓN] Pin 17 cambió a HIGH.
    [SIMULACIÓN] Pin 17 cambió a LOW.
    [SIMULACIÓN] Pin 17 cambió a HIGH.
    [SIMULACIÓN] Pin 17 cambió a LOW.
    [SIMULACIÓN] Pin 17 cambió a HIGH.
    [SIMULACIÓN] Pin 17 cambió a LOW.
Parpadeo completado.

=== MENÚ LED (Simulado) ===
1) Encender LED
2) Apagar LED
3) Blink LED (3 veces)
4) Salir
====================
Saliendo del programa...
    [SIMULACIÓN] Pines limpiados.
Pines GPIO limpiados correctamente.

# DEBER4
class MiClase:
    pass

obj1 = MiClase()

class Robot:
    def __init__(self, nombre, tipo, tarea):
        self.nombre = nombre
        self.tipo = tipo
        self.tarea = tarea

    def adelante():
        pass

    def atras():
        pass

    def giroiz():
        pass

    def girode():
        pass

        class Miclase2:
    pass
obj1= Miclase2()

class Arbol:
    def __init__(self, especie, altura, tipo_hoja, edad):
        self.especie = especie
        self.altura = altura
        self.tipo_hoja = tipo_hoja
        self.edad = edad
    def crecer(self, altura_ganada):
        pass

    def realizar_fotosintesis():
        pass

    def producir_fruta():
        pass
    def florecer():
        pass
class Miclase3:
   pass
obj1= Miclase3()

class IA:
    def __init__(self, modelo, dataset, funcion_objetivo, parametros):
        self.modelo = modelo
        self.dataset = dataset
        self.funcion_objetivo = funcion_objetivo
        self.parametros = parametros

    def entrenar(self):
        pass

    def aprender_de_errores():
        pass

    def predecir(nuevos_datos):
        pass

    def clasificar(entrada):
        pass
        class Miclase4:
    pass
obj1=Miclase4()

class IoT:

    def __init__(self, id_dispositivo, protocolo_comunicacion, ubicacion, tipo_dispositivo):
        self.id_dispositivo = id_dispositivo
        self.protocolo_comunicacion = protocolo_comunicacion
        self.ubicacion = ubicacion
        self.estado_actual = "Inactivo"
        self.tipo_dispositivo = tipo_dispositivo
    def capturar_datos(tipo_sensor):
        pass

    def enviar_datos(plataforma_destino):
        pass

    def recibir_comando(comando):
        pass

    def activar_actuador(accion):
        pass
        class Miclase5:
    pass
obj1= Miclase5()

class NavegadorWeb:

    def __init__(self, motor_renderizado, url_actual, modo_privacidad=False):
        self.motor_renderizado = motor_renderizado
        self.url_actual = url_actual
        self.historial = []  
        self.cookies = {}     
        self.modo_privacidad = modo_privacidad
    def interpretar_HTML_CSS():
        pass

    def renderizar_contenido():
        pass
        
    def gestionar_pestañas(accion):
        pass
        
    def limpiar_datos_navegacion():
        pass
        class Miclase6:
    pass
ob1=Miclase6()

class ComputadoraPersonal:

    def __init__(self, cpu, ram, almacenamiento, sistema_operativo, tipo_pc, estado_encendido=False):
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.sistema_operativo = sistema_operativo
        self.tipo_pc = tipo_pc
        self.estado_encendido = estado_encendido
        self.ip_conectada = None 
    def iniciar_sistema():
        pass

    def gestionar_memoria(proceso):
        pass

    def conectar_a_red(ip):
        pass
        
    def procesar_datos(input):
        pass
        
    def apagar_sistema():
        pass
        class Miclase7:
    pass
obj1=Miclase7()

class Telefono:

    def __init__(self, tipo, sistema_operativo, imei, numero_telefono, conectividad="Wi-Fi"):
        self.tipo = tipo
        self.sistema_operativo = sistema_operativo
        self.imei = imei
        self.numero_telefono = numero_telefono
        self.conectividad = conectividad
        self.ubicacion_gps = None
        self.bateria_cargada = 0 

    def realizar_llamada(numero):
        pass

    def capturar_fotografia():
        pass

    def instalar_aplicacion(app_store):
        pass
        
    def cargar_bateria():
        pass
        class Miclase8:
    pass
ob1=Miclase8()

class Cine:
    
    def __init__(self, titulo, duracion, director, formato, clasificacion="Exhibición"):
        self.titulo = titulo
        self.duracion = duracion  
        self.director = director
        self.formato = formato   
        self.clasificacion = clasificacion 
        self.entradas_vendidas = 0 

    def grabar_metraje():
        pass

    def editar_sonido():
        pass

    def proyectar_pelicula():
        pass

    def vender_entradas():
        pass
        class Miclase9:
    pass
obj1=Miclase9()

class RedSocial:
    
    def __init__(self, nombre, tipo_contenido_principal, algoritmo_feed, clasificacion):
        self.nombre = nombre
        self.tipo_contenido_principal = tipo_contenido_principal
        self.algoritmo_feed = algoritmo_feed
        self.clasificacion = clasificacion
        self.base_datos_usuarios = 0 

    def crear_cuenta(datos_usuario):
        pass

    def publicar_contenido(archivo, texto):
        pass

    def enviar_mensaje(destinatario):
        pass
        
    def generar_notificacion():
        pass

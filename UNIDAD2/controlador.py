# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:33:21 2025

@author: ESTUDIANTE
"""

# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
from modelo import RobotConstructor, RobotMedico, RobotExplorador
from vista import TelegramView
import RPi.GPIO as GPIO

class Controlador:
    def __init__(self, bot):
        self.bot = bot
        self.vista = TelegramView()

        self.constructor = RobotConstructor("Constructor")
        self.medico = RobotMedico("Medico")
        self.explorador = RobotExplorador("Explorador")

    def manejar_mensaje(self, msg):
        chat_id = msg["chat"]["id"]
        comando = msg.get("text", "")

        if comando == "start":
            self.vista.enviar(self.bot, chat_id, self.vista.menu_principal())

        elif comando == "constructor_on":
            self.vista.enviar(self.bot, chat_id, self.constructor.encender())

        elif comando == "constructor_off":
            self.vista.enviar(self.bot, chat_id, self.constructor.apagar())

        elif comando == "medico_temp":
            self.vista.enviar(self.bot, chat_id, self.medico.medir_temperatura())

        elif comando == "medico_hum":
            self.vista.enviar(self.bot, chat_id, self.medico.medir_humedad())

        elif comando == "explorar":
            self.vista.enviar(self.bot, chat_id, " Presiona el botón para comenzar la exploración...")
            resultado = self.explorador.explorar()
            self.vista.enviar(self.bot, chat_id, resultado)

        elif comando == "estado":
            self.vista.enviar(self.bot, chat_id, " Sistema funcionando correctamente.")

        elif comando == "salir":
            GPIO.cleanup()
            self.vista.enviar(self.bot, chat_id, " Sistema apagado.")

        else:
            self.vista.enviar(self.bot, chat_id, " Comando no reconocido.")


# === PROGRAMA PRINCIPAL ===
TOKEN = "8513640504:AAGJAzWpp5K6Ec8uw_4K8Nvyw9EjgEK5E1g"
bot = telepot.Bot(TOKEN)
controlador = Controlador(bot)

MessageLoop(bot, controlador.manejar_mensaje).run_as_thread()

print(" Bot Telegram activo...")

while True:
    time.sleep(10)

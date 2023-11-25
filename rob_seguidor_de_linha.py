from machine import Pin, PWM, ADC
import time

SensorTras = 7
SensorDir = 5
SensorMei = 4
SensorEsq = 3
SensorDirDir = 6
SensorEsqEsq = 2

in1 = 13
in2 = 12
in4 = 8
in3 = 9

velA = 11
velB = 10

pinPot1 = 0  # A0
pinPot2 = 1  # A1

# Configuração dos pinos
sensor_dir = Pin(SensorDir, Pin.IN)
sensor_mei = Pin(SensorMei, Pin.IN)
sensor_esq = Pin(SensorEsq, Pin.IN)
sensor_tras = Pin(SensorTras, Pin.IN)
sensor_esq_esq = Pin(SensorEsqEsq, Pin.IN)
sensor_dir_dir = Pin(SensorDirDir, Pin.IN)

motor_in1 = Pin(in1, Pin.OUT)
motor_in2 = Pin(in2, Pin.OUT)
motor_in3 = Pin(in3, Pin.OUT)
motor_in4 = Pin(in4, Pin.OUT)

motor_velA = PWM(Pin(velA), freq=1000, duty=0)
motor_velB = PWM(Pin(velB), freq=1000, duty=0)

pot1 = ADC(Pin(pinPot1))
pot2 = ADC(Pin(pinPot2))

def frente():
    vel1 = pot1.read()
    motor_in1.value(0)
    motor_in2.value(1)
    motor_velA.duty(vel1)
    motor_in3.value(1)
    motor_in4.value(0)
    motor_velB.duty(vel1)

def para():
    motor_in1.value(0)
    motor_in2.value(0)
    motor_in3.value(0)
    motor_in4.value(0)

def vira_direita():
    vel1 = pot1.read()
    motor_in1.value(0)
    motor_in2.value(1)
    motor_in3.value(0)
    motor_in4.value(0)
    motor_velB.duty(vel1)

def vira_esquerda():
    vel = pot1.read()
    motor_in1.value(0)
    motor_in2.value(0)
    motor_in3.value(1)
    motor_in4.value(0)
    motor_velA.duty(vel)

# Configuração inicial
motor_velA.duty(0)
motor_velB.duty(0)

while True:
    estado_sensor_mei = sensor_mei.value()
    estado_sensor_dir = sensor_dir.value()
    estado_sensor_esq = sensor_esq.value()
    estado_sensor_esq_esq = sensor_esq_esq.value()
    estado_sensor_dir_dir = sensor_dir_dir.value()
    estado_sensor_tras = sensor_tras.value()

    if (estado_sensor_mei == 1 and estado_sensor_dir == 0 and estado_sensor_esq == 0) or \
       (estado_sensor_mei == 1 and estado_sensor_dir == 1 and estado_sensor_esq == 1):
        frente()

    if (estado_sensor_mei == 1 and estado_sensor_dir == 1 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 0) or \
       (estado_sensor_mei == 1 and estado_sensor_dir == 1 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 1) or \
       (estado_sensor_mei == 1 and estado_sensor_dir == 0 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 0 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 1 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 1 and estado_sensor_esq == 0 and estado_sensor_dir_dir == 0):
        vira_esquerda()

    if (estado_sensor_mei == 1 and estado_sensor_dir == 0 and estado_sensor_esq == 1 and estado_sensor_esq_esq == 0) or \
       (estado_sensor_mei == 1 and estado_sensor_dir == 0 and estado_sensor_esq == 1 and estado_sensor_esq_esq == 1) or \
       (estado_sensor_mei == 1 and estado_sensor_dir == 0 and estado_sensor_esq == 0 and estado_sensor_esq_esq == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 0 and estado_sensor_esq == 1 and estado_sensor_esq_esq == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 0 and estado_sensor_esq == 0 and estado_sensor_esq_esq == 1) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 0 and estado_sensor_esq == 1 and estado_sensor_esq_esq == 0):
        vira_direita()

    if (estado_sensor_mei == 0 and estado_sensor_dir == 0 and estado_sensor_esq == 0) or \
       (estado_sensor_mei == 0 and estado_sensor_dir == 1 and estado_sensor_esq == 1):
        if estado_sensor_tras == 1:
            frente()
        else:
            para()

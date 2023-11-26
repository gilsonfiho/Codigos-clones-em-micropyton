from machine import Pin, PWM, ADC, Servo
import time

# Configuração dos pinos
echo_pin = 34
trig_pin = 32
servo_pin = 12
ldr_pin = 36
led1_pin = 26
led2_pin = 27
buzzer_pin = 25
in1_pin = 15
in2_pin = 2
in3_pin = 4
in4_pin = 16
speed_a_pin = 14
speed_b_pin = 13

# Inicializando os objetos
servo_motor = Servo(servo_pin)
ultrasonic_trig = Pin(trig_pin, Pin.OUT)
ultrasonic_echo = Pin(echo_pin, Pin.IN)
ldr = ADC(Pin(ldr_pin))
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
buzzer = Pin(buzzer_pin, Pin.OUT)
in1 = Pin(in1_pin, Pin.OUT)
in2 = Pin(in2_pin, Pin.OUT)
in3 = Pin(in3_pin, Pin.OUT)
in4 = Pin(in4_pin, Pin.OUT)
speed_a = PWM(Pin(speed_a_pin), freq=1000, duty=0)
speed_b = PWM(Pin(speed_b_pin), freq=1000, duty=0)

# Função para medir a distância do obstáculo
def ultrasonic():
    ultrasonic_trig.value(0)
    time.sleep_us(2)
    ultrasonic_trig.value(1)
    time.sleep_us(10)
    ultrasonic_trig.value(0)
    while ultrasonic_echo.value() == 0:
        pass
    pulse_start = time.ticks_us()
    while ultrasonic_echo.value() == 1:
        pass
    pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 0.0343) / 2
    return distance

# Função para controle do farol
def controlar_farol():
    pLdr = ldr.read()
    if pLdr > 880:
        led1.value(1)
        led2.value(1)
    else:
        led1.value(0)
        led2.value(0)

# Funções de controle do motor
def motor_frente():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)
    speed_a.duty(1000)
    speed_b.duty(1000)

def motor_re():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    speed_a.duty(1000)
    speed_b.duty(1000)

def motor_direita():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    speed_a.duty(1000)
    speed_b.duty(1000)

def motor_esquerda():
    in1.value(0)
    in2.value(1)
    in3.value(1)
    in4.value(0)
    speed_a.duty(1000)
    speed_b.duty(1000)

def motor_para():
    speed_a.duty(0)
    speed_b.duty(0)

# Função principal
def main():
    servo_motor.write_angle(90)
    while True:
        motor_frente()
        time.sleep_ms(100)
        distancia = ultrasonic()
        print(distancia)
        time.sleep_ms(10)
        controlar_farol()

        if distancia <= 7:
            buzzer.value(1)
            motor_re()
            time.sleep_ms(350)
            buzzer.value(0)
            motor_para()
            servo_motor.write_angle(0)
            time.sleep_ms(300)
            distancia = ultrasonic()
            time.sleep_ms(50)
            print(distancia)
            time.sleep_ms(10)
            servo_motor.write_angle(180)
            time.sleep_ms(300)
            distancia1 = ultrasonic()
            time.sleep_ms(50)
            print(distancia1)
            time.sleep_ms(10)

            if distancia <= distancia1:
                motor_direita()
                time.sleep_ms(500)
            else:
                motor_esquerda()
                time.sleep_ms(500)

# Executando o programa principal
main()

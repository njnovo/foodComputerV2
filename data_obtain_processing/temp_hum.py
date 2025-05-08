import RPi.GPIO as GPIO
import dht11


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

fc_1_pin = 21
fc_1_pin = 22
fc_1_pin = 23



def get_hum(fc):
    match fc:
        case 1:
            instance = dht11.DHT11(pin = fc_1_pin)
            result = instance.read()
                if result.is_valid():                    
                    return result.humidity
                else:
                    return result.error_code
        case 2:
            instance = dht11.DHT11(pin = fc_2_pin)
            result = instance.read()
                if result.is_valid():                   
                    return result.humidity
                else:
                    return result.error_code
        case 3:
            instance = dht11.DHT11(pin = fc_3_pin)
            result = instance.read()
                if result.is_valid():                    
                    return result.humidity
                else:
                    return result.error_code

def get_temp(fc):
    match fc:
        case 1:
            instance = dht11.DHT11(pin = fc_1_pin)
            result = instance.read()
                if result.is_valid():
                    return ((9/5)*result.temperature)+32
                else:
                    return result.error_code
        case 2:
            instance = dht11.DHT11(pin = fc_2_pin)
            result = instance.read()
                if result.is_valid():
                    return ((9/5)*result.temperature)+32
                else:
                    return result.error_code
        case 3:
            instance = dht11.DHT11(pin = fc_3_pin)
            result = instance.read()
                if result.is_valid():    
                    return ((9/5)*result.temperature)+32
                else:
                    return result.error_code
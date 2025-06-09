# control_temperature.py

import time
import subprocess
from pid_controller import PID # Assuming pid_controller.py is in the same directory
from temp_hum import get_temp
# --- Configuration ---
SET_POINT_TEMP = 77.0  # Desired temperature in Fahrenheit
KP = 0.5               # Proportional gain
KI = 0.1               # Integral gain
KD = 0.05              # Derivative gain
UPDATE_INTERVAL_SECONDS = 20 # How often to check temperature and update control

# Define deadband for stable operation (optional, but recommended)
# This prevents rapid switching of fan/heater when temperature is very close to setpoint
DEADBAND_TEMP_TOLERANCE = 0.5 # +/- 0.5 degrees Celsius around setpoint

# --- Actuator Control Functions ---
def run_script(script_name):
    """Executes an external Python script."""
    try:
        # Use python3 to execute the script
        result = subprocess.run(['python3', script_name], capture_output=True, text=True, check=True)
        print(f"Executed {script_name}. Output: {result.stdout.strip()}")
        if result.stderr:
            print(f"Errors from {script_name}: {result.stderr.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")
        print(f"Stderr: {e.stderr.strip()}")
    except FileNotFoundError:
        print(f"Error: python3 command not found. Ensure python3 is in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred while running {script_name}: {e}")

def fan_on():
    run_script('fan_on.py')

def fan_off():
    run_script('fan_off.py')

def heater_on():
    run_script('heater_on.py')

def heater_off():
    run_script('heater_off.py')


# --- Main Control Loop ---
def main():
    pid = PID(KP, KI, KD, SET_POINT_TEMP)
    print(f"Starting PID temperature control. Setpoint: {SET_POINT_TEMP}°C")
    print(f"Kp={KP}, Ki={KI}, Kd={KD}")

    # Initial state: ensure everything is off
    fan_off()
    heater_off()
    current_heater_state = False
    current_fan_state = False

    try:
        while True:
            current_time = time.time()
            current_temp = get_temp()

            if current_temp is None:
                print("Could not read temperature. Skipping this cycle.")
                time.sleep(UPDATE_INTERVAL_SECONDS)
                continue

            # Calculate PID output
            pid_output = pid.update(current_temp, current_time)
            print(f"\nTime: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))}")
            print(f"Current Temp: {current_temp:.2f}°C, Setpoint: {SET_POINT_TEMP}°C")
            print(f"PID Output: {pid_output:.2f}")

            # Control logic based on PID output
            # Positive PID output means temperature is too low (need heat)
            # Negative PID output means temperature is too high (need cooling)

            if abs(current_temp - SET_POINT_TEMP) <= DEADBAND_TEMP_TOLERANCE:
                # Within deadband, turn everything off for stability
                if current_heater_state:
                    heater_off()
                    current_heater_state = False
                if current_fan_state:
                    fan_off()
                    current_fan_state = False
                print("Temperature within deadband. Fan and Heater OFF.")
            elif pid_output > 0:  # Temperature is too low, need to heat
                if current_fan_state: # If fan was on, turn it off first
                    fan_off()
                    current_fan_state = False
                if not current_heater_state:
                    heater_on()
                    current_heater_state = True
                print("Temperature too low. Heater ON.")
            elif pid_output < 0:  # Temperature is too high, need to cool
                if current_heater_state: # If heater was on, turn it off first
                    heater_off()
                    current_heater_state = False
                if not current_fan_state:
                    fan_on()
                    current_fan_state = True
                print("Temperature too high. Fan ON.")

            time.sleep(UPDATE_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nExiting temperature control. Turning off all actuators.")
        fan_off()
        heater_off()
    finally:
        # Ensure actuators are off when the script exits
        fan_off()
        heater_off()

if __name__ == "__main__":
    main()
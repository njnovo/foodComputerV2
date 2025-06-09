import threading
import control_temperature
import run_data_entry

thread1 = threading.Thread(target=control_temperature.main)
thread2 = threading.Thread(target=run_data_entry.main)

thread1.start()
thread2.start()
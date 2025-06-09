# pid_controller.py

class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.last_error = 0
        self.last_time = None

    def update(self, current_value, current_time):
        if self.last_time is None:
            self.last_time = current_time
            return 0  # No control action on the very first call

        dt = current_time - self.last_time
        if dt == 0:
            return 0 # Avoid division by zero if time hasn't advanced

        error = self.setpoint - current_value

        # Proportional term
        P = self.Kp * error

        # Integral term
        self.integral += error * dt
        I = self.Ki * self.integral

        # Derivative term
        derivative = (error - self.last_error) / dt
        D = self.Kd * derivative

        # Store values for the next iteration
        self.last_error = error
        self.last_time = current_time

        # PID output
        output = P + I + D
        return output

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
        self.reset() # Reset integral and last_error when setpoint changes

    def reset(self):
        self.integral = 0
        self.last_error = 0
        self.last_time = None
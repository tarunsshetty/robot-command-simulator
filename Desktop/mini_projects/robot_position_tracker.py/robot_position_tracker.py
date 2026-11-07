import random
import matplotlib.pyplot as plt

random.seed(7)  # same noise every run, change it to get new data

steps = 60
speed = 1.0            # robot moves 1 unit per step
sensor_std = 4.0       # how noisy the sensor is
sensor_var = sensor_std ** 2
process_var = 0.1      # small uncertainty in the robot's own motion

true_pos = 0.0
estimate = 0.0         # our starting guess
error = 10.0           # how unsure we are at the start

true_list = []
sensor_list = []
est_list = []

for t in range(steps):
    # the robot actually moves
    true_pos += speed

    # the sensor gives a noisy reading of where it is
    reading = true_pos + random.gauss(0, sensor_std)

    # step 1: predict where the robot should be now
    estimate = estimate + speed
    error = error + process_var

    # step 2: correct the prediction using the sensor reading
    gain = error / (error + sensor_var)
    estimate = estimate + gain * (reading - estimate)
    error = (1 - gain) * error

    true_list.append(true_pos)
    sensor_list.append(reading)
    est_list.append(estimate)

# how far off was each one, on average?
sensor_err = sum(abs(s - t) for s, t in zip(sensor_list, true_list)) / steps
filter_err = sum(abs(e - t) for e, t in zip(est_list, true_list)) / steps
print("Average sensor error:", round(sensor_err, 2))
print("Average filter error:", round(filter_err, 2))

plt.plot(true_list, label="True position", color="green")
plt.scatter(range(steps), sensor_list, label="Noisy sensor", color="red", s=10)
plt.plot(est_list, label="Kalman estimate", color="blue")
plt.xlabel("Time step")
plt.ylabel("Position")
plt.title("Kalman filter on a noisy distance sensor")
plt.legend()
plt.show()
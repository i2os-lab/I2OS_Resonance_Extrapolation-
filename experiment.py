import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def f(x):
    return np.sin(x) + 0.3 * np.sin(3 * x)

x_train = np.linspace(0, 6, 40).reshape(-1, 1)
y_train = f(x_train).ravel()

x_test = np.linspace(6, 10, 80).reshape(-1, 1)
y_test = f(x_test).ravel()

x_all = np.linspace(0, 10, 300).reshape(-1, 1)
y_all = f(x_all).ravel()

baseline = LinearRegression()
baseline.fit(x_train, y_train)
y_base_test = baseline.predict(x_test)
y_base_all = baseline.predict(x_all)

def phi(x):
    return np.hstack([
        np.sin(x),
        np.cos(x),
        np.sin(2*x),
        np.cos(2*x),
        np.sin(3*x),
        np.cos(3*x),
    ])

model = LinearRegression()
model.fit(phi(x_train), y_train)

y_res_test = model.predict(phi(x_test))
y_res_all = model.predict(phi(x_all))

err_base = (y_test - y_base_test) ** 2
err_res = (y_test - y_res_test) ** 2

mse_base = mean_squared_error(y_test, y_base_test)
mse_res = mean_squared_error(y_test, y_res_test)

print("Baseline:", mse_base)
print("Resonance:", mse_res)

plt.figure()
plt.plot(x_all, y_all)
plt.plot(x_all, y_base_all, "--")
plt.plot(x_all, y_res_all)
plt.axvline(6)
plt.savefig("figure1.png")

plt.figure()
plt.plot(x_test, err_base, "--")
plt.plot(x_test, err_res)
plt.savefig("figure2.png")

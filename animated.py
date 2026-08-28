import matplotlib.pyplot as plt
import numpy as np

plt.ion()

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(0, 0.45)
ax.set_ylim(0, 0.22)
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Vertical distance (m)")

plot_objects = ax.plot([], [], "ro", markersize=10)
dot = plot_objects[0]


for angle in np.linspace(0, 89.9, num=10):  
    rad = np.radians(angle)

    tf = (2 * 2 * np.sin(rad)) / 10
    t_steps = np.linspace(0, tf, num=40)  

    for t in t_steps:
        x = 2 * np.cos(rad) * t
        y = 2 * np.sin(rad) * t - 0.5 * 10 * (t**2)

        dot.set_data([x], [y])
        ax.set_title(f"Launch Angle: {angle:.1f}° | Time: {t:.2f}s")

        plt.pause(0.01)

plt.ioff()
plt.show()

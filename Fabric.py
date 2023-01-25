import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_fabric():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    fabric = f.generate()
    # Add noise to the fractal shape to make it look more like fabric
    noise = np.random.normal(0, 0.05, fabric.shape)
    fabric = fabric + noise
    fabric = np.clip(fabric, 0, 1)
    # Apply a fabric-like color map to the fractal shape
    fabric = plt.cm.autumn(fabric)
    # Return the fractal fabric
    return fabric

# Generate 10 fractal fabric images
for i in range(10):
    fabric = generate_fractal_fabric()
    plt.imsave("fractal_fabric_{}.png".format(i), fabric)

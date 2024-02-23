//modeling exponential growth.

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
growth_rate = 0.05  # Growth rate (e.g., 5% growth)
initial_population = 100  # Initial population
time_period = 20  # Time period (in years)

# Define the time range
time = np.arange(0, time_period + 1)

# Calculate the population using the exponential growth formula
population = initial_population * np.exp(growth_rate * time)

# Plot the results
plt.plot(time, population, marker='o', linestyle='-')
plt.title('Exponential Growth Model')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.grid(True)
plt.show()

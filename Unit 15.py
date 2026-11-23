"""
        KennedY Walker
        This program is to create a SIN graph
        Date: 11.22.2026  """
import matplotlib.pyplot as plt
import math

 # Creating list for x and y
x = []
y = []
 
 #a sine function
for i in range(0, 361):  # degrees from 0 to 360
     x.append(i)
     y.append(math.sin(math.radians(i)))
 
 # Plot the data
plt.plot(
     x,
     y,
     color="red",      
     linestyle="--",    
     linewidth=2        
     )
 
 # Add title and labels
plt.title("Sine Wave (y = sin(x))")
plt.xlabel("Angle (degrees)")
plt.ylabel("Sine Value")
 
 # Add grid
plt.grid(True)
 
 # Save the plot to a file
plt.savefig("my_plot.png")
 
 # Show the plot
plt.show()
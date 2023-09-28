"""
To calculate the variance, i need to compute the squared differences between each 
color count and the mean count. Then, take the average of these squared differences. 

The formula for variance is the sum of (count - mean)^2 divided by the number of colors.
"""
# import the mean_color, all_colors from the mean module
from mean import mean_color, all_colors
 
# # Calculate the squared differences between each color and the mean color
squared_differences = [(color != mean_color) for color in all_colors]

# Calculate the variance as the average of squared differences
variance = sum(squared_differences) / len(squared_differences)

print(f"The variance of colors worn throughout the week is: {variance}")
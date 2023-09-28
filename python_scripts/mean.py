from collections import Counter

"""Define the colors worn on each day"""
colors_by_day = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

"""Create a list of all colors using list comprehension"""
all_colors = [color.strip() for colors in colors_by_day.values() for color in colors.split(",")]

""" Count occurrences of each color """
color_counts = Counter(all_colors)
print(color_counts)

"""
Calculate the mean color we can implement the mean formula

Mean = (Sum of all the observations/Total number of observations)
where Total number of observations = 'total_count' and 
Sum of all the observations = 'color_counts'

"""
total_count = len(all_colors)
mean_color = max(color_counts, key=lambda color: color_counts[color] / total_count)

print("Mean Color:", mean_color)

"""
To find the color that is most worn throughout the week, 
i iterate through the days and colors and keep a count of each color. 
Then, i determine which color that has the highest count.
"""

colors_by_day = {
    'MONDAY': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'TUESDAY': 'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE',
    'WEDNESDAY': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE',
    'THURSDAY': 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'FRIDAY': 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'
}
"""empty dictionary that store th color count"""
color_counts = {}

"""Iterate through the days and colors"""
for day, colors in colors_by_day.items():
    """Split the colors by comma and remove the leading and trailing white spaces"""
    color_list = [color.strip() for color in colors.split(',')]
    
    """Count the colors for the current day"""
    for color in color_list:

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

"""Find the most worn color"""
most_worn = max(color_counts, key=color_counts.get)

print(f"The most worn color is: {most_worn}")

"""
To find the median color, first, i created a sorted list of colors based on their frequencies. 
Then, i find the middle color in the sorted list. 
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
        # print(color_counts)
"""sort colors by their counts in descending order"""
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

"""median color(s) (middle color(s) in the sorted list)"""
total_colors = len(sorted_colors)
median_colors = []

if total_colors % 2 == 1:  # Odd number of colors
    median_index = total_colors // 2
    median_colors.append(sorted_colors[median_index][0])
else:  # Even number of colors
    median_index_1 = total_colors // 2 - 1
    median_index_2 = total_colors // 2
    median_colors.extend([sorted_colors[median_index_1][0], sorted_colors[median_index_2][0]])
    print(median_colors)

print(f"The median color(s) worn is/are: {', '.join(median_colors)}")
# Sample sequence of colors
colors = "0101101011101011011101101000111"

"""Count the occurrences of '111' in the sequence (1s that appear 3 times)"""
pattern_count = colors.count('111')

"""Calculate the total number of occurrences of '1'"""
total_ones_count = colors.count('1')

"""Calculate the probability of choosing red (getting '111')"""
probability_red = pattern_count / total_ones_count

# result
print(f"The probability of choosing red is: {probability_red:.2%}")

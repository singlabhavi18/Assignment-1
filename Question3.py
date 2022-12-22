seconds = int(input("Enter the number of seconds to be converted: "))
conv_mins = seconds // 60
conv_seconds = seconds % 60
print("There are", conv_mins, "minutes and", conv_seconds, "seconds in", seconds, "seconds.")
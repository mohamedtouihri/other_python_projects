seconds = int(input("Entrer the duration in second:\n"))
hours = seconds // 3600
minutes = seconds % 3600 // 60
remaining_seconds = seconds % 60
print(f"The duration is : {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")


# // : Floor division
# % : Modulo operator
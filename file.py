try:
    file = open("sample.txt", "r")        # Open the file in read mode
    lines = file.readlines()              # Read all lines

    for line in lines:                    # Print each line as-is
        print(line)

    file.close()                          # Close the file after reading

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)

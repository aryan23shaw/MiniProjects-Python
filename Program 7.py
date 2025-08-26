with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        if 'a' not in line.lower():
            outfile.write(line)

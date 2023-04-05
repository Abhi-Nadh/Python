with open("files.txt") as file1,open("Sports.txt") as file2:
    for line1,line2 in zip(file1,file2):
        print(line1+line2)
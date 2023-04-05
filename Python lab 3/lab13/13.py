with open('files.txt','r') as firstfile, open('Sports.txt','w') as secondfile:
    for name in firstfile:
        secondfile.write(name)
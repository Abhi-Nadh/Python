def lastNline(fname,N):
    with open(fname) as file:
        for line in (file.readlines()[-N:]):
            print(line,end='')
if __name__ == '__main__':
    fname='files.txt'
    N=int(input("No of N line to read:"))
    try:
        lastNline(fname,N)
    except:
        print("File Not Found")    
                
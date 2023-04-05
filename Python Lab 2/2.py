data=input("Enter the String: ")
check={}
for x in data:
    keys=check.keys()
    if x in keys:
        check[x]=check[x]+1
    else:
        check[x]=1
print(check)
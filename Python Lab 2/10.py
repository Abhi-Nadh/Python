data=('apple','orange','banana','grapse','kiwi')
revdata=()
for rev in data:
    revdata=(rev,)+revdata
print(revdata)


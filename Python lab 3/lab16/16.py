def remove_newlines(fname):
    flist = open(fname).readlines()
    return [name.rstrip('\n') for name in flist]

print(remove_newlines("files.txt"))

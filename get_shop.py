my_file = open("url.txt", "r")
data = my_file.read()
ls = data.split("\n")
my_file.close()

lss = list(set(ls))
for item in lss:
    print(item)
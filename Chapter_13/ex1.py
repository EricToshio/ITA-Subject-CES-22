#open old file
old_file = open("old_file.txt", "r")
#get all texts
read_all = old_file.readlines()
#close old file
old_file.close()

#reverse all
read_all.reverse()
write_all = []
for line in read_all:
    write_all += line[-2::-1] + "\n"

#write
new_file = open("new_file.txt", "w")
new_file.writelines(write_all)
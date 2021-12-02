lines_data = ['Shivam\n', 'Gaurav\n', 'Kite\n']

with open('data_folder/write_file.txt', 'a') as f:
	f.write('Anuj\n') #string
	f.writelines(lines_data)#sequence

























# with open('data_folder/data.txt') as f: (does not require closing file)
# 	# for line in f:
# 	# 	print(line)

# 	f.seek(20) move the cursor
# 	print(f.read(10)) reads whole file if no argument , if argument then starting 10 characters
#f=open('data_folder/data.txt')
#print(f.readline()) reads the file 
# dummy data has end as \n























# f = open('data_folder/data.txt', 'r')

# for line in f:

# 	print(line)


# a = []
# a[4]

# # print(f.readline())
# # print(f.readline())
# # print(f.readline())

# f.close()
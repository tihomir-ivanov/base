import os 
 
# define the path to the folder where you want to create the file 
folder_path = 'C://Users//Tihomir Ivanov//Desktop//TestStudioProject' 
 
# create the folder if it doesn't exist 
if not os.path.exists(folder_path): 
    os.makedirs(folder_path) 
 
# define the file name and path 
file_name = 'example.txt' 
file_path = os.path.join(folder_path, file_name) 
 
# create the file 
with open(file_path, 'w') as f: 
    f.write('This is an example file.') 

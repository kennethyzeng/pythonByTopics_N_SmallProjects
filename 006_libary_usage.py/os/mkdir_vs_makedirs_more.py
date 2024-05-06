"""
By using os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.
 This method raises FileExistsError if the directory to be created already exists.

 os.makedirs() method in Python is used to create a directory recursively. That means 
 while making leaf directory if any intermediate-level directory is missing, 
 os.makedirs() method will create them all.

mode 0o666     => the file permission set  6 is rw; octual
 
  os.listdir() method in Python is used to get the list of all files and directories in the specified directory. 

  #remove file 
  os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. 
  If the specified path is a directory then OSError will be raised by the method.

  #remove empty direcotry 
  os.rmdir() method in Python is used to remove or delete an empty directory. 
  OSError will be raised if the specified path is not an empty directory

  ##change file name 
  A file old.txt can be renamed to new.txt, using the function os.rename(). 
  The name of the file changes only if, the file exists and the user has sufficient 
  privilege permission to change the file.

  ##get file size 
   os.path.getsize() function, python will give us the size of the file in bytes. 
   To use this method we need to pass the name of the file as a parameter.

####get os operation
os.name
"""
import os
directory = "GeeksforGeeks"
parent_dir = "D:/Pycharm projects/"
path = os.path.join(parent_dir, directory)    ####

os.mkdir(path)         ####
print("Directory '% s' created" % directory)
directory = "Geeks"
parent_dir = "D:/Pycharm projects"
mode = 0o666        ####
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)        ###
print("Directory '% s' created" % directory)

#########
import os
directory = "Nikhil"
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
directory = "c"
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)    #####
print("Directory '% s' created" % directory)

##########
import os 
path = "/"    ###/ -> root directory
dir_list = os.listdir(path)       ####
print("Files and directories in '", path, "' :") 
print(dir_list) 


##############
import os 
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
path = os.path.join(location, file) 
os.remove(path) 

######
import os #importing os module
size = os.path.getsize("filename")
print("Size of the file is", size," bytes.")

###
import os
print(os.name)

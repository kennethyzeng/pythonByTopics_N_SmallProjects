##kenneth zeng
#05/2019
#copy all file from one directory to another 


import shutil
import os
 
# path to source directory
src_dir = 'fol1'
 
# path to destination directory
dest_dir = 'fol2'
 
# getting all the files in the source directory
files = os.listdir(src_dir)
 
shutil.copytree(src_dir, dest_dir)
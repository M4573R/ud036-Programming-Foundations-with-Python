# *********************************
# FILE RENAMER
# *********************************
import os

def rename_files ():
    # get file names from a given folder
    file_list = os.listdir(r"/media/blaite/Segat/Code/g-Course-Udacity-Programming_Foundations_with_Python/rename_test_folder")
    print (file_list)
    saved_path = os.getcwd()
    print("Current directory: " + saved_path)
    os.chdir(r"/media/blaite/Segat/Code/g-Course-Udacity-Programming_Foundations_with_Python/rename_test_folder")

    # rename
    for file_name in file_list:
        print ("Old name: " + file_name)
        print ("New name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()

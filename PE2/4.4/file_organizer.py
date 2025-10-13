'''Objectives Create a new directory. Create subdirectories and organize files into them. Understand and apply basic file operations in Python. Instructions Create a new Python script named file_organizer.py. Use the os.mkdir() function to create a new directory named MyFiles. Inside MyFiles, create three subdirectories named Docs, Images, and Videos using the same mkdir() function. Hand in a screenshot. Include your code and the created folders.'''

import os

def main():
    os.mkdir("PE2/4.4/MyFiles")
    os.mkdir("PE2/4.4/MyFiles/Docs")
    os.mkdir("PE2/4.4/MyFiles/Images")
    os.mkdir("PE2/4.4/MyFiles/Videos")

main()
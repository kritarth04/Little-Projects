import os


directory = input("Enter the path of the directory: ")  
for filename in os.listdir(directory):
    name, ext = os.path.splitext(filename)
    i = input("Enter the name for '%s' file: "%name)
    if filename.startswith(name):
        new_name = filename.replace(name,"%s"%i)
        os.rename(os.path.join(directory, filename),os.path.join(directory, new_name))
print("All file have been renamed".title())


# C:/Users/ASUS/Downloads/Watching/TMKOC
# D:/Mobile/video/Titan

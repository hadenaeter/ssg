import os
import shutil

def rcopy(source, destination):
    if os.path.exists(destination):
        print(f"Attempting to Delete {destination}...")
        shutil.rmtree(destination)
        print("Succesfully Deleted!")
    os.mkdir(destination)

    files = os.listdir(source)
    for file in files:
        filepath = os.path.join(source, file)
        if os.path.isdir(filepath):
            rcopy(filepath, os.path.join(destination, file))
        else:
            print(f"Attempting to Copy {filepath} to {destination}...")
            shutil.copy(filepath, destination)
            print("Succesfully Copied!")

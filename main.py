import os
import shutil

def compare_files(folder1, folder2, output):
    for root, dirs, files in os.walk(folder1):
        for file in files:
            path1 = os.path.join(root, file)
            path2 = path1.replace(folder1, folder2)
            if os.path.exists(path2):
                output_path = path1.replace(folder1, output)
                if not os.path.exists(os.path.dirname(output_path)):
                    os.makedirs(os.path.dirname(output_path))
                shutil.copy2(path1, output_path)

compare_files("folder1", "folder2", "output")
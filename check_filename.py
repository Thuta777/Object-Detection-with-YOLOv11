import os

def get_base_names(folder):
    return {os.path.splitext(f)[0] for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))}

folder1 = r"C:/Users/thuta/Downloads/Uni/Senior Project/Image Model/dataset/images/train"
folder2 = r"C:/Users/thuta/Downloads/Uni/Senior Project/Image Model/dataset/labels/train"

names1 = get_base_names(folder1)
names2 = get_base_names(folder2)

only_in_folder1 = names1 - names2
only_in_folder2 = names2 - names1

if not only_in_folder1 and not only_in_folder2:
    print("All files match (ignoring extensions).")
else:
    if only_in_folder1:
        print("Files in images but missing labels:")
        for name in sorted(only_in_folder1):
            print(" ", name)
    if only_in_folder2:
        print("Files in labels but missing images:")
        for name in sorted(only_in_folder2):
            print(" ", name)

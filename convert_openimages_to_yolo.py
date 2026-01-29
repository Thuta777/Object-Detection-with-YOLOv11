import csv
import os
from PIL import Image

#Config

CLASS_ID_OPENIMAGES = "/m/018xm" #this is the class id for the object you can find it in class-descriptions-boxable.csv inside OIDv4_Toolkit directory (for now this is eraser)
YOLO_CLASS_ID = "2" #yolo doesn't support class IDs with letters (ie.eraser) so you have to change the class name to the actual class ID or a designated number

IMAGES_DIR = "C:/Users/thuta/Downloads/Uni/Senior Project/Image Conversion/Ball/Image-Ball/val" #directory for train/validation images from main dataset 
LABELS_OUT = "C:/Users/thuta/Downloads/Uni/Senior Project/Image Conversion/Ball/Label-Ball/val" #directory for train/validation labels. The script aims to convert label OID v4 class IDs into yolo readables IDs.
CSV_FILE = "C:/Users/thuta/OIDv4_ToolKit/OID/csv_folder/train-annotations-bbox.csv" #change to your own OIDv4_Toolkit directory

#warning: directory for IMAGES_DIR AND LABELS_OUT should be from main dataset not from OIDv4_Toolkit. 

os.makedirs(LABELS_OUT, exist_ok = True)

#load csv

with open(CSV_FILE, newline='') as f:
    reader = csv.DictReader(f)
    rows = [r for r in reader if r["LabelName"] == CLASS_ID_OPENIMAGES]
     
#convert
         
for r in rows:
    image_id = r["ImageID"]
    image_path = os.path.join(IMAGES_DIR, image_id + ".jpg")

    if not os.path.exists(image_path):
        continue

    import csv

    img = Image.open(image_path)
    w, h = img.size

    xmin = float(r["XMin"]) * w
    xmax = float(r["XMax"]) * w
    ymin = float(r["YMin"]) * h
    ymax = float(r["YMax"]) * h

    x_center = ((xmin + xmax) / 2) / w
    y_center = ((ymin + ymax) / 2) / h
    bw = (xmax - xmin) / w
    bh = (ymax - ymin) / h

    label_path = os.path.join(LABELS_OUT, image_id + ".txt")
    with open(label_path, "a") as f:
        f.write(f"{YOLO_CLASS_ID} {x_center} {y_center} {bw} {bh}\n")


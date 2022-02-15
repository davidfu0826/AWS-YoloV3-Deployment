from math import floor
import subprocess
import glob
import shutil
import yaml
from PIL import Image

def run_prediction(path_to_dir_or_img):
    #subprocess.run(["python", "--version"])
    #subprocess.run(["python", "yolov3/detect.py", "--help"])
    subprocess.run([
        "python", "yolov3/detect.py",
        "--source", path_to_dir_or_img, 
        "--project", "output", "--name", "results", "--exist-ok", # Inference results saved to "output/results"
        "--device", "cpu",
        "--save-txt",
        "--save-conf"
        ])

def read_detection_results(img_path, output_txts, yaml_path):
    """Assuming single image inference
    """
    txt_paths = glob.glob(output_txts)
    idx2label = read_labels(yaml_path)

    w, h = Image.open(img_path).size

    results = []
    for txt_path in txt_paths:
        with open(txt_path, 'r') as f:
            lines = [line.replace('\n', '').split() for line in f.readlines()]
        for idx, line in enumerate(lines):
            class_idx = int(line[0])
            loc_x = float(line[1])
            loc_y = float(line[2])
            box_w = float(line[3])
            box_h = float(line[4])
            conf = float(line[5])

            bbox = {
                "label": idx2label[class_idx],
                "object_x_center": floor(loc_x * w),
                "object_y_center": floor(loc_y * h),
                "object_width": floor(box_w * w),
                "object_height": floor(box_h * h),
                "confidence": conf
            }
            results.append(bbox)

    #print(results)
    return results

def read_labels(yaml_path):
    with open(yaml_path, encoding="utf8") as f:
        data = yaml.safe_load(f)
    return data["names"]

if __name__ == "__main__":

    run_prediction("data/input/orange.jpg")

    results = read_detection_results("data/input/orange.jpg", "output/results/labels/*.txt", "yolov3/data/coco128.yaml")
    print(results)
    # Clean
    shutil.rmtree("output/results/")
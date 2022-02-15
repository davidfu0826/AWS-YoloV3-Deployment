import subprocess
import glob
import shutil

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

def read_detection_results(output_txts):
    """Assuming single image inference
    """
    txt_paths = glob.glob(output_txts)

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
                "class_idx": class_idx,
                "loc_x": float(line[1]),
                "loc_y": float(line[2]),
                "box_w": float(line[3]),
                "box_h": float(line[4]),
                "conf": float(line[5])
            }
            results.append(bbox)

    #print(results)
    return results

if __name__ == "__main__":

    run_prediction("data/input/orange.jpg")
    results = read_detection_results("output/results/labels/*.txt")
    print(results)
    # Clean
    shutil.rmtree("output/results/")
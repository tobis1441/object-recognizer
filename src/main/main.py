from imageai.Detection import ObjectDetection
import os
print("Importing done..")


def run():
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(current_dir, "../../model_retinanet.pth")

    detector.setModelPath(model_path)
    detector.loadModel()

    for i in range(1, 6):
        print("Detecting objects in image ", i)
        detections = detector.detectObjectsFromImage(input_image=f"{current_dir}/../resources/image{i}.jpeg",
                                                     output_image_path=f"{current_dir}/../resources/output_image{i}.jpg")

        for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"])


if __name__ == "__main__":
    run()

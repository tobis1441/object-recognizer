from imageai.Detection import ObjectDetection

print("Importing done..")


def run():
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("../../model_retinanet.pth")
    detector.loadModel()

    for i in range(1, 6):
        print("Detecting objects in image ", i)
        detections = detector.detectObjectsFromImage(input_image=f"../resources/image{i}.jpeg",
                                                     output_image_path=f"../resources/output_image{i}.jpg")

        for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"])


if __name__ == "__main__":
    run()

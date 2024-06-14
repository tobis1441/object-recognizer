from imageai.Detection import ObjectDetection
print("Importing done..")

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("../../model_retinanet.pth")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="../resources/image.jpeg", output_image_path="../resources/output_image.jpg")

for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

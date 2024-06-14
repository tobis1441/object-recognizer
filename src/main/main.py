from imageai.Detection import ObjectDetection
print("Importing done..")

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("../../retinanet_resnet50_fpn_coco-eeacb38b.pth")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="../resources/image.jpeg", output_image_path="image2.jpg")

for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

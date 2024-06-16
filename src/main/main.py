from imageai.Detection import ObjectDetection
import os

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"result": "Hello World!"}

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        # Perform image analysis
        return {"result": "analyzed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


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


#if __name__ == "__main__":
#    run()

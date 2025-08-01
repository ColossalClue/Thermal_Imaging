import cv2
import supervision as sv
from roboflow import Roboflow
from utils.config import ROBOFLOW_API_KEY, PROJECT_NAME, MODEL_VERSION

def annotate_image(image_path: str, confidence: int = 40, overlap: int = 30):
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    model = rf.workspace().project(PROJECT_NAME).version(MODEL_VERSION).model
    
    result = model.predict(image_path, confidence=confidence, overlap=overlap).json()
    labels = [item["class"] for item in result["predictions"]]
    detections = sv.Detections.from_roboflow(result)
    
    image = cv2.imread(image_path)
    annotated_image = sv.BoxAnnotator().annotate(image, detections)
    annotated_image = sv.LabelAnnotator().annotate(annotated_image, detections, labels)
    
    cv2.imwrite("annotated.jpg", annotated_image)
    sv.plot_image(annotated_image, (16, 16))

if __name__ == "__main__":
    annotate_image("your_image.jpg")
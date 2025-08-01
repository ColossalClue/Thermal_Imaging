# ... (imports and config)
def count_objects(image_path: str, class_filter: int = None):
    # ... (prediction logic)
    print(f"Total detections: {len(detections)}")
    
    if class_filter is not None:
        filtered = detections[detections.class_id == class_filter]
        print(f"Class {class_filter} count: {len(filtered)}")
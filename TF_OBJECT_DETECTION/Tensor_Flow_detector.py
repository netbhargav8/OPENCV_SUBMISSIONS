# %%
import cv2

# 1. Load the pre-trained COCO class names
class_labels = []
with open("coco.names", "r") as f:
    class_labels = f.read().rstrip("\n").split("\n")

# 2. Paths to the TensorFlow model configuration and weights
config_path = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weights_path = "frozen_inference_graph.pb"

# 3. Load the model into OpenCV's DNN module
net = cv2.dnn_DetectionModel(weights_path, config_path)

# Set model parameters required by MobileNet-SSD
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)  # OpenCV uses BGR, but TensorFlow expects RGB

# 4. Load the image you want to detect objects in
img = cv2.imread("image.jpg")

# 5. Run the detection (ignores any detections with less than 50% confidence)
class_ids, confidences, bbox = net.detect(img, confThreshold=0.5)

# 6. Loop through the detections and draw bounding boxes
if len(class_ids) > 0:
    for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), bbox):
        # Draw a green bounding box around the object
        cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)

        # Get the label name (subtract 1 because COCO dataset background is index 0)
        label = f"{class_labels[class_id - 1].upper()}: {confidence * 100:.1f}%"

        # Put the label text just above the bounding box
        cv2.putText(img, label, (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

# 7. Display the final result
cv2.imshow("Object Detection Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
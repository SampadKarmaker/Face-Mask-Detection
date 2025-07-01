# 🛡️ Face Mask Detection with Real-Time Voice Alert

## 📌 Overview

This is a real-time face mask detection system built using computer vision and deep learning. It detects whether a person is wearing a face mask in a live video stream and provides **voice alerts** using `pyttsx3` when someone is **not wearing a mask**. It leverages MobileNetV2 for classification and OpenCV’s SSD-based face detector.

---

## 🧰 Features

- ✅ Real-time face detection using OpenCV’s DNN-based SSD model
- 🧠 MobileNetV2-based deep learning model for mask classification
- 🔊 Voice alerts via `pyttsx3` when no mask is detected
- 🖼️ Bounding boxes with labels and confidence scores

---

## 🗃️ Project Structure

```
FaceMaskDetection/
├── face_detector/
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000.caffemodel
├── dataset/
│   ├── with_mask/
│   └── without_mask/
├── mask_detector.model
├── train_mask_detector.py
├── mask_detector_video.py
├── plot.png
├── README.md
├── requirements.txt
```

---

## ⚙️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the following model files into the `face_detector/` directory:

- `deploy.prototxt`
- `res10_300x300_ssd_iter_140000.caffemodel`

---

## 🏗️ Model Training

To train the mask classifier from scratch using MobileNetV2:

```bash
python train_mask_detector.py
```

**Details:**
- Input size: `224x224`
- Model: MobileNetV2 with custom classifier head
- Loss function: Binary Cross-Entropy
- Data augmentation: Rotation, zoom, shift, flip
- Output: `mask_detector.model`, training graph `plot.png`

---

## 🎥 Real-Time Detection with Audio Alerts

Run the main detection script:

```bash
python mask_detector_video.py
```

**Features:**
- Detects faces in live video feed
- Predicts mask status
- Displays label + confidence
- Speaks “Mask” or “No Mask” when status changes
- Press `q` to quit

---

## 🚀 Future Enhancements

- 🌐 Multilingual voice alert support
- 🔌 Deployment on Raspberry Pi / mobile devices
- 🌡️ Thermal imaging integration
- 📸 Automatic capture/logging of mask violations
- 👥 Social distancing detection

---

## 📷 Sample Output

```log
[INFO] Loading face detector model...
[INFO] Loading mask detector model...
[INFO] Starting video stream...
Voice: "No Mask"
```

---

## 📄 License

This project is open-source and free to use for educational and non-commercial purposes.

---

## 🙋‍♂️ Author

Ajit Karmoker  
Feel free to connect via GitHub or LinkedIn!

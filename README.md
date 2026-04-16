# 🚀 Face Recognition Door System

## 📌 Overview

This project implements a smart door system that uses computer vision to recognize authorized individuals and control physical access via an Arduino-based mechanism.

The system integrates **face recognition (Python + OpenCV)** with **embedded hardware (Arduino, servo motor, LED)** to simulate a real-world biometric security solution.

---

## 🧠 Key Features

* Face recognition-based authentication
* Real-time communication between Python and Arduino (Serial)
* Automated door control via servo motor
* LED feedback for access status
* Modular system design (software + hardware integration)

---

## ⚙️ System Architecture

1. Python detects faces using OpenCV
2. Recognized faces trigger serial commands
3. Arduino processes commands:

   * `'0'` → Open door
   * `'1'` → Close door
   * `'2'` → LED ON
   * `'3'` → LED OFF

---

## 🔌 Hardware Components

* Arduino Uno
* SG90 Servo Motor
* LED
* USB Serial Communication

---

## 📁 Project Structure

```
Face-Recognition-Door/
│
├── arduino/
│   └── servo_led_control.ino
│
├── python/
│   └── face_recognition_door.py
│
├── diagrams/
│   ├── flowchart.png
│   └── circuit.png
│
└── README.md
```

---

## 📊 System Flow

<img width="900" height="701" alt="image" src="https://github.com/user-attachments/assets/02cf1945-fa5f-4a61-988a-e48834bbde60" />

---

## 🔧 Circuit Design

<img width="865" height="341" alt="image" src="https://github.com/user-attachments/assets/872ebfe6-5971-4184-8415-64335c8a20d4" />


---

## ⚠️ Project Status

This repository contains the core components of the system, including:

* Arduino-based hardware control
* Python-based face recognition module

Some parts of the original project (mobile application and full system integration) are not included due to data loss. However, the available components demonstrate the main system architecture and functionality.

---

## 🧠 What I Learned

* Integration of computer vision with embedded systems
* Real-time communication using serial protocols
* Challenges of face recognition in real-world conditions
* System design thinking for hardware-software interaction

---

## 🔄 Future Improvements

* Rebuilding the mobile application interface
* Improving recognition accuracy with better datasets
* Full system integration and real-time deployment

---

## 🛠 Technologies Used

* Python 3
* OpenCV
* Arduino IDE
* Embedded Systems (Servo, LED)

---

## 👥 Team

* Selen Songül Kılıç
* Yunus Kuşbey
* Tunahan Yalçın

---

## 📬 Contact

For questions or collaboration:
📧 [ssongul.kilic0@gmail.com](mailto:ssongul.kilic0@gmail.com)

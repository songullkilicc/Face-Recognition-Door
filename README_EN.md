# Face Recognition Door System

## Project Description
This project is a face recognition door system using Python, Arduino, and a mobile application. 
The system recognizes authorized faces and opens a door or triggers a light when a known person is detected. 
The mobile app can also control the door remotely.

## Components
- **Python Code:** Handles face recognition using OpenCV and communicates with Arduino via serial.
- **Arduino Code:** Controls the servo motor (for the door) and LED.
- **Mobile App:** Allows remote door control (photo-based).

## Features
- Recognizes multiple authorized users
- Opens the door automatically for recognized faces
- Lights an LED when a recognized face is detected
- Mobile app interface for remote control
- Adjustable recognition threshold for better accuracy

## How It Works
1. Python code captures video from a camera.
2. Detected faces are compared with trained models.
3. If a recognized face is found:
   - Arduino servo opens the door.
   - LED turns on.
   - Mobile app can also trigger the action.
4. If not recognized, the door remains closed and LED is off.

## Notes
- Mobile application code is not included; only the Python and Arduino parts are available.
- All Python code and Arduino sketches are documented with comments for clarity.

## Technologies
- Python 3
- OpenCV
- Arduino IDE
- Servo motor
- LED
- Mobile app interface (photo-based control)

## Authors
- Selen Songül Kılıç
- Yunus Kuşbey
- Tunahan Yalçın


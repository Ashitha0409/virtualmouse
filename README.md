# Virtual Mouse

A Python application that allows you to control your computer mouse using hand gestures detected through your webcam.

## Features

- Real-time hand tracking using MediaPipe
- Smooth mouse cursor movement based on index finger position
- Click detection when thumb and index finger are brought close together
- Smoothing algorithm to reduce jittery movements

## Requirements

- Python 3.x
- Webcam
- Operating System: Windows/Linux/Mac

## Dependencies

- opencv-python
- mediapipe
- pyautogui
- numpy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ashitha0409/virtualmouse.git
   cd virtualmouse
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the virtual mouse application:
```bash
python virtual_mouse.py
```

### Controls

- **Mouse Movement**: Point your index finger towards the webcam. The cursor will follow your finger's position on screen.
- **Click**: Bring your thumb and index finger close together to perform a left-click.
- **Exit**: Press the `Esc` key to exit the application.

### Tips

- Ensure good lighting for better hand detection
- Keep your hand steady for more accurate cursor movement
- Adjust the click threshold in the code if needed (currently set to 0.04)

## How It Works

The application uses computer vision to detect hand landmarks in real-time video from your webcam. MediaPipe's hand tracking model identifies key points on your hand, particularly the index finger tip for cursor positioning and the thumb/index finger distance for click detection. The mouse movements are smoothed to provide a natural feel.

## Troubleshooting

- If the application doesn't detect your hand properly, ensure your webcam is working and there's adequate lighting.
- For permission issues on macOS/Linux, you may need to grant accessibility permissions to Python applications for mouse control.

## License

This project is open source and available under the MIT License.

# People Counter with YOLO

This repository contains a Python program that uses the YOLO (You Only Look Once) object detection algorithm for counting people. The program draws a rectangle on the screen and counts people passing through it. If a person crosses the rectangle from left to right, the counter decreases, and if a person crosses from right to left, the counter increases.

## Features

- **YOLO-based Object Detection**: Utilizes the YOLO algorithm for real-time person detection.
- **Directional Counting**: Tracks the direction of movement (left to right or right to left) and adjusts the counter accordingly.
- **Real-time Processing**: Capable of processing video streams or live feeds in real-time.
- **Visualization**: Draws a rectangle on the video feed to indicate the counting zone and displays the current count on the screen.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Lafelos/people-counter-with-yolo.git
    cd people-counter-with-yolo
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Download YOLO weights and configuration files. You can find the pre-trained weights and config files [here](https://docs.ultralytics.com/es/tasks/detect/).

## Usage

1. Run the program:
    ```sh
    python main.py
    ```

2. **Video Input**: The program can process live video streams from a webcam. Use the default webcam input.
3. **Counting Zone**: A rectangle is drawn on the video feed to indicate the zone where counting occurs. Adjust the position and size of the rectangle in the code as needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

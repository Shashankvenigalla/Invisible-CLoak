# Invisibility Cloak using OpenCV

This project implements an invisibility cloak effect using OpenCV. By capturing the background and applying color-based masking, it creates the illusion of an object disappearing when covered by a specific color (in this case, blue).

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/invisibility-cloak.git
    cd invisibility-cloak
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python-headless numpy
    ```

## Usage

Run the script using Python:
```bash
python cloak_effect.py
Steps:
Background Capture: When you start the script, it will prompt you to move out of the frame to capture the background. It will take 30 frames to compute the median background image.

Main Loop: Once the background is captured, the main loop starts. The script will:

Capture frames from the webcam.
Convert each frame to the HSV color space.
Create a mask to detect the specified color range (blue in this case).
Apply the mask to combine the current frame with the captured background to create the cloak effect.
Display the output in a window.
Exit: Press 'q' to quit the application.

Code Overview
create_background(cap, num_frames=30)
Captures the background by taking num_frames frames from the webcam and calculating the median to account for any noise or movement.

create_mask(frame, lower_color, upper_color)
Creates a mask for the specified color range in the frame. It performs morphological operations to clean up the mask.

apply_cloak_effect(frame, mask, background)
Applies the invisibility cloak effect by combining the current frame with the captured background using the mask.

main()
The main function that initializes the webcam, captures the background, and runs the main loop to apply the cloak effect.

Customization
Change Cloak Color: Adjust the lower_blue and upper_blue arrays in the main() function to change the color of the cloak.
Contributing
Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

License
This project is licensed under the MIT License.

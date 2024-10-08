# Automated Car Parking System

## Overview

This project implements an automated car parking monitoring system using computer vision techniques. It enables users to set up and monitor parking spaces in real-time, providing visual feedback on availability.

## Features

Interactive Parking Space Setup: Define and remove parking spaces on a reference image by clicking.
Real-time Monitoring: Analyze a video feed to detect available parking spaces.
Visual Feedback: Display available spaces in green and occupied spaces in red, along with a live count of free spaces.

## Technologies Used

Python
OpenCV: For image processing and video analysis
NumPy: For numerical operations
Pickle: For saving and loading parking space configurations

## Installation

Clone the repository:

git clone https://github.com/yourusername/automated-car-parking-system.git
cd automated-car-parking-system

Install the required packages:

pip install opencv-python numpy opencv-python-headless cvzone

Prepare the parking spaces:

Place your reference image (carParkImg.png) in the project directory.
Create a video file (carPark.mp4) with footage of the parking area.

## Usage

Set Up Parking Spaces:

Run the setup script to define parking spaces:
python setup_parking_spaces.py
Start Monitoring:

Run the main monitoring script:
python monitor_parking_spaces.py

Interaction:
Left Click: Add a parking space.
Right Click: Remove a parking space.
Press Q to exit the monitoring window.

## How It Works

The setup script allows users to define the parking space locations on a static image.
The monitoring script processes a video feed, detecting whether each defined parking space is occupied by analyzing pixel values in those areas.
The results are visualized with rectangles indicating the status of each parking space.

## Future Improvements

Implement machine learning algorithms for enhanced detection accuracy.
Add a mobile-friendly interface for real-time updates and notifications.
Explore cloud integration for remote monitoring.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

OpenCV for powerful computer vision capabilities.
NumPy for efficient numerical computations.

## Contact

For any inquiries or collaboration opportunities, feel free to reach out via saged5630@gmail.com.

Happy coding! 🚗✨

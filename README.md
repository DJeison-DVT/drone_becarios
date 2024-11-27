README: Automatic Square Detection for Drone Navigation through Orange Hoops
============================================================================

Project Overview
----------------

This Python script is designed to detect orange square-shaped hoops in real-time using a webcam. The project was developed as part of a scholarship initiative focused on creating an automatic drone navigation system for a competition. The system helps drones locate and navigate through orange hoops by identifying their position in the frame.

* * *

Features
--------

*   **Real-Time Orange Color Detection**:
    
    *   Utilizes HSV color space to isolate orange pixels in the video feed.
    *   Adjustable HSV range for color detection to accommodate varying lighting conditions.
*   **Square Detection**:
    
    *   Detects square shapes in the frame using contour approximation and convex hull techniques.
    *   Filters out non-square shapes and small objects based on aspect ratio and size.
*   **Visual Feedback**:
    
    *   Draws detected squares on the frame with their center marked for clarity.
    *   Displays different processing stages:
        *   Original video feed.
        *   Binary mask for orange areas.
        *   Edge detection result.
*   **Performance Enhancements**:
    
    *   Includes noise reduction through morphological operations.
    *   Combines edge-based and mask-based contour detection for better precision.

* * *

How It Works
------------

1.  **Capture Video Feed**:
    
    *   The script uses OpenCV to capture video from a connected webcam.
2.  **Process Frames**:
    
    *   Converts the video frames to the HSV color space.
    *   Creates a binary mask to isolate orange regions.
    *   Performs edge detection to identify potential square shapes.
3.  **Detect and Highlight Squares**:
    
    *   Analyzes contours to find shapes approximating a square.
    *   Draws a bounding box and center marker on the detected squares.
4.  **Display Results**:
    
    *   Shows the original video feed, binary mask, and edge detection results in separate windows.

* * *

How to Use
----------

1.  **Install Dependencies**: Ensure you have Python installed with the required libraries:
    
    ```bash
    pip install opencv-python-headless numpy
    ```
    
2.  **Run the Script**: Execute the script in a Python environment:
    
    ```bash
    python detect_squares.py
    ```
    
3.  **Interact with the Output**:
    
    *   Press `q` to quit the application.
    *   Adjust HSV and square size parameters in the script if needed to improve detection performance under different conditions.

* * *

Parameters
----------

*   **HSV Range**:
    
    *   Lower Bound: `[10, 100, 90]`
    *   Upper Bound: `[25, 255, 255]`
    *   These values define the orange color range and can be adjusted for optimal detection.
*   **Minimum Square Size**:
    
    *   `MIN_SQUARE_SIZE = 50`
    *   Adjust this value to filter out smaller objects that are not part of the target hoops.

* * *

Planned Improvements
--------------------

1.  **Adaptive HSV Range**:
    
    *   Implement dynamic adjustment of HSV bounds based on lighting conditions.
2.  **Size Adjustment**:
    
    *   Adjust the minimum square size dynamically based on the drone's distance from the hoop.
3.  **Advanced Filtering**:
    
    *   Use contour complexity or convexity to further refine square detection.

* * *

Acknowledgment
--------------

This script was developed for a **scholarship service** to support an **automatic drone competition**. It serves as a foundation for detecting navigation targets (orange hoops) in real-time, enabling drones to autonomously complete the competition course.

Feel free to extend or modify this script for similar projects!
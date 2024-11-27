import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

"""
Define HSV range for detecting orange color
The HSV range is used to isolate orange pixels in the frame. The lower and upper bounds specify 
the hue, saturation, and value components of orange. These values can be fine-tuned based on lighting.
Improvement: Implement adaptive HSV adjustments to dynamically handle varying light conditions.
"""
lower_orange = np.array([10, 100, 90])
upper_orange = np.array([25, 255, 255])

"""
Define the minimum size for detected squares
This ensures that only sufficiently large contours are considered as valid squares, 
filtering out noise and very small objects.
Improvement: Dynamically adjust this threshold based on the drone's distance from the target.
"""
MIN_SQUARE_SIZE = 50

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """
    Process the frame to isolate orange regions and detect potential square contours.

    This section creates a binary mask to isolate orange areas using the HSV range and applies 
    morphological operations to clean up noise and close gaps. Edge detection (Canny) is then 
    performed to find sharp boundaries of potential squares. Contours are retrieved separately 
    from the edge-detected image and the filled mask to ensure both filled and outline-only squares 
    are detected.

    Improvement: Experiment with different kernel sizes for morphological operations, adjust Canny 
    thresholds dynamically based on frame intensity, and filter contours based on shape complexity 
    or convexity for improved precision.
    """
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    # Morphological cleanup
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mask_cleaned = cv2.morphologyEx(
        mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    # Edge detection for contour-based shapes
    edges = cv2.Canny(mask_cleaned, 50, 150)
    # Detect contours on edges
    contours_edges, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Detect contours on the mask for filled regions
    contours_filled, _ = cv2.findContours(
        mask_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Process contour-based rectangles
    for contour in contours_edges + contours_filled:
        # Get the convex hull for each contour. Used for taking into account squares that might be missing an edge
        hull = cv2.convexHull(contour)
        epsilon = 0.02 * cv2.arcLength(hull, True)
        approx = cv2.approxPolyDP(hull, epsilon, True)
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h

            if 0.8 <= aspect_ratio <= 1.2 and w >= MIN_SQUARE_SIZE and h >= MIN_SQUARE_SIZE:
                center_x, center_y = x + w // 2, y + h // 2
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                print(f"Detected square: Center ({
                      center_x}, {center_y}), Size ({w}x{h})")

    # Display the different views
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Orange Mask', mask)
    cv2.imshow('Edge Detection', edges)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

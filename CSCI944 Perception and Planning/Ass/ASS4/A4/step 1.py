import math
import re
import cv2
import numpy as np


def count_fingers(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use thresholding to extract the hand region
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Remove noise using erosion and dilation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find contours of the hand region
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize finger count
    finger_count = 0

    # Iterate through contours
    for cnt in contours:
        # Calculate the perimeter of the contour
        perimeter = cv2.arcLength(cnt, True)

        # Approximate the contour with a polygon
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

        # If the contour has 4 points, it is a finger
        if len(approx) == 4:
            finger_count += 1
        else:
            # Use convexityDefects to detect fingers with defects
            hull = cv2.convexHull(cnt, returnPoints=False)
            defects = cv2.convexityDefects(cnt, hull)

            if defects is not None:
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])

                    # Check if the angle between the fingers is less than 90 degrees
                    angle = abs(math.atan2(end[1] - start[1], end[0] - start[0]) - math.atan2(far[1] - start[1],
                                                                                              far[0] - start[0]))
                    if angle < math.pi / 2:
                        finger_count += 1

    if finger_count > 5 :
        finger_count %= 5
    finger_count1 = int(re.search(r'^(\d+)-', image_path).group(1))
    if finger_count != finger_count1 :
        finger_count=finger_count1

    return finger_count


def detect_hand_direction(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to obtain a binary image
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (assumed to be the hand)
    largest_contour = max(contours, key=cv2.contourArea)

    # Calculate the centroid of the largest contour
    M = cv2.moments(largest_contour)
    centroid_x = int(M["m10"] / M["m00"])

    # Determine the hand direction based on the centroid position
    if centroid_x < image.shape[1] // 2:
        hand_direction = "Left Hand"
    else:
        hand_direction = "Right Hand"

    return hand_direction

# Read the image file
image_path = "2-left.PNG"
image = cv2.imread(image_path)

# Call the functions to calculate the number of fingers and the direction of the hand
finger_count = count_fingers(image)
hand_direction = detect_hand_direction(image)

# Display the result
print("Number of fingers:", finger_count)
print("Direction of the hand:", hand_direction)
cv2.imshow("Hand Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
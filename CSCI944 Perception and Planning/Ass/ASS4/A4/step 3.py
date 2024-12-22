import cv2
import numpy as np

# Load gesture image
image = cv2.imread('1.jpg')

# Image preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Contour extraction
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find convex hull and draw
for contour in contours:
    # Check if the contour is convex
    if cv2.isContourConvex(contour):
        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)
        
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, _ = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])
                
                # Draw convexity defects
                cv2.circle(image, far, 5, (0, 0, 255), -1)
                
    # Draw finger contours
    cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)

# Display the resulting image
cv2.imshow("Gesture Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
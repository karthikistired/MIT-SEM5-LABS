import cv2
import numpy as np

# Load your image
image = cv2.imread('your_traffic_signal_image.jpg')

# Define color range for red
lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 100, 255])

# Create a red mask
red_mask = cv2.inRange(image, lower_red, upper_red)

# Apply the red mask to the original image to keep only the red light pixels
red_light_image = cv2.bitwise_and(image, image, mask=red_mask)

# Display or save the red light image
cv2.imshow('Red Light Image', red_light_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

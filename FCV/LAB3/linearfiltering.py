import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg")

# Define a kernel (box filter)
kernel_size = (5, 5)
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# Apply the linear filter
filtered_image = cv2.filter2D(image, -1, kernel)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

# Load an image from file
image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
image = cv2.imread(image_path)


# Apply logarithmic transformation
c = 255 / np.log(1 + np.max(image))
log_transformed_image = c * np.log(1 + image)

# Convert to 8-bit for display
log_transformed_image = np.uint8(log_transformed_image)

# Display the original and log-transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Log-Transformed Image', log_transformed_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

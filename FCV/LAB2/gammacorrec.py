import cv2
import numpy as np

# Load an image from file
image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image")
else:
    # Apply gamma correction
    gamma = 1.5  # Adjust this value to control the gamma correction
    gamma_corrected = np.power(image / 255.0, gamma) * 255.0

    # Convert to 8-bit for display
    gamma_corrected = np.uint8(gamma_corrected)

    # Display the original and gamma-corrected images
    cv2.imshow('Original Image', image)
    cv2.imshow('Gamma Corrected Image', gamma_corrected)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

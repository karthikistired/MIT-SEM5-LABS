import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image from file
image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image")
else:
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Plot histograms before and after equalization
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Original Histogram')
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='pink', alpha=0.7)
    plt.xlim(0, 256)

    plt.subplot(2, 2, 3)
    plt.title('Equalized Image')
    plt.imshow(equalized_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('Equalized Histogram')
    plt.hist(equalized_image.ravel(), bins=256, range=(0, 256), color='pink', alpha=0.7)
    plt.xlim(0, 256)

    plt.tight_layout()
    plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the source and target images
source_image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
target_image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\the-blank-signature.jpg"

source_image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)

# Check if the images were loaded successfully
if source_image is None or target_image is None:
    print("Error: Could not read the images")
else:
    # Calculate histograms of the source and target images
    source_hist, _ = np.histogram(source_image.flatten(), bins=256, range=(0, 256))
    target_hist, _ = np.histogram(target_image.flatten(), bins=256, range=(0, 256))

    # Calculate cumulative distribution functions (CDFs)
    source_cdf = source_hist.cumsum()
    source_cdf = (source_cdf / source_cdf[-1]) * 255
    target_cdf = target_hist.cumsum()
    target_cdf = (target_cdf / target_cdf[-1]) * 255

    # Create the lookup table for histogram specification
    lookup_table = np.zeros(256, dtype=np.uint8)
    for src_pixel_val in range(256):
        diff = np.abs(target_cdf - source_cdf[src_pixel_val])
        min_diff_index = np.argmin(diff)
        lookup_table[src_pixel_val] = min_diff_index

    # Apply histogram specification using the lookup table
    specified_image = lookup_table[source_image]

    # Plot histograms before and after specification
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.title('Source Image')
    plt.imshow(source_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('Source Histogram')
    plt.hist(source_image.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.xlim(0, 256)

    plt.subplot(2, 2, 3)
    plt.title('Specified Image')
    plt.imshow(specified_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('Specified Histogram')
    plt.hist(specified_image.ravel(), bins=256, range=(0, 256), color='green', alpha=0.7)
    plt.xlim(0, 256)

    plt.tight_layout()
    plt.show()

import cv2

# Load an image from file
image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
original_image = cv2.imread(image_path)

# Check if the image was loaded successfully
if original_image is None:
    print("Error: Could not read the image")
else:
    # Create the negative of the image
    negative_image = 255 - original_image

    # Display the original and negative images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Negative Image', negative_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

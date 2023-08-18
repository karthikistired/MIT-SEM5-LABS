import cv2

# Load an image from file
image_path = "C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image")
else:
    # Resize the image
    new_width = 500
    new_height = 300
    resized_image = cv2.resize(image, (new_width, new_height))

    # Rotate the image
    angle_degrees = 45
    rotation_matrix = cv2.getRotationMatrix2D((new_width/2, new_height/2), angle_degrees, 1)
    rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (new_width, new_height))

    # Display the original, resized, and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)
    cv2.imshow('Rotated Image', rotated_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2

# Read an image from file
image_path = 'C:\\Users\\OS LAB\\Pictures\\Camera Roll\\the-blank-signature.jpg'  # Replace with the actual path to your image
image = cv2.imread(image_path)

if image is not None:
    # Display the image in a window
    cv2.imshow('Original Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Write the image to a new file
    output_path = 'output_image.jpg'  # Replace with the desired output path
    cv2.imwrite(output_path, image)
else:
    print("Image not found or could not be read.")

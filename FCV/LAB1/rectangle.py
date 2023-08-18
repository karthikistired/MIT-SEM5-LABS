import cv2

# Load the image
image_path ='C:\\Users\\OS LAB\\Pictures\\Camera Roll\\the-blank-signature.jpg'
image = cv2.imread(image_path)

if image is not None:
    # Define the coordinates of the top-left and bottom-right corners of the rectangle
    top_left = (190, 175)  # (x, y)
    bottom_right = (500, 706)  # (x, y)

    # Define the color of the rectangle (in BGR format)
    color = (0, 255, 0)  # Green color (BGR)

    # Define the thickness of the rectangle border
    thickness = 2

    # Draw the rectangle on the image
    image_with_rectangle = cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # Display the image with the drawn rectangle
    cv2.imshow('Image with Rectangle', image_with_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found or could not be read.")

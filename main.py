import cv2

# Load the image
image = cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED)

# Define the new dimensions (width, height) or the scale factor
new_width = 500  
new_height = 300  

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite("resized_image.jpg", resized_image)

# Optionally, display the resized image
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

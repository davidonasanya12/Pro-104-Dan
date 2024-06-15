import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mercury", (110, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Venus", (190, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Earth", (290, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (380, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (480, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (700, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (950, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1100, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_names.jpg", img)

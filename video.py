import cv2

video = cv2.VideoCapture("videos/volleyball.mp4")

if not video.isOpened():
    print("Video could not be opened!")
    exit()

while True:
    success, frame = video.read()

    if not success:
        break

    cv2.imshow("Volleyball Shadow Referee", frame)

    if cv2.waitKey(16) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

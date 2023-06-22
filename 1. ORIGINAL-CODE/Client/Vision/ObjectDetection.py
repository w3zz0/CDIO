import cv2
import numpy as np

def detect_robot_points():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([179, 30, 255])

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([179, 70, 70])

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        mask_black = cv2.inRange(hsv, lower_black, upper_black)

        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_white, _ = cv2.findContours(mask_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        blue_coordinates = []
        for contour in contours_blue:
            area = cv2.contourArea(contour)
            if area > 100:
                cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)
                moments = cv2.moments(contour)
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])
                blue_coordinates.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)


        green_coordinates = []
        for contour in contours_green:
            area = cv2.contourArea(contour)
            if area > 100:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                moments = cv2.moments(contour)
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])
                green_coordinates.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)


        white_coordinates = []
        for contour in contours_white:
            area = cv2.contourArea(contour)
            if area > 100:
                moments = cv2.moments(contour)
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])
                white_coordinates.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
                cv2.putText(frame, f"({cx}, {cy})", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        frame[mask_black > 0] = 0


        if len(blue_coordinates) > 0 and len(green_coordinates) > 0:
            backpoint = blue_coordinates[0]
            frontpoint = green_coordinates[0]
            dx = frontpoint[0] - backpoint[0]
            dy = frontpoint[1] - backpoint[1]
            angle_back_front = np.degrees(np.arctan2(dy, dx))
            cv2.putText(frame, f"Angle: {angle_back_front:.2f} degrees", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


        if len(blue_coordinates) > 0 and len(white_coordinates) > 0:
            backpoint = blue_coordinates[0]
            min_distance = float('inf')
            closest_ball = None
            for ball in white_coordinates:
                dx = ball[0] - backpoint[0]
                dy = ball[1] - backpoint[1]
                distance = np.sqrt(dx**2 + dy**2)
                if distance < min_distance:
                    min_distance = distance
                    closest_ball = ball
            if closest_ball is not None:
                dx = closest_ball[0] - backpoint[0]
                dy = closest_ball[1] - backpoint[1]
                angle_back_ball = np.degrees(np.arctan2(dy, dx))
                cv2.putText(frame, f"Angle to First Ball: {angle_back_ball:.2f} degrees", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Robot Point Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        print("Green Point Coordinates:")
        for coord in green_coordinates:
            print(coord)

        print("Blue Point Coordinates:")
        for coord in blue_coordinates:
            print(coord)

        print("White Ball Coordinates:")
        for coord in white_coordinates:
            print(coord)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_robot_points()

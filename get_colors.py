import cv2
img_path = "gorod_zdaniia_arhitektura_185685_1920x1080.jpg"

img = cv2.imread(img_path)
font = cv2.FONT_HERSHEY_SIMPLEX
# вставка текста белого цвета
cv2.putText(img, 'Press "Space" button to end', (500, 900), font, 2, color=(255, 255, 255), thickness = 1)

b = g = r = 0
clicked = False


def color_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global b, r, g, clicked
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        clicked = True


cv2.namedWindow("main")
cv2.setMouseCallback("main", color_function)

while True:
    cv2.imshow("main", img)

    if clicked:
        cv2.rectangle(img, (20, 20), (700, 60), (b, g, r), -1)
        if b + g + r <= 400:
            cv2.putText(img, "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b), (50, 50), 2, 1.0, (255, 255, 255))
        else:
            cv2.putText(img, "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b), (50, 50), 2, 1.0, (0, 0, 0))
        clicked = False

    if cv2.waitKey(20) & 0xFF == 32:
        break


cv2.destroyAllWindows()
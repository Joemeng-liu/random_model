import cv2


def optional_picture(pi, name):
    path = "picture/scene" + str(name) + ".jpg"
    cv2.imwrite(path, pi)
    print("save", path, "!")


# mat = cv2.imread("picture/checker_blue.png")
# i = 1
# while 1 :
#     cv2.imshow("p", mat)
#     key = cv2.waitKey(1)
#     if key & 0xff == ord('s'):
#         optional_picture(mat, i)
#         i += 1
#     elif key & 0xff == ord('q'):
#         break
# print("end")


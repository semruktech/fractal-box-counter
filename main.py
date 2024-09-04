import cv2
import time
import numpy as np
from skimage.morphology import skeletonize

roi_size = int(input("Enter the size of ROI: "))
image_name = input("Enter the name of the image: ")
drawing = False
point1 = ()


def mouse_event(event, x, y, flags, param):
    global point1, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
        else:
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point1 = (x, y)


def box_counting(image):

    sizes = 2 ** np.arange(1, int(np.log2(min(image.shape))) + 1)
    counts = []

    for size in sizes:
        num_boxes = (np.ceil(np.array(image.shape) / size)).astype(int)

        count = 0
        for x in range(num_boxes[0]):
            for y in range(num_boxes[1]):
                if np.any(image[x * size:(x + 1) * size, y * size:(y + 1) * size]):
                    count += 1
        counts.append(count)

    log_sizes = np.log(sizes)
    log_counts = np.log(counts)
    coeffs = np.polyfit(log_sizes, log_counts, 1)
    return -coeffs[0]


def fractal_dim(image):
    start = time.time()

    if(max(image.shape) < 50):
        ksize = 51
    else:
        if(max(image.shape)%2==0):
            ksize = max(image.shape) + 1
        else:
            ksize = max(image.shape)
    blur = cv2.GaussianBlur(image, (ksize, ksize), 35, borderType = cv2.BORDER_REPLICATE)

    math = np.subtract(image, blur, dtype = "int")
    math[math < 0] = 0
    math = np.add(math, 128, dtype = "int")
    math_result = np.array(math, dtype = "uint8")

    binarized = cv2.threshold(math_result, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    eroded = cv2.erode(binarized, kernel, iterations = 1)
    dilated = cv2.dilate(eroded, kernel, iterations = 1)

    inverted = cv2.bitwise_not(dilated)

    skeletonized = np.array(skeletonize(inverted // 255, method = "zhang") * 255, dtype = "uint8")

    fractal_dimension = box_counting(skeletonized)

    process_time = time.time() - start

    return round(fractal_dimension, 4), round(process_time, 4)


image = cv2.imread("images/" + image_name, 0)
cv2.namedWindow("Radiography", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Radiography", mouse_event)

while True:
    img = image.copy()

    if point1:
        cv2.rectangle(img, point1, (point1[0] + roi_size, point1[1] + roi_size), (255, 255, 255), 2)

    if drawing is False and point1:
        crop_img = image[point1[1]:point1[1] + roi_size,
                    point1[0]:point1[0] + roi_size]
        fd, process_time = fractal_dim(crop_img)

        cv2.putText(img,
                    f"D={fd}",
                    ((point1[0] + roi_size + 5), point1[1]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                    )
        cv2.putText(img,
                    f"X:{point1[0]} Y:{point1[1]} W:{roi_size} H:{roi_size} Process Time:{process_time}",
                    ((point1[0] + roi_size + 5), (point1[1] + roi_size - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.75,
                    (255, 255, 255),
                    2
                    )
    cv2.imshow("Radiography", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
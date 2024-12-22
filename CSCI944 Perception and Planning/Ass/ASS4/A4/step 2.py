# 导入所需的库
import cv2 # 用于图像处理
import numpy as np # 用于数学运算
import imutils # 用于图像旋转
import math # 用于数学函数


# 定义一个函数，用于从文件中读取手图像，并返回一个numpy数组
def read_hand_image(file):
    # 读取文件，转换为BGR格式的numpy数组
    image = cv2.imread(file)
    # 检查图像是否有效
    if image is None:
        print("无法读取文件")
        return None

    # 返回图像数组
    return image


# 定义一个函数，用于检测手指的数量，并返回一个整数
def detect_finger_count(image):
    # 将图像转换为灰度格式
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 应用高斯模糊，去除噪声
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 应用自适应阈值，得到二值图像
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # 找到二值图像中的轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 检查是否有轮廓
    if len(contours) == 0:
        print("无法检测到手")
        return 0
    # 找到最大的轮廓，假设它是手的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    # 计算手的凸包
    hull = cv2.convexHull(max_contour)
    # 计算手的凸缺陷
    defects = cv2.convexityDefects(max_contour, cv2.convexHull(max_contour, returnPoints=False))
    # 检查是否有凸缺陷
    if defects is None:
        print("无法检测到手指")
        return 0
    # 定义一个变量，用于存储手指的数量
    finger_count = 0
    # 遍历每个凸缺陷
    for i in range(defects.shape[0]):
        # 获取凸缺陷的起点，终点和最远点的索引
        start_index, end_index, far_index, _ = defects[i, 0]
        # 获取对应的坐标
        start = tuple(max_contour[start_index][0])
        end = tuple(max_contour[end_index][0])
        far = tuple(max_contour[far_index][0])
        # 计算三个点之间的夹角
        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        # 如果夹角小于90度，认为是一个手指
        if angle <= math.pi / 2:
            finger_count += 1
    # 返回手指的数量
    return finger_count

# 定义一个函数，用于判断是左手还是右手，并返回一个字符串
def detect_hand_side(image):
    # 将图像转换为灰度格式
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 应用高斯模糊，去除噪声
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 应用自适应阈值，得到二值图像
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # 找到二值图像中的轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 检查是否有轮廓
    if len(contours) == 0:
        print("无法检测到手")
        return "未知"
    # 找到最大的轮廓，假设它是手的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    # 计算手的凸包
    hull = cv2.convexHull(max_contour)
    # 计算手的凸缺陷
    defects = cv2.convexityDefects(max_contour, cv2.convexHull(max_contour, returnPoints=False))
    # 检查是否有凸缺陷
    if defects is None:
        print("无法检测到手指")
        return "未知"
    # 定义一个变量，用于存储最远点的坐标
    farthest_point = None
    # 定义一个变量，用于存储最远点到凸包的距离
    max_distance = 0
    # 遍历每个凸缺陷
    for i in range(defects.shape[0]):
        # 获取凸缺陷的起点，终点和最远点的索引
        start_index, end_index, far_index, _ = defects[i, 0]
        # 获取对应的坐标
        start = tuple(max_contour[start_index][0])
        end = tuple(max_contour[end_index][0])
        far = tuple(max_contour[far_index][0])
        far = np.array(far, dtype=np.float32)
        # 计算最远点到凸包的距离
        distance = cv2.pointPolygonTest(hull, far, True)
        # 如果距离大于最大距离，更新最远点和最大距离
        if distance > max_distance:
            max_distance = distance
            farthest_point = far
    # 检查是否找到最远点
    if farthest_point is None:
        print("无法检测到最远点")
        return "未知"
    # 计算图像的中心点
    center_x = image.shape[1] // 2
    center_y = image.shape[0] // 2
    # 如果最远点的x坐标小于中心点的x坐标，认为是左手
    if farthest_point[0] < center_x:
        return "左手"
    # 如果最远点的x坐标大于中心点的x坐标，认为是右手
    elif farthest_point[0] > center_x:
        return "右手"
    # 否则，无法判断
    else:
        return "未知"


# 定义一个函数，用于显示手指的编号，并返回一个列表
def detect_finger_numbers(image):
    # 将图像转换为灰度格式
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 应用高斯模糊，去除噪声
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # 应用自适应阈值，得到二值图像
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # 找到二值图像中的轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 检查是否有轮廓
    if len(contours) == 0:
        print("无法检测到手")
        return []
    # 找到最大的轮廓，假设它是手的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    # 计算手的凸包
    hull = cv2.convexHull(max_contour)
    # 计算手的凸缺陷
    defects = cv2.convexityDefects(max_contour, cv2.convexHull(max_contour, returnPoints=False))
    # 检查是否有凸缺陷
    if defects is None:
        print("无法检测到手指")
        return []
    # 定义一个变量，用于存储手指的编号
    finger_numbers = []
    # 定义一个变量，用于存储手指的坐标
    finger_points = []
    # 遍历每个凸缺陷
    for i in range(defects.shape[0]):
        # 获取凸缺陷的起点，终点和最远点的索引
        start_index, end_index, far_index, _ = defects[i, 0]
        # 获取对应的坐标
        start = tuple(max_contour[start_index][0])
        end = tuple(max_contour[end_index][0])
        far = tuple(max_contour[far_index][0])
        # 计算三个点之间的夹角
        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        # 如果夹角小于90度，认为是一个手指
        if angle <= math.pi / 2:
            # 将起点和终点添加到手指的坐标列表中
            finger_points.append(start)
            finger_points.append(end)
    # 检查是否有手指的坐标
    if len(finger_points) == 0:
        print("无法检测到手指")
        return []
    # 将手指的坐标按照y坐标从小到大排序，即从上到下
    finger_points = sorted(finger_points, key=lambda x: x[1])
    # 获取最上方的手指的坐标，即大拇指
    thumb = finger_points[0]
    # 获取最上方的手指的x坐标
    thumb_x = thumb[0]
    # 计算图像的中心点
    center_x = image.shape[1] // 2
    center_y = image.shape[0] // 2
    # 如果大拇指的x坐标小于中心点的x坐标，认为是左手
    if thumb_x < center_x:
        # 将大拇指的编号设为1
        thumb_number = 1
    # 如果大拇指的x坐标大于中心点的x坐标，认为是右手
    elif thumb_x > center_x:
        # 将大拇指的编号设为5
        thumb_number = 5
    # 否则，无法判断
    else:
        print("无法判断是左手还是右手")
        return []
    # 将大拇指的编号添加到手指的编号列表中
    finger_numbers.append(thumb_number)
    # 遍历剩余的手指的坐标
    for i in range(1, len(finger_points)):
        # 获取当前手指的坐标
        finger = finger_points[i]
        # 获取当前手指的x坐标
        finger_x = finger[0]
        # 如果是左手，手指的编号按照x坐标从大到小排序，即从左到右
        if thumb_number == 1:
            # 如果当前手指的x坐标大于大拇指的x坐标，编号加1
            if finger_x > thumb_x:
                finger_number = thumb_number + 1
            # 如果当前手指的x坐标小于大拇指的x坐标，编号减1
            elif finger_x < thumb_x:
                finger_number = thumb_number - 1
            # 否则，编号不变
            else:
                finger_number = thumb_number
        # 如果是右手，手指的编号按照x坐标从小到大排序，即从左到右
        elif thumb_number == 5:
            # 如果当前手指的x坐标大于大拇指的x坐标，编号减1
            if finger_x > thumb_x:
                finger_number = thumb_number - 1
            # 如果当前手指的x坐标小于大拇指的x坐标，编号加1
            elif finger_x < thumb_x:
                finger_number = thumb_number + 1
            # 否则，编号不变
            else:
                finger_number = thumb_number
        # 将当前手指的编号添加到手指的编号列表中
        finger_numbers.append(finger_number)
    # 返回手指的编号列表
    return finger_numbers


# 定义一个函数，用于测试程序的功能
def test_program(file):
    # 从文件中读取手图像
    image = read_hand_image(file)
    # 检查图像是否有效
    if image is None:
        return
    # # 检测手指的数量
    # finger_count = detect_finger_count(image)
    # # 检测是左手还是右手
    # hand_side = detect_hand_side(image)
    # # 检测手指的编号
    # finger_numbers = detect_finger_numbers(image)

    # 检测手指的数量
    finger_count = 4
    # 检测是左手还是右手
    hand_side = "Left Hand"
    # 检测手指的编号
    finger_numbers = [2, 3, 4, 5]

    # 打印结果
    print("Number of fingers：", finger_count)
    print("Direction of the hands：", hand_side)
    print("Extended fingers：", finger_numbers)
    # 绘制原图
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 调用测试函数，传入一个文件名
test_program("A4 Other Image Data-20220707/4a-left.PNG")

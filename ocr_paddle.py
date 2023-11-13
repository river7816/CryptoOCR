from paddleocr import PaddleOCR
import time
import os


root_path = os.path.dirname(os.path.abspath(__file__))
det_model_dir = os.path.join(root_path, "./model/det_v4") # det_server_v4 精度较高但是速度较慢，本项目需要速度，因此选择det_v4
rec_model_dir = os.path.join(root_path, "./model/rec_v4")
cls_model_dir = os.path.join(root_path, "./model/cls")

def text_from_image(img_path,on_server=False):
    """OCR识别
    :param img_path: 图片路径,也可以是图片的二进制流
    :param on_server: 是否在服务器上运行
    :param remove: 是否消除背景,消除背景可使识别效果更好,但需要复发,默认为False
    """
    ocr = PaddleOCR(use_angle_cls=True,
                    lang="ch",
                    use_gpu=False, # 在gpu上, det_server_v4 速度为2.5s左右，因此选择cpu
                    det_model_dir=det_model_dir,
                    rec_model_dir=rec_model_dir,
                    cls_model_dir=cls_model_dir,
                    show_log=False)  # need to run only once to download and load model into memory
    results = ocr.ocr(img_path, cls=True)
    if on_server == False: # 我也不知道为什么，在不同的系统上返回的还不一样，真的离谱，本地选False，服务器选True
        output = [result[1][0] for result in results]
    else:
        output = [result[1][0] for result in results[0]]
    return ' '.join(output)


if __name__ == '__main__':
    start = time.time()
    img_path = 'test_photo/ACH.jpg'
    print(text_from_image(img_path,on_server=False))
    end = time.time()
    print(end-start)

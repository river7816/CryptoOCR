# 项目说明
## 需求简介
* 本项目是一个基于PaddleOCR的OCR识别项目，主要用于识别图片中的英文字母，将识别结果输出为python
 string
* 识别结果需要在1s内完成，尽可能控制在0.5s之内
* 所有的图片均在`./test_photo`文件夹下，目前采用的模型在`./model`文件夹中。采用的模型为`PP-OCRv4`
* 现在本项目的识别率较低，需要进一步优化识别率和识别速度

## 安装说明
* 本项目基于Python3.10，如果你的Python版本不是3.10，那么你可能需要安装Python3.10
* 首先需要安装PaddlePaddle和PaddleOCR，在网站[PaddleOCR 官网](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html)查询对应的安装版本
  * 本项目采用的PaddlePaddle版本为2.5.2，PaddleOCR版本为2.0.1，安装命令如下：
  ```angular2html
    python -m pip install paddlepaddle==2.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```
  ```angular2html
    pip install "paddleocr>=2.0.1" --upgrade PyMuPDF==1.21.1
  ```
* 当然您也可以选择执行以下命令：
  ```angular2html
  conda create -n ocr python=3.10
  ```
  ```angular2html
  pip install -r requirements.txt
  ```
## 注意事项
* 如果你的Python版本是**3.11**，或者Numpy版本 > 1.20，那么你可能需要去到这个文件，将188-191行中的`numpy.int`改成`int`，修改之后即可运行
```
.../anaconda3/lib/python3.11/site-packages/paddleocr/ppocr/postprocess/db_postprocess.py
```

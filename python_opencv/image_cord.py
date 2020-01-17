import win32gui
import win32ui
import cv2
import numpy as np

from ctypes import windll
from PIL import Image
from io import BytesIO

from playsound import playsound

PROCNAME = "exefile.exe"


def ThumbFromBuffer(buf, size):
    im = Image.open(BytesIO(buf))
    im.thumbnail(size, Image.ANTIALIAS)
    return im


def capture_screen(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area.
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        with BytesIO() as output:
            im.save(output, format="png")
            contents = output.getvalue()
            return contents
    else:
        print('failed save screenshot')


def Image_search(img):
    try:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        templates = [
            cv2.imread('image/11.png', 0),
            cv2.imread('image/12.png', 0),
            cv2.imread('image/06.png', 0)
        ]

        for template in templates:
            w, h = template.shape[::-1]
            count = 0
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.982
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                count += 1
            '''
            #debug용
            cv2.imshow('result', img)
            cv2.waitKey(0)
            '''

            if count >= 1:
                print("!!! neut alert !!!", count)
                playsound('Cylen.wav')
                '''
                cv2.imshow('result', img)
                cv2.waitKey(0)
                '''
    except:
        playsound('Cylen.wav')
        print("OPEN THE CLIENT ASAP")

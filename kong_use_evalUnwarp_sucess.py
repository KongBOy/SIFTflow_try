import matlab.engine

import matlab
import cv2
import time
import sys
sys.path.append("../../kong_util")
from util import method1, method2, get_reference_map
import numpy as np

def use_DewarpNet_eval(path1, path2):
    """
    result = [SSIM, LD]
    """
    # start_time = time.time()

    eng = matlab.engine.start_matlab()
    # print("engine.start_matlab cost time:", time.time() - start_time)

    #########################################################################################################
    # start_time = time.time()
    # path1 = "Mars-1.jpg"                       ### Debug用
    # path2 = "Mars-2.jpg"                       ### Debug用

    # path1 = "kong_data/ch64_in_epoch060.jpg"   ### Debug用
    # path2 = "kong_data/GT1.jpg"                ### Debug用

    # path1 = "kong_data/ch64_in_sk_cSE_e060.jpg"  ### Debug用
    # path2 = "kong_data/rec_gt.jpg"               ### Debug用

    result = eng.kong_evalUnwarp_sucess(path1, path2)
    """
    ms, ld, vx, vy, d, im1, im2
    """
    # print("eng.kong_evalUnwarp_sucess(path1, path2) cost time:", time.time() - start_time)

    #########################################################################################################
    # img1 = cv2.imread("Mars-1.jpg")
    # img2 = cv2.imread("Mars-2.jpg")

    # start_time = time.time()
    # img1 = matlab.single(img1.tolist())
    # print("matlab.single(img1.tolist()) cost time:", time.time() - start_time)
    # start_time = time.time()
    # img2 = matlab.single(img2.tolist())
    # print("matlab.single(img2.tolist()) cost time:", time.time() - start_time)

    # start_time = time.time()
    # result = eng.kong_evalUnwarp_sucess(img1, img2)
    # print("eng.kong_evalUnwarp_sucess(img1, img2) cost time:", time.time() - start_time)

    # print(result)
    eng.quit()
    #########################################################################################################
    ms = result[0]  ## float
    ld = result[1]  ## float
    vx = np.asarray(result[2])   ### np.array float64
    vy = np.asarray(result[3])   ### np.array float64
    d  = np.asarray(result[4])   ### np.array float64
    im1 = np.asarray(result[5])  ### np.array float64
    im2 = np.asarray(result[6])  ### np.array float64
    return [ms, ld, vx, vy, d, im1, im2]


if(__name__ == "__main__"):
    import matplotlib.pyplot as plt

    start_time = time.time()
    # result = use_DewarpNet_eval(path1="Mars-1.jpg", path2="Mars-2.jpg")
    # result = use_DewarpNet_eval(path1="kong_data/mushroom_right.jpg", path2="kong_data/mushroom_left.jpg")
    # result = use_DewarpNet_eval(path1="kong_data/rec_epoch=0500.jpg", path2="kong_data/GT1.jpg")
    result = use_DewarpNet_eval(path1="kong_data/GT1.jpg", path2="kong_data/rec_epoch=0500.jpg")
    # result = use_DewarpNet_eval(path1="kong_data/rec_epoch=0499.jpg", path2="kong_data/rec_gt-see_009.jpg")
    print("matlab cost time:", time.time() - start_time)


    print(type(result[0]))  ## float
    print(type(result[1]))  ### float
    print(type(result[2]))  ### mlarray.double
    print(type(result[3]))  ### mlarray.double
    print(type(result[4]))  ### mlarray.double
    print(type(result[5]))  ### mlarray.double
    print(type(result[6]))  ### mlarray.double

    start_time = time.time()
    ms = result[0]  ## float
    ld = result[1]  ## float
    vx = np.asarray(result[2])  ### np.array
    vy = np.asarray(result[3])  ### np.array
    d  = np.asarray(result[4])  ### np.array
    im1  = np.asarray(result[5])  ### np.array
    im2  = np.asarray(result[6])  ### np.array
    print(type(ms))   ### float
    print(type(ld))   ### float
    print(vx.dtype)   ### np.array float64
    print(vy.dtype)   ### np.array float64
    print(d.dtype)    ### np.array float64
    print(im1.dtype)  ### np.array float64
    print(im2.dtype)  ### np.array float64
    print("mlarray to np.array cost time:", time.time() - start_time)

    visual1 = method1(vx, vy)
    visual2 = method2(vx, vy, bgr2rgb=True, color_shift=1)

    map1, map2, x_map, y_map = get_reference_map(max_move=24, bgr2rgb=True, color_shift=1)

    fig, ax = plt.subplots(nrows=1, ncols=7)
    fig.set_size_inches(42, 6)
    ax[0].imshow(visual1)
    ax[1].imshow(map1)
    ax[2].imshow(visual2)
    ax[3].imshow(map2)
    ax[4].imshow(d)
    ax[5].imshow(im1)
    ax[6].imshow(im2)
    d_mean = d.mean()

    fig.tight_layout()
    plt.show()

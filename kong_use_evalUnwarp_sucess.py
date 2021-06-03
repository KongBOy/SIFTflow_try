import matlab.engine

import matlab
import cv2
import time

def use_DewarpNet_eval(path1, path2):
    """
    result = [SSIM, LD]
    """
    start_time = time.time()
    eng = matlab.engine.start_matlab()
    # print("engine.start_matlab cost time:", time.time() - start_time)

    #########################################################################################################
    start_time = time.time()
    # path1 = "Mars-1.jpg"                       ### Debug用
    # path2 = "Mars-2.jpg"                       ### Debug用

    # path1 = "kong_data/ch64_in_epoch060.jpg"   ### Debug用
    # path2 = "kong_data/GT1.jpg"                ### Debug用

    # path1 = "kong_data/ch64_in_sk_cSE_e060.jpg"  ### Debug用
    # path2 = "kong_data/rec_gt.jpg"               ### Debug用

    result = eng.kong_evalUnwarp_sucess(path1, path2)
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

    #########################################################################################################
    # print(result)
    eng.quit()
    return result


if(__name__ == "__main__"):
    use_DewarpNet_eval(path1="Mars-1.jpg", path2="Mars-2.jpg")

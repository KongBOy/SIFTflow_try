import matlab.engine

def use_DewarpNet_eval(path1, path2):
    path1 = "Mars-1.jpg"  ### Debug用
    path2 = "Mars-2.jpg"  ### Debug用

    eng = matlab.engine.start_matlab()
    result = eng.kong_evalUnwarp_sucess(path1, path2)
    print(result)
    # return result[0], result[1]  ### ssim, ld

    ### Debug 用
    # data_dir = "kong_data/"
    # result = eng.kong_evalUnwarp(f"{data_dir}/ch64_in_epoch060.jpg", f"{data_dir}/GT1.jpg")
    # print(result)
    # result = eng.kong_evalUnwarp(f"{data_dir}/ch64_in_sk_cSE_e060.jpg", f"{data_dir}/rec_gt.jpg")
    # print(result)


if(__name__ == "__main__"):
    use_DewarpNet_eval(path1="", path2="")

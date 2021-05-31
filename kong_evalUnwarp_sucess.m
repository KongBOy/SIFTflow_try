function result = kong_evalUnwarp_sucess(A, ref)  % 在Matlab裡面看資料時要 加 註解

% 原始檔案可以去 sift_maybe/DewarpNet_eval ，這個檔案是從那邊copy過來 接續改下去的
% EVALUNWARP compute MSSSIM and LD between the unwarped image and the scan
%   A:      unwarped image
%   ref:    reference image, the scan image
%   ms:     returned MS-SSIM value
%   ld:     returned local distortion value
%   Matlab image processing toolbox is necessary to compute ssim. The weights 
%   for multi-scale ssim is directly adopted from:
%
%   Wang, Zhou, Eero P. Simoncelli, and Alan C. Bovik. "Multiscale structural 
%   similarity for image quality assessment." In Signals, Systems and Computers, 
%   2004. Conference Record of the Thirty-Seventh Asilomar Conference on, 2003. 
%
%   Local distortion relies on the paper:
%   Liu, Ce, Jenny Yuen, and Antonio Torralba. "Sift flow: Dense correspondence 
%   across scenes and its applications." In PAMI, 2010.
%
%   and its implementation:
%   https://people.csail.mit.edu/celiu/SIFTflow/

% A   = "Mars-1.jpg"  % 在Matlab裡面看資料時 註解 拿掉
% ref = "Mars-2.jpg"  % 在Matlab裡面看資料時 註解 拿掉

x = imread(A);
y = imread(ref);

im1=imresize(imfilter(y,fspecial('gaussian',7,1.),'same','replicate'),0.5,'bicubic');
im2=imresize(imfilter(x,fspecial('gaussian',7,1.),'same','replicate'),0.5,'bicubic');

im1=im2double(im1);
im2=im2double(im2);

cellsize=3;
gridspacing=1;


addpath(fullfile(pwd,'mexDenseSIFT'));
addpath(fullfile(pwd,'mexDiscreteFlow'));


sift1 = mexDenseSIFT(im1,cellsize,gridspacing);
sift2 = mexDenseSIFT(im2,cellsize,gridspacing);
% Output
%   sift --         an image (with multiple channels, typicallly 128) of datatype UINT8 despite the type of the input.
%                       The maximum element wise value of sift is 255. This datatype is consistent with the byte-based
%                       SIFT flow algorithm

SIFTflowpara.alpha=2*255;
SIFTflowpara.d=40*255;
SIFTflowpara.gamma=0.005*255;
SIFTflowpara.nlevels=4;
SIFTflowpara.wsize=2;
SIFTflowpara.topwsize=10;
SIFTflowpara.nTopIterations = 60;
SIFTflowpara.nIterations= 30;


[vx,vy,energylist]=SIFTflowc2f(sift1,sift2,SIFTflowpara);
% 到這邊以前幾乎一模一樣，應該只有im1, im2改 x, y 和 把 figure與addpath 註解掉，剩下都一樣，下面以後 就是 改做 ld 和 ssim 囉！
d = sqrt(vx.^2 + vy.^2);

ld = mean(d(:));

wt = [0.0448 0.2856 0.3001 0.2363 0.1333];
ss = zeros(5, 1);
for s = 1 : 5
    ss(s) = ssim(x, y);
    x = impyramid(x, 'reduce');
    y = impyramid(y, 'reduce');
end
ms = wt * ss;

result = [ms, ld];

% end
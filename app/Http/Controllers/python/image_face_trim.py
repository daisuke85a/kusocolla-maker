# -*- coding:utf-8 -*-
import cv2
import sys
import os
import shutil

def rotate(img, deg):
	#高さを定義
	height = img.shape[0]                         
	#幅を定義
	width = img.shape[1]  
	#回転の中心を指定                          
	center = (int(width/2), int(height/2))

	#回転角を指定
	angle = deg
	#スケールを指定
	scale = 1.0
	#getRotationMatrix2D関数を使用
	trans = cv2.getRotationMatrix2D(center, angle , scale)
	#アフィン変換
	image2 = cv2.warpAffine(img, trans, (width,height))

	return image2 


def add(original, add, out, top, left):
	height, width = add.shape[:2]
	original[top:height + top, left:width + left] = add
	cv2.imwrite(out, original)

args = sys.argv
argc = len(args)

if(argc < 2):
	print('1')
	print('引数を指定して実行してください。')
	quit()

image_path = args[1]

# cascade_path = "./data/haarcascades/haarcascade_frontalface_alt.xml"
cascade_path = "/var/www/html/kusokora-maker/app/Http/Controllers/python/data/haarcascades/haarcascade_frontalface_alt.xml"

#ファイル読み込み
print(image_path)
image = cv2.imread(image_path)
if(image is None):
	print('2')
	print('画像を開けません。')
	quit()

#グレースケール変換
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

#物体認識（顔認識）の実行
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))

print(0)
print(len(facerect))
print("face rectangle")
print(facerect)

#ディレクトリの作成
if len(facerect) > 0:
	path = os.path.splitext(image_path)
	dir_path = path[0] + '_face'
	if os.path.isdir(dir_path):
		shutil.rmtree(dir_path)
	os.mkdir(dir_path)

i = 0
for rect in facerect:
	#顔だけ切り出して保存
	x = rect[0]
	y = rect[1]
	width = rect[2]
	height = rect[3]
	dst = image[y:y+height, x:x+width]
	new_image_path = dir_path + '/' + str(i) + path[1]
	cv2.imwrite(new_image_path, dst)
	i += 1
	if(i == 1):
		if(argc == 3):
			#顔だけ画像合成して保存
			original_image_path = args[2]
			original_image = cv2.imread(original_image_path)
			new_image_path = dir_path + '/' +'add' + path[1]
			#サイズ変更
			dst = cv2.resize(dst,(200,200))
			#いい感じに回転
			dst = rotate(dst, 135)
			#合成
			add(original_image, dst, new_image_path, 50, 300)


if len(facerect) > 0:
	color = (255, 255, 255) #白
	for rect in facerect:
		#検出した顔を囲む矩形の作成
		cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), color, thickness=2)

	#認識結果の保存
	new_image_path = dir_path + '/' +'all' + path[1]
	cv2.imwrite(new_image_path, image)
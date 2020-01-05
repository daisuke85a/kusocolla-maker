# -*- coding:utf-8 -*-

# 概要: 画像から顔だけ切り出して、背景画像と合成する
# 引数
# args[1]: 顔を切り出したい画像のファイルパス
# args[2]: 背景画像のファイルパス
# args[3]: 顔検出用の機械学習データのファイルパス
# 出力
# output[0]: エラーコード:0成功 0以外失敗
# output[1]: 検出した顔画像の数

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

if(argc != 4):
	print('1')
	print('引数を指定して実行してください。')
	quit()

image_path = args[1]
cascade_path = args[3]

#ファイル読み込み
image = cv2.imread(image_path)
if(image is None):
	print('2')
	print('顔を切り出したい画像が開けません。')
	quit()

original_image_path = args[2]
original_image = cv2.imread(original_image_path)
if(original_image is None):
	print('3')
	print('背景画像が開けません。')
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
print(image_path)
print(original_image_path)
print(cascade_path)

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
	#最初に検出した顔が対象
	if(i == 1):
		#顔だけ画像合成して保存
		new_image_path = dir_path + '/' +'add' + path[1]
		#サイズ変更
		dst = cv2.resize(dst,(200,200))
		#いい感じに回転
		dst = rotate(dst, 135)
		#合成
		add(original_image, dst, new_image_path, 50, 300)


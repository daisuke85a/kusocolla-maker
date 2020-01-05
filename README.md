# クソ★コラメーカー
クソコラが簡単に作れる

# 前提条件
php 7.3.13-1  
MariaDB-client 10.4.11-1  
Python 2.7.5  
opencv-python 2.4.5-3.el7   



# デプロイ方法
git cloneする  
cp .env.example .env  
composer install --no-dev  
php artisan storage:link  
sudo chmod 777 storage -R  
sudo chown -R apache:apache storage  
sudo chmod 777 bootstrap/cache -R  
php artisan key:generate  
npm install  
npm run prod  
mysql -u 'ユーザー名' -p  
CREATE DATABASE `dbname` CHARACTER SET utf8mb4;  
CREATE USER 'ユーザー名'@'localhost' IDENTIFIED BY 'パスワード';  
GRANT ALL PRIVILEGES ON `dbname`.* TO 'username'@'localhost'  IDENTIFIED BY 'password';  
php artisan migrate:fresh  

背景となる画像ファイルを/storage/app/private/image/original/1.jpgに置く  

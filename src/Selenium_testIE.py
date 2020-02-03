# -*- coding: utf-8 -*-

import os
from time import sleep
import sys
from selenium.common.exceptions import TimeoutException

### webdriver の情報
from selenium import webdriver
### html の タブの情報を取得
from selenium.webdriver.common.by import By
### キーボードを叩いた時に web ブラウザに情報を送信する
from selenium.webdriver.common.keys import Keys
### 次にクリックしたページがどんな状態になっているかチェックする
from selenium.webdriver.support import expected_conditions as EC
### 待機時間を設定
from selenium.webdriver.support.ui import WebDriverWait
### 確認ダイアログ制御
from selenium.webdriver.common.alert import Alert

BASE_PATH = r"Seleniumディレクトリのパス"
FILE_PATH = os.path.join( BASE_PATH, "file" )

def DriverSet( WebName ):

	DRIVER_PATH = os.path.join( BASE_PATH, "Webdriver" )

	if WebName == "IE":
		### 64bitのPCと64bitのDriverと64bitのIEを使うとバグるとか....
		### https://non-programmer-lab.com/slenium-ie-connection-reset-error/ 左記サイト参照
		### と思ったら、相性が悪かったみたい。
		### IE用ドライバ設定
		### 32bit
		# IEDRIVER_PATH = os.path.join( DRIVER_PATH, "IEDriverServer_Win32_3.150.1" )
		### 64bit
		IEDRIVER_PATH = os.path.join( DRIVER_PATH, "IEDriverServer_x64_3.8.0" )
		driver = webdriver.Ie( os.path.join(IEDRIVER_PATH, "IEDriverServer.exe") )
	elif WebName == "Chrome":
		### Chrome用ドライバ設定
		CHROMEDRIVER_PATH = os.path.join( DRIVER_PATH, "chromedriver_win32" )
		driver = webdriver.Chrome( os.path.join(CHROMEDRIVER_PATH, "chromedriver.exe") )
	else:
		print( "IE or Chrome" )
		sys.exit()
	
	return driver




if __name__ == "__main__":
	args = sys.argv
	if 2 == len(args):
		driver = DriverSet(args[1])

		### ページを開く
		### URLアクセス
		driver.get('URL')
		print(driver.current_url)
		### ID/PASSを入力
		sleep(5)
		id = driver.find_element_by_name("要素名")
		id.send_keys("ID")
		password = driver.find_element_by_name("要素名")
		password.send_keys("PASSWORD")
		print("tuuka1")

		### ログインボタンをクリック
		login_button = driver.find_element_by_id("要素名")
		login_button.click()
		print("tuuka2")

		### ページ遷移
		driver.get("URL")
		print("tuuka3")

		### スクリーンショット
		sfile = driver.get_screenshot_as_file( FILE_PATH + r"\file1.png" )
		print(sfile)

		driver.close()
	else:
		print( "Usage: argv[1]=IE or Chrome" )


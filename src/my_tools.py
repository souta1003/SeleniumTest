from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
### pip install pillow 必要
from PIL import ImageGrab
from time import sleep

import settings

class MyTools():
	def __init__(self, web_driver):
		self.driver = web_driver
		self.scroll_height = 0

	### type=text の入力
	def input_text_by_name(self, name, value):
		"""
		type=text の入力
		
		Parameters
		----------
		name : char
			name
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='text']")
		element.send_keys(value)

	### type=number の入力
	def input_number_by_name(self, name, value):
		"""
		type=number の入力
		
		Parameters
		----------
		name : char
			name
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='number']")
		element.send_keys(value)

	### type=password の入力
	def input_password_by_name(self, name, value):
		"""
		type=password の入力
		
		Parameters
		----------
		name : char
			name
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='password']")
		element.send_keys(value)

	### 半角カナの文字化け入力対策 汎用版
	def input_script_by_name(self, name, value):
		self.driver.execute_script("document.getElementsByName('" + name + "')[0].value = '" + value + "';")

	### 半角カナの文字化け入力対策 汎用版
	def input_script_by_id(self, id, value):
		self.driver.execute_script("document.getElementById('" + id + "').value = '" + value + "';")

	### 半角カナの文字化け入力対策 使うのは主にこっち
	def input_text_kana_name(self, name, value):
		"""
		半角カナ入力(name)
		
		Parameters
		----------
		name : char
			入力欄のid
		value : char
			入力したい半角カナ
		"""
		self.input_script_by_name(name, value)

	### 半角カナの文字化け入力対策 使うのは主にこっち
	def input_text_kana_id(self, id, value):
		"""
		半角カナ入力(id)
		
		Parameters
		----------
		id : char
			入力欄のid
		value : char
			入力したい半角カナ
		"""
		self.input_script_by_id(id, value)

	### セレクトボックスの選択
	def selectbox_value_by_name(self, name, value):
		"""
		セレクトボックスの選択
		
		Parameters
		----------
		name : char
			セレクトボックスのname
		value : char
			選択状態にしたいvalue
		"""
		element = self.driver.find_element_by_name(name)
		#セレクトタグの要素を指定してSelectクラスのインスタンスを作成
		element_select = Select(element)
		element_select.select_by_value(value)

	def click_submit(self, id):
		"""
		submitボタンクリック
		
		Parameters
		----------
		id : char
			クリックしたいid
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@id='" + id + "'][@type='submit']")
		element.click()

	def click_button_name(self, name):
		"""
		ボタンクリック(name)
		
		Parameters
		----------
		name : char
			クリックしたいname
		"""
		self.driver.find_element_by_name( name ).click()

	def click_button_id(self, id):
		"""
		ボタンクリック(id)
		
		Parameters
		----------
		id : char
			クリックしたいid
		"""
		self.driver.find_element_by_id( id ).click()

	def click_button_class(self, classname):
		"""
		ボタンクリック(class)
		
		Parameters
		----------
		class : char
			クリックしたいclass
		"""
		self.driver.find_element_by_class_name( classname ).click()

	def select_classes(self, classname, index):
		"""
		選択状態にする(class)
		
		Parameters
		----------
		class : char
			選択状態にしたいclass
		index : int
			選択状態にしたいクラスの添字
		"""
		self.driver.find_elements_by_class_name( classname )[index].click()

	def click_img_by_alt(self, alt):
		"""
		imgのボタンクリック
		
		Parameters
		----------
		alt : char
			クリックしたいalt
		"""
		self.driver.find_element_by_xpath("//img[@alt='" + alt + "']").click()

	def screenshotOfDisplay(self, filename = 'screenshotOfDisplay.png'):
		"""
		ディスプレイ全体のスクリーンショット
		
		Parameters
		----------
		filename : char
			任意のファイル名。
			設定しない場合、screenshotOfDisplay.png というファイル名となる。
			ディレクトリは現在決め打ち(settings.py参照)
		"""
		# makeDirectoryIfNotExist(screenshotDirectoryName)

		sleep(2)
		path = settings.FILE_PATH + "\\" + filename
		print(path)
		img = ImageGrab.grab()
		img.save(path)

	def scroll_to(self, pitch):
		self.scroll_height = self.scroll_height + pitch
		self.driver.execute_script("window.scrollTo(0," + str(self.scroll_height) + ")")

	def scroll_to_bottom(self):
		"""
		一番下までスクロール
		
		Parameters
		----------
		なし
		"""
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
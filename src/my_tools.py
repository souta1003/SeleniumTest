from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

class MyTools():
	def __init__(self, web_driver):
		self.driver = web_driver
		self.scroll_height = 0

	### type=text の入力
	def input_text(self, name, value):
		"""
		type=text の入力
		
		Parameters
		----------
		name : char
			name要素
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='text']")
		element.send_keys(value)

	### type=number の入力
	def input_number(self, name, value):
		"""
		type=number の入力
		
		Parameters
		----------
		name : char
			name要素
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='number']")
		element.send_keys(value)

	### type=password の入力
	def input_password(self, name, value):
				"""
		type=password の入力
		
		Parameters
		----------
		name : char
			name要素
		value : char
			入力文字
		"""
		element = self.driver.find_element_by_xpath(
			"//input[@name='" + name + "'][@type='password']")
		element.send_keys(value)

	### 半角カナの文字化け入力対策 汎用版
	def input_by_name(self, name, value):
		self.driver.execute_script("document.getElementsByName('" + name + "')[0].value = '" + value + "';")

	### 半角カナの文字化け入力対策 汎用版
	def input_by_id(self, id, value):
		self.driver.execute_script("document.getElementById('" + id + "').value = '" + value + "';")

	### 半角カナの文字化け入力対策 使うのは主にこっち
	def input_text_kana_name(self, name, value):
		"""
		半角カナ入力(name)
		
		Parameters
		----------
		name : char
			入力欄のid要素
		value : char
			入力したい半角カナ
		"""
		self.input_by_name(name, value)

	### 半角カナの文字化け入力対策 使うのは主にこっち
	def input_text_kana_id(self, id, value):
		"""
		半角カナ入力(id)
		
		Parameters
		----------
		id : char
			入力欄のid要素
		value : char
			入力したい半角カナ
		"""
		self.input_by_id(id, value)

	### セレクトボックスの選択
	def select_by_value(self, name, value):
		"""
		セレクトボックスの選択
		
		Parameters
		----------
		name : char
			セレクトボックスのname要素名
		value : char
			選択状態にしたいvalue要素名
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
			クリックしたいid要素名
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
			クリックしたいname要素名
		"""
		self.driver.find_element_by_name( name ).click()

	def click_button_id(self, id):
		"""
		ボタンクリック(id)
		
		Parameters
		----------
		id : char
			クリックしたいid要素名
		"""
		self.driver.find_element_by_id( id ).click()

	def click_button_class(self, classname):
		"""
		ボタンクリック(class)
		
		Parameters
		----------
		class : char
			クリックしたいclass要素名
		"""
		self.driver.find_element_by_class_name( classname ).click()

	def click_img(self, alt):
		"""
		img要素のボタンクリック
		
		Parameters
		----------
		alt : char
			クリックしたいalt要素名
		"""
		self.driver.find_element_by_xpath("//img[@alt='" + alt + "']").click()


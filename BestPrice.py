from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import re

class Amazon:
	def __init__(self):
		self.chromepath=r"C:\\Users\\shmm\\Desktop\\ChromeDriver\\chromedriver.exe"
		self.driver=webdriver.Chrome(executable_path=self.chromepath)
		self.driver.get("https://www.amazon.in/")
		#print(self.driver.title)
		self.driver.maximize_window()

	
	def check(self):
		driver = self.driver
		window_before = driver.window_handles[0]
		print(driver.current_url)
		driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").click()
		driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys('Apple iPhone XR (64GB) Yellow')
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
		time.sleep(2)
		window_after = driver.window_handles[1]
		driver.switch_to.window(window_after)

		tree = driver.find_elements_by_xpath("//*[@id='priceblock_ourprice']")
		value = tree[0].text
		result = float(re.sub(r'[^0-9.]', '', value))
		print("Apple iPhone XR (64GB) Yellow value in Amazon :",result)
		driver.quit()
		return(result)
	
class Flipkart:
	def __init__(self):
		self.chromepath=r"C:\\Users\\shmm\\Desktop\\ChromeDriver\\chromedriver.exe"
		self.driver=webdriver.Chrome(executable_path=self.chromepath)
		self.driver.get("https://www.flipkart.com/")
		#print(self.driver.title)
		self.driver.maximize_window()
	
	def check(self):
		driver = self.driver
		window_before = driver.window_handles[0]
		print("\n")
		print(driver.current_url)
		driver.maximize_window()

		driver.implicitly_wait(2)
		try:
			if driver.switch_to_alert() != None:
				time.sleep(1)
				driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
		except:
			#print("No popup found!!")
			pass
		driver.implicitly_wait(2)
		driver.find_element_by_xpath("//div[@class='O8ZS_U']/input").click()
		driver.implicitly_wait(2)
		driver.find_element_by_xpath("//div[@class='O8ZS_U']/input").send_keys('Apple iPhone XR (64GB) Yellow')
		driver.implicitly_wait(2)
		try:
			if driver.switch_to_alert() != None:
				time.sleep(1)
				driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
		except:
			pass
		driver.find_element_by_xpath("//div[@class='O8ZS_U']/input").send_keys(Keys.ENTER)
		try:
			if driver.switch_to_alert() != None:
				time.sleep(1)
				driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
		except:
			pass
		driver.implicitly_wait(2)
		driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]").click()
		driver.implicitly_wait(2)
		driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
		driver.implicitly_wait(2)
		window_after = driver.window_handles[1]
		driver.switch_to.window(window_after)
		driver.implicitly_wait(2)
		value = driver.find_element_by_css_selector(".\_3qQ9m1")
		driver.implicitly_wait(2)
		result = value.text

		result = float(re.sub(r'[^0-9.]', '', result))
		print("Apple iPhone XR (64GB) Yellow value in Flipkart :",result)
	
		driver.quit()
		return(result)

if __name__ == '__main__':
	Amazonvalue = Amazon()
	A1 = Amazonvalue.check()
	
	Flipkartvalue = Flipkart()
	F1 = Flipkartvalue.check()
	

	if A1 > F1:
		print("\nBest price for Iphone XR (64GB) Yellow found in Flipkart : ",F1)
	else:
		print("\nBest price for Iphone XR (64GB)Yellow found in Amazon : ",A1)
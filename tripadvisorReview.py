from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

class Tripadvisor:
	def __init__(self):
		self.chromepath=r"C:\\Users\\shmm\\Desktop\\ChromeDriver\\chromedriver.exe"
		self.driver=webdriver.Chrome(executable_path=self.chromepath)
		self.driver.get("https://www.tripadvisor.in/")
		#print(self.driver.title)
		self.driver.maximize_window()

	
	def check(self):
		driver = self.driver
		window_before = driver.window_handles[0]
		print("\n")
		print(driver.current_url)
		try:
			driver.find_element_by_css_selector(".brand-global-nav-action-search-Search__searchButton--b9-IK").click()
		except :
			driver.find_element_by_xpath("//*[@id='component_4']/div/div/form/input[1]").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#mainSearch").click()
		
		driver.find_element_by_css_selector("#mainSearch").send_keys('Club Mahindra Madikeri, Coorg')
		time.sleep(2)
		driver.find_element_by_css_selector("#SEARCH_BUTTON").send_keys(Keys.ENTER)
		time.sleep(3)
		
		driver.find_element_by_class_name("result-title").click()
		
		window_after = driver.window_handles[1]
		driver.switch_to.window(window_after)
		time.sleep(4)
		driver.find_element_by_class_name("hotels-hotel-review-atf-info-parts-Rating__reviewCount--1sk1X").click()
		time.sleep(2)
		driver.find_element_by_css_selector(".hotels-community-content-common-ContextualCTA__currentOption--3Wd5D > .ui_button").click()
		time.sleep(2)
		window_after1 = driver.window_handles[2]
		driver.switch_to.window(window_after1)
		time.sleep(2)
		cal_button= driver.find_element_by_css_selector("#bubble_rating").click()
		
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='ReviewTitle']").click()
		time.sleep(1)
		driver.find_element_by_xpath("//*[@id='ReviewTitle']").send_keys("Awesome")
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='ReviewText']").click()
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='ReviewText']").send_keys("It was an amazing staying here. Staff was very amicable and the events organized was flawless.I experienced  a wonderful holiday at here with it was filled with lots of surprises and beautiful memories.")
		time.sleep(2)
		driver.find_element_by_css_selector(".category-soloTraveler").click()
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='trip_date_month_year']").click()
		time.sleep(2)
		driver.find_element_by_xpath("//*[@id='trip_date_month_year']").send_keys("October 2019")
		driver.find_element_by_xpath("//*[@id='trip_date_month_year']").send_keys(Keys.ENTER)
		time.sleep(2)
		driver.execute_script("window.scrollTo(300,900);")
		time.sleep(5)
		driver.find_element_by_xpath("//*[@id='noFraud']").click()
		time.sleep(4)
		
		'''Disabling Preview button as it is asking for credentials'''
		#driver.find_element_by_css_selector(".preview").click() 
		

		var = driver.find_element_by_class_name('ui_bubble_rating').get_attribute('class')
		review_rating = int(var.split("_")[-1])

		if (review_rating == 30):
			print("\nGiven 3 star rating is intack!!")
		else :
			print("Given Ratings are not saved corretly!!")

		
		time.sleep(5)
		driver.find_element_by_xpath("//*[@id='SUBMIT']/span").click()

		driver.quit()


if __name__ == '__main__':
	ta = Tripadvisor()
	A1 = ta.check()

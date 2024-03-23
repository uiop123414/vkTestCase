import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Используем Chrome, но можно выбрать другой браузер
        self.driver.get("https://ya.ru/")

    def test_search_selenium_on_first_position(self):


        
        # 1) Write "Sekenium" in the search bar
        search_input = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="text"]')))
        search_input.send_keys("Selenium")
        
        # 2) press Enter
        search_input.send_keys(Keys.RETURN)

        # 3) click to remove banner
        try:
            self.driver.find_element(By.XPATH,'/html/body/main/div[3]/button').click()
        except:
            print("")
        # 4) Get text from first line
        first_result_text = self.driver.find_element(By.XPATH,'//*[@id="search-result"]/li[2]/div/div[1]/a/h2/span/b').text


        expected_result = "Selenium"

        # We expect that the text of the first search result contains the word "Selenium"
        self.assertIn(expected_result, first_result_text, "Test passed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # Unique test case number
    test_case_number = "TC001"
    print(test_case_number)
        
    # Test Description
    test_case_name = "Search for Selenium on Yandex and verify it's on the first position"
    print(test_case_name)
    unittest.main()

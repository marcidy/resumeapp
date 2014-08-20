from selenium import webdriver
driver = webdriver.Firefox()
driver.set_window_size(1024, 768)
driver.maximize_window()
driver.get('http://arcidy.com')
driver.save_screenshot('/home/marcidy/Projects/Resumes/resume/resumes/static/img/resumes/1/preview.png')
driver.quit()

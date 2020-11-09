import time
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'C:\Users\user\Desktop\demo_elastic'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path=r"D:\JetBrains\chromedriver", options=options)
# driver.maximize_window()

driver.get("http://192.168.0.61:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d?_g=(filters:!(),refreshInterval:(pause:!f,value:900000),time:(from:now-1y,to:now))&_a=(description:'Analyze%20mock%20flight%20data%20for%20ES-Air,%20Logstash%20Airways,%20Kibana%20Airlines%20and%20JetBeats',filters:!(),fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!t),query:(language:kuery,query:''),timeRestore:!t,title:'%5BFlights%5D%20Global%20Flight%20Dashboard',viewMode:view)")

driver.implicitly_wait(999)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/dashboard-app/div[2]/div/div/div[2]/div/div/figcaption/h2/span/span[1]')
time.sleep(30)

scrollBy_list = [130, 195, 335, 395, 395, 415, 230, 400]
for i in range(len(scrollBy_list)):
    driver.execute_script('window.scrollBy(0,%s)' % scrollBy_list[i])
    driver.save_screenshot(r"C:\Users\user\Desktop\demo_elastic\screenshot%s.png" % str(i))

driver.quit()


import time
import json
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "scalingType": 3,
        "scaling": "70"
    }

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = r"D:\JetBrains\chromedriver"
driver = webdriver.Chrome(options=chrome_options, executable_path=CHROMEDRIVER_PATH)
driver.get("http://192.168.0.61:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d?_g=(filters:!(),refreshInterval:(pause:!f,value:900000),time:(from:now-1y,to:now))&_a=(description:'Analyze%20mock%20flight%20data%20for%20ES-Air,%20Logstash%20Airways,%20Kibana%20Airlines%20and%20JetBeats',filters:!(),fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!t),query:(language:kuery,query:''),timeRestore:!t,title:'%5BFlights%5D%20Global%20Flight%20Dashboard',viewMode:view)")
time.sleep(30)
driver.execute_script('window.print();')
time.sleep(30)
driver.quit()

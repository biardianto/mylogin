import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Read data from CSV
ph='2'
emb='soc'
fn='seed4insert_mvt_'+emb+'_ph'+ph+'.csv'
df1 = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
df = df1
# ph='2'
# fn='seed4insert_mvt_'+emb+'_ph'+ph+'.csv'
# df2 = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = df2
print("Simulate Entry SIMHAJ menu Movement Flight for Embarkasi ", str.upper(emb)," Phase ",ph)

# df = pd.read_csv('seed4insert_mvt_lop_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_mes_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_jkt_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_upg_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_bpn_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_btj_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
# df = pd.read_csv('seed4insert_mvt_soc_ph1.csv',dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# Configure the Selenium WebDriver (using webdriver-manager for simplicity)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)

# Target URL of the web form    
url = 'https://simhajtraining.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'
# url = 'https://simhaj.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'

driver.get(url)
time.sleep(2) # Wait for the page to load
# driver.quit()

driver.find_element(By.NAME, 'usernamemonitoring').send_keys(str('ch'))
driver.find_element(By.NAME, 'passwordmonitoring').send_keys(str('poskohalim'))
driver.find_element(By.NAME, 'Submit').click()

# url = 'https://simhajtraining.garuda-indonesia.com/monitoring/page_monitoring/fltmoninsert.php?embfm=&&kloterfm=&&flightnofm=&&origfm=&&registerfm=&&destfm=&&depdatefm=&&depdatetofm=&&arrdatetofm=&&arrdatefromfm='

# driver.get(url)
time.sleep(2) # Wait for the page to load

select_element = driver.find_element(By.NAME, "monitoring")
dropdown = Select(select_element)
dropdown.select_by_value("fltmon")
time.sleep(2)

# Find the element by partial link text and click it
link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Insert New Flight")
link_element.click()

idx=0
for index, row in df.iterrows():
    # if index==0: continue
    # url = 'https://simhajtraining.garuda-indonesia.com/monitoring/page_monitoring/fltmoninsert.php?embfm='+row['embinsert']+'&&kloterfm=&&flightnofm=&&origfm=&&registerfm=&&destfm=&&depdatefm=&&depdatetofm=&&arrdatetofm=&&arrdatefromfm='
    # driver.get(url)
    time.sleep(2) # Wait for the page to load

    try:
        # Find form elements by their ID, Name, or Xpath and fill them
        # Replace 'field_id_1', 'field_id_2', etc., with the actual IDs from the webpage's HTML
        # embinsert,kloterinsert,flightnoinsert,originsert,registerinsert,destinsert,depdateinsert,etdinsert,arrdateinsert,etainsert,actypeinsert
        bufactype = str(row['actypeinsert'])
        if(bufactype[:1]=="7"): bufactype = "B"+bufactype
        elif(bufactype[:1]=="3"): bufactype = "A"+bufactype
        driver.find_element(By.NAME, 'embinsert').send_keys(str(row['embinsert']))
        driver.find_element(By.NAME, 'kloterinsert').send_keys(str(row['kloterinsert']))
        driver.find_element(By.NAME, 'flightnoinsert').send_keys(row['flightnoinsert'])
        driver.find_element(By.NAME, 'originsert').send_keys(row['originsert'])
        driver.find_element(By.NAME, 'registerinsert').send_keys(row['registerinsert'])
        driver.find_element(By.NAME, 'destinsert').send_keys(str(row['destinsert']))
        driver.find_element(By.NAME, 'depdateinsert').send_keys(str(row['depdateinsert']) if len(str(row['depdateinsert']))==8 else '0'+str(row['depdateinsert']))
        driver.find_element(By.NAME, 'etdinsert').send_keys(str(row['etdinsert']) if len(str(row['etdinsert']))==4 else '0'+str(row['etdinsert']))
        driver.find_element(By.NAME, 'arrdateinsert').send_keys(str(row['arrdateinsert']) if len(str(row['arrdateinsert']))==8 else '0'+str(row['arrdateinsert']))
        driver.find_element(By.NAME, 'etainsert').send_keys(str(row['etainsert']) if len(str(row['etainsert']))==4 else '0'+str(row['etainsert']))
        driver.find_element(By.NAME, 'actypeinsert').send_keys(bufactype)
        
        # Find and click the submit button
        # print(bufactype[:2])
        # input("press enter console")
        driver.find_element(By.NAME, 'sub').click()
        time.sleep(2) # Wait for the page to load
        
        idx=idx+1
        print(f"Submitted data for row {idx} {index} {row['embinsert']}{row['kloterinsert']} ")
        # Find the element by partial link text and click it
        link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Insert New Flight")
        link_element.click()

    except Exception as e:
        print(f"Error submitting row {index}: {e} {row['embinsert']},{row['kloterinsert']},{row['flightnoinsert']},{row['originsert']},{row['registerinsert']},{row['destinsert']},{row['depdateinsert']},{row['etdinsert']},{row['arrdateinsert']},{row['etainsert']},{row['actypeinsert']}")

driver.quit()

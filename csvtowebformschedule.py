def samasama(parm1, parm2):
    """
    Purpose: parm1
    """
    return parm1==parm2


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

ph='1'
emb='lop'
fn='seed4insert_mvt_'+emb+'_ph'+ph+'.csv'
df1 = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
ph='2'
fn='seed4insert_mvt_'+emb+'_ph'+ph+'.csv'
df2 = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
print("Simulate Entry SIMHAJ menu Schedule Flight for Embarkasi ", str.upper(emb))

# LOGIN TO SIMHAJ FIRST

# CHROME
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# Configure the Selenium WebDriver (using webdriver-manager for simplicity)
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

# FIREFOX
# driver = webdriver.Firefox()

# Target URL of the web form    
url = 'https://simhajtraining.garuda-indonesia.com/login'   
# url = 'https://simhajtraining.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'
# url = 'https://simhaj.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'

driver.get(url)
time.sleep(2) # Wait for the page to load
# driver.quit()

driver.find_element(By.NAME, 'user_id').send_keys(str('y2k'))
driver.find_element(By.NAME, 'password').send_keys(str('wachid413'))
input("isi CAPTCHA dan klik submit SIGNIN manulally then press enter console")

# Find element with specific exact href
# url = 'https://simhajtraining.garuda-indonesia.com/penerbangan'
# driver.get(url)
# time.sleep(2) # Wait for the page to load

# url = 'https://simhajtraining.garuda-indonesia.com/penerbangan/show_add'
# driver.get(url)
# time.sleep(2) # Wait for the page to load

bufembarkasi=''
bufkloter=''
datajson = {}
# df1x = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
for index, row in df1.iterrows():
    url = 'https://simhajtraining.garuda-indonesia.com/penerbangan/show_add'
    driver.get(url)
    time.sleep(2) # Wait for the page to load

    bufembarkasi = row['embinsert']
    bufkloter = row['kloterinsert']
    bufflight = row['flightnoinsert'] #if(row['originsert']==row['embinsert']) elif (row['embinsert']=="JKT"): "CGK" else: "KNO"
    buforigin = row['originsert'] #if(row['originsert']==row['embinsert']) elif (row['embinsert']=="JKT"): "CGK" else: "KNO"
    bufdestination = row['destinsert'] #if(row['originsert']==row['embinsert']) else "" 
    bufregister = row['registerinsert'] #if(row['originsert']==row['embinsert']) else "" 

    if(((bufembarkasi == buforigin) or (bufembarkasi == "MES" and buforigin=="KNO") or (bufembarkasi == "JKT" and buforigin=="CGK"))):
        result1 = df1.query('embinsert==@bufembarkasi & kloterinsert==@bufkloter & originsert==@buforigin')
        bufflight1 = result1['flightnoinsert'].iloc[0]
        result11 = df1.query('embinsert==@bufembarkasi & kloterinsert==@bufkloter & flightnoinsert==@bufflight1 & (destinsert=="MED" or destinsert=="JED")')

        result2 = df2.query('embinsert==@bufembarkasi & kloterinsert==@bufkloter & (originsert=="MED" or originsert=="JED")')
        bufflight2 = result2['flightnoinsert'].iloc[0]
        result22 = df2.query('embinsert==@bufembarkasi & kloterinsert==@bufkloter & flightnoinsert==@bufflight2 & ((destinsert==@bufembarkasi) or (@bufembarkasi == "MES" and destinsert=="KNO") or (@bufembarkasi == "JKT" and destinsert=="CGK"))')
        print(result1)
        print(result11)
        print(result2)
        print(result22)
        
        select2_container = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection__placeholder"))
        )
        select2_container.click()

        target_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Pilih Embarkasi')]"))
        )
        target_option.click()

        bufembarkasi = str(result1['embinsert'].iloc[0])
        # print(bufembarkasi)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Pilih Embarkasi')]").click()
        time.sleep(2)
        input_field = driver.find_element(By.CLASS_NAME, "select2-search__field") 
        input_field.send_keys(str(result1['embinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)

        input_field = driver.find_element(By.NAME, 'kloter')
        input_field.click()
        text_to_send = str(result1['kloterinsert'].iloc[0])
        # Send keys one by one
        for character in text_to_send:
            input_field.send_keys(character)
            time.sleep(0.5)

        # PHASE I
        input_field = driver.find_element(By.NAME, 'flt_no1[]')
        input_field.click()
        input_field.send_keys(str(result1['flightnoinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)

        bufflight = str(result1['registerinsert'].iloc[0])
        # print(bufflight)
        target_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]"))
        )
        target_option.click()
        # driver.find_element(By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]").click()
        input_field = driver.find_element(By.CLASS_NAME, "select2-search__field") 
        input_field.send_keys(str(result1['registerinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)

        # PHASE II
        input_field = driver.find_element(By.NAME, 'flt_no2[]')
        input_field.click()
        input_field.send_keys(str(result2['flightnoinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)

        bufflight = str(result2['registerinsert'].iloc[0])
        # print(bufflight)
        target_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]"))
        )
        target_option.click()
        # driver.find_element(By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]").click()
        input_field = driver.find_element(By.CLASS_NAME, "select2-search__field") 
        input_field.send_keys(str(result2['registerinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)
        
        time.sleep(1)
        #SYNC TO HOME BUTTON
        target_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sync to homes')]"))
            # driver.find_element(By.XPATH, "//span[contains(text(), 'Sync to homes')]").click()
        )
        target_option.click()
        time.sleep(1) # Wait for the page to load

        #PHASE I
        input_element = driver.find_element(By.NAME, "tgl_berangkat1[]")
        current_value = driver.find_element(By.NAME, "tgl_berangkat1[]").get_attribute("value").replace("-", "")
        if (samasama(current_value,result1['depdateinsert'].iloc[0])==False):
            # comment: 
            print(f"Tanggal berangkat ph1: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "waktu_berangkat1[]")
        current_value = driver.find_element(By.NAME, "waktu_berangkat1[]").get_attribute("value").replace(":", "")
        if (samasama(current_value,result1['etdinsert'].iloc[0])==False):
            # comment: 
            print(f"Waktu berangkat ph1: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "tgl_tiba1[]")
        current_value = driver.find_element(By.NAME, "tgl_tiba1[]").get_attribute("value").replace("-", "")
        if (samasama(current_value,result11['arrdateinsert'].iloc[0])==False):
            # comment: 
            print(f"Tanggal tiba ph1: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "waktu_tiba1[]")
        current_value = driver.find_element(By.NAME, "waktu_tiba1[]").get_attribute("value").replace(":", "")
        if (samasama(current_value,result11['etainsert'].iloc[0])==False):
            # comment: 
            print(f"Waktu tiba ph1: {current_value} - BEDA")
            continue
            # pass
        # end if

        #PHASE II
        # input_element = driver.find_element(By.NAME, "tgl_berangkat2[]")
        current_value = driver.find_element(By.NAME, "tgl_berangkat2[]").get_attribute("value").replace("-", "")
        if (samasama(current_value,result2['depdateinsert'].iloc[0])==False):
            # comment: 
            print(f"Tanggal berangkat ph2: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "waktu_berangkat2[]")
        current_value = driver.find_element(By.NAME, "waktu_berangkat2[]").get_attribute("value").replace(":", "")
        if (samasama(current_value,result2['etdinsert'].iloc[0])==False):
            # comment: 
            print(f"Waktu berangkat ph2: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "tgl_tiba2[]")
        current_value =  driver.find_element(By.NAME, "tgl_tiba2[]").get_attribute("value").replace("-", "")
        if (samasama(current_value,result22['arrdateinsert'].iloc[0])==False):
            # comment: 
            print(f"Tanggal tiba ph2: {current_value} - BEDA")
            continue
            # pass
        # end if
        # input_element = driver.find_element(By.NAME, "waktu_tiba2[]")
        current_value = driver.find_element(By.NAME, "waktu_tiba2[]").get_attribute("value").replace(":", "")
        if (samasama(current_value,result22['etainsert'].iloc[0])==False):
            # comment: 
            print(f"Waktu tiba ph2: {current_value} - BEDA")
            continue
            # pass
        # end if

        # input("plis enter - COCOK")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2) # Wait for the page to load
        # if (len(driver.find_element(By.XPATH, "//li[contains(text(), 'Data kloter sudah ada')]"))>0):
        #     # comment: 
        #     continue
        # # end if
        try:
            driver.find_element(By.XPATH, "//li[contains(text(), 'Data kloter sudah ada')]")
            # print("Element exists")
            continue
        except NoSuchElementException:
            print("Element does not exist")
            continue

        time.sleep(3) # Wait for the page to load

 
        continue
    else:
        continue

    # continue

driver.quit()

quit()

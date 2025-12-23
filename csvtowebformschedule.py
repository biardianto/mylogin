import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

url = 'https://simhajtraining.garuda-indonesia.com/penerbangan/show_add'
driver.get(url)
# time.sleep(2) # Wait for the page to load
# element = driver.find_element(By.XPATH, f"//a[@href='{url}']")
# element.click()
time.sleep(2) # Wait for the page to load
# driver.quit()

bufembarkasi=''
bufkloter=''
datajson = {}
# df1x = pd.read_csv(fn,dtype={"kloterinsert":str,"depdateinsert":str,"etdinsert":str,"arrdateinsert":str,"etainsert":str})
for index, row in df1.iterrows():
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
            time.sleep(1)

        # PHASE I
        input_field = driver.find_element(By.NAME, 'flt_no1[]')
        input_field.click()
        input_field.send_keys(str(result1['flightnoinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)

        bufflight = str(result1['registerinsert'].iloc[0])
        # print(bufflight)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]").click()
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
        driver.find_element(By.XPATH, "//span[contains(text(), 'Pilih Pesawat')]").click()
        input_field = driver.find_element(By.CLASS_NAME, "select2-search__field") 
        input_field.send_keys(str(result2['registerinsert'].iloc[0]))
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)
        
        time.sleep(1)
        #SYNC TO HOME BUTTON
        driver.find_element(By.XPATH, "//span[contains(text(), 'Sync to homes')]").click()
        time.sleep(2) # Wait for the page to load
        input("plis enter")

 
        continue
    else:
        continue

    # continue

driver.quit()
quit()



# chrome_options = Options()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')
# # Configure the Selenium WebDriver (using webdriver-manager for simplicity)
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service,options=chrome_options)

# # Target URL of the web form    
# url = 'https://simhajtraining.garuda-indonesia.com/login'   
# # url = 'https://simhajtraining.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'
# # url = 'https://simhaj.garuda-indonesia.com/monitoring/monitoring.php?monitoring=fltmon'

# driver.get(url)
# time.sleep(2) # Wait for the page to load
# # driver.quit()

# driver.find_element(By.NAME, 'user_id').send_keys(str('y2k'))
# driver.find_element(By.NAME, 'password').send_keys(str('wachid413'))
# input("isi CAPTCHA dan klik submit SIGNIN manulally then press enter console")
# driver.find_element(By.NAME, 'Submit').click()

url = 'https://simhajtraining.garuda-indonesia.com/penerbangan/show_add'

driver.get(url)
time.sleep(4) # Wait for the page to load
driver.quit()

# select_element = driver.find_element(By.NAME, "monitoring")
# dropdown = Select(select_element)
# dropdown.select_by_value("fltmon")
# time.sleep(2)

# Find the element by partial link text and click it
# link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Insert New Flight")
# link_element.click()

for index, row in df1.iterrows():
    # driver.get(url)
    time.sleep(2) # Wait for the page to load

    try:
        # Find form elements by their ID, Name, or Xpath and fill them
        # Replace 'field_id_1', 'field_id_2', etc., with the actual IDs from the webpage's HTML
        # embinsert,kloterinsert,flightnoinsert,originsert,registerinsert,destinsert,depdateinsert,etdinsert,arrdateinsert,etainsert,actypeinsert
        embarkasi = str(row['embinsert'])
        kloter = str(row['kloterinsert'])
        fltno = row['flightnoinsert']
        origin = row['originsert']
        register = row['registerinsert']
        destination = str(row['destinsert'])


        driver.find_element(By.NAME, 'embarkasi').send_keys(embarkasi)
        driver.find_element(By.NAME, 'kloter').send_keys(kloter)
        driver.find_element(By.NAME, 'flt_no1[]').send_keys(fltno)
        driver.find_element(By.NAME, 'pesawat1[]').send_keys(row['flightnoinsert'])
        driver.find_element(By.NAME, 'flt_no2[]').send_keys(fltno)
        driver.find_element(By.NAME, 'pesawat2[]').send_keys(row['flightnoinsert'])
        driver.find_element(By.NAME, 'originsert').send_keys(origin)
        driver.find_element(By.NAME, 'registerinsert').send_keys(register)
        driver.find_element(By.NAME, 'destinsert').send_keys(destination)
        driver.find_element(By.NAME, 'depdateinsert').send_keys(str(row['depdateinsert']) if len(str(row['depdateinsert']))==8 else '0'+str(row['depdateinsert']))
        driver.find_element(By.NAME, 'etdinsert').send_keys(str(row['etdinsert']) if len(str(row['etdinsert']))==4 else '0'+str(row['etdinsert']))
        driver.find_element(By.NAME, 'arrdateinsert').send_keys(str(row['arrdateinsert']) if len(str(row['arrdateinsert']))==8 else '0'+str(row['arrdateinsert']))
        driver.find_element(By.NAME, 'etainsert').send_keys(str(row['etainsert']) if len(str(row['etainsert']))==4 else '0'+str(row['etainsert']))
        driver.find_element(By.NAME, 'actypeinsert').send_keys(str(row['actypeinsert']))
        
        # Find and click the submit button
        driver.find_element(By.NAME, 'sub').click()
        time.sleep(2) # Wait for the page to load
        
        print(f"Submitted data for row {index} ")
        # Find the element by partial link text and click it
        link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Insert New Flight")
        link_element.click()

    except Exception as e:
        print(f"Error submitting row {index}: {e} {row['embinsert']},{row['kloterinsert']},{row['flightnoinsert']},{row['originsert']},{row['registerinsert']},{row['destinsert']},{row['depdateinsert']},{row['etdinsert']},{row['arrdateinsert']},{row['etainsert']},{row['actypeinsert']}")

driver.quit()

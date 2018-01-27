import csv
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup

chrome = r"C:\Users\Ishant\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome)
url_extension = 'https://www.99acres.com/'
urls_page = ['https://www.99acres.com/property-in-bandra-west-mumbai-south-west-ffid-page-'+
             str(i) for i in range(1, 14)] #pagenation links

with open('C:\Users\Ishant\Desktop\\' + 'Khar(East).csv', 'a') as f:
    writer = csv.writer(f)
    rows = zip(['SuperBuiltUp Area'], ['Area'], ['Carpet Area'], ['Configuration'], ['Price'], ['Price per sq.Ft'], ['Age'],
               ['Floor Number'], ['Address'], ['Parking'], ['Furnishing'], ['Location'], '\n')
    for row in rows:
        print row
        writer.writerow(row)
        f.close
for x in range(1,14):
    driver.get(x)
    try:
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(1.5)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    except:
        print ''

    page = driver.page_source
    soup = BeautifulSoup(page,'html.parser')
    ab = soup.findAll('div', {"class": "wrapttl"}) #get all span tags which contain a tags

    for span in ab: #go through all links found on the page
        try:
            links = span.find_all('a') #extract the required links only
            for i in links:
                driver.get(url_extension+i['href'])
                pg = driver.page_source
                soup = BeautifulSoup(pg, 'html.parser')

                area = soup.find('span',{'id':'builtupArea_span'})
                if area is None:
                    area = '-'
                else:
                    area = area.text
                superbuiltuparea = soup.find('span', {'id': 'superbuiltupArea_span'})
                if superbuiltuparea is None:
                    superbuiltuparea = '-'
                else:
                    superbuiltuparea = superbuiltuparea.text

                carpetarea = soup.find('span', {'id': 'carpetArea_span'})
                if carpetarea is None:
                    carpetarea = '-'
                else:
                    carpetarea = carpetarea.text
                bedroom = soup.find('span', {'id': 'bedRoomNum'})
                if bedroom is None:
                    bedroom = ''
                else:
                    bedroom = bedroom.text
                bathroom = soup.find('span', {'id': 'bathroomNum'})
                if bathroom is None:
                    bathroom = ''
                else:
                    bathroom = bathroom.text
                balcony = soup.find('span', {'id': 'balconyNum'})
                if balcony is None:
                    balcony = ''
                else:
                    balcony = balcony.text
                configuration = bathroom + bedroom + balcony
                if configuration is None:
                    configuration = '-'
                else:
                    configuration = configuration
                price = soup.find('span',{'class':'pdPropValue'})
                if price is None:
                    price = '-'
                else:
                    price = price.text
                price_per_sq_feet = driver.find_element_by_xpath("""/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/div[3]""")
                if price_per_sq_feet is None:
                    price_per_sq_feet = '-'
                else:
                     price_per_sq_feet = price_per_sq_feet.text
                     price_per_sq_feet = re.sub('View Price Details','',price_per_sq_feet)
                     price_per_sq_feet = re.sub('@','',price_per_sq_feet)
                age = driver.find_element_by_xpath("""//*[@id="agePossessionLbl"]""")
                if age is None:
                    age = '-'
                else:
                    age = age.text

                floorno = soup.find('span', {'id': 'floorNumLabel'})
                if floorno is None:
                    floorno = '-'
                else:
                    floorno = floorno.text
                furnishing = soup.find('span', {'id': 'furnishing'})
                if furnishing is None:
                    furnishing = '-'
                else:
                    furnishing = furnishing.text
                parking = soup.find('span', {'id': 'reservedParking'})
                if parking is None:
                    parking = '-'
                else:
                    parking = parking.text
                    if parking.find('Covered') :
                        parking = re.sub('Covered','',parking)
                    else:
                        parking = re.sub('Open','',parking)
                address1 = driver.find_element_by_xpath("""/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[2]""")

                if address1 is None:
                    address1 = '-'
                else:
                    address1 = address1.text
                address2 = driver.find_element_by_xpath("""/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[3]""")
                if address2 is None:
                    address2 = ''
                else:
                    address2 = address2.text
                address = address1+address2

                print superbuiltuparea
                print carpetarea
                with open('C:\Users\Ishant\Desktop\\'+'Bandra(West).csv','a') as f:
                    writer = csv.writer(f)
                    rows = zip([superbuiltuparea], [area],[carpetarea],[configuration], [price],[price_per_sq_feet],[age],[floorno],[address],[parking],[furnishing] ,['Bandra West'],'\n')
                    for row in rows:
                        print row
                        writer.writerow(row)
                        f.close
        except Exception as e:
            with open('C:\Users\Ishant\Desktop\\' + 'log_Bandra(West).csv', 'a') as f1:
                     f1.write(str(url_extension+i['href'])+'\n')
                     f1.close()

driver.close()






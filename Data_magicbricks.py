import csv
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup

chrome = r"C:\Users\Ishant\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome)
url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=Santacruz-West&cityName=Mumbai'
driver.get(url)
for x in range(0,2):
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
    ab = soup.findAll('div', {"class": "m-srp-card__heading clearfix"}) #get all span tags which contain a tags

    for span in ab: #go through all links found on the page
        try:
            links = span.find_all('a') #extract the required links only
            for i in links:
                print i['href']

                driver.get(i['href'])
                pg = driver.page_source
                soup = BeautifulSoup(pg, 'html.parser')

                address = soup.find('span', {'class': 'prop_address'})
                if address is None:
                    address = '-'
                else:
                    address = address.text
                area = soup.find('span',{'id':'coveredAreaDisplay'})
                if area is None:
                    area = '-'
                else:
                    area = area.text

                bedroom = driver.find_element_by_xpath("""//*[@id="firstFoldDisplay"]/div[1]/div[2]/div""")
                if bedroom is None:
                    bedroom = ''
                else:
                    bedroom = bedroom.text
                bathroom = driver.find_element_by_xpath("""//*[@id="firstFoldDisplay"]/div[2]/div[2]""")
                if bathroom is None:
                    bathroom = ''
                else:
                    bathroom = bathroom.text
                pooja_room = driver.find_element_by_xpath("""//*[@id="firstFoldDisplay"]/div[3]/div[2]""")
                if pooja_room is None:
                    pooja_room = ''
                else:
                    pooja_room = pooja_room.text

                price = driver.find_element_by_xpath("""//*[@id="propertyDetailTabId"]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/meta[2]""")
                if price is None:
                    price = '-'
                else:
                    price = price.text
                price_per_sq_feet = driver.find_element_by_xpath("""//*[@id="secondFoldDisplay"]/div[1]/div[3]""")
                if price_per_sq_feet is None:
                    price_per_sq_feet = '-'
                else:
                     price_per_sq_feet = price_per_sq_feet.text
                age = driver.find_element_by_xpath("""//*[@id="agePossessionLbl"]""")
                if age is None:
                    age = '-'
                else:
                    age = age.text

                floorno = driver.find_element_by_xpath("""//*[@id="fourthFoldDisplay"]/div[3]/div[2]""")
                if floorno is None:
                    floorno = '-'
                else:
                    floorno = floorno.text
                    floorno = re.sub('&nbsp', '', floorno)
                    floorno = re.sub('()', '', floorno)
                status = driver.find_element_by_xpath("""//*[@id="fourthFoldDisplay"]/div[1]/div[2]""")
                if status is None:
                    status = '-'
                else:
                    status = status.text
                transaction = driver.find_element_by_xpath("""//*[@id="fourthFoldDisplay"]/div[2]/div[2]""")
                if transaction is None:
                    transaction = '-'
                else:
                    transaction = transaction.text
                configuration = bathroom + bedroom + pooja_room
                if configuration is None:
                    configuration = '-'
                else:
                    configuration = configuration



                with open('C:\Users\Ishant\Desktop\\'+'Santacruz(West).csv','a') as f:
                    writer = csv.writer(f)
                    rows = zip([area],['|'], [configuration], ['|'],[price], ['|'], [price_per_sq_feet], ['|'], [status],['|'],[transaction],['|'],[floorno],['|'],[address] ,'\n')
                    for row in rows:
                        print row
                        writer.writerow(row)
                        f.close
        except Exception as e:
            with open('C:\Users\Ishant\Desktop\\' + 'log_Santacruz(West).csv', 'a') as f1:
                     f1.write(str(['href'])+'\n')
                     f1.close()
    driver.find_element_by_xpath("""//*[@id="projectMiddleMainWrap"]/div[7]/span/a[5]""").click()
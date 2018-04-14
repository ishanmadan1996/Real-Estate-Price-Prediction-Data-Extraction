import csv
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup

chrome = r"C:\Users\Ishant\Downloads\chromedriver.exe" #chromedriver
driver = webdriver.Chrome(chrome) #initialise chrome webdriver
url_extension = 'https://www.99acres.com/'


with open('C:\Users\Ishant\Desktop\Data_99acres\CSV\\' + 'Mumbai.csv', 'a') as f: #creating csv file to store extracted data
    writer = csv.writer(f)
    rows = zip(['SuperBuiltUp Area'], ['Area'], ['Carpet Area'], ['Configuration'], ['Price'], ['Price per sq.Ft'], ['Age'],
               ['Floor Number'], ['Address'], ['Parking'], ['Furnishing'], ['Location'], ['Flooring'] ,'\n')
    for row in rows:
        print row
        writer.writerow(row)
        f.close
for i in range(1,2451):
    urls_page = ['https://www.99acres.com/property-in-mumbai-ffid-page-'+
             str(i)+'?sort_by=date_d']
    for k in urls_page:
        try:
            driver.get(k)
            # driver.get('https://www.99acres.com/search/property/buy/residential-all/mumbai?search_type=QS&search_location=SH&lstAcn=NPSEARCH&lstAcnId=3686471221736293&src=CLUSTER&preference=S&city=12&res_com=R&property_type=R&selected_tab=1&isvoicesearch=N&keyword=mumbai&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null') #connecting to the required website
            try:
                while True:  # used to simulate scrolling action of a webpage on selenium browser
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
            soup = BeautifulSoup(page, 'html.parser')
            ab = soup.findAll('div', {"class": "wrapttl"})  # get all span tags which contain 'a' tags

            for span in ab:  # go through all links found on the page
                try:
                    links = span.find_all('a')  # extract the required links only
                    for i in links:
                        driver.get(url_extension + i['href'])
                        pg = driver.page_source
                        soup = BeautifulSoup(pg, 'html.parser')


                        if soup.find('span', {'id': 'flooringType'}) is None:
                            flooring = ''
                        else:
                            flooring = soup.find('span', {'id': 'flooringType'}).text

                        if soup.find('span', {'id': 'builtupArea_span'}) is None:
                            area = ''
                        else:
                            area = soup.find('span', {'id': 'builtupArea_span'}).text

                        if soup.find('span', {'id': 'superbuiltupArea_span'}) is None:
                            superbuiltuparea = ''
                        else:
                            superbuiltuparea = soup.find('span', {'id': 'superbuiltupArea_span'}).text


                        if soup.find('span', {'id': 'carpetArea_span'}) is None:
                            carpetarea = ''
                        else:
                            carpetarea = soup.find('span', {'id': 'carpetArea_span'}).text

                        if soup.find('span', {'id': 'bedRoomNum'}) is None:
                            bedroom = ''
                        else:
                            bedroom = soup.find('span', {'id': 'bedRoomNum'}).text

                        if soup.find('span', {'id': 'bathroomNum'}) is None:
                            bathroom = ''
                        else:
                            bathroom = soup.find('span', {'id': 'bathroomNum'}).text

                        if soup.find('span', {'id': 'balconyNum'}) is None:
                            balcony = ''
                        else:
                            balcony = soup.find('span', {'id': 'balconyNum'}).text

                        if bathroom + bedroom + balcony is None:
                            configuration = ''
                        else:
                            configuration = bathroom + bedroom + balcony

                        if soup.find('span', {'class': 'pdPropValue'}) is None:
                            price = ''
                        else:
                            price = soup.find('span', {'class': 'pdPropValue'}).text

                        if driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/div[3]""") is None:
                            price_per_sq_feet = ''
                        else:
                            price_per_sq_feet = driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[1]/div[3]""").text
                            price_per_sq_feet = re.sub('View Price Details', '', price_per_sq_feet)
                            price_per_sq_feet = re.sub('@', '', price_per_sq_feet)

                        if driver.find_element_by_xpath("""//*[@id="agePossessionLbl"]""") is None:
                            age = ''
                        else:
                            age = driver.find_element_by_xpath("""//*[@id="agePossessionLbl"]""").text


                        if soup.find('span', {'id': 'floorNumLabel'}) is None:
                            floorno = ''
                        else:
                            floorno = soup.find('span', {'id': 'floorNumLabel'}).text

                        if soup.find('span', {'id': 'furnishing'}) is None:
                            furnishing = ''
                        else:
                            furnishing = soup.find('span', {'id': 'furnishing'}).text

                        if soup.find('span', {'id': 'reservedParking'}) is None:
                            parking = ''
                        else:
                            parking = soup.find('span', {'id': 'reservedParking'}).text
                            if parking.find('Covered'):
                                parking = re.sub('Covered', '', parking)
                            if parking.find('Open'):
                                parking = re.sub('Open', '', parking)



                        if driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[2]""") is None:
                            address1 = ''
                        else:
                            address1 = driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[2]""").text

                        if driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[3]""") is None:
                            address2 = ''
                        else:
                            address2 = driver.find_element_by_xpath(
                            """/html/body/div[4]/div[4]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div[3]""").text
                        address = address1 + address2

                        print superbuiltuparea
                        print carpetarea
                        with open('C:\Users\Ishant\Desktop\Data_99acres\CSV\\' + 'Mumbai.csv', 'a') as f:
                            writer = csv.writer(f)
                            rows = zip([superbuiltuparea], [area], [carpetarea], [configuration], [price],
                                       [price_per_sq_feet], [age], [floorno], [address], [parking], [furnishing],
                                       [i.string], [flooring],
                                       '\n')  # zip takes multiple iterables and returns an iterator of tuples
                            for row in rows:
                                print row
                                writer.writerow(row)
                                f.close
                except Exception as e:
                    with open('C:\Users\Ishant\Desktop\Data_99acres\Logs\\' + 'log_Mumbai.csv', 'a') as f1:
                        f1.write(str(url_extension + i['href']) + '\n')
                        f1.close()
        except Exception as e1:
            with open('C:\Users\Ishant\Desktop\Data_99acres\Logs\\' + 'log_Mumbai_pagelinks.csv', 'a') as f1:
                f1.write(str(url_extension + i['href']) + '\n')
                f1.close()




driver.close()






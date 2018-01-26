import csv
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import  lxml

chrome = r"C:\Users\Ishant\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome)
driver.get("https://www.99acres.com/search/property/buy/residential-all/santacruz-west-mumbai-south-west?search_type=QS&search_location=SH&lstAcn=SEARCH&lstAcnId=456325754502255&src=CLUSTER&preference=S&city=17&res_com=R&property_type=R&selected_tab=1&isvoicesearch=N&keyword_suggest=santacruz%20(west)%2C%20mumbai%20south%20west%3B&fullSelectedSuggestions=santacruz%20(west)%2C%20mumbai%20south%20west&strEntityMap=W3sidHlwZSI6ImxvY2FsaXR5In0seyIxIjpbInNhbnRhY3J1eiAod2VzdCksIG11bWJhaSBzb3V0aCB3ZXN0IiwiQ0lUWV8xNywgTE9DQUxJVFlfNDk0NCwgUFJFRkVSRU5DRV9TLCBSRVNDT01fUiJdfV0%3D&texttypedtillsuggestion=santacr&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_17%2C%20LOCALITY_4944%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&locality=4944&price_min=null&price_max=null")

url_extension = 'https://www.99acres.com/'

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

for span in ab:

        links = span.find_all('a')
        for i in links:
            driver.get(url_extension+i['href'])
            pg = driver.page_source
            soup = BeautifulSoup(pg, 'html.parser')
            div_soup = BeautifulSoup(soup,'lxml')
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
            bathroom = soup.find('span', {'id': 'bathroomNum'})
            balcony = soup.find('span', {'id': 'balconyNum'})
            configuration = bathroom.text + bedroom.text + balcony.text
            if configuration is None:
                configuration = '-'
            else:
                configuration = configuration
            price = soup.find('span',{'class':'pdPropValue'})
            if price is None:
                price = '-'
            else:
                price = price.text
            price_per_sq_feet = soup.find('div',{'class':'pdFactVal'})
            if price_per_sq_feet is None:
                price_per_sq_feet = '-'
            else:
                 for team in div_soup.findAll('div', 'pdFactVal'):
                    price_per_sq_feet = team.text
            age = soup.find('div',{'id':'agePossessionLbl'})
            if age is None:
                age = '-'
            else:
                age = age.encode('utf-8')

            print superbuiltuparea
            print carpetarea
            with open('C:\Users\Ishant\Desktop\\'+'Santacruz(West).csv','a') as f:
                writer = csv.writer(f)
                rows = zip([superbuiltuparea],['|'], [area], ['|'],[carpetarea], ['|'], [configuration], ['|'], [price],['|'],[price_per_sq_feet],['|'],[age],['|'],['Santacruz(West)'], '\n')
                for row in rows:
                    print row
                    writer.writerow(row)
                    f.close




# page_links = soup.find('div',{'class':'jpag'})
# # for i in page_links:
# #     print i
# urls_page = ['https://www.justdial.com/Mumbai/Exporters-Engineer-in-Kalpana-Cinema-Kurla-West/nct-10195860/page-'+
#              str(i) for i in range(2, 3)] #pagenation links
# for span in ab:
#     try:
#         links = span.find_all('a')  # get all a tags
#         for link in links:
#             driver.get(link['href'])
#             pg = driver.page_source
#             soup = BeautifulSoup(pg, 'html.parser')
#             ab = soup.find('span', {'class': 'telnowpr'})  # mobile no
#             info = soup.find('span', {'class': 'adrstxtr'})  # address
#             name = soup.find('span', {'class': 'fn'})  # name
#             nm = name.text
#             num = ab.text
#             addre = info.text
#             if (re.search(r'\(\w*\)', addre)):  # removing &
#                 addre = re.sub(r'\(\w*\)', '', addre)
#
#             addre = " ".join(addre.split()) #removing all extra whitespaces
#             print addre
#             print num
#             list_info = nm + '|' + num + '|' + '\t\t' + addre.rstrip('\n') + '\n'
#             with open('C:\Users\Ishant\Desktop\\' + 'Exporters_Mumbai.csv', 'a') as f:
#                 # f.write(list_info+'\n')
#                 writer = csv.writer(f)
#                 rows = zip([name.text], ['|'], [ab.text], ['|'], [addre], '\n')
#                 for row in rows:
#                     print row
#                     writer.writerow(row)
#                 f.close
#     except Exception as e:
#         with open('C:\Users\Ishant\Desktop\\'+'log_Exporters_Mumbai4.csv','a') as f1:
#             f1.write(str(link)+'\n')
#             f1.close()
# for x in urls_page:  # select the url in href for all a tags(links)
#     try:
#         driver.get(x)
#         while True:
#             last_height = driver.execute_script("return document.body.scrollHeight")
#             # Scroll down to bottom
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#             # Wait to load page
#             time.sleep(1.5)
#
#             # Calculate new scroll height and compare with last scroll height
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#             last_height = new_height
#         page = driver.page_source
#         soup = BeautifulSoup(page, 'html.parser')
#         ab = soup.findAll('span', {"class": "jcn"})
#         for span in ab:
#             try:
#                 links = span.find_all('a')  # get all a tags
#                 for link in links:
#                     # link_ad = link_ad.append(str(link['href']))
#                     driver.get(link['href'])
#                     pg = driver.page_source
#                     soup = BeautifulSoup(pg, 'html.parser')
#                     ab = soup.find('span', {'class': 'telnowpr'})  # mobile no
#                     info = soup.find('span', {'class': 'adrstxtr'})  # address
#                     name = soup.find('span', {'class': 'fn'})  # name
#                     nm = name.text
#                     num = ab.text
#                     addre = info.text
#                     if (re.search(r'\(\w*\)', addre)):  # removing &
#                         addre = re.sub(r'\(\w*\)', '', addre)
#
#                     addre = " ".join(addre.split())
#                     print addre
#                     print
#                     list_info = nm + '|' + num + '|' + '\t\t' + addre.rstrip('\n') + '\n'
#                     with open('C:\Users\Ishant\Desktop\\' + 'Exporters_Mumbai.csv', 'a') as f:
#                         # f.write(list_info+'\n')
#                         writer = csv.writer(f)
#                         rows = zip([name.text], ['|'], [ab.text], ['|'], [addre], '\n')
#                         for row in rows:
#                             print row
#                             writer.writerow(row)
#                         f.close
#             except Exception as e:
#                 with open('C:\Users\Ishant\Desktop\\' + 'log_Exporters_Mumbai5.csv', 'a') as f1:
#                     f1.write(str(link) + '\n')
#                     f1.close()
#         driver.close()
#     except Exception as ex:
#         with open('C:\Users\Ishant\Desktop\\' + 'log_jdial_Exporters_Mumbai5.csv', 'a') as f2:
#             f2.write(str(link) + '\n')
#             f2.close()
#         continue
#
#

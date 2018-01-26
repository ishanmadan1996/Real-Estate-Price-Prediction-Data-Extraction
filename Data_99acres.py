import csv
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup

chrome = r"C:\Users\Ishant\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome)
driver.get("https://www.99acres.com/search/property/buy/residential-all/mumbai-all?search_type=QS&search_location=NRI&lstAcn=NR_R&lstAcnId=-1&src=CLUSTER&preference=S&selected_tab=1&city=12&res_com=R&property_type=R&isvoicesearch=N&keyword_suggest=mumbai%20(all)%3B&fullSelectedSuggestions=mumbai%20(all)&strEntityMap=W3sidHlwZSI6ImNpdHkifSx7IjEiOlsibXVtYmFpIChhbGwpIiwiQ0lUWV8xMiwgUFJFRkVSRU5DRV9TLCBSRVNDT01fUiJdfV0%3D&texttypedtillsuggestion=Mumba&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_12%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&price_min=null&price_max=null")
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
    try:
        links = span.find_all('a')
        for i in links:
            driver.get(url_extension+i['href'])
            pg = driver.page_source
            soup = BeautifulSoup(pg, 'html.parser')
            area = soup.find('span',{'id':'builtupArea_span'})
            print area.text

            configuration = soup.find('div',{'class':'noEllipsis pdFactVal configDetails'})
            price = soup.find('span',{'class':'pdPropValue'})
            price_per_sq_feet = soup.find('div',{'class':'pdFactVal'})
            age = soup.find('div',{'id':'agePossessionLbl'})

            with open('C:\Users\Ishant\Desktop\\' + 'Santacruz(West).csv', 'a') as f:
                # f.write(list_info+'\n')
                writer = csv.writer(f)
                rows = zip([''+area.text], ['|'], [''+configuration], ['|'], [''+price.text],['|'],[price_per_sq_feet.text],['|'],[age.text],['|'],['Santacruz(West)'], '\n')
                for row in rows:
                    print row
                    writer.writerow(row)
                    f.close
    except Exception as e:
            with open('C:\Users\Ishant\Desktop\\' + 'log_Exporters_Mumbai4.csv', 'a') as f1:
                f1.write(url_extension+str(i) + '\n')
                f1.close()



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

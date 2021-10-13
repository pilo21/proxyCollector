#site http://free-proxy.cz/
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
urlList=['http://free-proxy.cz/en/proxylist/country/DE/https/ping/all',
         'http://free-proxy.cz/en/proxylist/country/DE/http/ping/all',
         'http://free-proxy.cz/en/proxylist/country/FR/https/ping/all',
         'http://free-proxy.cz/en/proxylist/country/FR/http/ping/all',
         'http://free-proxy.cz/en/proxylist/country/IT/https/ping/all',
         'http://free-proxy.cz/en/proxylist/country/IT/http/ping/all',
         'http://free-proxy.cz/en/proxylist/country/ES/https/ping/all',
         'http://free-proxy.cz/en/proxylist/country/ES/https/ping/all']



f= open("proxy.txt","w+")
       

for i in urlList:
    time.sleep(1)
    driver.get(i)
    lista=driver.find_elements_by_xpath('//*[@id="proxy_list"]/tbody/tr')
    for i in range(len(lista)):
        try:
            ip=lista[i].find_elements_by_tag_name('td')[0].text
            port=lista[i].find_elements_by_tag_name('td')[1].text
            typo=lista[i].find_elements_by_tag_name('td')[2].text
            print((lista[i].find_elements_by_tag_name('td')[0].text+':'+
                  lista[i].find_elements_by_tag_name('td')[1].text).replace(' ',''),
                  lista[i].find_elements_by_tag_name('td')[2].text)
            linea=ip+':'+port+' '#+typo
            f.write(linea+'\n')
            
        except:
            print('not founded...')
        
        
driver.close()
f.close()

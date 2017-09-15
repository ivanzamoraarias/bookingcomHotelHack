
import sys
import urllib
import urllib2
import re

from bs4 import BeautifulSoup
if not sys.argv[1] and not sys.argv[2]:
    print('No existen fechas, no se puede buscar')
    print('Formato: dd1/mm1/aa1 dd2/mm2/aa2 rooms adults child')
    sys.exit()

print(sys.argv[1])
print(sys.argv[2])
firstDate=str(sys.argv[1]).split('/')
secondDate=str(sys.argv[2]).split('/')

print("-----Booking para el Hotal Asuncion Madrid estas fechas----")
print(firstDate[0]+"----")
print(secondDate[0]+"----")
checkin_month=firstDate[1]
checkin_year=firstDate[2]
checkin_monthday=firstDate[0]

checkout_monthday=secondDate[0]
checkout_month=secondDate[1]
checkout_year=secondDate[2]

if len(sys.argv)<4:
    no_rooms =1
else:
    no_rooms = sys.argv[3]

if len(sys.argv)<5:
    group_adults = 1
else:
    group_adults = sys.argv[4]

if len(sys.argv)<6:
    group_children =0
else:
    group_children=sys.argv[5]


url = 'https://www.booking.com/searchresults.es.html'
values = {'label': 'gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaEGIAQGYAQrCAQN4MTHIAQzYAQPoAQGSAgF5qAID',
          'sid': 'e60090db197fe20c4aa33367b516e677',
          'sb': '1',
          'src': 'index',
          'src_elem': 'sb',
          'error_url': 'https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaEGIAQGYAQrCAQN4MTHIAQzYAQPoAQGSAgF5qAID%3Bsid%3De60090db197fe20c4aa33367b516e677%3Bsb_price_type%3Dtotal%26%3B',
          'ss': 'Hostal+Asunci%C3%B3n%2C+Madrid%2C+Comunidad+de+Madrid%2C+Espa%C3%B1a',
          'ssne': 'Madrid',
          'ssne_untouched': 'Madrid',
          'checkin_monthday':checkin_monthday,
          'checkin_month': checkin_month,
          'checkin_year': checkin_year,
          'checkout_monthday': checkout_monthday,
          'checkout_month': checkout_month,
          'checkout_year': checkout_year,
          'no_rooms': no_rooms,
          'group_adults': group_adults,
          'group_children': group_children,
          'from_sf': '1',
          'ss_raw': 'hostal+',
          'ac_history': '1',
          'ac_position': '0',
          'ac_langcode': 'es',
          'dest_id': '12082',
          'dest_type': 'hotel',
          'search_pageview_id': '098e2e0a6e5d0030',
          'search_selected': 'true',
          'search_pageview_id': '098e2e0a6e5d0030',
          'ac_suggestion_list_length': '5',
          'ac_suggestion_theme_list_length': '0',
          'map_tk': '1'}

data = urllib.urlencode(values)
data = data.encode('utf-8')
#print(data)
req = urllib2.Request(url, data)

resp = urllib2.urlopen(req);

urlss='https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaEGIAQGYAQrCAQN4MTHIAQzYAQPoAQGSAgF5qAID&sid=e60090db197fe20c4aa33367b516e677&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaEGIAQGYAQrCAQN4MTHIAQzYAQPoAQGSAgF5qAID%3Bsid%3De60090db197fe20c4aa33367b516e677%3Bsb_price_type%3Dtotal%26%3B&ss=Hostal+Asunci%C3%B3n%2C+Madrid%2C+Comunidad+de+Madrid%2C+Espa%C3%B1a&ssne=Madrid&ssne_untouched=Madrid&checkin_monthday=29&checkin_month='+str(checkin_month)+'&checkin_year=2017&checkout_monthday=30&checkout_month=9&checkout_year=2017&no_rooms=1&group_adults=2&group_children=0&from_sf=1&ss_raw=hostal+&ac_history=1&ac_position=0&ac_langcode=es&dest_id=12082&dest_type=hotel&search_pageview_id=098e2e0a6e5d0030&search_selected=true&search_pageview_id=098e2e0a6e5d0030&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&map_tk=1'
headers={}
headers['User-Agent']='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

reqq = urllib2.Request(url,data, headers=headers)
print('---+++------'+str(reqq))
respp=urllib2.urlopen(reqq)
print("-------++++---"+str(respp))
respddata= respp.read()
print('--**-*---'+str(respddata))
saveFie= open('index.html','w')
saveFie.write(str(respddata))
saveFie.close();

parag= re.findall(r'\b(?=\w*[US])\w+\b',respddata)
'''US$230 + por noche'''
print(str(parag))
soup= BeautifulSoup(str(respddata),"lxml");
ress= soup.findAll('b')
print('-----El precio es: -----  '+str(ress[0]).replace('<b>','').replace('</b>',''))

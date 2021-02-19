#Думаю надо подумать над переработкой. Какие мысли:
#Доработать на передачу нескольких параметров

def currency_rates(charcode):
    import requests
    import datetime
    curses = {}

    url = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")

    din=(url[0].find('<ValCurs Date="')+len('<ValCurs Date="'))
    dout=(url[0].find('" name'))

    realdate=url[0][din:dout]
    y=str(realdate)[6:]
    m=str(realdate)[3:5]
    d=str(realdate)[:2]
    print(datetime.datetime(year=int(y),month=int(m),day=int(d)))


    for i in url:
        incode = i.find('<CharCode>') + len('<CharCode>')
        outcode = i.find('</CharCode>')
        invalue = i.find('<Value>') + len('<Value>')
        outvalue = i.find('</Value>')
        codekey = i[incode:outcode]
        valuename = i[invalue:outvalue]
        curses[codekey] = valuename.replace(',','.')
    del curses['']
    curse = curses.get(charcode.upper())

    try:
        print(float(curse))
    except:
        print(None)
currency_rates('USD')
currency_rates('EUR')

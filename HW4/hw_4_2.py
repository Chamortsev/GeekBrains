def currency_rates(charcode):
    import requests

    curses = {}

    url = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")

    for i in url:
        incode = i.find('<CharCode>') + len('<CharCode>')
        outcode = i.find('</CharCode>')
        invalue = i.find('<Value>') + len('<Value>')
        outvalue = i.find('</Value>')
        codekey = i[incode:outcode]
        valuename = i[invalue:outvalue]
        curses[codekey] = valuename.replace(',', '.')
    del curses['']
    curse = curses.get(charcode.upper())

    try:
        print(float(curse))
    except:
        print(None)


currency_rates('USD')
currency_rates('EUR')

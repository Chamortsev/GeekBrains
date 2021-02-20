import urllib.request
import xml.etree.ElementTree as ET


def currency_rates(argv):
    url = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    tree = ET.parse(url)
    root = tree.getroot()
    print(root.items()[0][1])

    for i in argv:
        count = 0
        for child in root:
            for carparks in child:
                if carparks.text == i:
                    val = i
                    for carparks in child:
                        if carparks.tag == 'Value':
                            curs = carparks.text
                    print(val, curs)
                    count = count + 1
    if count == 0:
        print(None)

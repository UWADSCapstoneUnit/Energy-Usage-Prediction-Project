import ftplib
import os
import xml.etree.ElementTree as ET

def pull_forecast():
    with ftplib.FTP('ftp2.bom.gov.au', "anonymous", "guest") as ftp:
        ftp.cwd("anon/gen/")
        ftp.cwd('fwo')
        filenames = ftp.nlst()
        for filename in filenames:
            if filename == "IDW14199.xml":
                local_filename = os.path.join('Data/raw/BOM/7dayforecast/', filename)
                with open( local_filename, 'wb') as file :
                    ftp.retrbinary('RETR ' + filename, file.write)
                break
        ftp.quit()

def xml_to_frame():
    tree = ET.parse("Data/raw/BOM/7dayforecast/IDW14199.xml")
    root = tree.getroot()
    locs = root.findall(".//*[@type='location']")
    for loc in locs:
        print(loc.attrib)
        min = loc.findall(".//*[@type='air_temperature_minimum']")
        print([i.text for i in min])
        max = loc.findall(".//*[@type='air_temperature_maximum']")
        print([i.text for i in max])

#pull_forecast()
xml_to_frame()
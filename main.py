from bs4 import BeautifulSoup
import os


# Wrong format:: <string name="Start.1.CountryCode.EnterCountryNameExplain">select your country.</string>
# Fixed format:: <string name="Start_1_CountryCode_EnterCountryNameExplain">select your country.</string>

def convert_dot_to_under_bar(file):
    new_content = ""

    f = open(file, 'r')
    content = f.read()
    dir = os.path.dirname(f.name)
    soup = BeautifulSoup(content, 'lxml')
    strings = soup.find_all("string")
    for s in strings:
        content = s.text
        name = s['name']
        new_name = name.replace(".", "_")
        new_content += "<string name=\"%s\">" % new_name + content + '</string>' + "\n"

    print("string:::", new_content)

    new_file = open('%s/strings-converted.xml' % dir, 'w')
    new_file.write(new_content)
    new_file.close()

if __name__ == "__main__":
    path = input("enter file path to convert")
    convert_dot_to_under_bar(path)

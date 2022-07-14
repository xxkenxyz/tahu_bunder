from this import d
import requests

print ("""

BY XXKENXYZ

""")

domain = input("[+] input domain yang mau lu scan su")
print ("[+] sabar su baru proses scan ini ")

def main(domain):
        url = "https://sonar.omnisint.io/subdomains/{}".format(domain)
        data = requests.get(url).json()
        print ("[+] cuma dapat ini bangsat")
        for i in data:
            print (i)
            open('hasil.txt','a').write(str(i) + '\ln')

if __name__== "__main__":
        main(domain)
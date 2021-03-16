import requests
from bs4 import BeautifulSoup
import smtplib
url='https://www.amazon.in/dp/B08GYH6HKN/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=hO2Fp3FT8M7Hwq2bCwfjJw&hsa_cr_id=7816871090702&pd_rd_plhdr=t&pd_rd_r=954a5727-5ff6-4f1b-94b7-e7e353681134&pd_rd_w=NfSro&pd_rd_wg=pK5Fb&ref_=sbx_be_s_sparkle_lsi3d_asin_0_img'

headers={"User_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'}

def check_price():
    page=requests.get(url,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    # print(soup.prettify())
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[1:4])

    if(converted_price<80000):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price <80000):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('astro.paulus@gmail.com','oplejnjljkegpucs')

    subject='Price Fell Down'
    body='Check the amazon Link' 'https://www.amazon.in/dp/B08GYH6HKN/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=hO2Fp3FT8M7Hwq2bCwfjJw&hsa_cr_id=7816871090702&pd_rd_plhdr=t&pd_rd_r=954a5727-5ff6-4f1b-94b7-e7e353681134&pd_rd_w=NfSro&pd_rd_wg=pK5Fb&ref_=sbx_be_s_sparkle_lsi3d_asin_0_img'

    msg=f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'astro.paulus@gmail.com',
        'souryarouth@gmail.com',
        msg
    )

    print('Hey Email has been sent')
    server.quit()

check_price()
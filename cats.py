import requests
from email.message import EmailMessage
import smtplib
import imghdr

def retrieve_api_facts():
    # api-endpoint
    URL = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1"
   
    # sending get request and saving the response as response object
    r = requests.get(URL)
    # extracting data in json format
    data = r.json()
    return data['text']

def retrieve_api_img():
    URL = "https://cataas.com/cat/cute/says/comeme la cara"
    r = requests.get(URL)
    return r
def main():
    text = retrieve_api_facts()
    print(text)
    img = retrieve_api_img()
    file = open("cat.jpg", "wb")
    file.write(img.content)
    file.close()


    msg = EmailMessage()
    msg['Subject'] = 'Cosas de gatos para tú'
    msg['From'] = "aaronulsegura@gmail.com"
    msg['To'] = "sheila18.sa@gmail.com"
    msg.set_content(text+"\n\n Siento que esté el texto en inglés, pero te paso una foto random de un gatete!")
    with open('cat.jpg', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login("aaronulsegura@gmail.com", "ihusiayludsthprx")
        smtp.send_message(msg)





if __name__ == "__main__":
    main()


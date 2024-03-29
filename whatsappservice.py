import requests
import json

def SendMessageWhatsapp(textUser, number) :
    try:
        token = "EAALlkA1DD5kBO3KoHPPC1kWhvugisNrJQtQNbU046ro2J2l864iVZByzjdyd26EZA7wYR503eyMqza1cm36W9e1b3CyftazfiQMZCcFdBAxyuD3p6RYvloXK3c7cjfRKEnbUwxcoU9ImytOIijOnuZAek8UkKI47MW0zZBnOdp0enZBVUyAfnfraCHJUjZCj4vw"
        api_url = "https://graph.facebook.com/v19.0/242975282240040/messages"
        data = {
                    "messaging_product": "whatsapp" ,
                    "to": number ,
                    "type" : "TEXT",
                    "text" : {
                    "body": textUser
                    }
                }
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps (data) , headers = headers)

        if response.status_code == 200:
            return True

        return False
    
    except Exception as exception:
        print(exception)
        return False
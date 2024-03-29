def GetTextUser(message) :
    text = ""
    typeMessage = message ["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive" :
        interactiveObject = message["interactive"]
        typelnteractive = interactiveObject["type"]

        if typelnteractive == "button_reply" :
            text =(interactiveObject["button_reply"])["title"]
        elif typelnteractive == "list_reply":
            text= (interactiveObject["1ist_rep1y"])["tit1e"]
        else:
            print("sin mensaje")
    else:
        print ("sin mensaje")
    return text
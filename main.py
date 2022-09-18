from twilio.rest import Client

def sending_sms(text="Hello! How are you?", receiver='+78888888888'):
    try:
        account = 'bla_bla_bla_twilio'
        auth_token = "bla_bla_bla_twilio_vhvfhvfhvufhfu58y4hffddj385845fhddjhdhfdjdf"

        client = Client(account, auth_token)

        message = client.messages.create(
            body=text,
            from_="+14055925046",
            to=receiver
        )
        return "The message was successfully sent!"
    except Exception as ex:
        return "Something was wrong!", ex


def main():
    text = input("Input your text message: ")
    sending_sms(text=text, receiver='+78888888888')


if __name__ == '__main__':
    main()
    
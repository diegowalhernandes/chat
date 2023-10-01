import flet as ft

def main(pages):
    text = ft.Text("Hello World!")

    chat = ft.Column()

    userName = ft.TextField(label="write your name")

    def sendTunnelMessage(message):
        tipo = message["tipo"]
        if tipo == "message":
            textMessage = message["text"]
            userMessage = message["user"]

            chat.controls.append(ft.Text(f"{userMessage} : {textMessage}"))
        else:
            userMessage = message["user"]
            chat.controls.append(ft.Text(f"{userMessage} entrou no chat", size=12, italic=True, color=ft.colors.AMBER_700))
        pages.update()

    pages.pubsub.subscribe(sendTunnelMessage)

    def sendMessage(e):
        pages.pubsub.send_all({"text": mensageField.value, "user": userName.value,
                               "tipo": "message"})
        mensageField.value = ""
        pages.update()

    mensageField = ft.TextField(label="type a message")    
    sendMessageButton = ft.ElevatedButton("Send", on_click=sendMessage)

    def enterModal(e):
        pages.pubsub.send_all({"user": userName.value, "tipo": "entrada"})
        pages.add(chat)
        modal.open = False
        pages.remove(buttonInit)
        pages.add(ft.Row(
            [mensageField, sendMessageButton]
        ))
        pages.remove(text)
        pages.update()

    modal = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Welcome Matrix"),
        content=userName,
        actions=[ft.ElevatedButton("Enter", on_click=enterModal)],
    )

    def enterChat(e):
        pages.dialog = modal
        modal.open = True
        pages.update()
    
    buttonInit = ft.ElevatedButton("Enter Chat", on_click=enterChat)

    pages.add(text)
    pages.add(buttonInit)
    
ft.app(target=main, view=ft.WEB_BROWSER)
import flet as ft

def main(pages):
    text = ft.Text("Hello World!")

    chat = ft.Column()

    userName = ft.TextField(label="write your name")

    def sendTunnelMessage(message):
        chat.controls.append(ft.Text(message))
        pages.update()

    pages.pubsub.subscribe(sendTunnelMessage)

    def sendMessage(e):
        pages.pubsub.send_all(mensageField.value)
        mensageField.value = ""
        pages.update()

    mensageField = ft.TextField(label="type a message")    
    sendMessageButton = ft.ElevatedButton("Send", on_click=sendMessage)

    def enterModal(e):
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
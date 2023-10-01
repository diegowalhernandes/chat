import flet as ft

def main(pages):
    text = ft.Text("Hello World!")

    userName = ft.TextField()
    modal = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Welcome Matrix"),
        content=userName,
        actions=[ft.ElevatedButton("Enter")]
    )

    def enterChat(e):
        pages.dialog = modal
        modal.open = True
        pages.update()
    
    buttonInit = ft.ElevatedButton("Enter Chat", on_click=enterChat)

    pages.add(text)
    pages.add(buttonInit)
    
ft.app(target=main, view=ft.WEB_BROWSER)
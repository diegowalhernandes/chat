import flet as ft

def main(pages):
    text = ft.Text("Hello World!")
    buttonInit = ft.ElevatedButton("Init Chat")
    pages.add(text)
    pages.add(buttonInit)
    
ft.app(target=main, view=ft.WEB_BROWSER)
import flet as ft

def main(pages):
    text = ft.Text("Hello World!")
    pages.add(text)
ft.app(target=main)
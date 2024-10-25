from flet import *
def main(page:Page):
    pass
    page.bgcolor=colors.RED
    image = Image(src="logo.png")
    page.add(image)
    page.update()
app(main)
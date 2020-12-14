from pypercard import Card, CardApp

card = Card("hello",text="Hello World",text_color="yellow")

app = CardApp(stack=[card,])

app.run()
import turtle

# turtle.Screen() allows you to define your screen size

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#E314C7")

# dictionary of colors

color = {
  "blue": "#8AB6E4",
  "magenta": "#E314C7",
  "red": "#E72D2D",
  "gray": "#373535",
  "black": "#000000"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(color["blue"])

artist.penup()
artist.goto(0, 50)


style = ("Cursive", 30, "normal")
artist.write("--------------", font = style, align = "center")
artist.hideturtle()

artist.goto(0,0)
artist.color(color["black"])
style = ("Cursive", 30, "normal")
artist.write("Happy Thursday!", font = style, align = "center")
artist.hideturtle()

artist.goto(0, -50)
artist.color(color["blue"])
style = ("Cursive", 30, "normal")
artist.write("--------------", font = style, align = "center")
artist.hideturtle()

artist.goto(0, -200)
artist.color(color["gray"])
style = ("Comfortaa", 30, "normal")
artist.write("- Visham", font = style, align = "center")
artist.hideturtle()
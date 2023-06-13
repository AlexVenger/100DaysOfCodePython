import turtle
import prettytable


chungus = turtle.Turtle()
chungus.shape("turtle")
chungus.forward(100)

screen = turtle.Screen()
screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"], "r")
table.add_column("Type", ["Fire", "Water", "Grass", "Electric"], "l")

print(table)

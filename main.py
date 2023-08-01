import turtle
import pandas

screen = turtle.Screen()
screen.title("Italy Regions Game")
image = "italy_empty_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("20_regions.csv")
all_regions = data.region.to_list()
guessed_regions = []

while len(guessed_regions) < 20:
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/20 Guess the Region",
                                     prompt="What's ANOTHER region's name?").title()
    if answer_region == "Exit":
        missing_regions = []
        for region in all_regions:
            if region not in guessed_regions:
                missing_regions.append(region)
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv("regions_to_learn.csv")
        break
    if answer_region in all_regions:
        if answer_region not in guessed_regions:
            guessed_regions.append(answer_region)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            region_data = data[data.region == answer_region]
            t.goto(int(region_data.x), int(region_data.y))
            t.write(region_data.region.item())

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


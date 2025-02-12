import turtle
import pandas

# Set up the screen and load the map image
screen = turtle.Screen()
screen.title("Italy Regions Game")
image = "italy_empty_map.gif"
screen.addshape(image)
turtle.shape(image)

# Load regions with their coordinates from the CSV file
data = pandas.read_csv("20_regions.csv")  # Read the 20 regions CSV file containing coordinates
regions_data = pandas.read_csv("regions_to_learn.csv")  # Read the regions_to_learn.csv to track guessed regions

# List of all regions and initialize the guessed regions
all_regions = data['region'].to_list()
guessed_regions = []

# Game loop: ask the user to guess a region
while len(guessed_regions) < 20:
    answer_region = screen.textinput(title="{len(guessed_regions)}/20 Guess the Region",
                                     prompt="What's ANOTHER region's name?").title()

    if answer_region == "Exit":
        # Save the missing regions back into the CSV file
        missing_regions = [region for region in all_regions if region not in guessed_regions]
        new_data = pandas.DataFrame(missing_regions, columns=["region"])
        new_data.to_csv("regions_to_learn.csv", index=False)
        break

    if answer_region in all_regions:
        if answer_region not in guessed_regions:
            guessed_regions.append(answer_region)

            # Create a turtle object to mark the guessed region on the map
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            # Find the region's coordinates from the CSV
            region_data = data[data.region == answer_region]
            x, y = int(region_data.x), int(region_data.y)

            # Move to the correct coordinates on the map
            t.goto(x, y)
            t.write(answer_region, font=("Arial", 10, "normal"))

# End the game when done
turtle.mainloop()

# How I found the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

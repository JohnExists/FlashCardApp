from Button import Button

# import pygame module in this program
import pygame

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.font.init()
pygame.display.init()

# assigning values to X and Y variable
# create the display surface object
# of specific dimension..e(X, Y).
canvas = pygame.display.set_mode((400, 400))

# set the pygame window name
pygame.display.set_caption('Flashcard Game')

button = Button(10, 10, 100, 50, "+ New")

while True:
    # completely fill the surface object
    # with white color
    x, y = pygame.mouse.get_pos();
    button.hover(x, y)

    canvas.fill((75, 75, 75))
    button.draw(canvas)

    if (button.isClicked()):
        print("H!I")

    mouseClicked = False

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            button.click()
            mouseClicked = True

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

    # Draws the surface object to the screen.

    pygame.display.update()
    if (not mouseClicked): button.remove_click()
    print(mouseClicked)



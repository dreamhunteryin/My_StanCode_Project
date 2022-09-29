"""
File: bouncing_ball.py
Name:Shih Min Yin
-------------------------
The program make the bouncing ball drop and bounce according to gravity and initial velocity
"""


from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball_is_drop = False
cycle = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball_is_drop, cycle, ball, vy

    onmouseclicked(start)
    ball = int_ball()
    window.add(ball)
    vy = 0


def drop_the_ball():
    """
    The function will drop the ball until if the ball is not drop yet, until reach 3 cycle
    """

    global ball_is_drop, cycle, ball, vy

    while ball_is_drop and cycle <= 2:
        vy += GRAVITY
        ball.move(VX, vy)

        if ball.x > window.width:
            cycle += 1
            ball = int_ball()
            window.add(ball)
            ball_is_drop = False
            break

        if vy >= 0 and ball.y + ball.height >= window.height: # when reaching the window floor
            vy = -vy * REDUCE

        pause(DELAY)


def start(click):
    """
    The function receive the action of mouseclick, then change the status of ball-dropped or not
    """
    global ball_is_drop, cycle

    if not ball_is_drop:
        ball_is_drop = True
        drop_the_ball()


def int_ball():
    """
    The function create the object with oval figure that size and initial position as CONSTANT given
    """
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    return ball


if __name__ == "__main__":
    main()

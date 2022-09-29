"""
File: babygraphics.py
Name: Yin Shih Min
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_y_coordinate(height, rank):
    """
    Input:
    height (int): The width of the canvas
    rank (int): The rank of the current year according to specific name
    """
    rank_y = rank * height / MAX_RANK
    return rank_y


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    margin = GRAPH_MARGIN_SIZE
    year_width = ((width - margin * 2) / len(YEARS))
    x_coordinate = margin + year_width * (year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    margin = GRAPH_MARGIN_SIZE
    c_w = CANVAS_WIDTH
    c_h = CANVAS_HEIGHT
    canvas.create_line(margin, margin, c_w - margin, margin, width=LINE_WIDTH)
    canvas.create_line(margin, c_h - margin, c_w - margin, c_h - margin, width=LINE_WIDTH)

    n = 0
    for year in YEARS:
        year_x = get_x_coordinate(c_w, n) # 得到該年分的x座標值
        canvas.create_line(year_x, margin, year_x, c_h - margin, width=LINE_WIDTH)
        canvas.create_text(year_x + TEXT_DX, c_h - margin, text=f'{year}', anchor=tkinter.NW, font='times 15')
        n += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    c_w = CANVAS_WIDTH
    c_h = CANVAS_HEIGHT
    margin = GRAPH_MARGIN_SIZE
    n = 0
    c = 0
    year0 = str(YEARS[0])
    rank = None
    old_rank = None

    for name in lookup_names:
        dic_yr_rank = name_data[name]  # 把名字後面的year:rank放入dictionary
        old_x = get_x_coordinate(c_w, n)

        if year0 not in dic_yr_rank: # 如果第一個年份，在該名字中找不到
            old_y = c_h - margin * 2
        else:
            old_rank = dic_yr_rank[year0]
            old_y = get_y_coordinate(c_h, int(old_rank))
        for year in YEARS:
            year_x = get_x_coordinate(c_w, n)
            if str(year) not in dic_yr_rank: # 如果該個年份，在該名字中找不到
                rank_y = c_h - margin * 2

            else:
                rank = int(dic_yr_rank[f'{year}'])
                rank_y = get_y_coordinate(c_h, rank)

            if old_y == c_h - margin * 2: # 如果超出底線，名字後面為*
                canvas.create_text(old_x + TEXT_DX, old_y, text=f'{name}, *', anchor=tkinter.NW,
                                   font='times 10')
            else:
                canvas.create_text(old_x + TEXT_DX, old_y, text=f'{name}{old_rank}', anchor=tkinter.NW, font='times 10')

            canvas.create_line(old_x, int(old_y) + margin, year_x, int(rank_y) + margin, width=LINE_WIDTH,
                               fill=COLORS[c])

            old_x = year_x
            old_y = rank_y
            old_rank = rank
            n += 1

        n = 0
        if c + 1 < len(COLORS):
            c += 1
        else:
            c = 0
        canvas.create_text(old_x + TEXT_DX, old_y, text=f'{name}{old_rank}', anchor=tkinter.NW, font='times 10')


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

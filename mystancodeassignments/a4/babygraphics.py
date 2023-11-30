"""
File: babygraphics.py
Name: 
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
    avg = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * avg
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x_coord = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coord, GRAPH_MARGIN_SIZE, x_coord, CANVAS_HEIGHT)

        # 在每个垂直线的右侧添加年份标签
        canvas.create_text(x_coord + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX, text=str(YEARS[i]),
                           anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # 在name_data裡面找到排名
    # 排名數=y座標
    # step 1: 取得每個名字 for name in lookup_names: ...
    # step 2: 針對每個名字取得名次資料 name_data[name]
    # step 3：取得個年份名次
    # step 4: for loop 把line 跟 text 同時印出來
    def get_y_coordinate(rank):
        """
        給定一個排名，返回在畫布上的相應y坐標。
        input:
            rank（int）：名字的排名。
        return:
            int：畫布上的y坐標。
        """
        return GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * (int(rank) / 1000)

    # 計算每年空間的平均寬度
    avg = (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    count = 0
    # 遍歷要繪製的名字
    for name in lookup_names:
        # 獲取名字的數據
        new_ranking = name_data[name]
        print(f"Drawing data for {name}: {new_ranking}")

        if len(lookup_names) > len(COLORS):
            extra_colors = ['Yellow', 'Pink', 'Orange']
            COLORS.extend(extra_colors)
        color = COLORS[count]
        count += 1

        # 遍歷年份並繪製線條
        for i in range(len(YEARS) - 1):
            year_str = str(YEARS[i])
            next_year_str = str(YEARS[i + 1])

            if year_str in new_ranking and next_year_str in new_ranking:
                x1 = GRAPH_MARGIN_SIZE + i * avg
                y1 = get_y_coordinate(new_ranking[year_str])
                x2 = GRAPH_MARGIN_SIZE + (i + 1) * avg
                y2 = get_y_coordinate(new_ranking[next_year_str])
                # Draw line segment
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

                # Draw text label for the last year's rank
                if i == 0:
                    text_x = x1 + TEXT_DX
                    text_y = y1
                    rank_text = new_ranking[year_str]
                    canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                       fill=color)
                    canvas.create_text(x2 + TEXT_DX, y2, anchor=tkinter.SW, text=f"{name} {int(new_ranking[next_year_str])}",
                                       font="times", fill=color)
                else:
                    text_x = x2 + TEXT_DX
                    text_y = y2
                    rank_text = new_ranking[next_year_str]
                    canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                       fill=color)
            else:
                # If the name has no data for the current year, set y1 and y2 to the bottom
                x1 = GRAPH_MARGIN_SIZE + i * avg
                x2 = GRAPH_MARGIN_SIZE + (i + 1) * avg
                if year_str not in new_ranking and next_year_str in new_ranking:
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y2 = get_y_coordinate(new_ranking[next_year_str])
                    r = 0

                elif year_str in new_ranking and next_year_str not in new_ranking:
                    y1 = get_y_coordinate(new_ranking[year_str])
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    r = 1

                elif year_str not in new_ranking and next_year_str not in new_ranking:
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    r = 2

                # Draw line segment
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

                # Draw text label for the last year's rank with '*'
                if i == 0:
                    text_x = x1 + TEXT_DX
                    text_y = y1
                    if r == 0 or r == 2:
                        rank_text = '*'
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)
                    else:
                        text_x = x1 + TEXT_DX
                        text_y = y1
                        rank_text = new_ranking[year_str]
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)
                    if r == 1 or r == 2:
                        text_x = x2 + TEXT_DX
                        text_y = y2
                        rank_text = '*'
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)
                    else:
                        text_x = x2 + TEXT_DX
                        text_y = y2
                        rank_text = new_ranking[next_year_str]
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)
                else:
                    if r == 1 or r == 2:
                        text_x = x2 + TEXT_DX
                        text_y = y2
                        rank_text = '*'
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)
                    else:
                        text_x = x2 + TEXT_DX
                        text_y = y2
                        rank_text = new_ranking[next_year_str]
                        canvas.create_text(text_x, text_y, anchor=tkinter.SW, text=f"{name} {rank_text}", font="times",
                                           fill=color)


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

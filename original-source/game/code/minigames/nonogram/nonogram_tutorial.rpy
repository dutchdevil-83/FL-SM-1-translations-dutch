screen nonogram_tutorial(jump_to=None):
    modal True

    default page = 1
    if page == 1:
        use nonogram_tutorial_1
    elif page == 2:
        use nonogram_tutorial_2
    elif page == 3:
        use nonogram_tutorial_3
    elif page == 4:
        use nonogram_tutorial_4
    elif page == 5:
        use nonogram_tutorial_5
    if page < 5:
        button action SetScreenVariable("page", page + 1)
    else:
        if jump_to == None:
            button action [SetVariable("nonogram_timer_pause", False), Hide()]
        else:
            button action [Hide(), Jump(jump_to)]
    hbox:
        style_prefix "nonogram_tutorial_page"
        if page > 1:
            imagebutton auto "images/ui/phone/phone_back_%s.webp" yalign 0.5 focus_mask True action SetScreenVariable("page", page - 1)
        else:
            null height 57 width 41
        text _("Page {}".format(page))
        if page < 5:
            imagebutton auto "images/ui/phone/phone_next_%s.webp" yalign 0.5 focus_mask True action SetScreenVariable("page", page + 1)
        else:
            null height 57 width 41
    if jump_to == None:
        imagebutton auto "images/ui/buttons/close_%s.webp" xalign 0.99 yalign 0.99 action [SetVariable("nonogram_timer_pause", False), Hide()] focus_mask True
    else:
        imagebutton auto "images/ui/buttons/close_%s.webp" xalign 0.99 yalign 0.99 action [Hide(), Jump(jump_to)] focus_mask True
screen nonogram_tutorial_1():
    style_prefix "nonogram_tutorial_1"

    add "nonogram_tutorial_1"
    text _("Your goal in these puzzles is to fill the whole grid with green and black squares.\n\nAbove and to the left of the grid are numbers. These are the indicator numbers that tell you the number of green squares in that specific row and column.\n\nExample. If the row has a '3' next to it, that means there will be a set of three green (connected) squares somewhere in that row. It is the same for columns based on the numbers at the top of the puzzle. A '2' at the top of a column means that in that column, there is a set of two green squares running vertically.")
screen nonogram_tutorial_2():
    style_prefix "nonogram_tutorial_2"

    add "nonogram_tutorial_2"
    text _("You will notice some rows/columns have 2 numbers.\n\nIf you see '2 1', that tells you that somewhere in that line will be a run of exactly 2 green squares, followed by 1 or more black squares, followed by 1 green square.\n\nThere might be black squares before or after the green squares - only the runs of green squares are counted.")
screen nonogram_tutorial_3():
    style_prefix "nonogram_tutorial_2"

    add "nonogram_tutorial_3"
    text _("Left-click on a square to make it green. Right-click to mark with black.\n\nIn our system, the black squares represent the empty or blank squares and the green squares are the coded or filled squares.\n\nYou do not need to fill in the blank squares by marking them if you do not want to. It is not required to solve the puzzle.")
screen nonogram_tutorial_4():
    style_prefix "nonogram_tutorial_1"

    add "nonogram_tutorial_4"
    text _("It is strongly advised never to guess. Only squares that can be determined by logic should be coded or filled green.\n\nIt is easy for a single error to cause inaccuracies across the entire puzzle.\n\nSimple puzzles can usually be solved by figuring out the reasoning by focusing on a single row/column at a time. Then move to the next row and the next row until you have filled all the green squares.")
screen nonogram_tutorial_5():
    style_prefix "nonogram_tutorial_3"

    add "nonogram_tutorial_5"
    text _("Some more challenging puzzles may also require several types of reasoning that include more than one row (or column).\n\nYou might think that you have the correct answer for one row, but your answer might not work for an intersecting column. Resolving these contradictions is key to solving more complicated puzzles.\n\nWhen a cell cannot be a coded/green square because some other cell would produce an error, it should be a black/blank square - and vice versa.\n\nWhen you are confident in your solution, click the checkmark to submit the program for code review.")
style nonogram_tutorial_page_hbox:
    xalign 0.01
    yalign 0.99
    spacing 15
style nonogram_tutorial_page_text:
    size 40
    color "#dff8e1"
    yalign 0.5
style nonogram_tutorial_1_text:
    xalign 0.5
    yalign 0.05
    xsize 820
    text_align 0.5
    color "#dff8e1"
    size 31
style nonogram_tutorial_2_text:
    xalign 0.8
    yalign 0.15
    xsize 820
    text_align 0.5
    color "#dff8e1"
    size 31
style nonogram_tutorial_3_text:
    xalign 0.1
    yalign 0.15
    xsize 820
    text_align 0.5
    color "#dff8e1"
    size 31

define config.pre_screenshot_actions = [Hide("screenshot_screen", immediately=True), Hide("notify", immediately=True)]
define config.screenshot_callback = screenshot_callback_func
define screenshot_fade = 2


init -2 python:
    def screenshot_callback_func(file_name):
        renpy.show_screen("screenshot_screen", file_name)
        renpy.restart_interaction()

screen screenshot_screen(file_name):
    image "images/BookMenu/screenshot.png":
        align (0.05, 0.05)
        at Appear_ZoomOvershoot
    # vbox:
    #     align (0.5, 0.5)
    #     ysize 500
    #     xsize 1000

    #     text "A SCREENSHOT WAS TAKEN YAAAAAAY":
    #         size 30
    #         align (0.05, 0.05)
        # text "WITH THE NAME [file_name]":
        #     align (0.5, 0.5)
    # frame:
    #     align (0.5, 0.5)
    #     vbox:
    #         ysize 500
    #         xsize 1000
    #         text "A SCREENSHOT WAS TAKEN YAAAAAAY":
    #             align (0.5, 0.5)
    #         text "WITH THE NAME [file_name]":
    #             align (0.5, 0.5)
    
    timer screenshot_fade action Hide("screenshot_screen", transition=Dissolve(1.0))

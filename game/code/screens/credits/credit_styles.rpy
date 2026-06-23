## styles: change fonts, colours, et cetera over here

## style definitions

style credits_text:
    textalign 0.5

style about_header:
    size 60

style credits_category_header:
    size 50

# inherit style from text_button
style credits_url_button is text_button

#########################################################################################################################  

# style definitions only used by template 1
style creditshalf_hbox:
    xsize 400
    xalign 0.5
    yalign 0.5
    xfill True

style creditssmall_grid:
    xspacing 100
    # vertical spacing
    yspacing 100
    xalign 0.5
    xsize 1000


style credits_name:
    size 50
    #bold True
    textalign 0.5
    xalign 0.5

style credits_role:
    size 30
    textalign 0.5
    xalign 0.5
    
# inherit style from hyperlink_text
style credits_url_text is hyperlink_text
style credits_url_text:
    size 30

#########################################################################################################################    

# style definitions only used by template 2

style credits_name_small:
    size 25
    bold True

style credits_role_small:
    size 20

# inherit from hyperlink_text
style credits_url_text_small is hyperlink_text
style credits_url_text_small:
    size 15
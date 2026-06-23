define config.show = show_with_missing_support

init -1 python:
    
    # Change this to false to remove the notify warnings
    show_image_warnings = True
    def missing_img_callback(file_name):
        return Null()

    def show_with_missing_support(name, at_list=[], layer=None, what=None, zorder=0, tag=None, behind=[], atl=None, **kwargs):
        if renpy.has_image(name):
            renpy.show(name, at_list, layer, what, zorder, tag, behind, atl, **kwargs)
            return
        
        if renpy.can_show(name[0]):
            renpy.show(name, at_list, layer, what, zorder, tag, behind, atl, **kwargs)
            return

        if show_image_warnings and config.developer:
            renpy.show(name, at_list, layer, what, zorder, tag, behind, atl, **kwargs)
            
        print(f"HAS NO IMAGE NAMED {name}, PLEASE VERIFY")
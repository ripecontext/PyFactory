

def convert_to_screenspace_coords(pos, offset, zoom):

    offset_coords = [pos[0] - offset[0], pos[1] - offset[1]]
    zoom_adjusted = [offset_coords[0] * zoom, offset_coords[1] * zoom]
    return zoom_adjusted

def convert_from_screenscape_coords(pos, offset, zoom):

    zoom_unadjusted = [pos[0] / zoom, pos[1] / zoom]
    unoffset_coords = [zoom_unadjusted[0] + offset[0], zoom_unadjusted[1] + offset[1]]
    return unoffset_coords
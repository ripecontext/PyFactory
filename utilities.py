

def convert_to_screenspace_coords(pos, offset, zoom):

    offset_coords = [pos[0] - offset[0], pos[1] - offset[1]]
    zoom_adjusted = [offset_coords[0] * zoom, offset_coords[1] * zoom]
    return zoom_adjusted
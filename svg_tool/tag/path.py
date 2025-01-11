from . import base


class Path(base.Tag):
    fill = None
    stroke = None
    stroke_width = 1
    # TODO: class that interprets & holds `d` values
    # -- also needs to be able to create an enclosed shape
    # --- L to start from last (x,y)
    # --- shapes can be concave! break into simple AABBs first!
    # --- e.g. "left" of segment A in AABB A1

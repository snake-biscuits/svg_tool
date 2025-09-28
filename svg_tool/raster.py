from __future__ import annotations

import PIL

from . import parse
from .utils import vector


class Layer:
    gradient: parse.parents.Gradient
    mask: parse.parents.Mask
    mode: str = "RGBA"
    shape: parse.Shape

    def __init__(self):
        self.gradient = None
        self.mask = None

    @property
    def image(self) -> PIL.Image:
        canvas = PIL.Image.new(self.mode, self.size)
        artist = Artist(canvas)
        artist.draw(self.shape)
        return canvas


class Artist:
    cursor: vector.vec2

    def __init__(self, canvas: PIL.Image):
        self.pen = PIL.ImageDraw(canvas)
        self.cursor = vector.vec2(0, 0)

    def draw(self, shape: parse.Shape):
        # TODO: masking
        # -- have to split the mask <g> off into it's own Svg
        # -- then use Svg(mask).image to get the mask for Image.paste()
        match shape.tag:
            case "circle": self.draw_circle(shape)
            case "elipse": self.draw_elipse(shape)
            case "line": self.draw_line(shape)
            case "path":
                for instruction in shape.route.instructions:
                    ...
                    # TODO: function pointer table to draw each instruction
                    # instruction = ("mode", *args: List[float])
            case "rect": self.draw_rect(shape)

    # NOTE: each drawing should update self.cursor
    # -- how? idk!
    def draw_circle(self, shape):
        xy = shape.origin
        radius = shape.radius
        outline = shape.style.stroke
        fill = shape.style.fill
        width = shape.style.thickness
        self.pen.circle(xy, radius, fill, outline, width)

    def draw_line(self, shape):
        raise NotImplementedError()
        self.pen.line((start, end), fill)

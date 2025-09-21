from __future__ import annotations
from typing import Dict, List

import PIL

from . import tags


class Layer:
    # cache
    masks: Dict[str, Layer]
    gradients: Dict[str, Layer]
    children: List[Layer]
    # state
    tag: tags.Tag
    # bounds: ...  # ass.AABB but 2D?
    mask: str  # url(#mask)
    gradient: str  # url(#gradient)
    transform: tags.Transform  # ass.vec2 math
    # image
    mode: str = "RGBA"

    @property
    def size(self) -> (int, int):
        # TODO: tag -> bounds -> size
        # NOTE: need to round up to ints for PIL
        raise NotImplementedError()

    # TODO: self.tag.children -> self.children
    # def ???:
    #     for tag in self.tag.children:
    #         # TODO: sort / filter
    #         # -- script
    #         # -- style
    #         # -- <g> group
    #         # -- mask
    #         # -- gradient

    # TODO: cache until state changes
    @property
    def image(self) -> PIL.Image:
        canvas = PIL.Image.new(self.mode, self.size)
        artist = Artist(canvas)
        artist.draw(self.tag)
        raise NotImplementedError()
        # TODO: composite child layers w/ paste
        # -- simple way of handling transforms
        for layer in self.children:
            # TODO: paste mask
            # TODO: apply gradient
            canvas.paste(layer.image, layer.bounds)
        return canvas


class Artist:
    # cursor: vector.vec2  # from ass

    def __init__(self, canvas: PIL.Image):
        self.pen = PIL.ImageDraw(canvas)
        # self.cursor = vector.vec2()

    def draw(self, tag: tags.Tag):
        # TODO: masking
        # -- have to split the mask <g> off into it's own Svg
        # -- then use Svg(mask).image to get the mask for Image.paste()
        match tag.type:
            case "circle":
                self.draw_circle_fill(tag.center, tag.radius, tag.fill)
                self.draw_circle_stroke(
                    tag.center, tag.radius, tag.stroke, tag.thickness)
            case "line":
                ...
            case "path":
                # TODO: step by step lines & arcs w/ cursor position state
                ...
            case "rect":
                ...

    # NOTE: each drawing should update self.cursor
    # -- how? idk!
    def draw_circle_fill(self, center, radius, colour):
        ...

    def draw_circle_stroke(self, center, radius, colour, thickness):
        ...

    def draw_line(self, start, end, colour):
        self.pen.line((*start, *end), fill=colour)

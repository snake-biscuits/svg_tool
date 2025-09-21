from __future__ import annotations

from lxml import etree

from ..utils.colour import Colour


# TODO: cascading
# -- <style>
# -- <g> children
class Tag:
    type: str
    # indices / style
    # TODO: "id", "class"
    # common style attributes
    # TODO: "style" -> attributes
    fill_colour = Colour.from_css("transparent")
    stroke_colour = Colour.from_css("black")
    thickness: str = "1"  # TODO: Unit class (px vs. %age)
    # anything else? transform(s)?

    def __init__(self, type_: str, fill=None, stroke=None, thickness=None):
        self.type = type_
        self.fill_colour = self.fill_colour if fill is None else fill
        self.stroke_colour = self.stroke_colour if stroke is None else stroke
        self.thickness = self.thickness if thickness is None else thickness

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} @ 0x{id(self):016X}>"

    def __str__(self) -> str:
        etree.to_string(self.as_xml())

    def as_xml(self) -> etree.Element:
        raise NotImplementedError()

    # apply transform (implemented by subclass)
    def translate(self, x: float = 0, y: float = 0) -> Tag:
        raise NotImplementedError()

    @classmethod
    def from_tag(cls, element: etree.Element) -> Tag:
        type_ = element.tag
        fill = element.get("fill", None)
        stroke = element.get("stroke", None)
        thickness = element.get("stroke-width", None)
        return cls(type_, fill, stroke, thickness)

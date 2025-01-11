from __future__ import annotations

from lxml import etree

from ..utils.colour import Colour


class Tag:
    stroke = Colour.from_css("black")

    def translate(self, x: float = 0, y: float = 0) -> Tag:
        raise NotImplementedError()

    @classmethod
    def from_tag(cls, xml_tag: etree.Element) -> Tag:
        raise NotImplementedError()

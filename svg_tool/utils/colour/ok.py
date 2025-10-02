# https://en.wikipedia.org/wiki/Oklab_color_space
# https://bottosson.github.io/posts/oklab/
from __future__ import annotations

from . import base


class Lab(base.Colour):
    lightness: float  # 0 -> 1
    a: float  # -0.4 -> 0.4
    b: float  # -0.4 -> 0.4
    alpha: float  # 0 -> 1

    _channels = ["lightness", "a", "b", "alpha"]

    # TODO:
    # -- as_sRGB
    # -- from_sRGB
    ...


class Lch(base.Colour):
    lightness: float  # 0 -> 1
    chroma: float  # 0 -> 0.4
    hue: float  # 0 -> 360deg
    alpha: float  # 0 -> 1

    _channels = ["lightness", "chroma", "hue", "alpha"]

    def as_OkLab(self) -> Lab:
        return Lab(*self.as_cartesian())

    @classmethod
    def from_OkLab(cls, oklab) -> Lch:
        return cls(*oklab.as_polar())


class LMS(base.Colour):
    long: float  # ? -> ?
    medium: float  # ? -> ?
    short: float  # ? -> ?
    alpha: float  # 0 -> 1

    _channels = ["long", "medium", "short", "alpha"]

    ...

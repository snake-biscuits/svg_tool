# https://en.wikipedia.org/wiki/SRGB#From_sRGB_to_CIE_XYZ
# https://en.wikipedia.org/wiki/CIELAB_color_space
from __future__ import annotations

from . import base
# from . import srgb


class Lab(base.Colour):
    lightness: float  # 0 -> 1
    a: float  # -0.4 -> 0.4
    b: float  # -0.4 -> 0.4
    alpha: float  # 0 -> 1

    __slots__ = ["lightness", "a", "b", "alpha"]

    @staticmethod
    def f(t):
        delta = (6 / 29)
        if t > delta ** 3:
            return t ** (1/3)
        else:
            return (t * delta ** -2) / 3 + (4 / 29)

    @staticmethod
    def fi(t):  # inverse function
        delta = (6 / 29)
        if t > delta:
            return t ** 3
        else:
            return (3 * t * delta ** 2) * (t - 4 / 29)

    def as_CIEXYZ(self, white: XYZ = None) -> XYZ:
        white = XYZ(0.950489, 1, 1.088840) if white is None else white  # D65
        y_ = (self.L + 0.16) / 1.16
        x = white.x * self.fi(y_ + (self.a / 5))
        y = white.y * self.fi(y_)
        z = white.z * self.fi(y_ - (self.b / 2))
        return XYZ(x, y, z, self.alpha)

    @classmethod
    def from_CIEXYZ(cls, xyz: XYZ, white: XYZ = None) -> Lab:
        white = XYZ(0.950489, 1, 1.088840) if white is None else white  # D65
        fx = cls.f(xyz.x / white.x)
        fy = cls.f(xyz.y / white.y)
        fz = cls.f(xyz.z / white.z)
        L = 1.16 * fy - 0.16
        a = 5.00 * (fx - fy)
        b = 2.00 * (fy - fz)
        return cls(L, a, b, xyz.alpha)


class Lch(base.Colour):
    lightness: float  # 0 -> 1
    chroma: float  # 0 -> 0.4
    hue: float  # 0 -> 360deg
    alpha: float  # 0 -> 1

    __slots__ = ["lightness", "chroma", "hue", "alpha"]

    def as_CIELab(self) -> Lab:
        return Lab(*self.as_cartesian())

    @classmethod
    def from_CIELab(cls, oklab) -> Lch:
        return cls(*oklab.as_polar())


class XYZ(base.Colour):
    x: float  # 0 -> 1
    y: float  # 0 -> 1
    z: float  # 0 -> 1
    alpha: float  # 0 -> 1

    __slots__ = ["x", "y", "z", "alpha"]

    # TODO: basic matrix transforms
    # -- as_LinearRGB
    # -- from_LinearRGB
    ...


D65 = XYZ(0.950489, 1, 1.088840)  # standard
D50 = XYZ(0.964212, 1, 0.825188)  # print standard

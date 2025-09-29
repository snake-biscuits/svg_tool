# https://en.wikipedia.org/wiki/Gamma_correction
# https://en.wikipedia.org/wiki/Y%E2%80%B2UV
from . import base


def encode(value: float, gamma=2.2) -> float:
    return value ** gamma


def decode(value: float, gamma=2.2) -> float:
    return value ** (1 / gamma)


# NOTE:
# -- most formats here are based on gamma-corrected sRGB (gamma=2.2)
# -- PAL/SECAM B/G, H, I, D/K, K1, L & M use a gamma of 2.8
# -- SECAM IV is tuned to LinearRGB, not gamma-corrected sRGB


class YUV(base.Colour):
    """PAL"""
    luma: float  # 0 -> 1
    chroma_blue: float  # -0.5 -> 0.5
    chroma_red: float  # -0.5 -> 0.5
    alpha: float  # 0 -> 1
    # NOTE: chroma ranges are relative to white point

    __slots__ = ["luma", "chroma_blue", "chroma_red", "alpha"]

    ...


class YDbDr(base.Colour):
    """SECAM"""
    luma: float  # 0 -> 1
    chroma_blue: float  # -1.333 -> 1.333
    chroma_red: float  # -1.333 -> 1.333
    alpha: float  # 0 -> 1

    __slots__ = ["luma", "chroma_blue", "chroma_red", "alpha"]

    ...


class YIQ(base.Colour):
    """NTSC"""
    # NOTE: YIQ is YUV w/ the UV plane rotated 33deg
    ...

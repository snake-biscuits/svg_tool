# https://en.wikipedia.org/wiki/Gamma_correction
# https://en.wikipedia.org/wiki/Y%E2%80%B2UV
# https://en.wikipedia.org/wiki/YCbCr
# https://www.itu.int/rec/R-REC-BT/en
from __future__ import annotations

from . import base
from .srgb import sRGB


def encode(value: float, gamma=2.2) -> float:
    return value ** gamma


def decode(value: float, gamma=2.2) -> float:
    return value ** (1 / gamma)


# NOTE:
# -- most formats here are based on gamma-corrected sRGB (gamma=2.2)
# -- PAL/SECAM B/G, H, I, D/K, K1, L & M use a gamma of 2.8
# -- SECAM IV is tuned to LinearRGB, not gamma-corrected sRGB

# NOTE: transform constants could be cached
# -- could also use matrices for numpy / GPU

# NOTE: RGB -> YUV Matrix
# -- wikipedia uses Cxy constants on the Y'UV page
# -- however, the YCbCr page has formulae
# Uxb = -(Umax * (Wx / (1 - Wb)))
# Vxr = -(Vmax * (Wx / (1 - Wr)))
# [ Y' ]   [ Wr   Wg   Wb   ][ R' ]
# [ U  ] = [ Urb  Ugb  Umax ][ G' ]
# [ V  ]   [ Vmax Vgr  Vbr  ][ B' ]

# NOTE: YUV -> RGB Matrix
# Rv = (1 - Wr) / Vmax
# Bu = (1 - Wb) / Umax
# Gu = Bu * (Wb / Wg)
# Gv = Rv * (Wr / Wg)
# [ R' ]   [ 1  0  Rv ][ Y' ]
# [ G' ] = [ 1  Gu Gv ][ U  ]
# [ B' ]   [ 1  Bu 0  ][ V  ]


class YUV(base.Colour):
    """PAL"""
    _channels = ["luma", "chroma_blue", "chroma_red", "alpha"]
    # NOTE: Lightness, Chromacity x/y colour space
    # -- can use the .as_polar() & .as_cartesian() methods

    luma: float  # 0 -> 1
    chroma_blue: float  # -Umax -> Umax (~±0.4)
    chroma_red: float  # -Vmax -> Vmax (~±0.6)
    alpha: float  # 0 -> 1

    # RGB weights (Wr + Wg + Wb = 1)
    W = sRGB(0.299, 0.587, 0.114)  # SDTV
    W_hd = sRGB(0.2126, 0.7152, 0.0722)  # HDTV
    Umax, Vmax = 0.436, 0.615

    def as_sRGB(self, W=None) -> sRGB:
        W = self.W if W is None else W
        Wr, Wg, Wb = W[:3]
        Umax, Vmax = self.Umax, self.Vmax
        # scalar constants
        Rv = (1 - Wr) / Vmax
        Bu = (1 - Wb) / Umax
        Gu = Bu * (Wb / Wg)
        Gv = Rv * (Wr / Wg)
        # transform
        Y, U, V = self[:3]
        R = Y + Rv * V
        G = Y - Gu * U - Gv * V
        B = Y + Bu * U
        R, G, B = [min(max(C, 0), 1) for C in (R, G, B)]
        return sRGB(R, G, B, self.alpha)

    @classmethod
    def from_sRGB(cls, srgb, W=None) -> YUV:
        W = cls.W if W is None else W
        # NOTE: YUV is a transformation of sRGB, not LinearRGB
        Wr, Wg, Wb = W[:3]
        Umax, Vmax = cls.Umax, cls.Vmax
        R, G, B = srgb[:3]
        Y = Wr * R + Wg * G + Wb * B
        U = Umax * ((B - Y) / (1 - Wb))  # chroma_blue
        V = Vmax * ((R - Y) / (1 - Wr))  # chroma_red
        return cls(Y, U, V, srgb.alpha)


class YDbDr(base.Colour):
    """SECAM"""
    _channels = ["luma", "chroma_blue", "chroma_red", "alpha"]

    luma: float  # 0 -> 1
    chroma_blue: float  # -1.333 -> 1.333
    chroma_red: float  # -1.333 -> 1.333
    alpha: float  # 0 -> 1

    ...


class YIQ(base.Colour):
    """NTSC"""
    # NOTE: YIQ is YUV w/ the UV plane rotated 33deg
    ...

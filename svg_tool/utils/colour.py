from __future__ import annotations


class Colour:
    red: int
    green: int
    blue: int
    alpha: int

    def __init__(self, red, green, blue, alpha=255):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __repr__(self) -> str:
        args = f"{self.red}, {self.green}, {self.blue}"
        if self.alpha != 255:
            return f"Colour({args}, alpha={self.alpha})"
        else:
            return f"Colour({args})"

    def as_hex(self) -> str:
        return "".join([
            "#",
            *(f"{c:02X}" for c in (self.red, self.green, self.blue)),
            f"{self.alpha:02X}" if self.alpha != 255 else "",
            ";"])

    @classmethod
    def from_css(cls, css_text: str) -> Colour:
        """invalid input will produce opaque black"""
        css_text = css_text.rstrip(";")
        if css_text.startswith("#"):
            return cls.from_hex(css_text)
        elif "(" in css_text and ")" in css_text:
            raise NotImplementedError("cannot create Colour from function")
        return named_colours.get(css_text.lower(), cls(0, 0, 0, 255))

    # TODO: from_function (hsl, rgb etc.)
    # -- "rgb(0 0 0 / 0%)" is valid css; yikes!

    @classmethod
    def from_hex(cls, hex_code: str) -> Colour:
        """invalid input will produce opaque black"""
        r, g, b, a = 0, 0, 0, 255
        hex_code = hex_code.rstrip(";")
        assert hex_code.startswith("#"), "hex codes must start with '#'"
        hex_code = hex_code.strip("#")
        if len(hex_code) == 3:
            r, g, b = [int(x, base=16) for x in hex_code]
        elif len(hex_code) == 4:
            r, g, b, a = [int(x, base=16) for x in hex_code]
        elif len(hex_code) == 6:
            r, g, b = [
                int(hex_code[2*i:2*(i+1)], base=16)
                for i in range(3)]
        elif len(hex_code) == 8:
            r, g, b, a = [
                int(hex_code[2*i:2*(i+1)], base=16)
                for i in range(4)]
        return cls(r, g, b, a)


# extended colour keywords / X11 Colours / SVG Colours
# https://developer.mozilla.org/en-US/docs/Web/CSS/named-color
# generated by:
# -- copying html table from MDN
# -- html table -> json w/ online tool
# -- jq '.[] | "\(.hex_code|@sh): \(.name|@sh),"' colours.json > colour_names.py
# -- import in python to capitalise hex
hex_names = {
    # 16 Standard Colours (CSS Level 1)
    "#000000": "black",
    "#C0C0C0": "silver",
    "#808080": "grey",
    "#FFFFFF": "white",
    "#800000": "maroon",
    "#FF0000": "red",
    "#800080": "purple",
    "#FF00FF": "fuchsia",
    "#008000": "green",
    "#00FF00": "lime",
    "#808000": "olive",
    "#FFFF00": "yellow",
    "#000080": "navy",
    "#0000FF": "blue",
    "#008080": "teal",
    "#00FFFF": "aqua",
    # and ~150 others...
    "#F0F8FF": "aliceblue",
    "#FAEBD7": "antiquewhite",
    "#7FFFD4": "aquamarine",
    "#F0FFFF": "azure",
    "#F5F5DC": "beige",
    "#FFE4C4": "bisque",
    "#FFEBCD": "blanchedalmond",  # almond, not diamond
    "#8A2BE2": "blueviolet",
    "#A52A2A": "brown",
    "#DEB887": "burlywood",
    "#5F9EA0": "cadetblue",
    "#7FFF00": "chartreuse",
    "#D2691E": "chocolate",
    "#FF7F50": "coral",
    "#6495ED": "cornflowerblue",
    "#FFF8DC": "cornsilk",
    "#DC143C": "crimson",
    "#00008B": "darkblue",
    "#008B8B": "darkcyan",
    "#B8860B": "darkgoldenrod",
    "#A9A9A9": "darkgrey",
    "#006400": "darkgreen",
    "#BDB76B": "darkkhaki",
    "#8B008B": "darkmagenta",
    "#556B2F": "darkolivegreen",
    "#FF8C00": "darkorange",
    "#9932CC": "darkorchid",
    "#8B0000": "darkred",
    "#E9967A": "darksalmon",
    "#8FBC8F": "darkseagreen",
    "#483D8B": "darkslateblue",
    "#2F4F4F": "darkslategrey",
    "#00CED1": "darkturquoise",
    "#9400D3": "darkviolet",
    "#FF1493": "deeppink",
    "#00BFFF": "deepskyblue",
    "#696969": "dimgrey",
    "#1E90FF": "dodgerblue",
    "#B22222": "firebrick",
    "#FFFAF0": "floralwhite",
    "#228B22": "forestgreen",
    "#DCDCDC": "gainsboro",
    "#F8F8FF": "ghostwhite",
    "#FFD700": "gold",
    "#DAA520": "goldenrod",
    "#ADFF2F": "greenyellow",
    "#F0FFF0": "honeydew",
    "#FF69B4": "hotpink",
    "#CD5C5C": "indianred",
    "#4B0082": "indigo",
    "#FFFFF0": "ivory",
    "#F0E68C": "khaki",
    "#E6E6FA": "lavender",
    "#FFF0F5": "lavenderblush",
    "#7CFC00": "lawngreen",
    "#FFFACD": "lemonchiffon",
    "#ADD8E6": "lightblue",
    "#F08080": "lightcoral",
    "#E0FFFF": "lightcyan",
    "#FAFAD2": "lightgoldenrodyellow",
    "#D3D3D3": "lightgrey",
    "#90EE90": "lightgreen",
    "#FFB6C1": "lightpink",
    "#FFA07A": "lightsalmon",
    "#20B2AA": "lightseagreen",
    "#87CEFA": "lightskyblue",
    "#778899": "lightslategrey",
    "#B0C4DE": "lightsteelblue",
    "#FFFFE0": "lightyellow",
    "#32CD32": "limegreen",
    "#FAF0E6": "linen",
    "#66CDAA": "mediumaquamarine",
    "#0000CD": "mediumblue",
    "#BA55D3": "mediumorchid",
    "#9370DB": "mediumpurple",
    "#3CB371": "mediumseagreen",
    "#7B68EE": "mediumslateblue",
    "#00FA9A": "mediumspringgreen",
    "#48D1CC": "mediumturquoise",
    "#C71585": "mediumvioletred",
    "#191970": "midnightblue",
    "#F5FFFA": "mintcream",
    "#FFE4E1": "mistyrose",
    "#FFE4B5": "moccasin",
    "#FFDEAD": "navajowhite",
    "#FDF5E6": "oldlace",
    "#6B8E23": "olivedrab",
    "#FFA500": "orange",  # added in CSS Level 2
    "#FF4500": "orangered",
    "#DA70D6": "orchid",
    "#EEE8AA": "palegoldenrod",
    "#98FB98": "palegreen",
    "#AFEEEE": "paleturquoise",
    "#DB7093": "palevioletred",
    "#FFEFD5": "papayawhip",
    "#FFDAB9": "peachpuff",
    "#CD853F": "peru",
    "#FFC0CB": "pink",
    "#DDA0DD": "plum",
    "#B0E0E6": "powderblue",
    "#663399": "rebeccapurple",  # added in CSS Colors Level 4
    "#BC8F8F": "rosybrown",
    "#4169E1": "royalblue",
    "#8B4513": "saddlebrown",
    "#FA8072": "salmon",
    "#F4A460": "sandybrown",
    "#2E8B57": "seagreen",
    "#FFF5EE": "seashell",
    "#A0522D": "sienna",
    "#87CEEB": "skyblue",
    "#6A5ACD": "slateblue",
    "#708090": "slategrey",
    "#FFFAFA": "snow",
    "#00FF7F": "springgreen",
    "#4682B4": "steelblue",
    "#D2B48C": "tan",
    "#D8BFD8": "thistle",
    "#FF6347": "tomato",
    "#40E0D0": "turquoise",
    "#EE82EE": "violet",
    "#F5DEB3": "wheat",
    "#F5F5F5": "whitesmoke",
    "#9ACD32": "yellowgreen"}

named_colours = {
    name: Colour.from_hex(hex_code)
    for hex_code, name in hex_names.items()}

# transparent & none
named_colours.update({
    name: Colour(0, 0, 0, alpha=0)
    for name in ("none", "transparent")})

# NOTE: in a gradient, transparent should be consider as alpha-premultiplied
# -- meaning only opacity would be blended
# -- gradients will likely be process elsewhere though
# -- (which is preferable, since the gradient function takes multiple colours)

# synonyms & aliases
synonyms = {
    "cyan": "aqua",
    "magenta": "fuchsia"}

synonyms.update({
    name.replace("grey", "gray"): name
    for name in named_colours
    if "gray" in name})

named_colours.update({
    name: named_colours[base]
    for name, base in synonyms.items()})

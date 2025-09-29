## Goals
 * Generate Playing Cards Set
   - Suit Symbols
   - Face Cards (KQJ + Ace of Spades)
   - Glyphs (2-9 + KQJA)
   - Back (trim to match shape)

 * Generate Mahjong Set
   - 🀐 🀑 🀒 🀓 🀔 🀕 🀖 🀗 🀘 | Bamboos
   - 🀙 🀚 🀛 🀜 🀝 🀞 🀟 🀠 🀡 | Circles
   - 🀇 🀈 🀉 🀊 🀋 🀌 🀍 🀎 🀏 | Characters
   - 🀢 🀣 🀥 🀤 | Flowers
   - 🀦 🀧 🀨 🀩 | Seasons
   - 🀀 🀁 🀂 🀃 | Winds
   - 🀄🀅 🀆 | Dragons

 * Generate Hanafuda Deck
   - Use tools to edit multiple to keep things consistent
   - Baking styling & moving elements around

 * Node Graph with connecting lines


## Parsing
```
parse
 > base (Style, Transform, Shape)
 > parents (Group, Svg, Mask, Gradient)
   manage children and inheritance (style, transform, %age units etc.)
 > circle (Circle, Ellipse)
 > poly (Polygon, PolyLine)
 > rect (Rect)
 > path (Line, Path) [Route]
```

### `<path>`
 * `d`
   - `M x y`
     move cursor to (x, y)
   - `L x y`
     draw line to (x, y)
   - `C x1 y1, x2 y2, x, y`
     beizer curve w/ 2 control points and a terminus (x, y)
 * `fill`
   - need to determine interior shape
 * `stroke-width`
   - need normalised paralell axis to curve
 * bounds `@property`
   - iirc freyaholmer has resources on how to calculate this
 * `vec2` + lerp to draw `stroke`
   - need trig to work out inside & outside areas

### `<rect>`
 * `rx` & `ry`
   - 2 different radii for rounded corners

### CSS
 * `style` attribute
 * inheritance rules
 * override via direct assignment


## `raster`
so much work...


## `colour`
Colour spaces + CSS parser foundation
 * `colour.cie`
   - `Lab`
   - `XYZ`
 * `colour.Ok`
   - `Lab`
   - `Lch`
   - `LMS`
 * `colour.srgb`
   - `RGB`
 * `colour.x11`
   - `hex_names`
   - `named_colours`

> TODO: copy from `PartitionDB` (javascript implementation)

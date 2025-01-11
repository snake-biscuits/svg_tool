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


## We Need:
 * CSS Parser
 * 2D Vector math w/ lerping for Bezier Curves
 * Clearly communicate limitations to users
   - map out a list of common tags & attributes

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

### `<rect>`
 * `rx` & `ry`
   - 2 different radii for rounded corners

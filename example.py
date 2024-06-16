from gimpfu import *

def apply(image, tdrawable, brush_radius=2, make_centre=True, draw_diagonals=True):

    h = image.height
    w = image.width

    # Defines lines to draw
    hpoints1 = [0,h/3 , w,h/3]
    hpoints2 = [0,h/2 , w,h/2]
    hpoints3 = [0,2*(h/3) , w,2*(h/3)]
    vpoints1 = [w/3,0 , w/3,h]
    vpoints2 = [w/2,0 , w/2,h]
    vpoints3 = [2*(w/3),0 , 2*(w/3),h]
    dpoints1 = [0,0 , w,h]
    dpoints2 = [0,h , w,0]

    # Brush setup
    brush = pdb.gimp_brush_new("Block")
    pdb.gimp_brush_set_hardness(brush, 1.0)
    pdb.gimp_brush_set_shape(brush, BRUSH_GENERATED_SQUARE)
    pdb.gimp_brush_set_radius(brush, brush_radius)
    pdb.gimp_context_set_brush(brush)

    # Horizontals
    pdb.gimp_paintbrush(image.layers[0], 0, len(hpoints1), hpoints1, 0, 0)
    if make_centre:
        pdb.gimp_paintbrush(image.layers[0], 0, len(hpoints2), hpoints2, 0, 0)
    pdb.gimp_paintbrush(image.layers[0], 0, len(hpoints3), hpoints3, 0, 0)
    # Verticals
    pdb.gimp_paintbrush(image.layers[0], 0, len(vpoints1), vpoints1, 0, 0)
    if make_centre:
        pdb.gimp_paintbrush(image.layers[0], 0, len(vpoints2), vpoints2, 0, 0)
    pdb.gimp_paintbrush(image.layers[0], 0, len(vpoints3), vpoints3, 0, 0)
    # Diagonals
    pdb.gimp_paintbrush(image.layers[0], 0, len(dpoints1), dpoints1, 0, 0)
    pdb.gimp_paintbrush(image.layers[0], 0, len(dpoints2), dpoints2, 0, 0)
    

register(
    "Rule-of-Thirds",
    "Applies the rule of thirds to an image",
    "Applies the rule of thirds to an image",
    "John Lunt",
    "MIT Licence",
    "2024",
    "<Image>/Filters/RuleOfThirds",
    "",
    [
        (PF_INT, "brush_radius", "Brush radius", 2),
        (PF_TOGGLE, "make_centre", "Draw centered guides", True),
        (PF_TOGGLE, "draw_diagonals", "Draw diagonals", True),
    ],
    [],
    apply)

main()
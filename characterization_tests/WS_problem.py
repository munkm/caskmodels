from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "WSprob",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "Air",
                                  2:  "Carbon Steel",
                                  3:  "Water",
                                  4:  "Homogenized UO2 Fuel"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             2,
    "mesh_x":                    [0, 53],
    "mesh_x_ints":               [  52],
    "mesh_y":                    [0, 50],
    "mesh_y_ints":               [  49],
    "mesh_z":                    [0, 140],
    "mesh_z_ints":               [  139]
}

run(inp)

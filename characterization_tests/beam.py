from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "beam",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "Li-doped Polyethylene",
                                  3:  "NaI"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             2,
    "mesh_x":                    [0, 200],
    "mesh_x_ints":               [  40],
    "mesh_y":                    [0, 200],
    "mesh_y_ints":               [   40],
    "mesh_z":                    [0, 100],
    "mesh_z_ints":               [    20]
}

run(inp)

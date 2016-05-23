from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "prob_4",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "Li-doped Polyethylene",
                                  3:  "NaI",
                                  4:  "Carbon Steel"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             2,
    "mesh_x":                    [0, 50, 64, 66, 84, 86, 100, 150],
    "mesh_x_ints":               [  10, 7,  2,  9,  2,   7,   10],
    "mesh_y":                    [0, 200],
    "mesh_y_ints":               [    50],
    "mesh_z":                    [40, 59,  61,  79, 81, 99, 101, 119, 121, 139, 141, 160],
    "mesh_z_ints":               [    9,  2,   9,   2,  9,  2,  9,   2,   9,   2,   9]
}

run(inp)

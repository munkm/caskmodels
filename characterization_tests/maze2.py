from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "maze2",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "concrete",
                                  3:  "NaI"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             3,
    "denovo_x_blocks":             4,
    "denovo_y_blocks":             4,
    "denovo_z_blocks":             2,
    "mesh_x":                    [-100, -50, 50, 100],
    "mesh_x_ints":               [      25, 100,  25],
    "mesh_y":                    [-50, -10, 40,  50],
    "mesh_y_ints":               [      8, 25, 2],
    "mesh_z":                    [0, 40, 60,  100],
    "mesh_z_ints":               [     8, 10, 8]
}

run(inp)

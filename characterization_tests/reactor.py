from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "reactor",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "water",
                                  3:  "NaI",
                                  4:  "concrete",
                                  5:  "carbon steel"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             2,
    "mesh_x":                    [-2100, -1650, -530, 530, 1650, 2100],
    "mesh_x_ints":               [    30,     112,   106, 112,  30 ],
    "mesh_y":                    [-2100, -1650, -530, 530, 1650, 2100],
    "mesh_y_ints":               [    30,     112,   106, 112,  30 ],
    "mesh_z":                    [0, 612, 896, 1283, 2200],
    "mesh_z_ints":               [  30,  28,  38,  45  ]
}

run(inp)

from advantg.driver import run

inp = {
    "method":                    "cadis",
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "prob_2",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "Li-doped Polyethylene",
                                  3:  "NaI",
                                  4:  "Concrete"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             2,
    "mesh_x":                    [0, 100, 200, 300, 400, 500],
    "mesh_x_ints":               [  10, 20,   20,  20, 10],
    "mesh_y":                    [0, 250, 350, 450],
    "mesh_y_ints":               [    50, 20, 10],
    "mesh_z":                    [0, 200],
    "mesh_z_ints":               [    20]
}

run(inp)

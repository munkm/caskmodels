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
    "denovo_pn_order":             3,
    "mesh_x":                    [0, 45, 155, 200],
    "mesh_x_ints":               [   5, 25, 5],
    "mesh_y":                    [0, 45, 155, 200],
    "mesh_y_ints":               [   5, 25, 5],
    "mesh_z":                    [0, 45, 155, 200],
    "mesh_z_ints":               [    5, 25, 5]
}

run(inp)

from advantg.driver import run

inp = {
    "method":                 "cadis",
    "mcnp_input":             "ueki35",
    "mcnp_tallies":           5,
    "mcnp_material_names":   {1: "paraffin",
                              2: "graphite"},
    "anisn_library":          "27n19g",
    "denovo_pn_order":        1,
    "denovo_quad_num_polar":  2,
    "denovo_quad_num_azi":    2,
    "mesh_x":                 [-25, 107.5, 112.5],
    "mesh_x_ints":                    [53,     3],
    "mesh_y":                 [-40,  -2.5,   2.5,  40],
    "mesh_y_ints":                    [15,     3,  15],
    "mesh_z":                 [-40,  -2.5,   2.5,  40],
    "mesh_z_ints":                    [15,     3,  15]
}

run(inp)

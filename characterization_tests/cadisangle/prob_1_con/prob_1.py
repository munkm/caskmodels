from advantg.driver import run
from advantg.utils import time_this
import json

inp = {
    "method":                 "cadisangle",
    "omega_quantify_anisotropy": True,
    "omega_quantify_anisotropy_silo": True,
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "prob_1",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "Li-doped Polyethylene",
                                  3:  "NaI",
                                  4:  "Carbon Steel"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             3,
    "denovo_x_blocks":             4,
    "denovo_y_blocks":             4,
    "denovo_z_blocks":             2,
    "mesh_x":                    [-100, -50, 50, 80, 100],
    "mesh_x_ints":               [      10, 50, 10, 4],
    "mesh_y":                    [-50, -15, -5, 5, 15,  50],
    "mesh_y_ints":               [ 10, 10,  10, 10, 10 ],
    "mesh_z":                    [0, 35, 45, 55, 65,  100],
    "mesh_z_ints":               [ 10, 10, 10, 10, 10]
}

run(inp)
data = dict(time_this.times)
with open('./timing.json', 'w') as jf:
    json.dump(data, jf, sort_keys=True,indent=0)

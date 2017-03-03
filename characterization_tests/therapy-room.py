from advantg.driver import run
from advantg.utils import time_this
import json

inp = {
    "method":                 "cadisangle",
    "omega_quantify_anisotropy": True,
    "outputs":                  {"mcnp", "silo", "response"},
    "mcnp_input":                "therapy",
    "mcnp_tallies":              44,
    "mcnp_material_names":      { 1:  "air",
                                  2:  "water",
                                  3:  "concrete",
                                  4:  "NaI"},
    "anisn_library":             "27n19g",
    "denovo_quadrature":         "qr",
    "denovo_quad_order":          10,
    "denovo_pn_order":             3,
    "denovo_x_blocks":             4,
    "denovo_y_blocks":             4,
    "denovo_z_blocks":             2,
    "mesh_x":                    [0, 30, 610, 640],
    "mesh_x_ints":               [  3, 58,  3],
    "mesh_y":                    [0, 30, 150, 180, 610, 640],
    "mesh_y_ints":               [   3,  12,  3,  43,  3],
    "mesh_z":                    [0, 300],
    "mesh_z_ints":               [   30]
}

run(inp)
data = dict(time_this.times)
with open('./timing.json', 'w') as jf:
    json.dump(data, jf, sort_keys=True,indent=0)

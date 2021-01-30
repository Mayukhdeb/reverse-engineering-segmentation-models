import cv2
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torch_dreams.dreamer import dreamer

from core.model import BiSeNet
from core.classes import classnames_index
from core.utils import generate_layer_dict, make_custom_func

model = BiSeNet(n_classes = 19, checkpoint= "models/model.pth")
dreamy_boi = dreamer(model)

layers_dict = generate_layer_dict(model= model)

layers_to_use = [
    layers_dict[list(layers_dict.keys())[-1]]
]

config = {
    "image_path": "images/noise.jpg",
    "layers": layers_to_use,
    "octave_scale": 1.2,  
    "num_octaves": 15,  
    "iterations": 100,  
    "lr": 0.03,
    "max_rotation": 1.5,
    "gradient_smoothing_kernel_size": 3,  ## optional
    "gradient_smoothing_coeff": 0.5,       ## optional
}

all_outs = []
for i in range(len(classnames_index)):
     
    config["custom_func"] = make_custom_func(layer_number=0, channel_number= list(classnames_index.values())[i])

    out = dreamy_boi.deep_dream(config)  
    all_outs.append(out)
    plt.imshow(out)
    plt.show()

fig, ax = plt.subplots(nrows= 1, ncols= len(classnames_index), figsize=(18, 6))
for i in range(len(all_outs)):
    ax.flat[i].imshow(all_outs[i])
    ax.flat[i].set_title(list(classnames_index)[i], fontsize = 16)
    ax.flat[i].axis("off")

plt.show()
# fig.tight_layout()
fig.savefig("images/vis.jpg")

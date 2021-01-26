import cv2
import torch.nn as nn
import torchvision.transforms as transforms

def generate_layer_dict(model):
    layer_dict = {}
    for name, layer in model.named_modules():
        if isinstance(layer, nn.Conv2d) or isinstance(layer, nn.Linear) or isinstance(layer, nn.BatchNorm2d):
                layer_dict[name] = layer
    return layer_dict

def make_custom_func(layer_number = 0, channel_number= 0): 
    def custom_func(layer_outputs):
        loss = layer_outputs[layer_number][channel_number].mean()
        return loss
    return custom_func
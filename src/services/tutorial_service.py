import torch
import numpy as np

class TutorialService:
    def get_model(self):
        tensor = torch.rand(3,4)
        if torch.cuda.is_available():
            tensor = tensor.to('cuda')
        print(f"Device tensor is stored on: {tensor.device}")
    
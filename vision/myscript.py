import torch
from trainer import GaussianSQVAETrainer
PATH = "/home/cy/Desktop/ml-reps/sqvae/vision/configs/checkpoints/cifar10_sqvae_gaussian_1/resnet_seed0_1207_0317/best.pt"
model = GaussianSQVAETrainer()
# model = torch.load(PATH)
# model.eval()

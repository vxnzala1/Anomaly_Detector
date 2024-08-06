import torch
print(torch.cuda.is_available())
print("Number of GPU: ", torch.cuda.device_count())
print("GPU Name: ", torch.cuda.get_device_name(0))
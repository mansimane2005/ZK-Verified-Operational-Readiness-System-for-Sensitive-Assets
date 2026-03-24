import torch
from train_model import SmallModel


input_size = 24

model = SmallModel(input_size)
model.load_state_dict(
    torch.load("model/model.pth")
)

model.eval()

dummy_input = torch.randn(1, input_size)

torch.onnx.export(
    model,
    dummy_input,
    "onnx/model.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=11
)

print("ONNX model exported")
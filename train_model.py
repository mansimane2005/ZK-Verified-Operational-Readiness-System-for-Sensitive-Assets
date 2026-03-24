import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from preprocess import prepare_dataset


class SmallModel(nn.Module):

    def __init__(self, input_size):
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.model(x)


# Load dataset
X, y = prepare_dataset("data/train_FD001.txt")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Convert to tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

# Create model
model = SmallModel(X_train.shape[1])

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):

    optimizer.zero_grad()

    outputs = model(X_train)

    loss = criterion(outputs, y_train)

    loss.backward()

    optimizer.step()

    print("Epoch:", epoch, "Loss:", loss.item())


# Save model
torch.save(model.state_dict(), "model/model.pth")

print("Model training complete")
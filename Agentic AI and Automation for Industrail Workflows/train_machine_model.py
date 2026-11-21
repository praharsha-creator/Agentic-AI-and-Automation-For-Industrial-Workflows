import pandas as pd
import random

# Generate synthetic training data
data = []

for _ in range(200):
    temperature = random.randint(60, 110)
    vibration = round(random.uniform(0.3, 2.5), 2)
    usage_hours = random.randint(500, 3000)

    # Failure logic (hidden pattern)
    if temperature > 90 and vibration > 1.8: 
      failure = 1
    else:
       failure = 0
    data.append([temperature, vibration, usage_hours, failure])

df = pd.DataFrame(data, columns=[
    "temperature", "vibration", "usage_hours", "failure"
])

df.to_csv("machine_training_data.csv", index=False)

print("Training dataset created successfully")
print("File saaved as machine_training_data.csv")
print("Training data generated")

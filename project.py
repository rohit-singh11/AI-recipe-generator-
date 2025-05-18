# Import the AI model tools
from transformers import pipeline

# Load text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Ask user for input
food = input("Enter the name of the food: ")

# Create a prompt for AI
prompt = f"Write a cooking recipe for {food}:"

# Generate the recipe
result = generator(prompt, max_length=200, num_return_sequences=1)

# Print the generated recipe
print("\n🍽️ Recipe Generated:\n")
print(result[0]['generated_text'])

# # import tensorflow as tf
# #
# # # Load the data
# # data = tf.keras.datasets.mnist.load_data()
# #
# # # Split the data into train and test sets
# # (x_train, y_train), (x_test, y_test) = data
# #
# # # Create the model
# # model = tf.keras.Sequential([
# #     tf.keras.layers.Flatten(input_shape=(28, 28)),
# #     tf.keras.layers.Dense(128, activation='relu'),
# #     tf.keras.layers.Dense(10, activation='softmax')
# # ])
# #
# # # Compile the model
# # model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# #
# # # Train the model
# # model.fit(x_train, y_train, epochs=10)
# #
# # # Evaluate the model
# # model.evaluate(x_test, y_test)
# import tensorflow as tf
# import keras
# # Load the data
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
#
# # Normalize the data
# x_train = x_train / 255.0
# x_test = x_test / 255.0
#
# # Create the model
# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])
#
# # Compile the model
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# # Train the model
# model.fit(x_train, y_train, epochs=10)
#
# # Evaluate the model
# model.evaluate(x_test, y_test)

# Install required libraries
#pip install transformers

# Import necessary modules
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model
model_name = "gpt2"  # Choose a specific variant (e.g., gpt2-medium)
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Example prompt
user_prompt = "Tell me a joke:"

# Generate response
input_ids = tokenizer.encode(user_prompt, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print("AI's response:", response)

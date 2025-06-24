from stegano import lsb

# Step 1: Hide the message
secret_message = open("secret.txt").read()
output_image = lsb.hide("input_image.png", secret_message)
output_image.save("stegano_output.png")
print("[✅] Message successfully hidden in 'stegano_output.png'")

# Step 2: Reveal the hidden message
revealed_message = lsb.reveal("stegano_output.png")
print("[✅] Hidden message revealed from 'stegano_output.png':")
print("--------------------------------------------")
print(revealed_message)
print("--------------------------------------------")
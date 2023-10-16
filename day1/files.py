"""
Read and write files
"""
text = "hello world"
filepath = "/home/kristian/hello.txt"
winpath = r"C:\Users\1234\Documents\hello.txt"

# write a file
file = open(filepath, "w")
file.write(text)
file.write("hello from Bochum")
file.close()

# context manager: closes automatically
with open(filepath, "w") as file:
    file.write("hello world\n")
    file.write("hello from Bochum\n")


with open(filepath, "r") as file:
    lines = file.readlines()  # -> List[str]
    # OR file.read() -> str

# running a custom program
import os
os.system(f"code {filepath}")
os.system(f"nano {filepath}")
os.system(f"vi {filepath}")
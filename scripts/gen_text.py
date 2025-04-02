# Generate the text file for diffrent data size

import os
import random
import string
import faker

def generate_random_text(size_in_kb, filename):
    fake = faker.Faker()
    size_in_bytes = size_in_kb * 1024  # Convert KB to Bytes
    chunk_size = 1024  # 1KB chunk
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    
    with open(filename, "w", encoding="utf-8") as f:
        while os.path.getsize(filename) < size_in_bytes:
            random_text = ' '.join([fake.name(), fake.address(), fake.email(), fake.phone_number(), fake.company()])
            f.write(random_text + '\n')

    print(f"Generated: {filename} ({size_in_kb} KB)")

# List of file sizes in KB
sizes = [1, 2, 5, 7, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]  # 1KB to 1GB

output_dir = "pii_test_files"
os.makedirs(output_dir, exist_ok=True)

for size in sizes:
    filename = os.path.join(output_dir, f"random_text_{size}KB.txt")
    generate_random_text(size, filename)


---

### Code Sample for Day 3
Below is a single Python file (`Day3_Samples_001.py`) with five sample programs tailored to Module 3: File Operations (Days 11-15), focusing on Day 3's topics of filesystem operations and an introduction to AWS S3 (note: Azure integration requires setup beyond basic samples here, so it’s outlined conceptually).

```python
# Day3_Samples_001.py
# Program 1: Writing to a Local File
with open("day3_sample.txt", "w") as file:
    file.write("This is a sample file created on Day 3!")
print("File written successfully.")

# Program 2: Reading from a Local File
with open("day3_sample.txt", "r") as file:
    content = file.read()
print("File content:", content)

# Program 3: Moving a File with shutil
import shutil
shutil.move("day3_sample.txt", "moved_day3_sample.txt")
print("File moved to moved_day3_sample.txt")

# Program 4: Uploading to AWS S3 with boto3 (Basic Example)
import boto3
s3 = boto3.client('s3')
try:
    s3.upload_file("moved_day3_sample.txt", "your-bucket-name", "day3_sample.txt")
    print("File uploaded to S3 bucket.")
except Exception as e:
    print("Error uploading to S3:", e)

# Program 5: Listing S3 Bucket Contents
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket="your-bucket-name")
for obj in response.get('Contents', []):
    print("S3 Object:", obj['Key'])
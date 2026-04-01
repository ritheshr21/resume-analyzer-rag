import os
from src.data_loader import load_resume, load_job_description
from src.text_cleaner import clean_text

# Get project root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build relative paths (portable across systems)
resume_path = os.path.join(BASE_DIR, "data", "resume.pdf")
jd_path = os.path.join(BASE_DIR, "data", "job_description.txt")

# Load data
resume = load_resume(resume_path)
jd = load_job_description(jd_path)

# Clean data
resume = clean_text(resume)
jd = clean_text(jd)

# Output preview
print("=== Resume Preview ===")
print(resume[:300])

print("\n=== Job Description Preview ===")
print(jd[:300])

print(f"\nResume length: {len(resume)}")
print(f"JD length: {len(jd)}")
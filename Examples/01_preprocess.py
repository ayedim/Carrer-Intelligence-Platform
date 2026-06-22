from pathlib import Path
import json


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(
    r"C:\Work\Resume\Qwen_Resume_Workflow"
)

INPUT_DIR = (
    BASE_DIR /
    "input_jobs"
)

CONFIG_DIR = (
    BASE_DIR /
    "config"
)

TEMP_DIR = (
    BASE_DIR /
    "temp"
)

TEMP_DIR.mkdir(
    exist_ok=True
)

RESUME_PROFILES_PATH = (
    CONFIG_DIR /
    "resume_profiles.json"
)

OUTPUT_PATH = (
    TEMP_DIR /
    "runtime_payload.json"
)


# ==========================================================
# FIND LATEST INPUT FOLDER
# ==========================================================

date_folders = sorted(
    [
        p for p in INPUT_DIR.iterdir()
        if p.is_dir()
    ]
)

if not date_folders:

    raise FileNotFoundError(
        "No date folders found in input_jobs/"
    )

latest_folder = date_folders[-1]

input_date = (
    latest_folder.name
)

print(
    f"\nUsing folder:\n{latest_folder}\n"
)


# ==========================================================
# LOAD JOB FILES
# ==========================================================

jobs = []

txt_files = sorted(
    latest_folder.glob("*.txt")
)

if not txt_files:

    raise FileNotFoundError(
        f"No .txt files found in {latest_folder}"
    )

for job_file in txt_files:

    text = job_file.read_text(
        encoding="utf-8"
    ).strip()

    filename = (
        job_file.stem
    )

    parts = filename.split("_")

    company = (
        parts[0]
        if len(parts) >= 1
        else "Unknown"
    )

    title = (
        " ".join(parts[1:])
        if len(parts) >= 2
        else "Unknown"
    )

    jobs.append({

        "company":
            company,

        "title":
            title,

        "source_file":
            job_file.name,

        "description":
            text
    })


# ==========================================================
# LOAD RESUME PROFILES
# ==========================================================

with open(
    RESUME_PROFILES_PATH,
    "r",
    encoding="utf-8"
) as f:

    resume_profiles = json.load(f)


# ==========================================================
# BUILD PAYLOAD
# ==========================================================

payload = {

    "input_date":
        input_date,

    "job_count":
        len(jobs),

    "jobs":
        jobs,

    "resume_profiles":
        resume_profiles
}


# ==========================================================
# SAVE
# ==========================================================

with open(
    OUTPUT_PATH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        payload,
        f,
        indent=2
    )


# ==========================================================
# SUCCESS
# ==========================================================

print("\nSUCCESS\n")

print(
    f"Jobs loaded: {len(jobs)}"
)

print(
    f"Input date: {input_date}"
)

print(
    f"\nPayload saved:\n{OUTPUT_PATH}"
)
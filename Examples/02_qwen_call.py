import json
import requests
from pathlib import Path


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PAYLOAD_PATH = (
    BASE_DIR /
    "temp" /
    "runtime_payload.json"
)

PROMPT_PATH = (
    BASE_DIR /
    "config" /
    "qwen_prompt.txt"
)

OUTPUT_PATH = (
    BASE_DIR /
    "temp" /
    "qwen_output.json"
)

RAW_OUTPUT_PATH = (
    BASE_DIR /
    "temp" /
    "qwen_raw_output.txt"
)


# ==========================================================
# LOAD FILES
# ==========================================================

with open(
    PAYLOAD_PATH,
    "r",
    encoding="utf-8"
) as f:

    payload = json.load(f)

with open(
    PROMPT_PATH,
    "r",
    encoding="utf-8"
) as f:

    system_prompt = f.read()


# ==========================================================
# PROCESS JOBS
# ==========================================================

results = []

raw_outputs = []

jobs = payload["jobs"]

resume_profiles = payload[
    "resume_profiles"
]

for index, job in enumerate(
    jobs,
    start=1
):

    print(
        f"\n[{index}/{len(jobs)}] "
        f"{job['company']} - "
        f"{job['title']}"
    )

    prompt_payload = {

        "job": job,

        "resume_profiles":
            resume_profiles
    }

    full_prompt = f"""
{system_prompt}

INPUT DATA:

{json.dumps(
    prompt_payload,
    indent=2
)}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":
                "qwen2.5:14b",

            "prompt":
                full_prompt,

            "stream":
                False,

            "options": {
                "temperature":
                    0.1
            }
        },
        timeout=300
    )

    response.raise_for_status()

    raw_output = (
        response.json()
        ["response"]
        .strip()
    )

    raw_outputs.append(
        {
            "company":
                job["company"],

            "title":
                job["title"],

            "raw_output":
                raw_output
        }
    )

    # ----------------------------------
    # Clean markdown fences
    # ----------------------------------

    if raw_output.startswith(
        "```json"
    ):
        raw_output = (
            raw_output.replace(
                "```json",
                "",
                1
            )
        )

    if raw_output.startswith(
        "```"
    ):
        raw_output = (
            raw_output.replace(
                "```",
                "",
                1
            )
        )

    if raw_output.endswith(
        "```"
    ):
        raw_output = (
            raw_output[:-3]
        )

    raw_output = (
        raw_output.strip()
    )

    try:

        result = json.loads(
            raw_output
        )

        result[
            "company"
        ] = job[
            "company"
        ]

        result[
            "title"
        ] = job[
            "title"
        ]

        results.append(
            result
        )

    except json.JSONDecodeError:

        results.append({

            "company":
                job["company"],

            "title":
                job["title"],

            "recommended_resume":
                "",

            "confidence":
                0,

            "skills_additions":
                [],

            "skills_removals":
                [],

            "flags": [
                "invalid_json"
            ]
        })


# ==========================================================
# SAVE RAW OUTPUTS
# ==========================================================

with open(
    RAW_OUTPUT_PATH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        raw_outputs,
        f,
        indent=2
    )


# ==========================================================
# SAVE RESULTS
# ==========================================================

final_output = {

    "input_date":
        payload[
            "input_date"
        ],

    "job_count":
        len(results),

    "results":
        results
}

with open(
    OUTPUT_PATH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        final_output,
        f,
        indent=2
    )


# ==========================================================
# SUCCESS
# ==========================================================

print("\nSUCCESS\n")

print(
    f"Jobs processed: "
    f"{len(results)}"
)

print(
    f"\nOutput:\n"
    f"{OUTPUT_PATH}"
)
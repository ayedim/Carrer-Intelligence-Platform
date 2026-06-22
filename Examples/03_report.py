from pathlib import Path
from datetime import date
import json


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(
    r"C:\Work\Resume\Qwen_Resume_Workflow"
)

TEMP_DIR = (
    BASE_DIR /
    "temp"
)

OUTPUT_DIR = (
    BASE_DIR /
    "output"
)

PAYLOAD_PATH = (
    TEMP_DIR /
    "runtime_payload.json"
)

QWEN_OUTPUT_PATH = (
    TEMP_DIR /
    "qwen_output.json"
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
    QWEN_OUTPUT_PATH,
    "r",
    encoding="utf-8"
) as f:

    qwen = json.load(f)


# ==========================================================
# DATE FOLDER
# ==========================================================

input_date = payload.get(
    "input_date",
    date.today().isoformat()
)

output_folder = (
    OUTPUT_DIR /
    input_date
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================================
# OUTPUT FILES
# ==========================================================

json_report = (
    output_folder /
    "Resume_Routing_Report.json"
)

markdown_report = (
    output_folder /
    "Resume_Routing_Report.md"
)


# ==========================================================
# SAVE JSON REPORT
# ==========================================================

with open(
    json_report,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        qwen,
        f,
        indent=2
    )


# ==========================================================
# BUILD MARKDOWN
# ==========================================================

results = qwen.get(
    "results",
    []
)

lines = []

lines.append(
    "# Resume Routing Report"
)

lines.append("")

lines.append(
    f"Generated: {input_date}"
)

lines.append("")

lines.append(
    f"Jobs Reviewed: {len(results)}"
)

lines.append("")

lines.append("---")
lines.append("")


for result in results:

    company = result.get(
        "company",
        "Unknown"
    )

    title = result.get(
        "title",
        "Unknown"
    )

    resume = result.get(
        "recommended_resume",
        ""
    )

    confidence = result.get(
        "confidence",
        0
    )

    additions = result.get(
        "skills_additions",
        []
    )

    removals = result.get(
        "skills_removals",
        []
    )

    flags = result.get(
        "flags",
        []
    )

    lines.append(
        f"## {company} — {title}"
    )

    lines.append("")

    lines.append(
        f"**Recommended Resume:** {resume}"
    )

    lines.append("")

    lines.append(
        f"**Confidence:** {confidence}"
    )

    lines.append("")

    lines.append(
        "**Skills To Add:**"
    )

    if additions:

        for skill in additions:

            lines.append(
                f"- {skill}"
            )

    else:

        lines.append(
            "- None"
        )

    lines.append("")

    lines.append(
        "**Skills To Remove:**"
    )

    if removals:

        for skill in removals:

            lines.append(
                f"- {skill}"
            )

    else:

        lines.append(
            "- None"
        )

    lines.append("")

    lines.append(
        "**Flags:**"
    )

    if flags:

        for flag in flags:

            lines.append(
                f"- {flag}"
            )

    else:

        lines.append(
            "- None"
        )

    lines.append("")
    lines.append("---")
    lines.append("")


# ==========================================================
# SAVE MARKDOWN
# ==========================================================

with open(
    markdown_report,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(lines)
    )


# ==========================================================
# SUCCESS
# ==========================================================

print("\nSUCCESS\n")

print(
    f"JSON Report:\n{json_report}"
)

print(
    f"\nMarkdown Report:\n{markdown_report}"
)
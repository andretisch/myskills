#!/usr/bin/env python3
"""Convert project resume/cover MD (subset) to Word."""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Pt


def add_runs(paragraph, text: str, base_bold=False):
    """Parse **bold** and `code` in text."""
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Courier New"
        else:
            run = paragraph.add_run(part)
            if base_bold:
                run.bold = True


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and "|" in s[1:-1]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.match(r"^:?-+:?$", c.strip()) for c in cells if c.strip())


def convert(md_path: Path, docx_path: Path) -> None:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    i = 0
    table_buffer: list[list[str]] = []

    def flush_table():
        nonlocal table_buffer
        if not table_buffer:
            return
        rows = [[c.strip() for c in row.strip().strip("|").split("|")] for row in table_buffer]
        table_buffer = []
        if len(rows) < 2:
            return
        if is_separator_row(rows[1]):
            rows.pop(1)
        ncol = max(len(r) for r in rows)
        tbl = doc.add_table(rows=len(rows), cols=ncol)
        tbl.style = "Table Grid"
        for ri, row in enumerate(rows):
            for ci in range(ncol):
                val = row[ci] if ci < len(row) else ""
                cell = tbl.rows[ri].cells[ci]
                cell.text = ""
                p = cell.paragraphs[0]
                add_runs(p, val)

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if is_table_row(line):
            table_buffer.append(line)
            i += 1
            continue
        flush_table()

        if stripped == "---":
            doc.add_paragraph().add_run().add_break(WD_BREAK.LINE)
            i += 1
            continue

        if stripped.startswith("# "):
            doc.add_heading(stripped[2:].strip(), level=1)
            i += 1
            continue
        if stripped.startswith("## "):
            doc.add_heading(stripped[3:].strip(), level=2)
            i += 1
            continue
        if stripped.startswith("### "):
            doc.add_heading(stripped[4:].strip(), level=3)
            i += 1
            continue

        if stripped.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, stripped[2:])
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        p = doc.add_paragraph()
        add_runs(p, stripped)

        i += 1

    flush_table()
    doc.save(docx_path)
    print(docx_path)


def main():
    if len(sys.argv) != 3:
        print("Usage: md_to_docx.py input.md output.docx")
        sys.exit(1)
    convert(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
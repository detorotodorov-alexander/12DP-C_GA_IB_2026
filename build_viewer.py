#!/usr/bin/env python3
"""Builds index.html: a simple viewer of the repo for the teachers.
Run from the repo root:  python3 build_viewer.py
It embeds README.md and report/project_plan.md, so index.html works
offline, on GitHub Pages or just by downloading it."""
import json, subprocess, pathlib, html

REPO = "https://github.com/detorotodorov-alexander/12DP-C_GA_IB_2026"
BRANCH = "main"
root = pathlib.Path(__file__).resolve().parent

plan = (root / "report/project_plan.md").read_text(encoding="utf-8")
readme = (root / "README.md").read_text(encoding="utf-8")
try:
    files = subprocess.run(["git", "ls-files"], cwd=root, capture_output=True,
                           text=True, check=True).stdout.split("\n")
except Exception:
    files = [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
files = sorted(f for f in files if f and not f.endswith(".gitkeep"))

page = (root / "viewer_template.html").read_text(encoding="utf-8")
data = {"plan": plan, "readme": readme, "files": files, "repo": REPO, "branch": BRANCH}
page = page.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html written,", len(files), "files listed")

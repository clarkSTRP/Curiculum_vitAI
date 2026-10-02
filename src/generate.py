import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


BASE_DIR = Path(__file__).resolve().parent.parent

JSON_PATH = BASE_DIR / "data" / "profile_master_sustek_yoni.json"
TEMPLATE_DIR = BASE_DIR / "templates"
TEMPLATE_NAME = "modern_cv.html.j2"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "cv.html"


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_cv():
    OUTPUT_DIR.mkdir(exist_ok=True)

    profile = load_json(JSON_PATH)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=True
    )

    template = env.get_template(TEMPLATE_NAME)

    html = template.render(**profile)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"CV généré : {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_cv()
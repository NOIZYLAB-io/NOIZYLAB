from pydantic import BaseModel, Field
from pathlib import Path
import json
import datetime

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "prompts"
PACKS_DIR = PROMPTS_DIR / "packs"
TEMPLATES_DIR = PROMPTS_DIR / "templates"
OUT_MD_DIR = PROMPTS_DIR / "packs"

class OutputSpec(BaseModel):
    format: str = "png"
    size: str = "1024x1024"

class Prompt(BaseModel):
    project: str
    act: str
    style: str
    palette: list[str] = Field(default_factory=list)
    voice: str = ""
    use_case: str
    output: OutputSpec = OutputSpec()
    notes: str = ""

def to_markdown(p: Prompt) -> str:
    palette = ", ".join(p.palette) if p.palette else "default"
    return f"""Project: {p.project}
Act: {p.act}
Style: {p.style}
Palette: {palette}
Voice: {p.voice}
Use case: {p.use_case}
Output: {p.output.format.upper()} {p.output.size}
Notes: {p.notes}
"""

def save_prompt(p: Prompt, pack_name: str):
    PACKS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    json_path = PACKS_DIR / f"{pack_name}__{p.project}__{p.act}__{stamp}.json"
    md_path = PACKS_DIR / f"{pack_name}__{p.project}__{p.act}__{stamp}.md"
    json_path.write_text(json.dumps(p.model_dump(), indent=2))
    md_path.write_text(to_markdown(p))
    print(f"Saved:\n- {json_path}\n- {md_path}")

def new_from_template(template_name: str, overrides: dict, pack_name: str):
    tpl_path = TEMPLATES_DIR / f"{template_name}.json"
    data = json.loads(tpl_path.read_text())
    data.update(overrides or {})
    p = Prompt(**data)
    save_prompt(p, pack_name)

if __name__ == "__main__":
    # Example: generate a NoizyRubber poster prompt from base template with quick overrides
    overrides = {
        "act": "Campaign Poster A2",
        "notes": "Add QR code for donations; emphasize modularity."
    }
    new_from_template("base", overrides, pack_name="NoizyRubber_Revival")

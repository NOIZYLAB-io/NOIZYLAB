os
import datetime
import sys

SAVE_DIR = "VS_Buddy_Setup/Saved_Notes"

def save_output(text):
    os.makedirs(SAVE_DIR, exist_ok=True)
    fname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M") + ".txt"
    fpath = os.path.join(SAVE_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n💾 Saved output to {fpath}")

answer = response.choices[0].message.content
print("🎯 Super Brain says:\n")
print(answer.strip())

if "--save" in sys.argv:
    save_output(answer.strip())
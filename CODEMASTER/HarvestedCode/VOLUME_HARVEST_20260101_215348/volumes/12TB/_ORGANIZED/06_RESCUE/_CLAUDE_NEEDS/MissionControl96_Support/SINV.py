import os
import shutil
import argparse
from pathlib import Path
from PIL import Image

def auto_save_script():
    script_path = Path(__file__)
    with open(script_path, 'r') as f:
        content = f.read()
    with open(script_path, 'w') as f:
        f.write(content)

def ensure_extension(file_path):
    valid_exts = ['.icns', '.png', '.jpg', '.jpeg']
    ext = file_path.suffix.lower()
    if ext in valid_exts:
        return file_path
    try:
        with Image.open(file_path) as img:
            if img.format == 'PNG':
                new_path = file_path.with_suffix('.png')
            elif img.format == 'JPEG':
                new_path = file_path.with_suffix('.jpg')
            else:
                return file_path
            return new_path
    except Exception:
        return file_path

def move_and_fix_extensions(src_dir, dst_dir, dry_run=False):
    os.makedirs(dst_dir, exist_ok=True)
    files_moved = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = Path(root) / file
            # Only move image/icon files
            if src_file.suffix.lower() in ['.icns', '.png', '.jpg', '.jpeg'] or not src_file.suffix:
                dst_file = Path(dst_dir) / file
                # Avoid overwriting files with same name
                if dst_file.exists():
                    dst_file = Path(dst_dir) / (src_file.stem + '_' + str(len(files_moved)) + src_file.suffix)
                fixed_file = ensure_extension(dst_file)
                if dry_run:
                    print(f"[DRY RUN] Would move: {src_file} -> {dst_file}")
                    if fixed_file != dst_file:
                        print(f"[DRY RUN] Would rename: {dst_file} -> {fixed_file}")
                else:
                    shutil.move(str(src_file), str(dst_file))
                    if fixed_file != dst_file:
                        dst_file.rename(fixed_file)
                        print(f"Renamed {dst_file} to {fixed_file}")
                files_moved.append(str(fixed_file))
    # Remove empty folders
    for root, dirs, files in os.walk(src_dir, topdown=False):
        if not os.listdir(root):
            if dry_run:
                print(f"[DRY RUN] Would remove empty folder: {root}")
            else:
                try:
                    os.rmdir(root)
                except Exception:
                    pass

def main():
    auto_save_script()
    parser = argparse.ArgumentParser(description="Organize and clean icon files.")
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done, but do not move files.')
    args = parser.parse_args()

    src_dir = '/Users/rsp_ms/Pictures/iCons'
    dst_dir = '/Users/rsp_ms/Pictures/iCons/Source_All_iCons_CLEANED'
    move_and_fix_extensions(src_dir, dst_dir, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
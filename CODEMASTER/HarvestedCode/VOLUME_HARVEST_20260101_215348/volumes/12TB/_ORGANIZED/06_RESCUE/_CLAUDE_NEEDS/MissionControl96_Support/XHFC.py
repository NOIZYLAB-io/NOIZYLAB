import os
import shutil
import argparse
from pathlib import Path
from PIL import Image

def get_fixed_extension(file_path):
    valid_exts = ['.icns', '.png', '.jpg', '.jpeg']
    ext = file_path.suffix.lower()
    if ext in valid_exts or not file_path.is_file():
        return file_path
    # Only try to fix files with no extension
    if ext == '':
        try:
            with Image.open(file_path) as img:
                if img.format == 'PNG':
                    return file_path.with_suffix('.png')
                elif img.format == 'JPEG':
                    return file_path.with_suffix('.jpg')
        except Exception:
            pass
    return file_path

def move_and_fix_extensions(src_dir, dst_dir, dry_run=False):
    os.makedirs(dst_dir, exist_ok=True)
    files_moved = []
    for root, dirs, files in os.walk(src_dir):
        # Skip the destination folder
        if Path(root).resolve() == Path(dst_dir).resolve():
            continue
        for file in files:
            if file == '.DS_Store':
                continue
            src_file = Path(root) / file
            # Only move image/icon files or files without extension
            if src_file.suffix.lower() in ['.icns', '.png', '.jpg', '.jpeg'] or not src_file.suffix:
                fixed_dst_file = get_fixed_extension(Path(dst_dir) / file)
                # Avoid overwriting files with same name
                if fixed_dst_file.exists():
                    fixed_dst_file = fixed_dst_file.with_name(f"{fixed_dst_file.stem}_{len(files_moved)}{fixed_dst_file.suffix}")
                if dry_run:
                    print(f"[DRY RUN] Would move: {src_file} -> {fixed_dst_file}")
                else:
                    shutil.move(str(src_file), str(fixed_dst_file))
                files_moved.append(str(fixed_dst_file))
    # Remove empty folders except destination
    for root, dirs, files in os.walk(src_dir, topdown=False):
        if Path(root).resolve() == Path(dst_dir).resolve():
            continue
        if not os.listdir(root):
            if dry_run:
                print(f"[DRY RUN] Would remove empty folder: {root}")
            else:
                try:
                    os.rmdir(root)
                except Exception:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Organize and clean icon files.")
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done, but do not move files.')
    args = parser.parse_args()

    src_dir = '/Users/rsp_ms/Pictures/iCons'
    dst_dir = '/Users/rsp_ms/Pictures/iCons/Source_All_iCons_CLEANED'
    move_and_fix_extensions(src_dir, dst_dir, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
ls -l /Users/rsp_ms/The_Aquarium/NoizyWorkspace/
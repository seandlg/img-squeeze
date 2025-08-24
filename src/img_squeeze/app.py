import argparse
import sys
from pathlib import Path
from typing import Sequence

from PIL import Image

# Using a high-quality resampling filter is important for downscaling.
RESAMPLE_FILTER = Image.Resampling.LANCZOS


def process_image(
    input_path: Path,
    output_dir: Path,
    max_dim: int,
    jpeg_quality: int,
    png_compression: int,
) -> None:
    """Resizes and compresses a single image, saving it to the output directory."""
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(
            f"Error: Could not open {input_path}. Skipping. ({e})",
            file=sys.stderr,
        )
        return

    original_w, original_h = img.size
    if max(original_w, original_h) > max_dim:
        print(f"Resizing {input_path.name}...")
        aspect_ratio = original_w / original_h
        if original_w > original_h:
            new_w = max_dim
            new_h = int(new_w / aspect_ratio)
        else:
            new_h = max_dim
            new_w = int(new_h * aspect_ratio)

        img = img.resize((new_w, new_h), resample=RESAMPLE_FILTER)

    # Determine output path and save with appropriate compression
    output_path = output_dir / input_path.name
    # Use the suffix to determine format, falling back to Pillow's detection
    suffix = input_path.suffix.lower()

    try:
        if suffix in (".jpeg", ".jpg"):
            # Convert RGBA to RGB for JPEG compatibility
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(
                output_path,
                "jpeg",
                quality=jpeg_quality,
                optimize=True,
                progressive=True,
            )
            print(f"Saved {output_path} (JPEG quality: {jpeg_quality})")
        elif suffix == ".png":
            img.save(
                output_path,
                "png",
                compress_level=png_compression,
                optimize=True,
            )
            print(f"Saved {output_path} (PNG compression: {png_compression})")
        else:
            print(
                f"Warning: Unsupported format '{suffix}' for {input_path.name}. Skipping.",
                file=sys.stderr,
            )
    except Exception as e:
        print(
            f"Error: Could not save {output_path}. Skipping. ({e})",
            file=sys.stderr,
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="A CLI tool to resize and compress JPEG/PNG images.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input_files",
        metavar="FILE",
        type=Path,
        nargs="+",
        help="One or more image files to process.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("./processed_images"),
        help="Directory to save processed images.",
    )
    parser.add_argument(
        "--max-dim",
        type=int,
        default=1024,
        help="Maximum width or height for resized images.",
    )
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=85,
        choices=range(1, 96),
        metavar="[1-95]",
        help="JPEG quality for compression (1-95).",
    )
    parser.add_argument(
        "--png-compression",
        type=int,
        default=6,
        choices=range(0, 10),
        metavar="[0-9]",
        help="PNG compression level (0=none, 9=max).",
    )

    args = parser.parse_args(argv)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in args.input_files:
        if not file_path.is_file():
            print(
                f"Warning: {file_path} is not a file. Skipping.",
                file=sys.stderr,
            )
            continue
        process_image(
            file_path,
            args.output_dir,
            args.max_dim,
            args.jpeg_quality,
            args.png_compression,
        )

    print(f"\nProcessing complete. Output is in '{args.output_dir}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

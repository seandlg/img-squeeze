# img-squeeze

A simple tool to resize images.

## Usage

First, install [uv](https://docs.astral.sh/uv/).

### Ephemeral Usage

To run `img-squeeze` without installing it globally, use `uvx`:

#### Show Help

```bash
uvx --from git+https://github.com/seandlg/img-squeeze -- img-squeeze --help
```

```text
usage: img-squeeze [-h] [-o OUTPUT_DIR] [--max-dim MAX_DIM] [--jpeg-quality [1-95]] [--png-compression [0-9]] FILE [FILE ...]

A CLI tool to resize and compress JPEG/PNG images.

positional arguments:
  FILE                  One or more image files to process.

options:
  -h, --help            show this help message and exit
  -o, --output-dir OUTPUT_DIR
                        Directory to save processed images. (default: processed_images)
  --max-dim MAX_DIM     Maximum width or height for resized images. (default: 1024)
  --jpeg-quality [1-95]
                        JPEG quality for compression (1-95). (default: 85)
  --png-compression [0-9]
                        PNG compression level (0=none, 9=max). (default: 6)
```

#### Compress an Image

```bash
uvx --from git+https://github.com/seandlg/img-squeeze -- img-squeeze img.jpg
```

```text
Resizing img.jpg...
Saved processed_images/img.jpg (JPEG quality: 85)

Processing complete. Output is in 'processed_images'.
```

> [!TIP]
> If you use `img-squeeze` a lot, install it as a tool:
> ```bash
> uv tool install git+https://github.com/seandlg/img-squeeze
> ```
> This enables running `img-squeeze` in the terminal.

## License

MIT

## Feature requests

Please [open an issue](https://github.com/seandlg/img-squeeze/issues/new) if you have a feature request. I will add features as I need them.

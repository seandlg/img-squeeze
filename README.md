# img-squeeze

A simple tool to resize images to a maximum dimension and save them as JPEG or PNG.

## Usage

Install [uv](https://docs.astral.sh/uv/).

Ephemeral usage:

```bash
# Show help
uvx --from git+https://github.com/seandlg/img-squeeze -- img-squeeze --help
# Compress an image
uvx --from git+https://github.com/seandlg/img-squeeze -- img-squeeze img.jpg
```

or install as a tool:

```bash
uv tool install git+https://github.com/seandlg/img-squeeze
```

and use anywhere as `img-squeeze`.

## License

MIT

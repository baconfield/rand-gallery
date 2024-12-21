Extremely simple gallery site that displays random images from a directory.

```sh
uv sync
# Defaults to files added to the 'images' directory
uv run uvicorn --reload 'index:app'
# Alternatively, specify a directory
env RAND_IMAGES='/home/<user>/Pictures' uv run uvicorn --reload 'index:app'
```

Once running, the page is accessible on port 8000: `http://localhost:8000/`. You can specify a maximum image count by adding the parameter `?maximum=<int>` to the URL.

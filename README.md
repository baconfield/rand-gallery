This is an extremely simple gallery that displays a random image from a directory of images.

```sh
uv sync
# Defaults to files added to the 'images' directory
uv run uvicorn --reload 'index:app'
# Alternatively, specify a directory
env RAND_IMAGES='/home/<user>/Pictures' uv run uvicorn --reload 'index:app'
```

Page accessable at `http://localhost:8000/`, and can specify the maximum image count by adding the parameter `?maximum=<int>` to the URL.

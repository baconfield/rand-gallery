Extremely simple gallery site that displays random images from a directory.

```sh
uv sync
# Defaults to files added to the 'images' directory
uv run uvicorn --reload 'index:app'
# Alternatively, specify a directory
env RAND_IMAGES='/home/<user>/Pictures' uv run uvicorn --reload 'index:app'
```

Once running, the page is accessible on port 8000: `http://localhost:8000/`. You can specify a maximum image count by adding the parameter `?maximum=<int>` to the URL.

Note: This uses the Masonry grid layout, and depending on when this is used, a feature flag may need to be enabled in the browser. https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Masonry_layout

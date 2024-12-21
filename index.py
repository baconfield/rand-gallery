from os import environ, getcwd, walk
from os.path import isfile, join
from random import shuffle

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

STYLE = """
<style>
* {
	box-sizing: border-box;
}
body {
  font-family: sans-serif;
  background: linear-gradient(90deg, #157858, #012b3b);
}
div {
  display: grid;
  grid-template-rows: masonry;
  grid-template-columns: repeat(auto-fill, max(19rem));
  grid-gap: 0.7rem;
}
card {
  margin: 0;
  box-shadow: 0px 0px 2px #012029;
  background: #00000054;
  border-radius: 5px;
  backdrop-filter: blur(15px);
}
card-title {
  padding: 0.2rem 0.6rem;
  color: #fff;
  font-size: 0.8rem;
}
img {
  width: 100%;
  display: block;
  border-radius: 5px;
}
</style>
"""
CARD_TEMPLATE = (
    "\n<card><card-title>{title}</card-title><img src=/pictures/{path}></card>"
)


server_route = getcwd()
image_route = environ.get("RAND_IMAGES", join(server_route, "pictures"))
supported_files = (  # Add more as needed, just filtering out random junk
    ".png",
    ".jpeg",
    ".gif",
    ".jpg",
)

app = FastAPI()
app.mount("/pictures", StaticFiles(directory=image_route))


@app.get("/", response_class=HTMLResponse)
async def index(
    maximum: int = 15,
):
    body = "<!DOCTYPE html>" + STYLE + "<body><div>"
    for image in await random_images(maximum):
        title = image.split("/")[-1].split(".")[0]
        path = image.replace(" ", "%20")
        body += CARD_TEMPLATE.format(title=title, path=path)
    body += "</div></body>"

    return body


async def random_images(maximum: int = 15):
    images = list(await get_images(image_route))
    shuffle(images)
    return images[: min(len(images), maximum)]


async def get_images(folder: str):
    images = set()
    for dirpath, folders, files in walk(folder):
        images.update(
            [
                join(dirpath.replace(image_route, ""), f)
                for f in files
                if isfile(join(dirpath, f)) and f.endswith(supported_files)
            ]
        )
        for subfolder in folders:
            images.update(await get_images(subfolder))
    return images

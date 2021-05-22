import re, os, mimetypes

BUILD_PATH = os.getcwd() + "/../sv/build"

def load_from_route(path):
    # Manually added route regexes
    match = re.search(r"^/airplane/(\d+)$", path)
    if match:
        path = BUILD_PATH + "/airplane/XXX/index.html"
        if os.path.isfile(path):
            with open(path, "rb") as f:
                return f.read()
    return None

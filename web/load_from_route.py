import re, os, mimetypes

BUILD_PATH = os.getcwd() + "/../sv/build"

def load_from_route(path):
    # Manually added route regexes
    match = re.search(r"^/airplane/(\w+)$", path)
    if match:
        path = BUILD_PATH + "/airplane/[id]/index.html"
        if os.path.isfile(path):
            with open(path, "rb") as f:
                html = f.read().decode("utf-8")
                # Can't just replace [id] everywhere because that gets one of
                # the modulepreload link tags.
                # return html.replace("[id]", match[1]).encode("utf-8")

                # For a first pass we just do something hacky, since the ones
                # we want to replace all end with a quote.
                return html.replace("[id]\"", match[1] + "\"").encode("utf-8")

    return None

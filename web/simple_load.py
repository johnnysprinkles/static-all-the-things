import re, os, mimetypes

BUILD_PATH = os.getcwd() + "/../sv/build"

"""
This just looks in the /build folder for a file of the same
name, and has no knowledge of the routes in
.svelte-kit/build/generated/manifest.js

This obviously won"t work for routes with square bracket
parameters.
"""
def simple_load(path):
    artifact_path = BUILD_PATH + path
    if not re.search(r"\.\w+$", artifact_path):
        artifact_path += "/index.html"

    if os.path.isfile(artifact_path):
        type, encoding = mimetypes.guess_type(artifact_path)
        with open(artifact_path, "rb") as f:
            return (f.read(), type)

    return (None, None)

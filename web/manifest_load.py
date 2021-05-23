import re, os, mimetypes

BUILD_PATH = os.getcwd() + "/../sv/build"
MANIFEST_PATH = os.getcwd() + "/../sv/.svelte-kit/build/generated/manifest.js"

routes = []

with open(MANIFEST_PATH) as f:
    manifest = f.read()
    routes_match = re.search(r"export const routes = \[\n(.*?)\n\];", manifest, re.DOTALL)
    for route_string in routes_match[1].split("\n\n"):
        route_match = re.search(r"^.*//\s*src/routes(.*)\.svelte\n\s*\[/(.*)/.*", route_string)
        if route_match:
            route_file, route_regex = route_match.groups()
            if route_file.endswith("/index"):
                route_file += ".html"
            else:
                route_file += "/index.html"
            routes.append((BUILD_PATH + route_file, re.compile(route_regex)))

def manifest_load(path):
    for route in routes:
        m = route[1].search(path)
        if m:
            with open(route[0], "rb") as f:
                html = f.read().decode("utf-8")
                # Hacky regex to pull out hydrate.page object as passed to start().
                page_store = re.search(r"page: {(.*?)\n\s*}", html, re.DOTALL)
                if page_store:
                    # Will be false if no hydration on the page.
                    start_params = page_store.group(1)
                    span = page_store.span(1)
                    params = re.findall(r"\[\w+\]", route[0])
                    for name, value in zip(params, m.groups()):
                        start_params = start_params.replace(name, value)
                    html = html[:span[0]] + start_params + html[span[1]:] # splice
                    # TODO: Also go ahead and set "host" and "query".
                return html.encode("utf-8")

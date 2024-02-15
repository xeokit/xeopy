from xeopy import *
import webbrowser


class Xeokit:
    def __init__(self, **kwargs):
        default_kwargs = {
            "header": """<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>xeokit Example</title>
    <style>
        body {
            margin: 0;
            width: 100%;
            height: 100%;
            user-select: none;
        }

        #xeokit_canvas {
            width: 100%;
            height: 100%;
            position: absolute;
            background: lightblue;
            background-image: linear-gradient(lightblue, white);
        }
    </style>
</head>
<body>
<canvas id="xeokit_canvas"></canvas>
</body>
<script id="source" type="module">
""",
            "content": [Viewer(), CameraSettings()],
            "footer": """
</script>
</html>
""",
        }
        kwargs = default_kwargs | kwargs
        self.header = kwargs["header"]
        self.content = kwargs["content"]
        self.footer = kwargs["footer"]

    def create(self):
        script = ""
        for i in self.content:
            script += str(i) + "\n"
        return self.header + self.__create_import() + script + self.footer

    def __create_import(self):
        libraries_needed = set()
        for i in self.content:
            for j in i.get_xeokit_modules_needed():
                libraries_needed.add(j)
        return "import " + str(libraries_needed).replace("'", "") + """ from
                "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";
"""

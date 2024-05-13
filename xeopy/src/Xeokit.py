from xeopy import *


class Xeokit:
    def __init__(self, **kwargs):
        self.content = kwargs["content"]
        self.file_path = kwargs["file_path"]

    def create(self):
        script = ""
        for i in self.content:
            if isinstance(i, list):
                for j in i:
                    script += str(j) + "\n"
            else:
                script += str(i) + "\n"

        return self.__create_header() +\
            self.__create_xeokit_modules_import() +\
            self.__create_additional_imports() +\
            script +\
            self.__create_footer()

    def create_and_save(self):
        xeokit_content = self.create()
        f = open(self.file_path, "w")
        f.write(xeokit_content)
        f.close()

    def __create_header(self):
        return """<!doctype html>
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
"""

    def __create_footer(self):
        return """
</script>
</html>
"""

    def __create_xeokit_modules_import(self):
        libraries_needed = set()
        for i in self.content:
            if isinstance(i, list):
                for j in i:
                    for k in j.get_xeokit_modules_needed():
                        libraries_needed.add(k)
            else:
                for j in i.get_xeokit_modules_needed():
                    libraries_needed.add(j)
        return "import " + str(libraries_needed).replace("'", "") + """ from
                "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/xeokit-sdk.es.min.js";
"""

    def __create_additional_imports(self):
        imports_needed = set()
        for i in self.content:
            if isinstance(i, list):
                for j in i:
                    for k in j.get_additional_imports():
                        imports_needed.add(k)
            else:
                for j in i.get_additional_imports():
                    imports_needed.add(j)
        imports_string = ""
        for i in imports_needed:
            imports_string += i + "\n"
        return imports_string

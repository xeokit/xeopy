
class Mesh:
    def __init__(self, **kwargs):
        default_kwargs = {"positions": [0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 5.0, 0.0],
                          "indices": [0, 1, 2],
                          "normals": [],
                          "uv": [],
                          "color": [0.0, 1.0, 0.0],
                          "edges": True,
                          "viewer_variable_name": "viewer"}
        kwargs = default_kwargs | kwargs
        self.positions = kwargs["positions"]
        self.indices = kwargs["indices"]
        self.normals = kwargs["normals"]
        self.uv = kwargs["uv"]
        self.color = kwargs["color"]
        self.edges = kwargs["edges"]
        self.viewer_variable_name = kwargs["viewer_variable_name"]

    def __str__(self):
        return "".join(["new Mesh(", self.viewer_variable_name, ".scene,", "{\n",
                        "   geometry: new ReadableGeometry(", self.viewer_variable_name, ".scene, {", "\n",
                        "       primitive: \"triangles\",\n",
                        "       positions: ", str(self.positions), ",\n",
                        "       indices: ", str(self.indices), ",\n",
                        "       normals: ", str(self.normals), ",\n",
                        "       uv: ", str(self.uv), ",\n",
                        "   }),", "\n",
                        "   material: new PhongMaterial(", self.viewer_variable_name, ".scene, {", "\n"
                        "       diffuse: ", str(self.color), ",", "\n",
                        "   }),", "\n",
                        "   edges: ", str(self.edges).lower(), ",", "\n",
                        "});"])

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"ReadableGeometry", "Mesh", "PhongMaterial"}

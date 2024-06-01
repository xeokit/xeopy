
class VectorText:
    def __init__(self, **kwargs):
        default_kwargs = {"text": "Vector text content",
                          "size": 2,
                          "line_width": 2,
                          "position": [0.0, 0.0, 0.0],
                          "color": [0.0, 0.0, 0.0],
                          "viewer_variable_name": "viewer"}
        kwargs = default_kwargs | kwargs
        self.text = kwargs["text"]
        self.size = kwargs["size"]
        self.line_width = kwargs["line_width"]
        self.position = kwargs["position"]
        self.color = kwargs["color"]
        self.viewer_variable_name = kwargs["viewer_variable_name"]

    def __str__(self):
        return "".join(["new Mesh(", self.viewer_variable_name, ".scene,", "{\n",
                        "   geometry: new ReadableGeometry(", self.viewer_variable_name, ".scene, buildVectorTextGeometry({", "\n",
                        "       text: `", self.text, "`,\n",
                        "       size: ", str(self.size), ",\n",
                        "   })),", "\n",
                        "   material: new PhongMaterial(", self.viewer_variable_name, ".scene, {", "\n"
                        "       diffuse: ", str(self.color), ",", "\n",
                        "       lineWidth: ", str(self.line_width), ",", "\n",
                        "   }),", "\n",
                        "position: ", str(self.position), "\n",
                        "});"])

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"ReadableGeometry", "buildVectorTextGeometry", "Mesh", "PhongMaterial"}


class Box:
    def __init__(self, **kwargs):
        default_kwargs = {"x_size": 1.0,
                          "y_size": 1.0,
                          "z_size": 1.0,
                          "center": [0.0, 0.0, 0.0],
                          "color": [0.0, 0.0, 0.0],
                          "viewer_id": "viewer"}
        kwargs = default_kwargs | kwargs
        self.x_size = kwargs["x_size"]
        self.y_size = kwargs["y_size"]
        self.z_size = kwargs["z_size"]
        self.center = kwargs["center"]
        self.color = kwargs["color"]
        self.viewer_id = kwargs["viewer_id"]

    def __str__(self):
        return "".join(["new Mesh(", self.viewer_id, ".scene,", "{\n",
                        "   geometry: new ReadableGeometry(", self.viewer_id, ".scene, buildBoxGeometry({", "\n",
                        "       center: ", str(self.center), ",\n",
                        "       xSize: ", str(self.x_size), ",\n",
                        "       ySize: ", str(self.y_size), ",\n",
                        "       zSize: ", str(self.z_size), ",\n",
                        "   })),", "\n",
                        "   material: new PhongMaterial(", self.viewer_id, ".scene, {", "\n"
                        "       diffuse: ", str(self.color), ",", "\n",
                        "   })",
                        "});"])

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"ReadableGeometry", "buildBoxGeometry", "Mesh", "PhongMaterial"}

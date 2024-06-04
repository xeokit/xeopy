
class Sphere:
    def __init__(self, **kwargs):
        default_kwargs = {"radius": 1.0,
                          "height_segments": 60,
                          "width_segments": 60,
                          "center": [0.0, 0.0, 0.0],
                          "color": [0.0, 0.0, 0.0],
                          "viewer_variable_name": "viewer"}
        kwargs = default_kwargs | kwargs
        self.radius = kwargs["radius"]
        self.height_segments = kwargs["height_segments"]
        self.width_segments = kwargs["width_segments"]
        self.center = kwargs["center"]
        self.color = kwargs["color"]
        self.viewer_variable_name = kwargs["viewer_variable_name"]

    def __str__(self):
        return "".join(["new Mesh(", self.viewer_variable_name, ".scene,", "{\n",
                        "   geometry: new ReadableGeometry(", self.viewer_variable_name, ".scene, buildSphereGeometry({", "\n",
                        "       center: ", str(self.center), ",\n",
                        "       radius: ", str(self.radius), ",\n",
                        "       heightSegments: ", str(self.height_segments), ",\n",
                        "       widthSegments: ", str(self.width_segments), ",\n",
                        "   })),", "\n",
                        "   material: new PhongMaterial(", self.viewer_variable_name, ".scene, {", "\n"
                        "       diffuse: ", str(self.color), ",", "\n",
                        "   })",
                        "});"])

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"ReadableGeometry", "buildSphereGeometry", "Mesh", "PhongMaterial"}

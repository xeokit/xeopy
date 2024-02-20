class CameraSettings:
    def __init__(self, **kwargs):
        default_kwargs = {"viewer_id": "viewer", "eye": [-3.933, 2.855, 27.018], "look": [4.400, 3.724, 8.899],
                          "up": [-0.018, 0.999, 0.039]}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.eye = kwargs["eye"]
        self.look = kwargs["look"]
        self.up = kwargs["up"]

    def __str__(self):
        return "".join([self.viewer_id, ".camera.eye = + ", str(self.eye), ";\n",
                        self.viewer_id, ".camera.look = + ", str(self.look), ";\n",
                        self.viewer_id, ".camera.up = + ", str(self.up), ";\n"])

    @staticmethod
    def get_xeokit_modules_needed():
        return {}

class CameraSettings:
    def __init__(self, **kwargs):
        default_kwargs = {"viewer_variable_name": "viewer", "eye": [-3.933, 2.855, 27.018], "look": [4.400, 3.724, 8.899],
                          "up": [-0.018, 0.999, 0.039]}
        kwargs = default_kwargs | kwargs
        self.viewer_variable_name = kwargs["viewer_variable_name"]
        self.eye = kwargs["eye"]
        self.look = kwargs["look"]
        self.up = kwargs["up"]

    def __str__(self):
        return "".join([self.viewer_variable_name, ".camera.eye = + ", str(self.eye), ";\n",
                        self.viewer_variable_name, ".camera.look = + ", str(self.look), ";\n",
                        self.viewer_variable_name, ".camera.up = + ", str(self.up), ";\n"])

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}

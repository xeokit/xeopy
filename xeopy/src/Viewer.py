class Viewer:
    def __init__(self, **kwargs):
        default_kwargs = {"variable_name": "viewer", "canvas_id": "xeokit_canvas", "transparent": True, "dtx_enabled": True}
        kwargs = default_kwargs | kwargs
        self.variable_name = kwargs["variable_name"]
        self.canvas_id = kwargs["canvas_id"]
        self.transparent = kwargs["transparent"]
        self.dtx_enabled = kwargs["dtx_enabled"]

    def __str__(self):
        return "".join(["const ", self.variable_name, " = new Viewer({\n",
                        "    canvasId: \"", self.canvas_id, "\",\n",
                        "    transparent: ", str(self.transparent).lower(), ",\n",
                        "    dtxEnabled: ", str(self.dtx_enabled).lower(), "\n",
                        "});"])

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"Viewer"}

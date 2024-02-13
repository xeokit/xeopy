class Viewer:
    def __init__(self, **kwargs):
        default_kwargs = {"viewer_id": "viewer", "canvas_id": "xeokit_canvas", "transparent": True, "dtx_enabled": True}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.canvas_id = kwargs["canvas_id"]
        self.transparent = kwargs["transparent"]
        self.dtx_enabled = kwargs["dtx_enabled"]

    def __str__(self):
        return "const " + self.viewer_id + " = new Viewer({\n" + "    canvasId: \"" + self.canvas_id + "\",\n" + "    transparent: " + str(self.transparent).lower() + ",\n" + "    dtxEnabled: " + str(self.dtx_enabled).lower() + "\n""});"

    @staticmethod
    def get_xeokit_modules_needed():
        return {"Viewer"}

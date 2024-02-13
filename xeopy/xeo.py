class Viewer:
    def __init__(self, **kwargs):
        default_kwargs = {"viewer_id": "viewer", "canvas_id": "xeokit_canvas", "transparent": True, "dtx_enabled": True}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.canvas_id = kwargs["canvas_id"]
        self.transparent = kwargs["transparent"]
        self.dtx_enabled = kwargs["dtx_enabled"]

    def __str__(self):
        return """const {} = new Viewer({
        canvasId: "{}",
        transparent: {},
        dtxEnabled: {} // Enable data texture model representation
        });""".format(self.viewer_id, self.canvas_id, self.transparent.lower(), self.dtx_enabled.lower())

    @staticmethod
    def get_libraries_needed():
        return {"Viewer"}

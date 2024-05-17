class SectionPlanesPlugin:

    def __init__(self, **kwargs):
        default_kwargs = {"viewer_id": "viewer",
                          "section_planes_plugin_id": "sectionPlanes",
                          "overview_canvas_id": "mySectionPlanesOverviewCanvas",
                          "overview_visible": True}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.section_planes_plugin_id = kwargs["section_planes_plugin_id"]
        self.overview_canvas_id = kwargs["overview_canvas_id"]
        self.overview_visible = kwargs["overview_visible"]

    def __str__(self):
        return "".join(
            ["const ", self.section_planes_plugin_id, "= new SectionPlanesPlugin(", self.viewer_id, ", {", "\n",
             "overviewCanvasId: \"", self.overview_canvas_id, "\",", "\n",
             "overviewVisible: ", str(self.overview_visible).lower(), ",", "\n",
             "});"])

    def get_additional_styles(self):
        return {"""#""" + self.overview_canvas_id + """ {
            position: absolute;
            width: 250px;
            height: 250px;
            bottom: 70px;
            right: 10px;
            z-index: 200000;
            /*border: 1px solid blue;*/
        }"""}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"SectionPlanesPlugin"}

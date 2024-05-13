class IfcLoader:
    def __init__(self, **kwargs):
        default_kwargs = {"path": "Duplex.ifc", "edges": True, "viewer_id": "viewer"}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.path = kwargs["path"]
        self.edges = kwargs["edges"]

    def __str__(self):
        return """
    const IfcAPI = new WebIFC.IfcAPI();
    IfcAPI.SetWasmPath("https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/");

    IfcAPI.Init().then(() => {
        const ifcLoader = new WebIFCLoaderPlugin(""" + self.viewer_id + """, {
            WebIFC,
            IfcAPI
        });

        const model = ifcLoader.load({
            src: \"""" + self.path + """\",
            edges: """ + str(self.edges).lower() + """
        });
    });
"""

    @staticmethod
    def get_additional_styles():
        return {}

    @staticmethod
    def get_additional_imports():
        return {'import * as WebIFC from "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/web-ifc-api.js";'}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"WebIFCLoaderPlugin"}

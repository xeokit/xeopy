class WebIFCLoaderPlugin:
    def __init__(self, **kwargs):
        default_kwargs = {"variable_name": "sceneModel",
                          "viewer_variable_name": "viewer",
                          "path": "Duplex.ifc",
                          "edges": True,
                          }
        kwargs = default_kwargs | kwargs
        self.variable_name = kwargs["variable_name"]
        self.viewer_variable_name = kwargs["viewer_variable_name"]
        self.path = kwargs["path"]
        self.edges = kwargs["edges"]

    def __str__(self):
        return """
    const IfcAPI = new WebIFC.IfcAPI();
    IfcAPI.SetWasmPath("https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/");

    IfcAPI.Init().then(() => {
        const ifcLoader = new WebIFCLoaderPlugin(""" + self.viewer_variable_name + """, {
            WebIFC,
            IfcAPI
        });

        const """ + self.variable_name + """ = ifcLoader.load({
            src: \"""" + self.path + """\",
            edges: """ + str(self.edges).lower() + """
        });
    });
"""

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {'import * as WebIFC from "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/web-ifc-api.js";'}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"WebIFCLoaderPlugin"}

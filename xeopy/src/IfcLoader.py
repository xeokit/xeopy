class IfcLoader:
    def __init__(self, **kwargs):
        default_kwargs = {"path": "Duplex.ifc", "edges": True, "viewer_id": "viewer"}
        kwargs = default_kwargs | kwargs
        self.viewer_id = kwargs["viewer_id"]
        self.path = kwargs["path"]
        self.edges = kwargs["edges"]

    def __str__(self):
        return """
    const webIFCLoader = new WebIFCLoaderPlugin(""" + self.viewer_id + """, {
        wasmPath: "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/"
    });

    const model = webIFCLoader.load({
        src: \"""" + self.path + """\",
        edges: """ + str(self.edges).lower() + """
    });
"""

    @staticmethod
    def get_xeokit_modules_needed():
        return {"WebIFCLoaderPlugin"}

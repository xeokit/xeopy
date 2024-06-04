class XKTLoaderPlugin:
    def __init__(self, **kwargs):
        default_kwargs = {"variable_name": "xktLoader",
                          "viewer_variable_name": "viewer",
                          "path": "Duplex.xkt",
                          "edges": True,
                          }
        kwargs = default_kwargs | kwargs
        self.variable_name = kwargs["variable_name"]
        self.viewer_variable_name = kwargs["viewer_variable_name"]

    def __str__(self):
        return """
    const """ + self.variable_name + """ = new XKTLoaderPlugin(""" + self.viewer_variable_name + """);
"""

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {"XKTLoaderPlugin"}

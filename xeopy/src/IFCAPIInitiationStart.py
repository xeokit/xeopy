class IFCAPIInitiationStart:
    def __init__(self, **kwargs):
        default_kwargs = {"wasm_path": "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/",}
        kwargs = default_kwargs | kwargs
        self.wasm_path = kwargs["wasm_path"]

    def __str__(self):
        return """
    const IfcAPI = new WebIFC.IfcAPI();
    IfcAPI.SetWasmPath(\"""" + self.wasm_path + """\");

    IfcAPI.Init().then(() => {"""

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {'import * as WebIFC from "' + self.wasm_path + 'web-ifc-api.js' + '";'}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}

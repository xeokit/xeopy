
class SceneModelOnLoaded:
    def __init__(self, **kwargs):
        default_kwargs = {"scene_model_id": "sceneModel", "start": True}
        kwargs = default_kwargs | kwargs
        self.scene_model_id = kwargs["scene_model_id"]
        self.start = kwargs["start"]

    def __str__(self):
        if self.start:
            return "".join([self.scene_model_id + ".on(\"loaded\", () => {"])
        else:
            return "});"

    def get_additional_styles(self):
        return {}

    @staticmethod
    def get_additional_imports():
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}

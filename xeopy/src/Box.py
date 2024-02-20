
class Box:
    def __init__(self, **kwargs):
        default_kwargs = {"x_size": 1.0, "y_size": 1.0, "z_size": 1.0, "position": [0.0, 0.0, 0.0]}
        kwargs = default_kwargs | kwargs
        self.x_size = kwargs["x_size"]
        self.y_size = kwargs["y_size"]
        self.z_size = kwargs["z_size"]
        self.position = kwargs["position"]

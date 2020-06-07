class Dimensions:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def raw(self):
        return (self.width, self.height)


RES_4_BY_3 = (
    Dimensions(width=1024, height=768),
    Dimensions(width=800, height=600),
    Dimensions(width=640, height=480),
)

RES_16_BY_9 = (
    Dimensions(width=2560, height=1440),
    Dimensions(width=1920, height=1080),
    Dimensions(width=1366, height=768),
    Dimensions(width=1280, height=720),
)

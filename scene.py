from model import *
import glm

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
        
        # 
        n, s = 15, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, s+16, z)))

        # columns
        for i in range(9):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        add(Cat(app, pos=(0, -1, -10)))

        # girl
        add(girl(app, pos=(5, 3, 20)))

        # house
        #add(house(app, pos=(0, 1, 10)))

        # moving cat
        #self.moving_cube = Cat(app, pos=(0, -1, -10))
        #add(self.moving_cube)

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 8, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time

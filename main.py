import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Charger les textures
textures = {
    1: load_texture("Assets/Textures/Brick.png"),
    2: load_texture("Assets/Textures/Dirt.png"),
    3: load_texture("Assets/Textures/Grass.png"),
    4: load_texture("Assets/Textures/Stone.png"),
    5: load_texture("Assets/Textures/Wood.png")
}


sky_bg = load_texture("Assets/Textures/Sky.png")
build_sound = Audio("Assets/SFX/Build_Sound.wav", loop=False, autoplay=False)

# Création du bloc
class Block(Button):
    def __init__(self, position=(0, 0, 0), texture=textures[3], breakable=True):
        super().__init__(
            parent=scene,
            position=position,
            model="Assets/models/Block.obj",
            origin_y=0.5,
            texture=texture,
            color=color.white,
            highlight_color=color.light_gray,
            scale=0.5
        )
        self.breakable = breakable

    # Lorsque la souris passe sur le bloc
    def on_hover(self):
        self.color = color.gray  # Appliquer la teinte grise quand la souris survole

    # Lorsque la souris quitte le bloc
    def on_out(self):
        self.color = self.original_color  # Restaurer la couleur d'origine

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_bg,
            scale=150,
            double_sided = True

        )

    def input(self, key):
        if self.hovered:
            if key == "up":
                build_sound.play()
                new_block = Block(position=self.position + mouse.normal,
                                texture=textures[3])
        elif key == "right mouse down":
            build_sound.play()
            destroy(self)


# Créer un terrain avec des blocs
for z in range(20):
    for x in range(20):
        block = Block(position=(x, 0, z))
        bedrock = Block(position=(x, -1, z), texture=textures[4], breakable=False)

player = FirstPersonController(position = (10,10,10))
player.cursor.visible = True
sky = Sky()


# Mettre à jour la scène
def update():
    if held_keys["escape"]:
        application.quit()

if __name__ == "__main__":
    app.run()
from ursina import*

app = Ursina()
player = Entity(
    model = "cube",
    color = color.gray,
    scale = (1, 2, 1),

)
def update():
    player.x += held_keys["d"] * .1
    player.x -= held_keys["a"] * .1
    player.y -= held_keys["s"] * .1
    player.y += held_keys["w"] * .1

Entity(
    model = "cube",
    color = color.white,
    y = 3,
    z = 5,
    scale = (30, 2, 20),
    origin = (0 ,5)

)

    
app.run()
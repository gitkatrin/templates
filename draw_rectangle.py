import carla

def draw_rectangle(world, center_location, dimensions):
    # calculate corners
    half_x = dimensions.x / 2.0
    half_y = dimensions.y / 2.0

    corners = [
        carla.Location(x=center_location.x - half_x, y=center_location.y - half_y, z=center_location.z),
        carla.Location(x=center_location.x + half_x, y=center_location.y - half_y, z=center_location.z),
        carla.Location(x=center_location.x + half_x, y=center_location.y + half_y, z=center_location.z),
        carla.Location(x=center_location.x - half_x, y=center_location.y + half_y, z=center_location.z),
        carla.Location(x=center_location.x - half_x, y=center_location.y - half_y, z=center_location.z)
    ]

    # draw the lines
    for i in range(len(corners) - 1):
        world.debug.draw_line(corners[i], corners[i + 1], thickness=0.1, color=carla.Color(255, 0, 0))
    
    print("Rectangle is visible now!")

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

world = client.get_world()

# coordinates of the center of the rectangle
center_location = carla.Location(x=-46.9, y=21.2, z=0.1)

dimensions = carla.Vector3D(x=70.0, y=70.0, z=0.1)

# draw the rectangle
draw_rectangle(world, center_location, dimensions)
#world.debug.draw_point()

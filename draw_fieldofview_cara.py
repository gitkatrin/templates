import carla
import numpy as np

# Connect to the CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()

# Assuming you have a camera attached to a vehicle
actor_list = world.get_actors()
vehicle = actor_list.find(id)  # replace 'id' with your vehicle's actual id
camera = None
for sensor in vehicle.get_children():
    if sensor.type_id == 'sensor.camera.rgb':
        camera = sensor
        break

if camera is not None:
    # Get camera transform
    transform = camera.get_transform()
    camera_location = transform.location
    camera_rotation = transform.rotation

    # Calculate the field of view endpoints
    fov_angle = 45  # half-angle of the FOV in degrees
    view_distance = 50  # how far the camera can see

    # Calculate direction vectors for the edges of the FOV
    direction = transform.get_forward_vector()
    yaw = np.radians(camera_rotation.yaw)
    left_yaw = yaw - np.radians(fov_angle)
    right_yaw = yaw + np.radians(fov_angle)
    left_direction = carla.Vector3D(x=np.cos(left_yaw), y=np.sin(left_yaw))
    right_direction = carla.Vector3D(x=np.cos(right_yaw), y=np.sin(right_yaw))

    # Calculate points
    left_point = camera_location + left_direction * view_distance
    right_point = camera_location + right_direction * view_distance

    # Draw lines
    world.debug.draw_line(camera_location, left_point, thickness=0.1, color=carla.Color(255,0,0), life_time=0.0)
    world.debug.draw_line(camera_location, right_point, thickness=0.1, color=carla.Color(255,0,0), life_time=0.0)
    world.debug.draw_line(left_point, right_point, thickness=0.1, color=carla.Color(255,0,0), life_time=0.0)

else:
    print("Camera not found on the vehicle.")

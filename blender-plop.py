ANGLE_INCREMENT = 45 * 3.14159265 / 180
ANGLE_RANDOMNESS = 0.4
DISTANCE_INCREMENT = 2.0
DISTANCE_RANDOMNESS = 0.3
RADIUS_MIN = 0.6
RADIUS_MAX = 0.8
MATERIAL_COUNT = 4

TAU = 2.0 * 3.14159265358979

import sys
sys.path.append("D:/tests/lsystem")

import lsystem
import bpy
import math
import random

plant = lsystem.grow_barnsley(4)

position = 0, 0
angle = 0

state_stack = []

materials = []
for i in range(MATERIAL_COUNT):
    name = "Plant_Material_{}".format(i)
    material = bpy.data.materials.get(name)
#    material = None
    if material is None:
        material = bpy.data.materials.new(name=name)
        material.diffuse_color = random.random(), random.random(), random.random()
    materials.append(material)

for atom in plant:
    if atom == "F":
        # spawn a cube and move forward
        x, y = position
        bpy.ops.mesh.primitive_cube_add(
            location=(x, y, random.uniform(0.0, DISTANCE_INCREMENT)),
            rotation=(random.random() * TAU, random.random() * TAU, random.random() * TAU),
            radius=random.uniform(RADIUS_MIN, RADIUS_MAX)
        )
        
        obj = bpy.context.object
        
        # random material
        material_index = random.randint(0, MATERIAL_COUNT - 1)
        obj.data.materials.append(materials[material_index])
        
        # add some animation
        obj.keyframe_insert(data_path="location", frame=0)
        obj.keyframe_insert(data_path="rotation_euler", frame=0)
        obj.keyframe_insert(data_path="scale", frame=0)
        
        next_frame = int(random.uniform(25.0, 50.0) + abs(y) * 3.0)
        obj.location = x + random.uniform(-1.0, 1.0) * DISTANCE_INCREMENT, y + random.uniform(-1.0, 1.0) * DISTANCE_INCREMENT, 0.0
        obj.rotation_euler = random.random() * TAU, random.random() * TAU, random.random() * TAU
        obj.scale = 0.0, 0.0, 0.0
        obj.keyframe_insert(data_path="location", frame=next_frame)
        obj.keyframe_insert(data_path="rotation_euler", frame=next_frame)
        obj.keyframe_insert(data_path="scale", frame=next_frame)
        
        distance = DISTANCE_INCREMENT * (1.0 + random.uniform(-1.0, 1.0) * DISTANCE_RANDOMNESS)
        position = x + math.cos(angle) * DISTANCE_INCREMENT, y + math.sin(angle) * DISTANCE_INCREMENT
        
    elif atom == "+":
        angle += ANGLE_INCREMENT * (1.0 + random.uniform(-1.0, 1.0) * ANGLE_RANDOMNESS)
    elif atom == "-":
        angle -= ANGLE_INCREMENT * (1.0 + random.uniform(-1.0, 1.0) * ANGLE_RANDOMNESS)
    elif atom =="[":
        state_stack.append((position, angle))
    elif atom =="]":
        position, angle = state_stack.pop()

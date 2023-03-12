def export(voxel_data, file_name):
    # Start file
    dt = ""
    dt += "mtllib color_map.mtl\n"
    dt += "o Render\n"
    dt += "usemtl color_map\n"

    # Set up vertex normals, which do not vary between voxels
    dt += f"vn -1 0 0\n" # 1
    dt += f"vn 1 0 0\n"  # 2
    dt += f"vn 0 -1 0\n" # 3
    dt += f"vn 0 1 0\n"  # 4
    dt += f"vn 0 0 -1\n" # 5
    dt += f"vn 0 0 1\n"  # 6

    vi = 0
    for voxel in voxel_data:
        # Get voxel coords
        coords = voxel.split(',')
        x = int(coords[0])
        z = int(coords[1])
        y = int(coords[2])

        # Set up vertex texture coordinates for the voxel's color
        WIDTH = 128
        r = int(voxel_data[voxel][0] * (WIDTH-1))
        g = int(voxel_data[voxel][1] * (WIDTH-1))
        b = int(voxel_data[voxel][2] * (WIDTH-1))

        tx = r/WIDTH + (1/(WIDTH*2))
        ty = (g/(WIDTH**2)) + (b/WIDTH) + (1/((WIDTH**2)*2))

        # print(r, g, b)
        # print(tx, 1-ty)
        # print("------------------")
        dt += f"vt {tx} {1-ty}\n"

        # Vertices
        dt += f"v {x  } {y  } {z  }\n" # 1
        dt += f"v {x  } {y  } {z+1}\n" # 2
        dt += f"v {x  } {y+1} {z  }\n" # 3
        dt += f"v {x  } {y+1} {z+1}\n" # 4
        dt += f"v {x+1} {y  } {z  }\n" # 5
        dt += f"v {x+1} {y  } {z+1}\n" # 6
        dt += f"v {x+1} {y+1} {z  }\n" # 7
        dt += f"v {x+1} {y+1} {z+1}\n" # 8

        # Faces
        dt += f"f {vi+1}/-1/1 {vi+2}/-1/1 {vi+3}/-1/1\n"
        dt += f"f {vi+4}/-1/1 {vi+3}/-1/1 {vi+2}/-1/1\n"

        dt += f"f {vi+5}/-1/2 {vi+6}/-1/2 {vi+7}/-1/2\n"
        dt += f"f {vi+8}/-1/2 {vi+7}/-1/2 {vi+6}/-1/2\n"

        dt += f"f {vi+1}/-1/3 {vi+2}/-1/3 {vi+5}/-1/3\n"
        dt += f"f {vi+6}/-1/3 {vi+5}/-1/3 {vi+2}/-1/3\n"

        dt += f"f {vi+3}/-1/4 {vi+4}/-1/4 {vi+7}/-1/4\n"
        dt += f"f {vi+8}/-1/4 {vi+7}/-1/4 {vi+4}/-1/4\n"

        dt += f"f {vi+1}/-1/5 {vi+3}/-1/5 {vi+5}/-1/5\n"
        dt += f"f {vi+7}/-1/5 {vi+5}/-1/5 {vi+3}/-1/5\n"

        dt += f"f {vi+2}/-1/6 {vi+4}/-1/6 {vi+6}/-1/6\n"
        dt += f"f {vi+8}/-1/6 {vi+6}/-1/6 {vi+4}/-1/6\n"

        # Increase the vertex index
        vi += 8

    # Add floor
    fs = 25
    fh = 0.01
    dt += f"vt 0.25 0.8\n" # Hard-coded greenish color
    dt += f"v {fs} {fh} {fs}\n"   # -4
    dt += f"v {fs} {fh} {-fs}\n"  # -3
    dt += f"v {-fs} {fh} {fs}\n"  # -2
    dt += f"v {-fs} {fh} {-fs}\n" # -1
    dt += f"f -1/-1/4 -2/-1/4 -3/-1/4\n"
    dt += f"f -4/-1/4 -3/-1/4 -2/-1/4\n"

    text_file = open(f"{file_name}.obj", "w")
    text_file.write(dt)
    text_file.close()
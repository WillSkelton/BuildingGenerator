import constants

BLOCK_WIDTH = constants.BLOCK_WIDTH
BLOCK_HEIGHT = constants.BLOCK_HEIGHT
BUILDING_APOTHEM = constants.BUILDING_APOTHEM

Model = {
    "vertexList": [
        # Bottom face of base
        (0,           0,           0),  # 0
        (BLOCK_WIDTH, 0,           0),  # 1
        (BLOCK_WIDTH, BLOCK_WIDTH, 0),  # 2
        (0,           BLOCK_WIDTH, 0),  # 3
        # Top face of base
        (0,           0,           BLOCK_HEIGHT),  # 4
        (BLOCK_WIDTH, 0,           BLOCK_HEIGHT),  # 5
        (BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT),  # 6
        (0,           BLOCK_WIDTH, BLOCK_HEIGHT),  # 7
        # Bottom face of building,
        ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2) + \
         BUILDING_APOTHEM, BLOCK_HEIGHT),  # 8
        ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2) + \
         BUILDING_APOTHEM, BLOCK_HEIGHT),  # 9
        ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2) - \
         BUILDING_APOTHEM, BLOCK_HEIGHT),  # 10
        ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2) - \
         BUILDING_APOTHEM, BLOCK_HEIGHT),  # 11
        # Top face of building,
        ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2) + \
         BUILDING_APOTHEM, BLOCK_HEIGHT+50),  # 12
        ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2) + \
         BUILDING_APOTHEM, BLOCK_HEIGHT+50),  # 13
        ((BLOCK_WIDTH/2)-BUILDING_APOTHEM, (BLOCK_WIDTH/2) - \
         BUILDING_APOTHEM, BLOCK_HEIGHT+50),  # 14
        ((BLOCK_WIDTH/2)+BUILDING_APOTHEM, (BLOCK_WIDTH/2) - \
         BUILDING_APOTHEM, BLOCK_HEIGHT+50),  # 15
    ],
    # Define edges (for reference, but we're focusing on faces)
    "edgeList": [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
        (0, 4), (1, 5), (2, 6), (3, 7),   # Vertical edges

        (8, 9), (9, 10), (10, 11), (11, 8),     # Bottom face of building
        (12, 13), (13, 14), (14, 15), (15, 12),  # Top face of building
        (8, 12), (9, 13), (10, 14), (11, 15)    # Vertical edges of building
    ],
    # Define faces
    "faceList": [
        (0, 1, 2, 3),  # Bottom face
        (4, 5, 6, 7),  # Top face
        (0, 1, 5, 4),  # Front face
        (1, 2, 6, 5),  # Right face
        (2, 3, 7, 6),  # Back face
        (3, 0, 4, 7),  # Left face
        (8, 9, 10, 11),   # Bottom face
        (12, 13, 14, 15),  # Top face
        (8, 9, 13, 12),   # Front face
        (9, 10, 14, 13),  # Right face
        (10, 11, 15, 14),  # Back face
        (11, 8, 12, 15)   # Left face
    ]
}

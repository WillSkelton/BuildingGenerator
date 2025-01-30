SimpleCityBlock = {
  "vertexList": [
    # Bottom face
    (0,           0,           0), 
    (BLOCK_WIDTH, 0,           0),
    (BLOCK_WIDTH, BLOCK_WIDTH, 0), 
    (0,           BLOCK_WIDTH, 0), 
    # Top face
    (0,           0,           BLOCK_HEIGHT), 
    (BLOCK_WIDTH, 0,           BLOCK_HEIGHT), 
    (BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT), 
    (0,           BLOCK_WIDTH, BLOCK_HEIGHT) 
  ],
   # Define edges (for reference, but we're focusing on faces)
  "edgeList": [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
      (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
      (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
  ],
   # Define faces
  "faceList": [
      (0, 1, 2, 3),  # Bottom face
      (4, 5, 6, 7),  # Top face
      (0, 1, 5, 4),  # Front face
      (1, 2, 6, 5),  # Right face
      (2, 3, 7, 6),  # Back face
      (3, 0, 4, 7)   # Left face
  ]
}

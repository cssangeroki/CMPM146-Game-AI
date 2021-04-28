# check every space and waypoint to see if coordinates are within 1 in both x and y directions
#     if a space/waypoint is within 1 cell x and 1 cell y of the initial cell:
#         compute weight, append tuple of ((x,y), w) to adjacency list
def navigation_edges(level, cell):
    spcs = level['spaces']
    wypts = level['waypoints']
    cX = cell[0]
    cY = cell[1]
    # output adj list for adjacent cells to input
    adj = []
    
    # NOTE: what if your start location is waypoint!! need to check which dict the cell is in first
    
    # looping for adjacent spaces
    for x,y in spc:
        # if x,y coords are within 1 cell (if this x,y cell is adjacent to starting cell:)
        if (((x-cX)<=1) and (abs(y-cY)<=1)) and (x!=cX or y!=cY):
            # if one of the coords is the same, not diagonal
            if((x==cX and y!=cY) or (x!=cX and y==cY)):
                # edge weight calculation for nondiagonal
                w = 0.5*(spcs[cX,cY]) + 0.5*(spcs[x,y])
            else:  # both x and y coords are different -> diagonal 
                # weight calculation for diagonal
                w = 0.5*(sqrt(2))*(spcs[cX,cY]) + 0.5*(sqrt(2))*(spcs[x,y])
    
            # cellAdj = tuple of (coords, weight), append to adj list
            cellAdj = ((x,y), w)
            adj.append(cellAdj)
        
    # looping for adjacent waypoints
    for k in wypts:
        wypt = wypts[k]
        x = wypt[0]
        y = wypt[1]
        # if x,y coords are within 1 cell (if this x,y cell is adjacent to starting cell:)
        if (((x-cX)<=1) and (abs(y-cY)<=1)) and (x!=cX or y!=cY):
            # if one of the coords is the same, not diagonal
            if((x==cX and y!=cY) or (x!=cX and y==cY)):
                # edge weight calculation for nondiagonal
                w = 0.5*(spcs[cX,cY]) + 0.5*(spcs[x,y])
            else:
                # weight calculation for diagonal
                w = 0.5*(sqrt(2))*(spcs[cX,cY]) + 0.5*(sqrt(2))*(spcs[x,y])
            
            # cellAdj = tuple of (coords, weight), append to adj list [note: waypoints have weight of 1]
            cellAdj = ((x,y), w)
            adj.append(cellAdj)
    
    return adj
    pass
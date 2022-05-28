from CGAL import CGAL_Polygon_mesh_processing

import trimesh
from CGAL.CGAL_Polyhedron_3 import Polyhedron_modifier, Polyhedron_3
from CGAL.CGAL_Kernel import Point_3

def trimesh2cgal(mesh):
    '''trimesh2cgal.
    Input:
        trimesh.Trimesh
    Output:
        CGAL polyhedron_3
    '''

    num_vertices = len(mesh.vertices)
    num_faces = len(mesh.faces)

    m = Polyhedron_modifier()

    m.begin_surface(num_vertices, num_faces)
    for i in range(num_vertices):
        m.add_vertex(Point_3(mesh.vertices[i][0], mesh.vertices[i][1], mesh.vertices[i][2]))
    for i in range(num_faces):
        m.begin_facet()
        m.add_vertex_to_facet(int(mesh.faces[i][0]))
        m.add_vertex_to_facet(int(mesh.faces[i][1]))
        m.add_vertex_to_facet(int(mesh.faces[i][2]))
        m.end_facet()

    P = Polyhedron_3()
    P.delegate(m)
    return P

def cgal2trimesh(P):
    # 获得vertices
    vertices=[]
    for point in P.points():
        vertice = (point.x(), point.y(), point.z())
        vertices.append(vertice)

    vertices_tuple=tuple(vertices)
    # 构建dict,用于后面的查找。用list index查找太慢了
    dic_vertice_index = {vertice: index for index, vertice in enumerate(vertices_tuple)}
    # faces
    faces=[]
    for facet in P.facets():
        face=[]
        start = facet.facet_begin()
        stop = facet.facet_begin().deepcopy()

        while True:
            halfedge_facet = start.next()
            point_halfedge =halfedge_facet.vertex().point()
            vertice_point = (point_halfedge.x(), point_halfedge.y(), point_halfedge.z())
            index_vertice = dic_vertice_index[vertice_point]
            face.append(index_vertice)
            if (start.__eq__(stop)):
                break
        faces.append(face)
    mesh = trimesh.Trimesh(vertices=vertices_tuple, faces=faces)
    return mesh


m = trimesh.load("11.stl")
P = trimesh2cgal(m)
for h in P.halfedges():
    if h.is_border():
        outf = []
        outv = []
        CGAL_Polygon_mesh_processing.triangulate_refine_and_fair_hole(P, h, outf, outv)

out_mesh = cgal2trimesh(P)
out_mesh.show()

'''
https://codeforces.com/problemset/problem/785/A
Solution: Keep a dictionary for polyhedron name to the total sides it has. Run through the input list of polyhedrons 
and sum their sides using this dictionary. 
'''
polyhedronSides = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}

def solve(polyhedrons):
    sideCount = 0
    for polyhedron in polyhedrons:
        sideCount += polyhedronSides[polyhedron]
    return sideCount

if __name__ == '__main__':
    n = int(input())
    polyhedrons = list()
    for i in range(0, n): 
        polyhedron = input()
        polyhedrons.append(polyhedron)
    print(solve(polyhedrons)) 
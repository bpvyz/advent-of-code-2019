orbits = [line.rstrip() for line in open('input.txt')]

#part1
orbit_num = {}
orbit_map = {}
def update_children(child):
    for c in orbit_map.get(child, []):
        orbit_num[c] = orbit_num[child] + 1
        update_children(c)

for orbit in orbits:
    orbitee = orbit.split(")")[0]
    orbiter = orbit.split(")")[1]
    existing = orbit_map.get(orbitee, [])
    existing.append(orbiter)
    orbit_map[orbitee] = existing
    orbit_num[orbiter] = orbit_num.get(orbitee, 0) + 1
    update_children(orbiter)

print(sum(orbit_num.values()))

#part 2
dest1 = "YOU"
dest2 = "SAN"
path1 = set()
path2 = set()

while dest1 != dest2:
    for orbit in orbit_map:
        if dest1 in orbit_map[orbit]:
            print(f"{dest1} FOUND")
            dest1 = orbit
            print(f"NEW DEST1: {dest1}")
            path2.add(dest1)
        if dest2 in orbit_map[orbit]:
            print(f"{dest2} FOUND")
            dest2 = orbit
            print(f"NEW DEST2: {dest2}")
            path1.add(dest2)

print(len(path1.symmetric_difference(path2)))

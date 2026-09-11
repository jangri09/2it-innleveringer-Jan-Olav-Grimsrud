import random
list_of_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "⬜"]

def ramdomice():
    return random.choice(list_of_colors)

def generate_cube():
    cube = {}
    face_names = ["Foran", "Bak", "Høyre", "Venstre", "Topp", "Bunn"]
    for name in face_names:
        # Generer en 3x3 side
        face = [[ramdomice() for _ in range(3)] for _ in range(3)]
        cube[name] = face
    return cube



rubiks_kube = generate_cube()

def print_cube(rubiks_kube):
    for name, face in rubiks_kube.items():
        print(f"--- {name} ---")
        for row in face:
            print(" ".join(row))
        print()

print("Første tilstand:")
print_cube(rubiks_kube)


print("Etter å ha rotert foran med klokken:")
print_cube(rubiks_kube)



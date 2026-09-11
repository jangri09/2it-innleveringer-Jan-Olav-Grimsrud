import random
list_of_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "⬜"]

def ramdomice():
    return random.choice(list_of_colors)

def generate_complete_cube():
    # Kobler hver side til sin standardfarge
    color_scheme = {
        "topp": "⬜",  # Topp
        "bunn": "🟨",  # Bunn
        "foran": "🟩",  # Foran
        "bak": "🟦",  # Bak
        "venstre": "🟧",  # Venstre
        "høyre": "🟥",  # Høyre
    }
    
    cube = {}
    for face_name, color in color_scheme.items():
        # Lager en 3x3-flate fylt med den tildelte fargen
        face = [[color for _ in range(3)] for _ in range(3)]
        cube[face_name] = face
        
    return cube

def generate_cube():
    cube = {}
    face_names = ["foran", "bak", "høyre", "venstre", "topp", "bunn"]
    for name in face_names:
        # Generer en 3x3 side
        face = [[ramdomice() for _ in range(3)] for _ in range(3)]
        cube[name] = face
    return cube


def rotate_face(face, times=1):
    for _ in range(times % 4):
        face = [list(row) for row in zip(*face[::-1])]
    return face

def move_R(cube, notasjon="R"):
    # "R" betyr 1 rotasjon, "R'" betyr 3 rotasjoner
    repeat = 3 if "'" in notasjon else 1

    for _ in range(repeat):
        # 1. Roter selve høyre-flaten 90 grader med klokken
        cube["høyre"] = rotate_face(cube["høyre"], 1)
        
        # 2. Skift stolpene (kolonne 2 på foran/topp/bak/bunn)
        temp_foran = [cube["foran"][i][2] for i in range(3)]
        
        for i in range(3):
            cube["foran"][i][2] = cube["bunn"][i][2]
            cube["bunn"][i][2] = cube["bak"][2 - i][0]
            cube["bak"][2 - i][0] = cube["topp"][i][2]
            cube["topp"][i][2] = temp_foran[i]

def move_L(cube, notasjon="L"):
    # "L" betyr 1 rotasjon, "L'" betyr 3 rotasjoner
    repeat = 3 if "'" in notasjon else 1

    for _ in range(repeat):
        # 1. Roter selve venstre-flaten 90 grader med klokken
        cube["venstre"] = rotate_face(cube["venstre"], 1)
        
        # 2. Skift stolpene (kolonne 0 på foran/topp/bunn og kolonne 2 på bak)
        # RIKTIG: Hent ut kolonne 0 (venstre side)
        temp_foran = [cube["foran"][i][0] for i in range(3)]
        
        # RIKTIG: Riktig sirkelretning for standard L-trekk
        for i in range(3):
            cube["foran"][i][0] = cube["topp"][i][0]
            cube["topp"][i][0] = cube["bak"][2 - i][2]
            cube["bak"][2 - i][2] = cube["bunn"][i][0]
            cube["bunn"][i][0] = temp_foran[i]

rubiks_kube = generate_complete_cube()

def print_cube(rubiks_kube):
    for name, face in rubiks_kube.items():
        print(f"--- {name} ---")
        for row in face:
            print(" ".join(row))
        print()

print("Første tilstand:")
print_cube(rubiks_kube)

while True:
    move = input("Skriv inn et trekk (R, R', L, L') eller 'exit' for å avslutte: ").strip()
    if move.lower() == 'exit':
        break
    if move in ["R", "R'", "L", "L'"]:
        if move.startswith("R"):
            move_R(rubiks_kube, move)
        elif move.startswith("L"):
            move_L(rubiks_kube, move)
        print_cube(rubiks_kube)
    else:
        print("Ugyldig trekk. Vennligst skriv inn R, R', L, L' eller 'exit'.")

import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
valid_moves = [
    "R",
    "R'",
    "L",
    "L'",
    "U",
    "U'",
    "D",
    "D'",
    "F",
    "F'",
    "B",
    "B'",
    "M",
    "M'",
]

def generate_complete_cube():
    color_scheme = {
        "topp": "🟨",
        "bunn": "⬜",
        "foran": "🟦",
        "bak": "🟩",
        "venstre": "🟧",
        "høyre": "🟥",
    }
    cube = {}
    for face_name, color in color_scheme.items():
        cube[face_name] = [[color for _ in range(3)] for _ in range(3)]
    return cube


def print_cube(cube):
    indent = "         "

    # 1. Topp
    for row in cube["topp"]:
        print(indent + " ".join(row))

    # 2. Venstre | Foran | Høyre | Bak
    for i in range(3):
        row_l = " ".join(cube["venstre"][i])
        row_f = " ".join(cube["foran"][i])
        row_r = " ".join(cube["høyre"][i])
        row_b = " ".join(cube["bak"][i])
        print(f"{row_l} {row_f} {row_r} {row_b}")

    # 3. Bunn
    for row in cube["bunn"]:
        print(indent + " ".join(row))
    print()


def rotate_face(face, times=1):
    res = face
    for _ in range(times % 4):
        res = [list(row) for row in zip(*res[::-1])]
    return res


def move_R(cube, notasjon="R"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["høyre"] = rotate_face(cube["høyre"], 1)
        temp_foran = [cube["foran"][i][2] for i in range(3)]
        for i in range(3):
            cube["foran"][i][2] = cube["bunn"][i][2]
            cube["bunn"][i][2] = cube["bak"][2 - i][0]
            cube["bak"][2 - i][0] = cube["topp"][i][2]
            cube["topp"][i][2] = temp_foran[i]


def move_L(cube, notasjon="L"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["venstre"] = rotate_face(cube["venstre"], 1)
        temp_foran = [cube["foran"][i][0] for i in range(3)]
        for i in range(3):
            cube["foran"][i][0] = cube["topp"][i][0]
            cube["topp"][i][0] = cube["bak"][2 - i][2]
            cube["bak"][2 - i][2] = cube["bunn"][i][0]
            cube["bunn"][i][0] = temp_foran[i]


def move_U(cube, notasjon="U"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["topp"] = rotate_face(cube["topp"], 1)
        temp_foran = cube["foran"][0].copy()
        cube["foran"][0] = cube["høyre"][0]
        cube["høyre"][0] = cube["bak"][0]
        cube["bak"][0] = cube["venstre"][0]
        cube["venstre"][0] = temp_foran


def move_D(cube, notasjon="D"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["bunn"] = rotate_face(cube["bunn"], 1)
        temp_foran = cube["foran"][2].copy()
        cube["foran"][2] = cube["venstre"][2]
        cube["venstre"][2] = cube["bak"][2]
        cube["bak"][2] = cube["høyre"][2]
        cube["høyre"][2] = temp_foran


def move_B(cube, notasjon="B"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["bak"] = rotate_face(cube["bak"], 1)
        temp_topp = cube["topp"][0].copy()
        for i in range(3):
            cube["topp"][0][i] = cube["venstre"][2 - i][0]
        for i in range(3):
            cube["venstre"][i][0] = cube["bunn"][2][i]
        for i in range(3):
            cube["bunn"][2][i] = cube["høyre"][2 - i][2]
        for i in range(3):
            cube["høyre"][i][2] = temp_topp[i]


def move_F(cube, notasjon="F"):
    repeat = 3 if "'" in notasjon else 1
    for _ in range(repeat):
        cube["foran"] = rotate_face(cube["foran"], 1)
        temp_topp = cube["topp"][2].copy()
        for i in range(3):
            cube["topp"][2][i] = cube["venstre"][2 - i][2]
        for i in range(3):
            cube["venstre"][i][2] = cube["bunn"][0][i]
        for i in range(3):
            cube["bunn"][0][i] = cube["høyre"][2 - i][0]
        for i in range(3):
            cube["høyre"][i][0] = temp_topp[i]


def move_M(cube, notasjon="M"):
    repeat = 3 if "'" in notasjon else 1

    for _ in range(repeat):
        # 1. Ta vare på 'foran' sin midtkolonne
        temp_foran = [cube["foran"][i][1] for i in range(3)]

        for i in range(3):
            # Foran får fra Topp
            cube["foran"][i][1] = cube["topp"][i][1]

            # Topp får fra Bak (må speilvendes med 2 - i)
            cube["topp"][i][1] = cube["bak"][2 - i][1]

            # Bak får fra Bunn (må også speilvendes med 2 - i)
            cube["bak"][2 - i][1] = cube["bunn"][i][1]

            # Bunn får fra temp (opprinnelig Foran)
            cube["bunn"][i][1] = temp_foran[i]


def is_cube_solved(cube):
    for face in cube.values():
        first_color = face[0][0]
        for row in face:
            for color in row:
                if color != first_color:
                    return False
    return True


def scramble_cube(cube, moves=20):
    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(moves):
        move = random.choice(valid_moves)
        if move.startswith("R"):
            move_R(cube, move)
        elif move.startswith("L"):
            move_L(cube, move)
        elif move.startswith("U"):
            move_U(cube, move)
        elif move.startswith("D"):
            move_D(cube, move)
        elif move.startswith("F"):
            move_F(cube, move)
        elif move.startswith("B"):
            move_B(cube, move)
        print("scrambler...")
        print_cube(rubiks_kube)
        print(move)
        time.sleep(0.4)
        os.system('cls' if os.name == 'nt' else 'clear')
        



# --- SPILLSTART ---
rubiks_kube = generate_complete_cube()

def start_spill():
    scramble_cube(rubiks_kube, moves=10)
    print("Kuben er scramblet! Første tilstand:")
    print_cube(rubiks_kube)
start_spill()

while True:
    move = input(
        "Skriv inn et trekk (R, R', L, L', U, U', D, D', F, F', B, B', M, M')\n" \
        "Skriv scramble for å scramble kuben\n" \
        "Eller skriv exit for å avslutte: "
    ).strip()

    if move.lower() == "exit":
        break

    if move in valid_moves:
        if move.startswith("R"):
            move_R(rubiks_kube, move)
        elif move.startswith("L"):
            move_L(rubiks_kube, move)
        elif move.startswith("U"):
            move_U(rubiks_kube, move)
        elif move.startswith("D"):
            move_D(rubiks_kube, move)
        elif move.startswith("F"):
            move_F(rubiks_kube, move)
        elif move.startswith("B"):
            move_B(rubiks_kube, move)
        elif move.startswith("M"):
            move_M(rubiks_kube, move)

        os.system('cls' if os.name == 'nt' else 'clear')
        print_cube(rubiks_kube)

        if is_cube_solved(rubiks_kube):
            print("Gratulerer! Du har løst kuben! 🎉")
            break
    elif move.lower() == "scramble":
            start_spill()
    else:
        print("Ugyldig trekk. Prøv igjen.")

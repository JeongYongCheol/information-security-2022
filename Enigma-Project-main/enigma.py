# Enigma Template Code for CNU Information Security 2022
# Resources from https://www.cryptomuseum.com/crypto/enigma

# This Enigma code implements Enigma I, which is utilized by 
# Wehrmacht and Luftwaffe, Nazi Germany. 
# This version of Enigma does not contain wheel settings, skipped for
# adjusting difficulty of the assignment.

from copy import deepcopy
from ctypes import ArgumentError

# Enigma Components
ETW = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

WHEELS = {
    "I" : {
        "wire": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "turn": 16
    },
    "II": {
        "wire": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "turn": 4
    },
    "III": {
        "wire": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "turn": 21
    }
}

UKW = {
    "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

# Enigma Settings
SETTINGS = {
    "UKW": None,
    "WHEELS": [],
    "WHEEL_POS": [],
    "ETW": ETW,
    "PLUGBOARD": []
}

def apply_settings(ukw, wheel, wheel_pos, plugboard):
    if not ukw in UKW:
        raise ArgumentError(f"UKW {ukw} does not exist!")
    SETTINGS["UKW"] = UKW[ukw]

    wheels = wheel.split(' ')
    for wh in wheels:
        if not wh in WHEELS:
            raise ArgumentError(f"WHEEL {wh} does not exist!")
        SETTINGS["WHEELS"].append(WHEELS[wh])

    wheel_poses = wheel_pos.split(' ')
    for wp in wheel_poses:
        if not wp in ETW:
            raise ArgumentError(f"WHEEL position must be in A-Z!")
        SETTINGS["WHEEL_POS"].append(ord(wp) - ord('A'))
 
    plugboard_setup = plugboard.split(' ')
    for ps in plugboard_setup:
        if not len(ps) == 2 or not ps.isupper():
            raise ArgumentError(f"Each plugboard setting must be sized in 2 and caplitalized; {ps} is invalid")
        SETTINGS["PLUGBOARD"].append(ps)

# Enigma Logics Start

# Plugboard
def pass_plugboard(input):
    for plug in SETTINGS["PLUGBOARD"]:
        if str.startswith(plug, input):
            return plug[1]
        elif str.endswith(plug, input):
            return plug[0]

    return input

# ETW
def pass_etw(input):
    return SETTINGS["ETW"][ord(input) - ord('A')]

# Wheels
def pass_wheels(input, reverse = False):
    # Implement Wheel Logics
    # Keep in mind that reflected signals pass wheels in reverse order
    encoded_ch = '';

    # reverse가 참일 경우, 반사판에서 돌아오는 신호이므로 로터 순서를 뒤->앞으로 통과한다.
    if reverse :
        encoded_ch = SETTINGS["WHEELS"][2]["wire"][ord(input) - ord('A')]
        encoded_ch = SETTINGS["WHEELS"][1]["wire"][ord(encoded_ch) - ord('A')]
        encoded_ch = SETTINGS["WHEELS"][0]["wire"][ord(encoded_ch) - ord('A')]
    else :
        encoded_ch = SETTINGS["WHEELS"][0]["wire"][ord(input) - ord('A')]
        encoded_ch = SETTINGS["WHEELS"][1]["wire"][ord(encoded_ch) - ord('A')]
        encoded_ch = SETTINGS["WHEELS"][2]["wire"][ord(encoded_ch) - ord('A')]

    return encoded_ch

# UKW
def pass_ukw(input):
    return SETTINGS["UKW"][ord(input) - ord('A')]

# Wheel Rotation
def rotate_wheels():
    # Implement Wheel Rotation Logics
    # 알파벳의 갯수는 26개 이므로, 26회 회전하면 원위치로 되돌아온다.
    # 따라서 회전수가 26회 이상일 경우, 다음 로터를 1회전하고 현 로터의 회전수를 0으로 설정해준다.
    # 회전수를 증가시킬 때, 해당하는 로터의 알파벳 위치를 1칸 씩 옮긴다. -> wire_rotate()
    if SETTINGS["WHEELS"][0]["turn"] < 26 :
        SETTINGS["WHEELS"][0]["turn"] =+ 1; wire_rotate(0)
        if SETTINGS["WHEELS"][0]["turn"] > 25 :
            SETTINGS["WHEELS"][1]["turn"] =+ 1; wire_rotate(1)
            SETTINGS["WHEELS"][0]["turn"] = 0;
            if SETTINGS["WHEELS"][1]["turn"] > 25 :
                SETTINGS["WHEELS"][2]["turn"] =+ 1; wire_rotate(2)
                SETTINGS["WHEELS"][1]["turn"] = 0
                if SETTINGS["WHEELS"][2]["turn"] > 25 :
                    SETTINGS["WHEELS"][2]["turn"] = 0

# wire rotate
def wire_rotate(index):
    # 맨 앞 글자를 뒤로 옮기고 한칸씩 땡긴다.
    temp = SETTINGS["WHEELS"][index]["wire"][0];
    SETTINGS["WHEELS"][index]["wire"] = SETTINGS["WHEELS"][index]["wire"][1:] + temp

# Enigma Exec Start
plaintext = input("Plaintext to Encode: ")
ukw_select = input("Set Reflector (A, B, C): ")
wheel_select = input("Set Wheel Sequence L->R (I, II, III): ")
wheel_pos_select = input("Set Wheel Position L->R (A~Z): ")
plugboard_setup = input("Plugboard Setup: ")
apply_settings(ukw_select, wheel_select, wheel_pos_select, plugboard_setup)

for ch in plaintext:
    
    rotate_wheels()
    encoded_ch = ch

    encoded_ch = pass_plugboard(encoded_ch)
    encoded_ch = pass_etw(encoded_ch)
    encoded_ch = pass_wheels(encoded_ch)
    encoded_ch = pass_ukw(encoded_ch)
    encoded_ch = pass_wheels(encoded_ch, reverse = True)
    encoded_ch = pass_plugboard(encoded_ch)

    print(encoded_ch, end='')
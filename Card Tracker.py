import pyautogui as pag
import time
import cv2 as cv
import numpy as np
import keyboard as kb
from PIL import Image, ImageDraw, ImageFont

card1_status = [1]
card2_status = [1]
card3_status = [1]
card4_status = [1]
card5_status = [1]
card6_status = [1]
card7_status = [1]
card8_status = [1]

card1_default = []
card2_default = []
card3_default = []
card4_default = []
card5_default = []
card6_default = []
card7_default = []
card8_default = []

played_status1 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status3 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status4 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status5 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status6 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status7 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
played_status8 = [1, 1, 1, 1, 1, 1, 1, 1, 1]

cycle = ['card 1.png',-1, 'card 2.png',-1, 'card 3.png',-1, 'card 4.png',-1, 'card 5.png',-1, 'card 6.png',-1, 'card 7.png',-1, 'card 8.png',-1]

if card1_status[0] != 'saved':
    unknown1 = cv.imread('Unknown/unknown 1.png')
    cv.imwrite('card 1.png', unknown1)
if card2_status[0] != 'saved':
    unknown2 = cv.imread('Unknown/unknown 2.png')
    cv.imwrite('card 2.png', unknown2)
if card3_status[0] != 'saved':
    unknown3 = cv.imread('Unknown/unknown 3.png')
    cv.imwrite('card 3.png', unknown3)
if card4_status[0] != 'saved':
    unknown4 = cv.imread('Unknown/unknown 4.png')
    cv.imwrite('card 4.png', unknown4)
if card5_status[0] != 'saved':
    unknown5 = cv.imread('Unknown/unknown 5.png')
    cv.imwrite('card 5.png', unknown5)
if card6_status[0] != 'saved':
    unknown6 = cv.imread('Unknown/unknown 6.png')
    cv.imwrite('card 6.png', unknown6)
if card7_status[0] != 'saved':
    unknown7 = cv.imread('Unknown/unknown 7.png')
    cv.imwrite('card 7.png', unknown7)
if card8_status[0] != 'saved':
    unknown8 = cv.imread('Unknown/unknown 8.png')
    cv.imwrite('card 8.png', unknown8)


background = cv.imread("Background.png")
background = cv.resize(background, (700, 800))

font_path = 'supercell-magic-webfont.ttf'
font_size = 32
font = ImageFont.truetype(font_path, font_size)

pil_img = Image.fromarray(cv.cvtColor(background, cv.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img)
text1 = "Current Hand"
draw.text((190, 50), text1, font=font, fill=(255, 255, 255))
text2 = "Coming Up"
draw.text((230, 300), text2, font=font, fill=(255, 255, 255))
text2 = "Champion in Play"
draw.text((160, 550), text2, font=font, fill=(255, 255, 255))
background = cv.cvtColor(np.array(pil_img), cv.COLOR_RGB2BGR)

# Add text labels to the background


champion_played = []
champion_status = []

champion_kill_status = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

card1_elixir = [-1]
card2_elixir = [-1]
card3_elixir = [-1]
card4_elixir = [-1]
card5_elixir = [-1]
card6_elixir = [-1]
card7_elixir = [-1]
card8_elixir = [-1]
champion_elixir = [-1]

current_elixir = [0]


def card_images():
    if card1_status[0] != 'saved' and pag.pixel(800, 103)[0] not in range(50, 60) and pag.pixel(800,103)[1] not in range(20,30):
        print("sleeping now... (1)")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 1.png', region=(752, 96, 60, 77))
        card1_status.pop()
        card1_status.append('saved')
        card1_default.append(pag.pixel(781, 132))
        index1=cycle.index('card 1.png')
        cycle.pop(index1+1)
        cycle.remove('card 1.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(775, 155, 13, 13), confidence=0.8):
            card1_status.append(9)
        else:
            card1_status.append(10)
        cycle.append('card 1.png')
        cycle.append(card1_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(752, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(752, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(752, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card1_elixir[0])
            champion_played.append('card 1.png')
            champion_status.append('alive')
            cycle.remove('card 1.png')
            cycle.pop()
            # print('champion detected')
        # print('card 1')
    print(cycle)
    print(f"because 800, 103 is RGB={pag.pixel(800, 103)}")
    if card2_status[0] != 'saved' and pag.pixel(859, 103)[0] not in range(50, 60) and pag.pixel(859,103)[1] not in range(20,30):
        print("sleeping now... (2)")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 2.png', region=(811, 96, 60, 77))
        card2_status.pop()
        card2_status.append('saved')
        card2_default.append(pag.pixel(840, 132))
        index2 = cycle.index('card 2.png')
        cycle.pop(index2 + 1)
        cycle.remove('card 2.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(834, 155, 13, 13), confidence=0.8):
            card2_status.append(9)
        else:
            card2_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 2.png')
        cycle.append(card2_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(811, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(811, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(811, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card2_elixir[0])
            champion_played.append('card 2.png')
            champion_status.append('alive')
            cycle.remove('card 2.png')
            cycle.pop()
            # print('champion detected')
        # print('card 2')

    print(cycle)
    print(f"because 859, 103 is RGB={pag.pixel(859, 103)}")
    if card3_status[0] != 'saved' and pag.pixel(918, 103)[0] not in range(65, 75) and pag.pixel(918, 103)[1] not in range(30,35):
        print("sleeping now... (3)")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 3.png', region=(870, 96, 60, 77))
        card3_status.pop()
        card3_status.append('saved')
        card3_default.append(pag.pixel(899, 132))
        index3=cycle.index('card 3.png')
        cycle.pop(index3+1)
        cycle.remove('card 3.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(893, 155, 13, 13), confidence=0.8):
            card3_status.append(9)
        else:
            card3_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 3.png')
        cycle.append(card3_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(870, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(870, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(870, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card3_elixir[0])
            champion_played.append('card 3.png')
            champion_status.append('alive')
            cycle.remove('card 3.png')
            cycle.pop()
            # print('champion detected')
        # print('card 3')

    print(cycle)
    print(f"because 918, 103 is RGB={pag.pixel(918, 103)}")
    if card4_status[0] != 'saved' and pag.pixel(977, 103)[0] not in range(75, 80) and pag.pixel(977, 103)[1] not in range(35,40):
        print("sleeping now... (4)")
        print(f"because 977, 103 is RGB={pag.pixel(977, 103)}")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 4.png', region=(929, 96, 60, 77))
        card4_status.pop()
        card4_status.append('saved')
        card4_default.append(pag.pixel(958, 132))
        index4=cycle.index('card 4.png')
        cycle.pop(index4+1)
        cycle.remove('card 4.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(952, 155, 13, 13), confidence=0.8):
            card4_status.append(9)
        else:
            card4_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 4.png')
        cycle.append(card4_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(929, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(929, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(929, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card4_elixir[0])
            champion_played.append('card 4.png')
            champion_status.append('alive')
            cycle.remove('card 4.png')
            cycle.pop()
            # print('champion detected')
        # print('card 4')

    print(cycle)
    if card5_status[0] != 'saved' and pag.pixel(1036, 103)[0] not in range(75, 80) and pag.pixel(1036,103)[1] not in range(35, 40):
        print("sleeping now... (5)")
        print(f"because 1036, 103 is RGB={pag.pixel(1036, 103)}")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 5.png', region=(988, 96, 60, 77))
        card5_status.pop()
        card5_status.append('saved')
        card5_default.append(pag.pixel(1017, 132))
        index5 = cycle.index('card 5.png')
        cycle.pop(index5 + 1)
        cycle.remove('card 5.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(1011, 155, 13, 13), confidence=0.8):
            card5_status.append(9)
        else:
            card5_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 5.png')
        cycle.append(card5_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(988, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(988, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(988, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card5_elixir[0])
            champion_played.append('card 5.png')
            champion_status.append('alive')
            cycle.remove('card 5.png')
            cycle.pop()
            # print('champion detected')
        # print('card 5')

    print(cycle)
    if card6_status[0] != 'saved' and pag.pixel(1095, 103)[0] not in range(70, 80) and pag.pixel(1095,103)[1] not in range(30,40):
        print("sleeping now... (6)")
        print(f"because 1095, 103 is RGB={pag.pixel(1095, 103)}")
        time.sleep(1.5)
        print("doene sleeping!")
        pag.screenshot('card 6.png', region=(1047, 96, 60, 77))
        card6_status.pop()
        card6_status.append('saved')
        card6_default.append(pag.pixel(1076, 132))
        index6 = cycle.index('card 6.png')
        cycle.pop(index6 + 1)
        cycle.remove('card 6.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(1070, 155, 13, 13), confidence=0.8):
            card6_status.append(9)
        else:
            card6_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 6.png')
        cycle.append(card6_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(1047, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(1047, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(1047, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card6_elixir[0])
            champion_played.append('card 6.png')
            champion_status.append('alive')
            cycle.remove('card 6.png')
            cycle.pop()
            # print('champion detected')
        # print('card 6')

    print(cycle)
    if card7_status[0] != 'saved' and pag.pixel(1154, 103)[0] not in range(60, 70) and pag.pixel(1154,103)[1] not in range(20,35):
        print("sleeping now... (7)")
        print(f"because 1154, 103 is RGB={pag.pixel(1154, 103)}")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 7.png', region=(1106, 96, 60, 77))
        card7_status.pop()
        card7_status.append('saved')
        card7_default.append(pag.pixel(1135, 132))
        index7 = cycle.index('card 7.png')
        cycle.pop(index7 + 1)
        cycle.remove('card 7.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(1129, 155, 13, 13), confidence=0.8):
            card7_status.append(9)
        else:
            card7_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 7.png')
        cycle.append(card7_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(1106, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(1106, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(1106, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card7_elixir[0])
            champion_played.append('card 7.png')
            champion_status.append('alive')
            cycle.remove('card 7.png')
            cycle.pop()
            # print('champion detected')
        # print('card 7')

    print(cycle)
    if card8_status[0] != 'saved' and pag.pixel(1213, 103)[0] not in range(50, 60) and pag.pixel(1213,103)[1] not in range(20,35):
        print("sleeping now... (8)")
        print(f"because 1213, 103 is RGB={pag.pixel(1213, 103)}")
        time.sleep(1.5)
        print("done sleeping!")
        pag.screenshot('card 8.png', region=(1165, 96, 60, 77))
        card8_status.pop()
        card8_status.append('saved')
        card8_default.append(pag.pixel(1194, 132))
        index8 = cycle.index('card 8.png')
        cycle.pop(index8 + 1)
        cycle.remove('card 8.png')
        if pag.locateOnScreen('Card elixir/0.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(0)
        elif pag.locateOnScreen('Card elixir/1.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(1)
        elif pag.locateOnScreen('Card elixir/2.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(2)
        elif pag.locateOnScreen('Card elixir/3.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(3)
        elif pag.locateOnScreen('Card elixir/4.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(4)
        elif pag.locateOnScreen('Card elixir/5.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(5)
        elif pag.locateOnScreen('Card elixir/6.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(6)
        elif pag.locateOnScreen('Card elixir/7.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(7)
        elif pag.locateOnScreen('Card elixir/8.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(8)
        elif pag.locateOnScreen('Card elixir/9.png', region=(1188, 155, 13, 13), confidence=0.8):
            card8_status.append(9)
        else:
            card8_status.append(10)
            #print('mirror has no fixed elixir')
        cycle.append('card 8.png')
        cycle.append(card8_status[-1])
        if pag.locateOnScreen('Skeleton King.png', region=(1165, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Golden Knight.png', region=(1165, 96, 60, 77), confidence=0.7) or pag.locateOnScreen(
            'Archer Queen.png', region=(1165, 96, 60, 77), confidence=0.7):
            champion_elixir.append(card8_elixir[0])
            champion_played.append('card 8.png')
            champion_status.append('alive')
            cycle.remove('card 8.png')
            cycle.pop()
            # print('champion detected')
        # print('card 8')


def card_played():
    if card1_status[0] == 'saved' and card1_default != [] and pag.pixel(781, 132) != card1_default[0]:

        '''cycle_8 = cv.imread('card 1.png')
        cv.imshow('card 1', cycle_8)
        cv.moveWindow('card 1', 800, 400)
        key1 = cv.waitKey(0)
        if key1 == ord('1'):
            cv.destroyWindow('card 1')'''
        if champion_played == ['card 1.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index1=cycle.index('card 1.png')
            cycle.pop(index1+1)
            cycle.remove(champion_played[0])
        if len(played_status1) == 9:
            # print('card 1')
            try:
                index1=cycle.index('card 1.png')
                cycle.pop(index1+1)
                cycle.remove('card 1.png')
                cycle.append('card 1.png')
                cycle.append(card1_status[-1])
            except:
                pass
            for i in range(9):
                played_status1.pop()
    if len(played_status1) != 9:
        played_status1.append(1)

    print(cycle)
    if card2_status[0] == 'saved' and card2_default != [] and pag.pixel(840, 132) != card2_default[0]:
        '''cycle_8 = cv.imread('card 2.png')
        cv.imshow('card 2', cycle_8)
        cv.moveWindow('card 2', 950, 400)
        key2 = cv.waitKey(0)
        if key2 == ord('2'):
            cv.destroyWindow('card 2')'''
        if champion_played == ['card 2.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index2 = cycle.index('card 2.png')
            cycle.pop(index2 + 1)
            cycle.remove(champion_played[0])
        if len(played_status2) == 9:
            # print('card 2')
            try:
                index2 = cycle.index('card 2.png')
                cycle.pop(index2 + 1)
                cycle.remove('card 2.png')
                cycle.append('card 2.png')
                cycle.append(card2_status[-1])
            except:
                pass
            for i in range(9):
                played_status2.pop()
    if len(played_status2) != 9:
        played_status2.append(1)

    print(cycle)
    if card3_status[0] == 'saved' and card3_default != [] and pag.pixel(899, 132) != card3_default[0]:
        '''cycle_8 = cv.imread('card 3.png')
        cv.imshow('card 3', cycle_8)
        cv.moveWindow('card 3', 1100, 400)
        key3 = cv.waitKey(0)
        if key3 == ord('3'):
            cv.destroyWindow('card 3')'''
        if champion_played == ['card 3.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index3 = cycle.index('card 3.png')
            cycle.pop(index3 + 1)
            cycle.remove(champion_played[0])
        if len(played_status3) == 9:
            # print('card 3')
            try:
                index3 = cycle.index('card 3.png')
                cycle.pop(index3 + 1)
                cycle.remove('card 3.png')
                cycle.append('card 3.png')
                cycle.append(card3_status[-1])
            except:
                pass
            for i in range(9):
                played_status3.pop()
    if len(played_status3) != 9:
        played_status3.append(1)

    print(cycle)
    if card4_status[0] == 'saved' and card4_default != [] and pag.pixel(958, 132) != card4_default[0]:
        '''cycle_8 = cv.imread('card 4.png')
        cv.imshow('card 4', cycle_8)
        cv.moveWindow('card 4', 1250, 400)
        key4 = cv.waitKey(0)
        if key4 == ord('4'):
            cv.destroyWindow('card 4')'''
        if champion_played == ['card 4.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index4 = cycle.index('card 4.png')
            cycle.pop(index4 + 1)
            cycle.remove(champion_played[0])
        if len(played_status4) == 9:
            # print('card 4')
            try:
                index4 = cycle.index('card 4.png')
                cycle.pop(index4 + 1)
                cycle.remove('card 4.png')
                cycle.append('card 4.png')
                cycle.append(card4_status[-1])
            except:
                pass
            for i in range(9):
                played_status4.pop()
    if len(played_status4) != 9:
        played_status4.append(1)

    print(cycle)
    if card5_status[0] == 'saved' and card5_default != [] and pag.pixel(1017, 132) != card5_default[0]:
        '''cycle_8 = cv.imread('card 4.png')
        cv.imshow('card 5', cycle_8)
        cv.moveWindow('card 5', 1400, 400)
        key5 = cv.waitKey(0)
        if key5 == ord('5'):
            cv.destroyWindow('card 5')'''
        if champion_played == ['card 5.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index5 = cycle.index('card 5.png')
            cycle.pop(index5 + 1)
            cycle.remove(champion_played[0])
        if len(played_status5) == 9:
            # print('card 5')
            try:
                index5 = cycle.index('card 5.png')
                cycle.pop(index5 + 1)
                cycle.remove('card 5.png')
                cycle.append('card 5.png')
                cycle.append(card5_status[-1])
            except:
                pass
            for i in range(9):
                played_status5.pop()
    if len(played_status5) != 9:
        played_status5.append(1)

    print(cycle)
    if card6_status[0] == 'saved' and card6_default != [] and pag.pixel(1076, 132) != card6_default[0]:
        '''cycle_8 = cv.imread('card 6.png')
        cv.imshow('card 6', cycle_8)
        cv.moveWindow('card 6', 1550, 400)
        key6 = cv.waitKey(0)
        if key6 == ord('6'):
            cv.destroyWindow('card 6')'''
        if champion_played == ['card 6.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index6 = cycle.index('card 6.png')
            cycle.pop(index6 + 1)
            cycle.remove(champion_played[0])
        if len(played_status6) == 9:
            # print('card 6')
            try:
                index6 = cycle.index('card 6.png')
                cycle.pop(index6 + 1)
                cycle.remove('card 6.png')
                cycle.append('card 6.png')
                cycle.append(card6_status[-1])
            except:
                pass
            for i in range(9):
                played_status6.pop()
    if len(played_status6) != 9:
        played_status6.append(1)

    print(cycle)
    if card7_status[0] == 'saved' and card7_default != [] and pag.pixel(1135, 132) != card7_default[0]:
        '''cycle_8 = cv.imread('card 7.png')
        cv.imshow('card 7', cycle_8)
        cv.moveWindow('card 7', 1700, 400)
        key7 = cv.waitKey(0)
        if key7 == ord('7'):
            cv.destroyWindow('card 7')'''
        if champion_played == ['card 7.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index7 = cycle.index('card 7.png')
            cycle.pop(index7 + 1)
            cycle.remove(champion_played[0])
        if len(played_status7) == 9:
            # print('card 7')
            try:
                index7 = cycle.index('card 7.png')
                cycle.pop(index7 + 1)
                cycle.remove('card 7.png')
                cycle.append('card 7.png')
                cycle.append(card7_status[-1])
            except:
                pass
            for i in range(9):
                played_status7.pop()
    if len(played_status7) != 9:
        played_status7.append(1)

    print(cycle)
    if card8_status[0] == 'saved' and card8_default != [] and pag.pixel(1194, 132) != card8_default[0]:
        '''cycle_8 = cv.imread('card 4.png')
        cv.imshow('card 8', cycle_8)
        cv.moveWindow('card 8', 1850, 400)
        key8 = cv.waitKey(0)
        if key8 == ord('8'):
            cv.destroyWindow('card 8')'''
        if champion_played == ['card 8.png'] and champion_status != ['alive']:
            champion_status.append('alive')
            index8 = cycle.index('card 8.png')
            cycle.pop(index8 + 1)
            cycle.remove(champion_played[0])
        if len(played_status8) == 9:
            # print('card 8')
            try:
                index8 = cycle.index('card 8.png')
                cycle.pop(index8 + 1)
                cycle.remove('card 8.png')
                cycle.append('card 8.png')
                cycle.append(card8_status[-1])
            except:
                pass
            for i in range(9):
                played_status8.pop()
    if len(played_status8) != 9:
        played_status1.append(1)

    print(cycle)
print('''log=58
earthquake=162
log+earthquake=220
2 earthquakes+log=382
2 earthquakes+2 logs=440


fireball=207
zap=58
fireball+zap=265''')
while True:
    #print(cycle)
    '''print(card1_status)
    print(card2_status)
    print(card3_status)
    print(card4_status)
    print(card5_status)
    print(card6_status)
    print(card7_status)
    print(card8_status)
    # print(cycle)'''
    '''print(card1_elixir)
    print(card2_elixir)
    print(card3_elixir)
    print(card4_elixir)
    print(card5_elixir)
    print(card6_elixir)
    print(card7_elixir)
    print(card8_elixir)'''
    card_images()
    print("Finished card_images")
    card_played()
    print("Finished card_played")
    # print(current_elixir)
    # print(card1_elixir)
    cv.imshow("Opponent's cycle", background)
    cv.moveWindow("Opponent's cycle", 583, 187)
    if pag.locateOnScreen('Elixir bar/0.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(0)
    elif pag.locateOnScreen('Elixir bar/1.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(1)
    elif pag.locateOnScreen('Elixir bar/2.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(2)
    elif pag.locateOnScreen('Elixir bar/3.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(3)
    elif pag.locateOnScreen('Elixir bar/4.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(4)
    elif pag.locateOnScreen('Elixir bar/5.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(5)
    elif pag.locateOnScreen('Elixir bar/6.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(6)
    elif pag.locateOnScreen('Elixir bar/7.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(7)
    elif pag.locateOnScreen('Elixir bar/8.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(8)
    elif pag.locateOnScreen('Elixir bar/9.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(9)
    elif pag.locateOnScreen('Elixir bar/10.png', region=(705, 42, 35, 37), confidence=0.9):
        current_elixir.pop()
        current_elixir.append(10)
    else:
        pass
    # print(current_elixir)
    if card1_status[-1] in range(0,10):
        if current_elixir[0] >= cycle[1]:
            cycle_1 = cv.imread(cycle[0])
        else:
            cycle_1 = cv.imread(cycle[0], 0)
            #print('card 1')
        cv.imshow('card 1', cycle_1)
        cv.moveWindow('card 1', 1083, 350)
        # cv.waitKey(1)
    if card2_status[-1] in range(0,10):
        if current_elixir[0] >= cycle[3]:
            cycle_2 = cv.imread(cycle[2])
        else:
            cycle_2 = cv.imread(cycle[2], 0)
            #print('      card 2')
        cv.imshow('card 2', cycle_2)
        cv.moveWindow('card 2', 933, 350)
        # cv.waitKey(1)
    if card3_status[-1] in range(0,10):
        if current_elixir[0] >= cycle[5]:
            cycle_3 = cv.imread(cycle[4])
        else:
            cycle_3 = cv.imread(cycle[4], 0)
            #print('            card 3')
        cv.imshow('card 3', cycle_3)
        cv.moveWindow('card 3', 783, 350)
        # cv.waitKey(1)
    if card4_status[-1] in range(0, 10):
        if current_elixir[0] >= cycle[7]:
            cycle_4 = cv.imread(cycle[6])
        else:
            cycle_4 = cv.imread(cycle[6], 0)
            #print('                  card 4')
        cv.imshow('card 4', cycle_4)
        cv.moveWindow('card 4', 633, 350)
        # cv.waitKey(1)
    cycle_5 = cv.imread(cycle[8])
    # print('card 5 unavailable')
    cv.imshow('card 5', cycle_5)
    cv.moveWindow('card 5', 633, 600)
    # cv.waitKey(1)
    cycle_6 = cv.imread(cycle[10])
    # print('card 6 unavailable')
    cv.imshow('card 6', cycle_6)
    cv.moveWindow('card 6', 783, 600)
    # cv.waitKey(1)
    cycle_7 = cv.imread(cycle[12])
    # print('card 7 unavailable')
    cv.imshow('card 7', cycle_7)
    cv.moveWindow('card 7', 933, 600)
    # cv.waitKey(1)
    if card8_status[-1] in range(0,10):
        try:
            cycle_8 = cv.imread(cycle[14])
            # print('card 8 unavailable')
            cv.imshow('card 8', cycle_8)
            cv.moveWindow('card 8', 1083, 600)
            #cv.waitKey(1)
        except:
            cv.moveWindow('card 8', 1920, 1030)
            #cv.waitKey(1)
    # print(cycle)
    if kb.is_pressed('space'):
        try:
            if len(champion_kill_status) == 30:
                #cycle.insert(12, champion_played[0])
                #cycle.insert(13, champion_elixir[0])
                cycle.append(champion_played[0])
                cycle.append(champion_elixir[0])
                for i in range(len(champion_status)):
                    champion_status.pop()
                for i in range(30):
                    champion_kill_status.pop()
        except:
            print('No champion in play!')
    if len(champion_kill_status) != 30:
        champion_kill_status.append(1)
    if champion_status == ['alive']:
        if current_elixir[0] >= champion_elixir[0]:
            champion_cycle = cv.imread(champion_played[0])
        else:
            champion_cycle = cv.imread(champion_played[0], 0)
        # champion_cycle = cv.imread(champion_played[0])
        cv.imshow('champion in play', champion_cycle)
        cv.moveWindow('champion in play', 858, 850)
        #cv.waitKey(1)
    else:
        try:
            cv.moveWindow('champion in play', 1920, 1080)
        except:
            pass
    cv.waitKey(1)
    '''cv.destroyWindow('card 1')
    cv.destroyWindow('card 2')
    cv.destroyWindow('card 3')
    cv.destroyWindow('card 4')
    cv.destroyWindow('card 5')
    cv.destroyWindow('card 6')
    cv.destroyWindow('card 7')
    cv.destroyWindow('card 8')'''

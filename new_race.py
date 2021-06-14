import pygame
import math
import pickle
import Libraries.LibraryGame as lg
import Libraries.collisionDetection as cd
import Libraries.LibraryNeuralNetwork as lnn

TIME_TRACE = 300
from win32api import GetSystemMetrics
print(GetSystemMetrics(0),GetSystemMetrics(1)-50)

#pygame.init() # Long to charge
pygame.font.init()
gameDisplay = pygame.display.set_mode((GetSystemMetrics(0),GetSystemMetrics(1)-50))
pygame.display.set_caption("Racing")
myfont = pygame.font.SysFont('Arial', 20)
font_text = pygame.font.SysFont('Arial', 40)
clock = pygame.time.Clock()

back = pygame.image.load('imgs/screen3.png').convert_alpha()
#back = pygame.transform.rotozoom(back, 0, 2)
## 1
#exterior = [(355, 55), (407, 59), (468, 59), (489, 74), (503, 104), (495, 135), (467, 165), (449, 178), (399, 190), (347, 195), (277, 205), (269, 239), (275, 278), (287, 311), (323, 334), (360, 339), (421, 342), (471, 338), (525, 317), (561, 311), (603, 327), (636, 361), (652, 399), (645, 454), (604, 518), (547, 552), (449, 568), (374, 569), (315, 552), (249, 515), (185, 469), (126, 402), (109, 343), (109, 301), (122, 263), (142, 244), (175, 216), (197, 184), (190, 158), (166, 133), (148, 121), (137, 96), (155, 92), (195, 71), (219, 68), (254, 64), (302, 64), (324, 59)]
#pygame.draw.lines(gameDisplay, (255,255,255), True, exterior)
#interior = [(307, 95), (337, 97), (378, 96), (427, 91), (444, 102), (443, 124), (414, 148), (359, 159), (326, 156), (283, 160), (261, 163), (245, 174), (234, 185), (222, 202), (218, 230), (219, 260), (224, 301), (232, 320), (247, 342), (277, 357), (305, 367), (337, 375), (370, 380), (409, 386), (454, 383), (506, 376), (550, 370), (576, 373), (597, 406), (593, 444), (575, 468), (553, 492), (520, 516), (461, 530), (421, 534), (382, 524), (337, 512), (307, 499), (279, 481), (241, 454), (216, 437), (194, 413), (181, 385), (167, 355), (155, 328), (157, 301), (171, 277), (187, 263), (206, 244), (211, 222), (214, 203), (222, 187), (227, 176), (230, 158), (232, 141), (218, 121), (204, 110), (235, 105), (265, 104), (309, 92)]
#pygame.draw.lines(gameDisplay, (255,255,255), True, interior)
# wall = [(0,0),(1,1)]
# pygame.draw.lines(gameDisplay, (255,255,255), True, wall)

## 2
exterior = [(409, 57), (440, 55), (504, 48), (536, 47), (587, 48), (657, 44), (722, 39), (806, 32), (892, 39), (982, 35), (1070, 39), (1158, 45), (1221, 46), (1286, 46), (1335, 61), (1372, 96), (1390, 143), (1409, 199), (1422, 252), (1416, 295), (1400, 333), (1365, 358), (1326, 374), (1270, 377), (1208, 380), (1156, 367), (1092, 359), (1045, 345), (1006, 330), (955, 328), (923, 338), (899, 360), (875, 394), (855, 430), (847, 485), (851, 517), (857, 550), (857, 597), (843, 643), (816, 687), (793, 
700), (733, 717), (662, 727), (622, 721), (562, 714), (482, 693), (436, 688), (383, 669), (313, 658), (261, 640), (221, 617), (186, 578), (159, 527), (137, 466), (117, 404), (101, 351), (89, 306), (85, 270), (88, 219), (97, 179), (110, 143), (132, 114), (158, 98), (200, 87), (247, 75), (297, 69), (351, 66), (401, 60), (409, 57)]
pygame.draw.lines(gameDisplay, (255,255,255), True, exterior)
interior = [(414, 92), (466, 92), (483, 96), (512, 105), (566, 113), (601, 115), (641, 118), (695, 114), (725, 102), (752, 89), (779, 74), (814, 65), (835, 61), (862, 62), (878, 61), (907, 62), (952, 68), (983, 70), (1000, 62), (1036, 63), (1088, 77), (1141, 83), (1174, 85), (1243, 101), (1258, 107), (1278, 119), (1302, 153), (1314, 176), (1327, 209), (1333, 237), (1332, 252), (1321, 273), (1299, 287), (1275, 301), (1229, 304), (1161, 307), (1135, 305), (1103, 297), (1081, 292), (1057, 283), (1029, 275), (991, 273), (937, 275), (894, 283), (859, 294), (832, 305), (811, 317), (801, 335), (791, 364), (786, 382), (778, 409), (773, 438), (770, 454), (766, 478), (766, 513), (766, 535), (766, 568), (755, 611), (746, 625), (715, 636), (672, 651), (645, 647), (613, 644), (566, 637), (527, 629), (490, 620), (431, 615), (395, 605), (364, 600), (335, 590), (323, 585), (295, 561), (279, 539), (264, 515), (245, 502), (222, 493), (207, 488), (190, 482), (182, 476), (168, 455), (162, 443), (161, 420), (162, 403), (162, 378), (164, 352), (165, 327), (165, 311), (164, 296), (162, 258), (162, 246), (167, 223), (187, 195), (211, 162), (229, 139), (240, 130), (253, 123), (292, 111), (319, 105), (336, 101), (391, 97), (430, 94), (469, 96), (492, 101), (527, 105)]
pygame.draw.lines(gameDisplay, (255,255,255), True, interior)
true_wall1 = [(768, 478), (797, 508), (802, 526), (802, 547), (797, 581), (793, 601), (782, 618), (770, 630), (757, 637), (734, 643), (710, 646), (703, 646), (700, 644), (741, 630), (750, 620), (766, 589), (768, 569), (766, 540), (766, 529), (766, 523), "|",
(1279, 119), (1351, 169), (1374, 251), (1328, 325), (1244, 345), (1203, 325), (1179, 304), (1275, 298), (1319, 274), (1332, 253), (1331, 227), (1315, 185), (1298, 147)]
wall = true_wall1

points = []
currentPoints = []
traces = []

THRESHOLD = 0.5
VIEW_RANGE = 150

carImg = pygame.image.load("imgs/car.png").convert_alpha()

def generateCar():
    car = lg.Car()
    car.orientedCarImg = pygame.transform.rotate(carImg, 90)
    car.selected = True
    with (open("car_nn150.pkl", "rb")) as file :
        car.nn = pickle.load(file)
    return car

car = generateCar()

# print(car.nn.layers)
# with (open("NeuralNetwork.txt", "rb")) as file :
#     line = file.readline().split()
#     for l in car.nn.layers[1:]:
#         line = file.readline().split()
#         print(line)
#         i=0
#         for j in range(len(l.neurons)):
#             #l.neurons[j] = lnn.Neuron(dimension=len(l.neurons[j].weights))
#             for k in range(len(l.neurons[j].weights)):
#                 l.neurons[j].weights[k] = float(line[i])
#                 i+=1
#     print(car.nn.layers)

# NN area
X_SIZE = 400
Y_SIZE = 250
TOP_LEFT_X = 1000
TOP_LEFT_Y = 450

# Text area
TOP_LEFT_X_TEXT = 300
TOP_LEFT_Y_TEXT = 200

# Text 2 area
TOP_LEFT_X_TEXT_2 = 1100
TOP_LEFT_Y_TEXT_2 = 150

def draw_lines(surf, points, width=1):
    for i in range(len(points)-1):
        if points[i] != "|" and points[i+1] != "|" :
            pygame.draw.line(surf, (255,255,255), points[i], points[i+1], width)


draw_lines(gameDisplay, wall)
drawing = False
finished = False
while not finished :

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_w :
                if wall == [(0,0),(1,1)] :
                    wall = true_wall1.copy()
                else :
                    wall = [(0,0),(1,1)]
            if event.key == pygame.K_e :
                # Add wall
                drawing = False
                wall.append("|")
                for p in points[:-1] :
                    wall.append(p)
                points = []
            if event.key == pygame.K_r :
                # Restart
                car = generateCar()
                traces = []
            if event.key == pygame.K_c :
                # Clear
                wall = []


        if(event.type == pygame.MOUSEBUTTONDOWN):
                    # Below for debugging
                    currentPoints = event.pos
                    if len(currentPoints) == 2:
                        points.append(currentPoints)
                        currentPoints = None 
                    print(points)
                    drawing = True

    gameDisplay.fill((0,0,0), (0,0,GetSystemMetrics(0),GetSystemMetrics(1)-50))
    gameDisplay.fill((0,0,0), (TOP_LEFT_X-10,TOP_LEFT_Y-20,TOP_LEFT_X+X_SIZE,TOP_LEFT_Y+Y_SIZE))
    gameDisplay.blit(back, (0,0))

    if drawing and len(points) > 0:
        if len(points) == 1 :
            points.append(pygame.mouse.get_pos())
        else :
            points[-1] = pygame.mouse.get_pos()
        pygame.draw.lines(gameDisplay, (0,0,0), False, points)
        if len(points) > 2 :
            if (pygame.mouse.get_pos()[0] < points[0][0]+5 and pygame.mouse.get_pos()[0] > points[0][0]-5 and
                pygame.mouse.get_pos()[1] < points[0][1]+5 and pygame.mouse.get_pos()[1] > points[0][1]-5 ) :
                drawing = False
                wall.append("|")
                for p in points :
                    wall.append(p)
                wall.append(points[0])
                points = []

    ######## Text
    textsurface = []
    textsurface.append(font_text.render("Projet par Arnoux Arthur & Pèlegrin Grégoire", False, (255, 255, 255)))
    textsurface.append(font_text.render("       Réseaux de neurones", False, (255, 255, 255)))
    textsurface.append(font_text.render("                &        ", False, (255, 255, 255)))
    textsurface.append(font_text.render("       Algorithme génétique", False, (255, 255, 255)))
    for line in range(len(textsurface)) :
        gameDisplay.blit(textsurface[line],(TOP_LEFT_X_TEXT, TOP_LEFT_Y_TEXT+line*60))
        
    ######## Text 2
    textsurface = []
    textsurface.append(myfont.render("[R] Reset car", False, (255, 255, 255)))
    textsurface.append(myfont.render("[clics + E] Create wall", False, (255, 255, 255)))
    textsurface.append(myfont.render("[C] Clear walls", False, (255, 255, 255)))
    textsurface.append(myfont.render("[W] Activate walls", False, (255, 255, 255)))
    for line in range(len(textsurface)) :
        gameDisplay.blit(textsurface[line],(TOP_LEFT_X_TEXT_2, TOP_LEFT_Y_TEXT_2+line*30))

    ######## NN inputs & outputs
    textsurface = []
    textsurface.append(myfont.render("Speed", False, (255, 255, 255)))
    textsurface.append(myfont.render("Left", False, (255, 255, 255)))
    textsurface.append(myfont.render("Straight", False, (255, 255, 255)))
    textsurface.append(myfont.render("Right", False, (255, 255, 255)))
    for line in range(len(textsurface)) :
        gameDisplay.blit(textsurface[line],(TOP_LEFT_X-70, TOP_LEFT_Y+20+line*60))
    textsurface = []
    textsurface.append(myfont.render("Go left", False, (255, 255, 255)))
    textsurface.append(myfont.render("Accelerate", False, (255, 255, 255)))
    textsurface.append(myfont.render("Slow down", False, (255, 255, 255)))
    textsurface.append(myfont.render("Go right", False, (255, 255, 255)))
    for line in range(len(textsurface)) :
        gameDisplay.blit(textsurface[line],(TOP_LEFT_X+330, TOP_LEFT_Y+20+line*60))

    pygame.draw.lines(gameDisplay, (255,255,255), False, interior)
    pygame.draw.lines(gameDisplay, (255,255,255), False, exterior)
    #pygame.draw.lines(gameDisplay, (255,255,255), True, wall)
    draw_lines(gameDisplay, wall)


    car.orientedCarImg = pygame.transform.rotate(carImg, -car.orientation)
    new_rect = car.orientedCarImg.get_rect(center = (car.x,car.y))

    lineSurface = pygame.Surface((800,600), pygame.SRCALPHA, 32)
    lineSurface = lineSurface.convert_alpha()

    if car.selected :
        i = 0
        nb_layers = len(car.nn.layers)
        for layer in car.nn.layers :
            j = 0
            nb_neurons = len(layer.neurons)
            for neuron in layer.neurons :
                k = 0
                nb_weights = len(neuron.weights)
                try:
                    for weight in neuron.weights :
                        pygame.draw.line(gameDisplay, (255,255,255),(TOP_LEFT_X+(i-1)*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_weights)/2+k*(Y_SIZE/nb_weights)),
                                                                    (TOP_LEFT_X+i*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_neurons)/2+j*(Y_SIZE/nb_neurons)))
                        k += 1
                    if i == nb_layers-1: # if last layer
                        if neuron.value > THRESHOLD :
                            pygame.draw.circle(gameDisplay, (0,255,0), (TOP_LEFT_X+i*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_neurons)/2+j*(Y_SIZE/nb_neurons)), 7)
                        else :
                            pygame.draw.circle(gameDisplay, (255,255-min(1,neuron.value)*255,255-min(1,neuron.value)*255), (TOP_LEFT_X+i*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_neurons)/2+j*(Y_SIZE/nb_neurons)), 7)

                    elif i > 0 : # if not first layer
                        pygame.draw.circle(gameDisplay, (255,255-min(1,neuron.value)*255,255-min(1,neuron.value)*255), (TOP_LEFT_X+i*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_neurons)/2+j*(Y_SIZE/nb_neurons)), 7)


                    else : # if first layer
                        pygame.draw.circle(gameDisplay, (255,min(1,neuron.value)*255,min(1,neuron.value)*255), (TOP_LEFT_X+i*(X_SIZE/nb_layers), TOP_LEFT_Y+(Y_SIZE/nb_neurons)/2+j*(Y_SIZE/nb_neurons)), 7)
                except :
                    print(i ,neuron.value)

                j+=1
            i+=1
        #gameDisplay.fill((0,0,0), (TOP_LEFT_X+40,TOP_LEFT_Y-20,300,20))
        textsurface = []
        textsurface.append(myfont.render("Car speed : {}".format(car.speed), False, (255, 255, 255)))
        textsurface.append(myfont.render("Car distance : {}".format(car.totalDistance), False, (255, 255, 255)))
        for line in range(len(textsurface)) :
            gameDisplay.blit(textsurface[line],(TOP_LEFT_X+50+line*200, TOP_LEFT_Y-10))

    car.visible and gameDisplay.blit(car.orientedCarImg, new_rect.topleft)

    dx1 = math.cos((car.orientation-90) * math.pi / 180)
    dy1 = math.sin((car.orientation-90) * math.pi / 180)
    dx2 = math.cos((car.orientation-45) * math.pi / 180)
    dy2 = math.sin((car.orientation-45) * math.pi / 180)
    dx3 = math.cos((car.orientation-135) * math.pi / 180)
    dy3 = math.sin((car.orientation-135) * math.pi / 180)

    dist1 = None
    dist2 = None
    dist3 = None
    for p in range(len(interior)-1):
        if dist1 is None :
            dist1 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx1*VIEW_RANGE,car.y+dy1*VIEW_RANGE],
                                    interior[p], interior[p+1])
        if dist2 is None :
            dist2 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx2*VIEW_RANGE,car.y+dy2*VIEW_RANGE],
                                [interior[p][0], interior[p][1]], [interior[p+1][0], interior[p+1][1]])
        if dist3 is None :
            dist3 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx3*VIEW_RANGE,car.y+dy3*VIEW_RANGE],
                                [interior[p][0], interior[p][1]], [interior[p+1][0], interior[p+1][1]])

    for p in range(len(exterior)-1):
        if dist1 is None :
            dist1 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx1*VIEW_RANGE,car.y+dy1*VIEW_RANGE],
                                [exterior[p][0], exterior[p][1]], [exterior[p+1][0], exterior[p+1][1]])
        if dist2 is None :
            dist2 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx2*VIEW_RANGE,car.y+dy2*VIEW_RANGE],
                                [exterior[p][0], exterior[p][1]], [exterior[p+1][0], exterior[p+1][1]])
        if dist3 is None :
            dist3 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx3*VIEW_RANGE,car.y+dy3*VIEW_RANGE],
                                [exterior[p][0], exterior[p][1]], [exterior[p+1][0], exterior[p+1][1]])
    
    dist1_wall = None
    dist2_wall = None
    dist3_wall = None
    for p in range(len(wall)-1):
        if wall[p] != "|" and wall[p+1] != "|" :
            if dist1 is None :
                dist1 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx1*VIEW_RANGE,car.y+dy1*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])
            elif dist1_wall is None :
                dist1_wall = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx1*VIEW_RANGE,car.y+dy1*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])
                
            if dist2 is None :
                dist2 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx2*VIEW_RANGE,car.y+dy2*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])
            elif dist2_wall is None :
                dist2_wall = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx2*VIEW_RANGE,car.y+dy2*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])
                
            if dist3 is None :
                dist3 = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx3*VIEW_RANGE,car.y+dy3*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])
            elif dist3_wall is None :
                dist3_wall = cd.calculateIntersectPoint([car.x, car.y], [car.x+dx3*VIEW_RANGE,car.y+dy3*VIEW_RANGE],
                                    [wall[p][0], wall[p][1]], [wall[p+1][0], wall[p+1][1]])


    if dist1 is None :
        dist1 = VIEW_RANGE
    else :
        dist1 = math.sqrt( (car.x-dist1[0])**2 + (car.y-dist1[1])**2 )
        if dist1_wall is not None :
            dist1 = min(dist1, math.sqrt( (car.x-dist1_wall[0])**2 + (car.y-dist1_wall[1])**2 ) )
    if dist2 is None :
        dist2 = VIEW_RANGE
    else :
        dist2 = math.sqrt( (car.x-dist2[0])**2 + (car.y-dist2[1])**2 )
        if dist2_wall is not None :
            dist2 = min(dist2, math.sqrt( (car.x-dist2_wall[0])**2 + (car.y-dist2_wall[1])**2 ) )
    if dist3 is None :
        dist3 = VIEW_RANGE
    else :
        dist3 = math.sqrt( (car.x-dist3[0])**2 + (car.y-dist3[1])**2 )
        if dist3_wall is not None :
            dist3 = min(dist3, math.sqrt( (car.x-dist3_wall[0])**2 + (car.y-dist3_wall[1])**2 ) )
    if(dist1 < 5 or dist2 < 5 or dist3 < 5):
        car.alive = False
        continue


    car.x += dx1*car.speed
    car.y += dy1*car.speed
    traces.append((car.x,car.y))
    if len(traces) > 2 :
        pygame.draw.lines(gameDisplay, (65,65,65), False, traces)
    if len(traces) > TIME_TRACE :
        del traces[0]
    #car.totalDistance += (dx1**2+dy1**2+car.speed**2)**0.5
    #car.totalDistance = round(car.totalDistance, 1)
    car.totalDistanceAfterCheckpoint += (dx1**2+dy1**2)**0.5
    car.totalDistanceAfterCheckpoint = round(car.totalDistanceAfterCheckpoint, 1)
    car.totalDistance = car.nextCheckpointId * 100 + car.totalDistanceAfterCheckpoint

    ######## Neural network inputs
    speed_normalized = (car.speed +5) / 15  
    dist2_normalized = dist2 / VIEW_RANGE
    dist1_normalized = dist1 / VIEW_RANGE
    dist3_normalized = dist3 / VIEW_RANGE
    listInput = car.nn.evaluate([speed_normalized, dist3_normalized, dist1_normalized, dist2_normalized])
    #listInput = [random.uniform(0, 1),random.uniform(0, 1)]
    
    if(listInput[0] >= THRESHOLD):
        car.orientation -= 5

    if(listInput[1] >= THRESHOLD):
        if car.speed <= 10 :
            car.speed += 1
    if(listInput[2] >= THRESHOLD):
        if car.speed >= -5 :
            car.speed -= 0.5


    if(listInput[3] >= THRESHOLD):
        car.orientation += 5
    #########

    if car.x != car.lastX or car.y != car.lastY:
        tokenStop = False

    car.nn.fitness = car.fitness()

    pygame.display.update()
    clock.tick(30)
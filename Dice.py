import random
running = True
while running:
    choice = input("ENTER CHOICE[Y TO ROLL,N TO EXIT):")
    if choice == 'n' or choice == 'N':
        running = False
    elif choice == 'y' or 'Y':
        x = random.randint(1, 6)
        print(x)
        if x == 1:
            for i in range(1, 7, 1):
                if i == 4:
                    print('[          0         ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
        elif x == 2:
            for i in range(1, 7, 1):
                if i == 4:
                    print('[       0     0      ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
        elif x == 3:
            for i in range(1, 7, 1):
                if i == 2:
                    print('[  0                 ]')
                if i == 4:
                    print('[         0          ]')
                if i == 6:
                    print('[                 0  ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
        elif x == 4:
            for i in range(1, 7, 1):
                if i == 3 or i == 5:
                    print('[    0           0   ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
        elif x == 5:
            for i in range(1, 7, 1):
                if i == 2 or i == 6:
                    print('[    0           0   ]')
                if i == 4:
                    print('[          0         ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
        elif x == 6:
            for i in range(1, 7, 1):
                if i == 2 or i == 4 or i == 6:
                    print('[    0           0   ]')
                if i == 1 or i == 6:
                    print('[--------------------]')
                else:
                    print('[                    ]')
    else:
        print("INVALID CHOICE\n")

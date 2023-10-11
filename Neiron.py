from PIL import Image

#---------------------------------------------------------
# Функции
#---------------------------------------------------------

def Do_Black(img, pixels):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixels[i,j] != (255, 255, 255):
                pixels[i,j] = (0, 0 ,0)
        
#---------------------------------------------------------

def difference_images(arr, img1, px1, px2, px3, px4, px5):
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            if px1[i,j] == (0, 0, 0) and px2[i,j] == (0, 0, 0) and px3[i,j] == (0, 0, 0) and px4[i,j] == (0, 0, 0) and px5[i,j] == (0, 0, 0):
                arr.append(1)
            else:
                arr.append(0)

#---------------------------------------------------------

def test_array(arr, img, px):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if px[i,j] != (255, 255, 255):
                arr.append(1)
            else:
                arr.append(0)

#---------------------------------------------------------

def Calc_number(arr_t, arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9):
    global Counter_0
    global Counter_1
    global Counter_2
    global Counter_3
    global Counter_4
    global Counter_5
    global Counter_6
    global Counter_7
    global Counter_8
    global Counter_9

    for i in range(0, len(arr_t)):
        if arr_t[i] == arr0[i]:
            Counter_0 += 1
        if arr_t[i] == arr1[i]:
            Counter_1 += 1
        if arr_t[i] == arr2[i]:
            Counter_2 += 1
        if arr_t[i] == arr3[i]:
            Counter_3 += 1
        if arr_t[i] == arr4[i]:
            Counter_4 += 1
        if arr_t[i] == arr5[i]:
            Counter_5 += 1
        if arr_t[i] == arr6[i]:
            Counter_6 += 1
        if arr_t[i] == arr7[i]:
            Counter_7 += 1
        if arr_t[i] == arr8[i]:
            Counter_8 += 1
        if arr_t[i] == arr9[i]:
            Counter_9 += 1

def definition_num(c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, res):
    Maximum = max([c0, c1, c2, c3, c4, c5, c6, c7, c8, c9])
    if Maximum == c0:
        res = "Test number: 0"
    if Maximum == c1:
        res = "Test number: 1"
    if Maximum == c2:
        res = "Test number: 2"
    if Maximum == c3:
        res = "Test number: 3"
    if Maximum == c4:
        res = "Test number: 4"
    if Maximum == c5:
        res = "Test number: 5"
    if Maximum == c6:
        res = "Test number: 6"
    if Maximum == c7:
        res = "Test number: 7"
    if Maximum == c8:
        res = "Test number: 8"
    if Maximum == c9:
        res = "Test number: 9"
    print(res)

#---------------------------------------------------------
# Инициализация данных обучения
#---------------------------------------------------------

Null_1 = Image.open("Learn-materials/0/1.png")
Null_1_p = Null_1.load()

Null_2 = Image.open("Learn-materials/0/2.png")
Null_2_p = Null_2.load()

Null_3 = Image.open("Learn-materials/0/3.png")
Null_3_p = Null_3.load()

Null_4 = Image.open("Learn-materials/0/4.png")
Null_4_p = Null_4.load()

Null_5 = Image.open("Learn-materials/0/5.png")
Null_5_p = Null_5.load()

#---------------------------------------------------------

One_1 = Image.open("Learn-materials/1/1.png")
One_1_p = One_1.load()

One_2 = Image.open("Learn-materials/1/2.png")
One_2_p = One_2.load()

One_3 = Image.open("Learn-materials/1/3.png")
One_3_p = One_3.load()

One_4 = Image.open("Learn-materials/1/4.png")
One_4_p = One_4.load()

One_5 = Image.open("Learn-materials/1/5.png")
One_5_p = One_5.load()

#---------------------------------------------------------

Two_1 = Image.open("Learn-materials/2/1.png")
Two_1_p = Two_1.load()

Two_2 = Image.open("Learn-materials/2/2.png")
Two_2_p = Two_2.load()

Two_3 = Image.open("Learn-materials/2/3.png")
Two_3_p = Two_3.load()

Two_4 = Image.open("Learn-materials/2/4.png")
Two_4_p = Two_4.load()

Two_5 = Image.open("Learn-materials/2/5.png")
Two_5_p = Two_5.load()

#---------------------------------------------------------

Three_1 = Image.open("Learn-materials/3/1.png")
Three_1_p = Three_1.load()

Three_2 = Image.open("Learn-materials/3/2.png")
Three_2_p = Three_2.load()

Three_3 = Image.open("Learn-materials/3/3.png")
Three_3_p = Three_3.load()

Three_4 = Image.open("Learn-materials/3/4.png")
Three_4_p = Three_4.load()

Three_5 = Image.open("Learn-materials/3/5.png")
Three_5_p = Three_5.load()

#---------------------------------------------------------

Four_1 = Image.open("Learn-materials/4/1.png")
Four_1_p = Four_1.load()

Four_2 = Image.open("Learn-materials/4/2.png")
Four_2_p = Four_2.load()

Four_3 = Image.open("Learn-materials/4/3.png")
Four_3_p = Four_3.load()

Four_4 = Image.open("Learn-materials/4/4.png")
Four_4_p = Four_4.load()

Four_5 = Image.open("Learn-materials/4/5.png")
Four_5_p = Four_5.load()

#---------------------------------------------------------

Five_1 = Image.open("Learn-materials/5/1.png")
Five_1_p = Five_1.load()

Five_2 = Image.open("Learn-materials/5/2.png")
Five_2_p = Five_2.load()

Five_3 = Image.open("Learn-materials/5/3.png")
Five_3_p = Five_3.load()

Five_4 = Image.open("Learn-materials/5/4.png")
Five_4_p = Five_4.load()

Five_5 = Image.open("Learn-materials/5/5.png")
Five_5_p = Five_5.load()

#---------------------------------------------------------

Six_1 = Image.open("Learn-materials/6/1.png")
Six_1_p = Six_1.load()

Six_2 = Image.open("Learn-materials/6/2.png")
Six_2_p = Six_2.load()

Six_3 = Image.open("Learn-materials/6/3.png")
Six_3_p = Six_3.load()

Six_4 = Image.open("Learn-materials/6/4.png")
Six_4_p = Six_4.load()

Six_5 = Image.open("Learn-materials/6/5.png")
Six_5_p = Six_5.load()

#---------------------------------------------------------

Seven_1 = Image.open("Learn-materials/7/1.png")
Seven_1_p = Seven_1.load()

Seven_2 = Image.open("Learn-materials/7/2.png")
Seven_2_p = Seven_2.load()

Seven_3 = Image.open("Learn-materials/7/3.png")
Seven_3_p = Seven_3.load()

Seven_4 = Image.open("Learn-materials/7/4.png")
Seven_4_p = Seven_4.load()

Seven_5 = Image.open("Learn-materials/7/5.png")
Seven_5_p = Seven_5.load()

#---------------------------------------------------------

Eight_1 = Image.open("Learn-materials/8/1.png")
Eight_1_p = Eight_1.load()

Eight_2 = Image.open("Learn-materials/8/2.png")
Eight_2_p = Eight_2.load()

Eight_3 = Image.open("Learn-materials/8/3.png")
Eight_3_p = Eight_3.load()

Eight_4 = Image.open("Learn-materials/8/4.png")
Eight_4_p = Eight_4.load()

Eight_5 = Image.open("Learn-materials/8/5.png")
Eight_5_p = Eight_5.load()

#---------------------------------------------------------

Nine_1 = Image.open("Learn-materials/9/1.png")
Nine_1_p = Nine_1.load()

Nine_2 = Image.open("Learn-materials/9/2.png")
Nine_2_p = Nine_2.load()

Nine_3 = Image.open("Learn-materials/9/3.png")
Nine_3_p = Nine_3.load()

Nine_4 = Image.open("Learn-materials/9/4.png")
Nine_4_p = Nine_4.load()

Nine_5 = Image.open("Learn-materials/9/5.png")
Nine_5_p = Nine_5.load()

#---------------------------------------------------------
#---------------------------------------------------------

arr_0 = []
arr_1 = []
arr_2 = []
arr_3 = []
arr_4 = []
arr_5 = []
arr_6 = []
arr_7 = []
arr_8 = []
arr_9 = []

#---------------------------------------------------------
# Инициализация тестовых данных 
#---------------------------------------------------------

Test_img = Image.open("Test-materials/test.png")
Test_px = Test_img.load()

Test_arr = []

Counter_0 = 0
Counter_1 = 0
Counter_2 = 0
Counter_3 = 0
Counter_4 = 0
Counter_5 = 0
Counter_6 = 0
Counter_7 = 0
Counter_8 = 0
Counter_9 = 0

Result = "-"

#---------------------------------------------------------
# Вызов функций
#---------------------------------------------------------
print("Start learning.")

Do_Black(Null_1, Null_1_p)
Do_Black(Null_2, Null_2_p)
Do_Black(Null_3, Null_3_p)
Do_Black(Null_4, Null_4_p)
Do_Black(Null_5, Null_5_p)
Do_Black(One_1, One_1_p)
Do_Black(One_2, One_2_p)
Do_Black(One_3, One_3_p)
Do_Black(One_4, One_4_p)
Do_Black(One_5, One_5_p)
Do_Black(Two_1, Two_1_p)
Do_Black(Two_2, Two_2_p)
Do_Black(Two_3, Two_3_p)
Do_Black(Two_4, Two_4_p)
Do_Black(Two_5, Two_5_p)
Do_Black(Three_1, Three_1_p)
Do_Black(Three_2, Three_2_p)
Do_Black(Three_3, Three_3_p)
Do_Black(Three_4, Three_4_p)
Do_Black(Three_5, Three_5_p)
Do_Black(Four_1, Four_1_p)
Do_Black(Four_2, Four_2_p)
Do_Black(Four_3, Four_3_p)
Do_Black(Four_4, Four_4_p)
Do_Black(Four_5, Four_5_p)
Do_Black(Five_1, Five_1_p)
Do_Black(Five_2, Five_2_p)
Do_Black(Five_3, Five_3_p)
Do_Black(Five_4, Five_4_p)
Do_Black(Five_5, Five_5_p)
Do_Black(Six_1, Six_1_p)
Do_Black(Six_2, Six_2_p)
Do_Black(Six_3, Six_3_p)
Do_Black(Six_4, Six_4_p)
Do_Black(Six_5, Six_5_p)
Do_Black(Seven_1, Seven_1_p)
Do_Black(Seven_2, Seven_2_p)
Do_Black(Seven_3, Seven_3_p)
Do_Black(Seven_4, Seven_4_p)
Do_Black(Seven_5, Seven_5_p)
Do_Black(Eight_1, Eight_1_p)
Do_Black(Eight_2, Eight_2_p)
Do_Black(Eight_3, Eight_3_p)
Do_Black(Eight_4, Eight_4_p)
Do_Black(Eight_5, Eight_5_p)
Do_Black(Nine_1, Nine_1_p)
Do_Black(Nine_2, Nine_2_p)
Do_Black(Nine_3, Nine_3_p)
Do_Black(Nine_4, Nine_4_p)
Do_Black(Nine_5, Nine_5_p)

#---------------------------------------------------------
#---------------------------------------------------------
difference_images(arr_0, Null_1, Null_1_p, Null_2_p, Null_3_p, Null_4_p, Null_5_p)
difference_images(arr_1, One_1, One_1_p, One_2_p, One_3_p, One_4_p, One_5_p)
difference_images(arr_2, Two_1, Two_1_p, Two_2_p, Two_3_p, Two_4_p, Two_5_p)
difference_images(arr_3, Three_1, Three_1_p, Three_2_p, Three_3_p, Three_4_p, Three_5_p)
difference_images(arr_4, Four_1, Four_1_p, Four_2_p, Four_3_p, Four_4_p, Four_5_p)
difference_images(arr_5, Five_1, Five_1_p, Five_2_p, Five_3_p, Five_4_p, Five_5_p)
difference_images(arr_6, Six_1, Six_1_p, Six_2_p, Six_3_p, Six_4_p, Six_5_p)
difference_images(arr_7, Seven_1, Seven_1_p, Seven_2_p, Seven_3_p, Seven_4_p, Seven_5_p)
difference_images(arr_8, Eight_1, Eight_1_p, Eight_2_p, Eight_3_p, Eight_4_p, Eight_5_p)
difference_images(arr_9, Nine_1, Nine_1_p, Nine_2_p, Nine_3_p, Nine_4_p, Nine_5_p)

print("End learning.")

#---------------------------------------------------------
#---------------------------------------------------------

test_array(Test_arr, Test_img, Test_px)

#---------------------------------------------------------
#---------------------------------------------------------

Calc_number(Test_arr, arr_0, arr_1, arr_2, arr_3, arr_4, arr_5, arr_6, arr_7, arr_8, arr_9)

#---------------------------------------------------------
#---------------------------------------------------------

definition_num(Counter_0, Counter_1, Counter_2, Counter_3, Counter_4, Counter_5, Counter_6, Counter_7, Counter_8, Counter_9, Result)
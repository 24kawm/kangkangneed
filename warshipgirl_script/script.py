import cv2 as cv
import numpy as np
import aircv as ac
import subprocess
import sys
import time


def check_chuzheng():
    subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
    subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
    image_origin = cv.imread('./screenshot/screenshot.png')
    image_template = cv.imread('./target_img/start_fight.png')
    match_result = ac.find_template(image_origin, image_template, threshold=0.95)
    if match_result:
        return 1
    else:
        return 0


def check_home():
    subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
    subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
    image_origin = cv.imread('./screenshot/screenshot.png')
    image_template1 = cv.imread('./target_img/task.png')
    image_template2 = cv.imread('./target_img/home.png')
    #match_result1 = ac.find_template(image_origin, image_template1, threshold=0.95)
    #print(match_result1)
    match_result2 = ac.find_template(image_origin, image_template2, threshold=0.9)
    #if match_result1 and match_result2:
    if match_result2:
        print('已在主页')
        return 1
    else:
        print('不在主页，准备返回主页')
        return 0


def connect():
    ip_port = '127.0.0.1:7555'  # md，代码不会写，自己找连接端口自己改去
    orderlist = 'adb connect ' + ip_port
    state = subprocess.run(orderlist, shell=True)
    if state.returncode == 0:
        print('连接成功')
    else:
        print('连接失败')
        sys.exit(1)


def back_home():  # 在当前页面没有返回按钮且当前页面不是主页时，产生死循环;在老婆
    x = 0
    while x == 0:
        subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
        subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
        image_origin = cv.imread('./screenshot/screenshot.png')
        image_template1 = cv.imread('./target_img/back_button1.png')
        image_template2 = cv.imread('./target_img/back_button2.png')
        image_template3 = cv.imread('./target_img/everyday.png')
        match_result1 = ac.find_template(image_origin, image_template1, threshold=0.95)
        match_result2 = ac.find_template(image_origin, image_template2, threshold=0.95)
        match_result3 = ac.find_template(image_origin, image_template3, threshold=0.95)
        if match_result1 or match_result2 or match_result3:
            if match_result1:
                orderlist = 'adb shell input tap ' + str(int(match_result1['result'][0])) + ' ' + str(
                    int(match_result1['result'][1]))
                subprocess.run(orderlist, shell=True)
            elif match_result2:
                orderlist = 'adb shell input tap ' + str(int(match_result2['result'][0])) + ' ' + str(
                    int(match_result2['result'][1]))
                subprocess.run(orderlist, shell=True)
            elif match_result3:
                print('在每日登录处')
                orderlist = 'adb shell input tap 806 591'
                subprocess.run(orderlist, shell=True)
                time.sleep(1)
                orderlist = 'adb shell input tap 811 502'
                subprocess.run(orderlist, shell=True)
        else:

            if check_home():
                x = 1
            else:
                subprocess.run('adb shell input tap 58 55', shell=True)

        time.sleep(1)




def direct_decompose():             #提示船坞已满进行操作
    subprocess.run('adb shell input tap 600 500 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 120 300 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1450 270 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1340 580 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 600 500 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 50 50 ', shell=True)
    time.sleep(1)
    return 0

def direct_strengthen():         #提示船坞已满进行操作
    return 0

def decompose_from_home():
    while True:
        if not check_home():
            back_home()
        else:
            break
    subprocess.run('adb shell input tap 80 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 200 340 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 600 340 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 500 50 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 120 300 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1450 270 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1340 580 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 600 500 ', shell=True)
    time.sleep(1)
    back_home()


def special_dock():                  #提示船坞已满进行操作
    subprocess.run('adb shell input tap 600 500 ', shell=True)
    print('进入分解页面')
    time.sleep(2)
    back_home()

    time.sleep(2)
    subprocess.run('adb shell input tap 80 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 200 340 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 630 420 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1500 800 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 1500 270 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 1450 270 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(2)
    subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
    subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
    image_origin = cv.imread('./screenshot/screenshot.png')
    image_template = cv.imread('./target_img/special_dock_confirm.png')
    match_result = ac.find_template(image_origin, image_template, threshold=0.95)
    if match_result:
        subprocess.run('adb shell input tap 600 500 ', shell=True)
        time.sleep(1)
    else:
        subprocess.run('adb shell input tap 50 50 ', shell=True)
        time.sleep(1)
    subprocess.run('adb shell input tap 1500 460 ', shell=True)       #开始第二项任务
    time.sleep(1)
    subprocess.run('adb shell input tap 1450 270 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 1400 800 ', shell=True)
    time.sleep(1)
    subprocess.run('adb shell input tap 600 500 ', shell=True)
    time.sleep(1)
    back_home()

    return 0



def harvest():
    if check_home():
        subprocess.run('adb shell input tap 1480 800', shell=True)
        time.sleep(1)
    else:
        back_home()
        return 'error 返回主页'
    x = 0
    while x == 0:
        subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
        subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
        image_origin = cv.imread('./screenshot/screenshot.png')
        image_template = cv.imread('./target_img/harvest.png')
        match_result = ac.find_template(image_origin, image_template, threshold=0.95)
        if match_result:
            print('有待收获')
            orderlist = 'adb shell input tap ' + str(int(match_result['result'][0])) + ' ' + str(
                int(match_result['result'][1]))
            subprocess.run(orderlist, shell=True)
            time.sleep(1)
            subprocess.run('adb shell input tap 1265 413', shell=True)
            time.sleep(1)
            subprocess.run('adb shell input tap 618 562', shell=True)
        else:
            x = 1
        time.sleep(1)


def choose_map(des):
    if des == 2:
        subprocess.run('adb shell input tap 180 600 ', shell=True)
    elif des == 3:
        subprocess.run('adb shell input tap 160 700 ', shell=True)
    elif des == 4:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
    elif des == 5:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 180 600 ', shell=True)
    elif des == 6:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 180 700 ', shell=True)
    elif des == 7:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 180 800 ', shell=True)
    elif des == 8:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 180 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 160 600 ', shell=True)
    elif des == 9:
        subprocess.run('adb shell input tap 160 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 180 800 ', shell=True)
        time.sleep(0.5)
        subprocess.run('adb shell input tap 160 700 ', shell=True)
    time.sleep(0.5)


def choose_chapter(des):
    for i in range(des - 1):
        subprocess.run('adb shell input swipe 1380 400 600 400', shell=True)
        time.sleep(0.5)
    subprocess.run('adb shell input tap 1000 600 ', shell=True)
    time.sleep(1.5)


def choose_team(team):
    if team == 1:
        subprocess.run('adb shell input tap 180 140 ', shell=True)

    elif team == 2:
        subprocess.run('adb shell input tap 370 140 ', shell=True)

    elif team == 3:
        subprocess.run('adb shell input tap 580 140 ', shell=True)

    elif team == 4:
        subprocess.run('adb shell input tap 770 140 ', shell=True)
    time.sleep(0.5)


def fix():
    for i in range(6):
        subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
        subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
        image_origin = cv.imread('./screenshot/screenshot.png')
        image_template = cv.imread('./target_img/need_repair.png')
        match_result = ac.find_template(image_origin, image_template, threshold=0.95)
        if match_result:
            subprocess.run('adb shell input tap 700 700 ', shell=True)
            time.sleep(0.5)
            orderlist = 'adb shell input tap ' + str(int(match_result['result'][0])) + ' ' + str(
                int(match_result['result'][1]))
            subprocess.run(orderlist, shell=True)
            time.sleep(1)
        else:
            break


def assist():
    subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
    subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
    image_s1 = cv.imread('./screenshot/screenshot.png')
    s1 = np.array(image_s1)
    if [s1[130][1042][0], s1[130][1042][1], s1[130][1042][2]] == [253, 149, 39]:
        print('支援未开启')
        return 0
    elif [s1[130][1042][0], s1[130][1042][1], s1[130][1042][2]] == [58, 185, 243]:
        print('支援已开启')
        return 1
    elif [s1[130][1042][0], s1[130][1042][1], s1[130][1042][2]] == [146, 146, 146]:
        print('支援已用完')
        return 1


def prepare_fight(des=[9, 3], team=4, ):  # des->刷哪张图（目前只做了9图的，前面的图要用再加），team->用哪一队刷（1<=team<=4我懒得在代码里判断了）
    harvest()
    subprocess.run('adb shell input tap 300 45', shell=True)
    time.sleep(1)
    subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
    subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
    image_origin = cv.imread('./screenshot/screenshot.png')
    image_template = cv.imread('./target_img/' + str(des[0]) + '-' + str(des[1]) + '.png')
    match_result = ac.find_template(image_origin, image_template, threshold=0.95)
    print(match_result)
    if match_result:
        print('正在目标出征地图' + str(des[0]) + '-' + str(des[1]))
        subprocess.run('adb shell input tap 1000 600 ', shell=True)
        time.sleep(1.5)

    else:
        print('调整出征地图')
        for i in range(3):
            subprocess.run('adb shell input tap 200 170 ', shell=True)
            time.sleep(0.5)
        subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
        subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
        image_origin = cv.imread('./screenshot/screenshot.png')
        image_template = cv.imread('./target_img/1-1.png')
        match_result = ac.find_template(image_origin, image_template, threshold=0.95)
        if match_result:
            print('在图1-1')
        else:
            back_home()
            return 'error 从远征返回主页'

        choose_map(des[0])
        choose_chapter(des[1])

    choose_team(team)
    fix()
    if check_chuzheng():
        print('准备出征')
    else:
        print('不在出征页面，返回主页')
        back_home()
        return 'error 从出征返回主页'




def go_fight(depth=2, except_en=[], lineup=[4,4], night_fight=[0,0]):        #depth->刷几个点，repeat->刷多少次（-1表示刷到手动停止 ），except_en->出现什么敌人选择撤退（1：重巡，2：轻巡，3：潜艇），lineup->选择阵型
    if len(lineup) != depth:
        print('阵型与战斗次数不符')
        return 'error'
    if len(night_fight) != depth:
        print('夜战选择与战斗次数不符')
        return 'error'
    enemy_class_dict = {1:'zhongxun', 2:'qingxun', 3:'qianting'}
    lineup_dict = {1:'1200 200', 2:'1200 350', 3:'1200 500', 4:'1200 650', 5:'1200 800'}
    deep = 0
    while True:
        if assist():
            break
        else:
            subprocess.run('adb shell input tap 1060 145 ', shell=True)
            time.sleep(1)
            subprocess.run('adb shell input tap 1250 450 ', shell=True)
            time.sleep(1)
            subprocess.run('adb shell input tap 730 830 ', shell=True)
            time.sleep(1)

    while True:
        subprocess.run('adb shell input tap 1400 850 ', shell=True)                #准备页面点击出征按钮
        time.sleep(1)

        subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
        subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
        image_origin = cv.imread('./screenshot/screenshot.png')
        image_full = cv.imread('./target_img/full.png')
        match_full = ac.find_template(image_origin, image_full, threshold=0.95)
        if match_full:
            print('船舱已满')
            special_dock()
            decompose_from_home()
            prepare_fight()                    #手动输入参数，同主函数中的prepare_fight
        else:
            break

    while deep < depth:
        while True:
            subprocess.run('adb shell input tap 400 400 ', shell=True)
            time.sleep(0.5)
            subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
            subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
            image_origin = cv.imread('./screenshot/screenshot.png')
            image_template1 = cv.imread('./target_img/enemy.png')
            image_template2 = cv.imread('./target_img/choice.png')
            match_result1 = ac.find_template(image_origin, image_template1, threshold=0.95)
            match_result2 = ac.find_template(image_origin, image_template2, threshold=0.95)
            print(match_result1)
            if match_result1 or match_result2:
                break
        if match_result1:
            subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
            subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
            image_origin = cv.imread('./screenshot/screenshot.png')
            for temp in except_en:
                address = './target_img/' + enemy_class_dict[temp] + '.png'
                image_temp = cv.imread(address)
                match = ac.find_template(image_origin, image_temp, threshold=0.95)
                if match:
                    subprocess.run('adb shell input tap 1200 830 ', shell=True)
                    time.sleep(1)
                    subprocess.run('adb shell input tap 1000 400 ', shell=True)
                    return 'error 返回出征页面'
            subprocess.run('adb shell input tap 1400 830 ', shell=True)
        time.sleep(1)
        print('选择阵型')
        orderlist = 'adb shell input tap ' + lineup_dict[lineup[deep]]
        subprocess.run(orderlist, shell=True)
        while True:
            subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
            subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
            image_origin = cv.imread('./screenshot/screenshot.png')
            image_t1 = cv.imread('./target_img/night_fight.png')
            image_t2 = cv.imread('./target_img/over.png')
            match1 = ac.find_template(image_origin, image_t1, threshold=0.95)
            match2 = ac.find_template(image_origin, image_t2, threshold=0.95)
            if match1:
                if night_fight[deep]:
                    subprocess.run('adb shell input tap 550 580 ', shell=True)
                    time.sleep(1)
                else:
                    subprocess.run('adb shell input tap 1050 580 ', shell=True)
                    time.sleep(1)
            if match2:
                time.sleep(3)
                for i in range(3):
                    subprocess.run('adb shell input tap 820 350 ', shell=True)
                    time.sleep(0.5)
                break
        while True:
            subprocess.run('adb shell screencap -p /sdcard/screenshot.png', shell=True)
            subprocess.run('adb pull /sdcard/screenshot.png D:\\games\\warshipgirl_script\\screenshot', shell=True)
            image_origin = cv.imread('./screenshot/screenshot.png')
            image_s1 = cv.imread('./target_img/damage_seriously.png')       #旗舰大破
            image_s2 = cv.imread('./target_img/damage.png')                #队伍有大破
            image_s3 = cv.imread('./target_img/continue.png')
            match_s1 = ac.find_template(image_origin, image_s1, threshold=0.95)
            match_s2 = ac.find_template(image_origin, image_s2, threshold=0.95)
            match_s3 = ac.find_template(image_origin, image_s3, threshold=0.95)
            if match_s1:
                #图没截到，一般用不上，先不写
                return 'error 旗舰大破'
            if match_s2:
                subprocess.run('adb shell input tap 1000 580 ', shell=True)
                time.sleep(1)
                return 'error 有大破'
            if not match_s1 and not match_s2 and match_s3:
                if deep < depth-1:
                    deep = deep + 1
                    subprocess.run('adb shell input tap 550 580 ', shell=True)
                    time.sleep(1)
                    print('进下个点')
                    break
                if deep >= depth-1:
                    deep = deep + 1
                    subprocess.run('adb shell input tap 1000 580 ', shell=True)
                    time.sleep(1)
                    break
    subprocess.run('adb shell input tap 1200 580 ', shell=True)
    time.sleep(1)
    if check_chuzheng():
        return 0
    else:
        return 1

def repeat_fight(repeat=2):          #repeat->重复战斗次数，-1表示手动停止
    times = 0
    count = 0
    while True:
        go_fight()
        count = count + 1
        print('已成功' + str(count) + '次')
        if repeat != -1:
            times = times + 1
            if times >= repeat:
                break


if __name__ == '__main__':
    connect()
    back_home()
    prepare_fight()
    repeat_fight(-1)

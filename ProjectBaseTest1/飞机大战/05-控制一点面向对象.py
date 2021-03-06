#coding=utf-8
import pygame
from pygame.locals import *
import time

"""玩家飞机类"""
class HearPlan(object):
    def __init__(self,screen_temp):
        self.hero_x=210
        self.hero_y=720
        self.image=pygame.image.load("./feiji/hero1.png")
        self.screen=screen_temp
    def display(self):
        self.screen.blit(self.image,(self.hero_x,self.hero_y))
    def move_left(self):
        self.hero_x-=5
    def move_right(self):
        self.hero_x+=5

"""键盘事件"""
def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():
            
        #判断是否点击了退出按钮
        if event.type==QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')

'''
    1.搭建界面，主要完成窗口和背景图片
'''
def main():

    #1.创建一个窗口，用来显示内容
    screen=pygame.display.set_mode((480,852),0,32)

    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机图图片
    hero=HearPlan(screen)
    
    hero_x=210
    hero_y=700

    #图片放到窗口中显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        hero.display()
        
        key_control(hero)
       
        #更新需要显示的内容
        pygame.display.update()

        time.sleep(0.1)


if __name__ == '__main__':
    main()
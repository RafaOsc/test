import pygame
import random
game_over = False
run = True
exit_window = False
again = False
text = ""
screen =  pygame.display.set_mode((500, 500))
width,height = pygame.display.get_window_size()
Font = pygame.font.init()
Font = pygame.font.Font('freesansbold.ttf',20)
words_toplay =["literally","regardless","whom","nonplussed"]
pygame.init()
pygame.display.set_caption("Hangman ")
def main(words):
    global game_over,run,exit_window,screen,Font,txt
    bad = []
    correct = []
    hidden_word = words[random.randint(0,len(words)-1)]
    attempt = 5
    w = width-10
    w = int (w/(len(hidden_word)))
    h = int( height/1.3)
    length = len(hidden_word)
    init = 10
    incorrect = (width-10)/5
    for n in range (len(hidden_word)):
        pygame.draw.line(screen, (255,255,255), (init ,h), (w*(n+1),h))
        init+=w
    init = 10
    
    text=Font.render('Attempt: '+str(attempt), False, (255,255,255),False)  
    screen.blit(text, (0,30))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   exit_window = True
                   run = False
                   break
            elif(event.type == pygame.TEXTINPUT):
                    if('a' <=event.text.lower()<= 'z' ):
                        char = event.text.lower()
                        if(char in hidden_word):
                            for n in range(len(hidden_word)):
                                if(hidden_word[n]==char):
                                   text=Font.render(char.upper(), False, (255,255,255),False)  
                                   textRect = text.get_rect()
                                   textRect.center=(int(((n+1)*w)-(w/2)+5),h-10)
                                   screen.blit(text, textRect)
                                   if(correct.count(char)!=hidden_word.count(char)):
                                       correct.append(char)
                                       length-=1
                                   if(length == 0):
                                       txt = " Winner "
                                       run = False
                                       game_over = True
                                       break
                        else:
                            if(bad.count(char) == 0):
                                attempt -=1
                                bad.append(char)
                                text=Font.render('Attempt: '+str(attempt), False, (255,255,255),False)
                                screen.blit(text, (0,30))
                                text=Font.render(char.upper(), False, (255,0,0),False)
                                textRect = text.get_rect()
                                textRect.center=((init+(incorrect*(5-attempt)-init)/2 ),height-height/8)
                                screen.blit(text, textRect)
                                init+=incorrect
                           
        if(attempt ==4):
            pygame.draw.line(screen, (255,255,255), (width-width/4,height-height/3), (width-width/2,height-height/3))
            pygame.draw.line(screen, (255,255,255), (width-width/2.7,height-height/3), (width-width/2.7,height-height/1.2))
            pygame.draw.line(screen, (255,255,255), (width-width/2.7,height-height/1.2), (width-width/1.8,height-height/1.4))
        elif(attempt ==3):
            pygame.draw.circle(screen,(255,255,255),(width-width/1.8,height-height/1.4-30),30,2);
        elif(attempt ==2):
            pygame.draw.line(screen, (255,255,255), (width-width/1.8,height-height/1.4), (width-width/1.8,height-height/2))
        elif(attempt ==1):
            pygame.draw.line(screen, (255,255,255), (width-width/1.8,height-height/1.4), (width-width/2.2,height-height/2))
            pygame.draw.line(screen, (255,255,255), (width-width/1.8,height-height/1.4), (width-width/1.6,height-height/2))
     
        if(attempt == 0):
            pygame.draw.line(screen, (255,255,255), (width-width/1.8,height-height/2), (width-width/2.2,height-height/2.8))
            pygame.draw.line(screen, (255,255,255), (width-width/1.8,height-height/2), (width-width/1.6,height-height/2.8))
            game_over = True
            txt = "Game Over"
            break
        pygame.display.update()
    if(exit_window==True):
        pygame.quit() 
if __name__ == '__main__': 
    main(words_toplay)
    while game_over:
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(width/4, height/4,width/2, height/4),2)
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(width/4+2, height/4+2,width/2-4, height/4-4))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(width/4+width/3,height/4+2+height/4-4-(height/4-4)/4,width/8,height/20))
        Font_1 = pygame.font.Font('freesansbold.ttf',30)
        text=Font_1.render(txt, False, (255,0,0),False)  
        screen.blit(text, (width/4+2+40,height/4+2+30))
        text=Font.render('Again',False , (255,255,255),(255,0,0))  
        screen.blit(text, (width/4+width/3+2,height/4+2+height/4-4-(height/4-4)/4+5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                again = False
                game_over = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if( game_over == True and width/4+width/3<=x<=width/4+width/3+width/8 and height/4+2+height/4-4-(height/4-4)/4<=y<=height/4+2+height/4-4-(height/4-4)/4+height/20):
                    screen.fill((0, 0, 0))
                    again = True
                    run = True
                    game_over = False
                    pygame.display.update()
                    main(words_toplay)
        if(pygame.display.get_init()):
            pygame.display.update()
    if(again==False):
        pygame.quit()
       
           
            
       
        
         


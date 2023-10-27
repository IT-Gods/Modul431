import pygame
import sys, os
ENEMIES1 = [pygame.image.load(os.path.join("DesignElements/Enemy1_T1.png")),pygame.image.load(os.path.join("DesignElements/Enemy2_T1.png")),pygame.image.load(os.path.join("DesignElements/Enemy3_T1.png")),pygame.image.load(os.path.join("DesignElements/Enemy4_T1.png"))]
ENEMIES2 = [pygame.image.load(os.path.join("DesignElements/Enemy1_T2.png")),pygame.image.load(os.path.join("DesignElements/Enemy2_T2.png")),pygame.image.load(os.path.join("DesignElements/Enemy3_T2.png")),pygame.image.load(os.path.join("DesignElements/Enemy4_T2.png"))]
ENEMIES3 = [pygame.image.load(os.path.join("DesignElements/Enemy1_T3.png")),pygame.image.load(os.path.join("DesignElements/Enemy2_T3.png")),pygame.image.load(os.path.join("DesignElements/Enemy3_T3.png")),pygame.image.load(os.path.join("DesignElements/Enemy4_T3.png"))]
THEME1 = [pygame.image.load(os.path.join("DesignElements/StarshipsWereMeantToFly_T1.png")),ENEMIES1,pygame.image.load(os.path.join("DesignElements/BulletSprite.png")),pygame.image.load(os.path.join("DesignElements/Heart.png"))]
THEME2 = [pygame.image.load(os.path.join("DesignElements/StarshipsWereMeantToFly_T2.png")),ENEMIES2,pygame.image.load(os.path.join("DesignElements/BulletSprite.png")),pygame.image.load(os.path.join("DesignElements/Heart.png"))]
THEME3 = [pygame.image.load(os.path.join("DesignElements/StarshipsWereMeantToFly_T3.png")),ENEMIES3,pygame.image.load(os.path.join("DesignElements/BulletSprite.png")),pygame.image.load(os.path.join("DesignElements/Heart.png"))]

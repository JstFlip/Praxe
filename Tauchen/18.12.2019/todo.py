#TODO: Boundy                                                                                #
#   SOLUTION: Velikost okna                                                                  #
#   (Předešlý nápad)Kontrola bude prováděna jednou za cykl pro všechny quady                 #
#   (Nový nápad)Kontrola bude prováděna jednou za cykl a bude prováděna na seřazených polích #
###########################HOTOVO#############################################################
#                                                                                       #
#TODO: Pohyb kostek                                                                     #
#   Pohyb souřadnic quadu pomocí jejich směrové vektoru                                 #
#   quad.x+=quad.smer[0]                                                                #
#   quad.y+=quad.smer[1]                                                                #
#                                                                                       #
###########################HOTOVO########################################################
#                                                                                       #
#TODO: Seřadit quady podle pozice do polí pro lepší optimalizaci                        #
#   SOLUTION:dictionary comprehension                                                   #
###########################HOTOVO#########################################################
#
#TODO: Kontrola kolizí
#
#
#TODO: Reakce na kolizi
#   Při kolizi rychlejší quad (quad_1) předá svůj směrový vektor pomalejšímu quadu (quad_2) a směrový vektor předešle rychlejšího quad (quad_1) bude roven jejich prvotního rozdílu
#   def colide(quad_1,quad_2):
#       if quad_1.velocity>quad_2.velocity:
#           temp=quad_1-quad_2 (-> udělat __sub__ <-)
#           quad_2.vector=quad_1.vector
#           quad_1.vector=temp
#       else:
#           colide(quad_2,quad_1)
#
#TODO if 7,8,9: Screenshot obrazovky
#   Najít nějakou knihovnu
#
#TODO if 7,8,9: Nastavení alphy pro OpenGL
#   Najít nějakou dobrou dokumentaci
#
#TODO if 7,8,9: Nastavení screenshotu obrazovky jako texturu a dát jí jako pozadí pro OpenGL
#   Najít nějakou Hodně Dobrou dokumentaci
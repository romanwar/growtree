import random as rd
import pprint
from PIL import Image

print("grow tree")
#print(round(rd.random()*100, 0))

########        Глобальные переменные
waterfall = 0 #кол-во литров воды которым полито дерево. Должно суммироваться с осадками и подземной водой


########        Словари
trees_dict = {
'акация':'acacia',
'баобаб':'baobab',
'берёза':'birch',
'бук':'beech',
'вяз':'elm',
'грецкий орех':'walnut',
'груша':'pear tree',
'дуб':'oak',
'ель':'spruce',
'ива':'willow',
'инжир':'fig',
'каштан':'chestnut',
'кедр':'cedar',
'кипарис':'cypress',
'клён':'maple',
'лавр':'bay',
'липа':'linden',
'лиственница':'larch',
'олива':'olive',
'мирт':'myrtle',
'можжевельник':'juniper',
'ольха':'alder',
'орешник':'hazel',
'осина':'aspen',
'пальма':'palm',
'пихта':'fir',
'платан':'plane',
'рябина':'mountain ash',
'секвойя':'sequoia',
'сирень':'lilac',
'слива':'plum tree',
'сосна':'pine',
'тис':'yew tree',
'тополь':'poplar',
'эвкалипт':'eucalyptu',
'яблоня':'apple tree',
'ясень':'ash'

}


#http://les.novosibdom.ru/node/442

trees_description = {
'ясень':
'Ясень (Fraxinus) — род листопадных растений семейства маслиновых (Oleaceae), который насчитывает около 70 видов, распространенных в основном в умеренном поясе Северного полушария, реже в субтропических и тропических зонах.',
'яблоня':'Яблоня (Malus) — род листопадных деревьев и кустарников семейства Розовые  — дерево с древесиной твёрдой, сильно усыхающей, хотя высушить её непросто. Изделия из хорошо высушенной древесины никогда не трескаются и не коробятся. При благоприятных условиях дикая яблоня может прожить до 200 лет, образуя ствол диаметром до 40 см.'

'''Растёт ясень одиночно или группами в смешанных лесах, часто вместе с дубом и другими лиственными породами, реже с хвойными. Иногда преобладает
в породном составе, образуя ясеневые леса. Высота дерева до 30 — 50 м, диаметр ствола до 1,5 м. Крона удлиненно-яйцевидная, с возрастом высокоподнятая, широко-округлая с изогнутыми молодыми ветвями.
Кора у молодых деревьев зеленоватая или светло-коричневая, с возрастом становится серой или коричневой с четкими неглубокими трещинами.
Норвежские мифы описывают ясень как могучее дерево, поддерживающее небеса, а под землей его корни доходят до ада. Ясень принадлежит семейству маслиновых, 
хотя его плод представляет собой похожее на дротик летающее семя. Ясень широко используется в изготовлении ёмкостей для пищи, поскольку древесина не имеет вкуса. 
Адмирал Ричард Берд во время своих полярных экспедиций носил снегоступы, изготовленные из ясеня. Первые ветряные мельницы строились с применением этой породы дерева.'''

}







class Tree():
    def __init__(self, name):
        self.height = 0
        self.age = 0
        self.name = name
    def info (self):
        return f'{self.height}, {self.age}, {self.name}'
    def grow(self):
        self.age +=1
        self.height = 2**self.age
    def getTreeList(self):
        for key in trees_dict:
            print(key)
     

def get_picture(tree_name):
    im = Image.open(f'H:\\python\\growtree\\img_tree\\{tree_name}.jpg')
    im.show()


     
class UserActions():
    
    def __init__(self):
        self.action = action
    def waterThePlant():
        global waterfall
        print('Сколько литров воды нужно использовать?')
        waterThePlantUser = int(input())
        waterfall = waterfall + waterThePlantUser
    def UserActionsInfo():
        print('Вы полили дерево на: ', str(waterfall), ' литров')



print('Какое дерево мы будем выращивать сегодня? Введите название или выберите из списка') #список добавить либо щелчок по дереву            
treeUser = input().lower()

try:
    print(trees_dict[treeUser])
    print(trees_description[treeUser])
    get_picture(trees_dict[treeUser])
    tree = Tree(trees_dict[treeUser])
    UserActions.waterThePlant()
    UserActions.UserActionsInfo()
    tree.grow()
    print(tree.info())
except KeyError as ke:
    print('Дерево не найдено в списке: ', ke)






#класс погоды + осадки
#класс достаточность подземной воды
#класс достаточность света
#класс тип дерева
#рандомные катаклизым (в том числе техногенные)
#добавить действий пользователя с возможностью накопления эффекта
#добавить стадии ростков
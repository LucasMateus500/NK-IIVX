from kivy.lang import Builder
from kivymd.app import MDApp
from samila import GenerativeImage
import random
import math
from samila import Projection
from kivymd.uix.menu import MDDropdownMenu
import webbrowser
from kivymd.uix.snackbar import BaseSnackbar
import time
import glitchart


import threading





c1='black'
c2='white'





class M1(MDApp):

	def build(self):
		self.theme_cls.material_style = "M3"
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"


		return Builder.load_string(
		'''
#:import Snackbar kivymd.uix.snackbar.Snackbar


<Check@MDCheckbox>:
	group:'group'
	size_hint:None,None
	size:dp(48),dp(48)

<Check1@MDCheckbox>:
	group:'group1'
	size_hint:None,None
	size:dp(48),dp(48)

<Checkeffect@MDCheckbox>:
	group:'group2'
	size_hint:None,None
	size:dp(48),dp(48)


MDScreen:
	MDBottomNavigation:
		#panel_color:"#eeeaea"
		selected_color_background:"grey"
		text_color_active:"lightgrey"

		MDBottomNavigationItem:
			name:'screen 1'
			text: 'NFT'
			icon: 'git'



			Image:
				source:'images/7.png'
				size_hint: .3 , .3
				pos_hint:{"center_x": .5,"center_y": .7}

			MDLabel:
				text:''
				halign: 'center'
				color:'gray'
				pos_hint:{"center_x": .5 , "center_y": .1}



			MDTextField:
				id : Text1
				size_hint_x : .5
				pos_hint:{"center_x": .5, "center_y": .4}
				hint_text:"NFT Name"
				icon_left: "key-variant"
				text_color_focus:"gray"
				line_color_focus:"gray"
				hint_text_color_focus: "gray"
				icon_left_color_focus:"gray"



			MDRoundFlatButton:
				id: tk
				text:"NFT_TK1"
				text_color:"gray"
				line_color:"gray"
				pos_hint:{"center_x": .3 , "center_y": .2}
				on_press : app.nftimage2()
				on_release: Snackbar(text="teste").open()

			MDRoundFlatButton:
				id: tk2
				text:"NFT_TK2"
				text_color: "gray"
				line_color:"gray"
				pos_hint:{"center_x": .5,  "center_y": .2}
				on_release: app.nftimage3()

			MDRoundFlatButton:
				id : tk3
				text: "NFT_TK3"
				text_color:'gray'
				line_color:"gray"
				pos_hint:{"center_x": .7 , "center_y": .2}
				on_press: app.nftimage4()



		MDBottomNavigationItem:
			name: 'screen 2'
			text:'OPENSEA'
			text_color:"gray"
			icon: 'git'

			Image:
				source:'images/opensea1.png'
				size_hint: .1 , .1
				pos_hint:{"center_x": .5,"center_y": .7}

			MDLabel:
				text:'OPENSEA'
				halign: 'center'
				color:'gray'
				pos_hint:{"center_x": .5 , "center_y": .6}

			MDTextButton:
				text:"htts://opensea.io"
				color: "gray"
				pos_hint: {"center_x": .5, "center_y": .55}
				on_press: app.opensea()


			Image:
				source:'images/mtmask1.png'
				size_hint: .1 , .1
				pos_hint:{"center_x": .5 , "center_y": .4}
			MDLabel:
				text:'METAMASK'
				halign: 'center'
				color: 'gray'
				pos_hint:{"center_x": .5 , "center_y": .3}

			MDTextButton:
				text:"https://metamask.io"
				color: "gray"
				pos_hint: {"center_x": .5, "center_y": .25}
				on_press: app.metamask()

		MDBottomNavigationItem:
			name: 'screen 3'
			text:'TKN'
			icon: 'git'



			Image:
				source:'images/th.png'
				pos_hint:{"center_x": .5  , "center_y":  .6}
				size_hint: .11, .11




			MDLabel:
				text:"NATRON"
				pos_hint:{"center_x": .5 ,"center_y": .5}
				halign:"center"
				color:"gray"

			MDTextButton:
				text:"https://natrongithub.github.io/"
				color: "gray"
				pos_hint: {"center_x": .5 ,"center_y": .45}
				on_press :  app.natron()

			MDTextButton:
				text:"https://youtube.com/watch?v=H73v27O2Tb8"
				color: "gray"
				pos_hint: {"center_x": .5 ,"center_y": .4}
				on_press :  app.natronGlitch()


			MDLabel:
				id:3l1
				text:"PORTIFOLIO"
				pos_hint:{"center_x": .5 ,"center_y": .25}
				halign:"center"
				color:"gray"

			MDTextButton:
				text:"https://razaugun500.github.io/LucasMateus.github.io/"
				color: "gray"
				pos_hint: {"center_x": .5 ,"center_y": .2}
				on_press: app.portifolio()









		MDBottomNavigationItem:
			name:'screen 4'
			text: 'CONFIG'
			icon: 'git'

			MDLabel:
				text:"COLOR:"
				halign:"center"
				pos_hint:{"center_x": .15 , "center_y": .9}
				color:"gray"
			MDLabel:
				text:"BACKGROUND:"
				halign:"center"
				pos_hint:{"center_x": .55 , "center_y": .9}
				color:"gray"

			MDLabel:
				text:"EFFECT:"
				halign:"center"
				pos_hint:{"center_x": .85,"center_y": .9}
				color:"gray"



			MDLabel:
				text: "BLACK"
				halign:"center"
				pos_hint: {"center_x": .15 , "center_y": .8}
				color:"gray"


			Check:
				id: t1
				active:True
				pos_hint:{'center_x': .2,'center_y': .8}

			MDLabel:
				text:"RED"
				halign:"center"
				pos_hint:{"center_x": .15 , "center_y": .7}
				color:"gray"

			Check:
				id: t2
				pos_hint:{'center_x': .2,'center_y': .7}

			MDLabel:
				text:"BLUE"
				halign:"center"
				pos_hint:{"center_x": .15 , "center_y": .6}
				color:"gray"

			Check:
				id: t3
				pos_hint:{'center_x': .2,'center_y': .6}

			MDLabel:
				text:"YELLOW"
				halign:"center"
				pos_hint:{"center_x": .14 , "center_y": .5}
				color:"gray"
			Check:
				id: t4
				pos_hint:{'center_x': .2,'center_y': .5}
			MDLabel:
				text:"ORANGE"
				halign:"center"
				pos_hint:{"center_x": .14 , "center_y": .4}
				color:"gray"
			Check:
				id: t5
				pos_hint:{'center_x': .2,'center_y': .4}

			MDLabel:
				text:"GREEN"
				halign:"center"
				pos_hint:{"center_x": .15 , "center_y": .3}
				color:"gray"
			Check:
				id: t6
				pos_hint:{'center_x': .2,'center_y': .3}
			MDLabel:
				text:'WHITE'
				halign:"center"
				pos_hint:{"center_x": .15 ,"center_y": .2}
				color:'gray'
			Check:
				id:t7
				pos_hint:{"center_x": .2, "center_y": .2}

			MDLabel:
				text:'WHITE'
				halign:"center"
				pos_hint:{"center_x": .5 ,"center_y": .8}
				color:'gray'
			Check1:
				id:c2t1
				active: True
				pos_hint:{"center_x": .55, "center_y": .8}
			MDLabel:
				text:'BLACK'
				halign:"center"
				pos_hint:{"center_x": .5 ,"center_y": .7}
				color:'gray'
			Check1:
				id:c2t2
				pos_hint:{"center_x": .55, "center_y": .7}

			MDLabel:
				text:'TRANSPARENT'
				halign:"center"
				pos_hint:{"center_x": .5, "center_y": .6}
				color:'gray'
			Check1:
				id:c2t3
				pos_hint:{"center_x": .55,"center_y": .6}



			MDLabel:
				text:"EFFECT:"
				halign:"center"
				pos_hint:{"center_x": .85,"center_y": .9}
				color:"gray"


			MDLabel:
				text:'EFFECT 1'
				halign:"center"
				pos_hint:{"center_x": .81,"center_y": .8}
				color:"gray"

			Checkeffect:
				id: ef1
				active:False
				pos_hint:{'center_x': .87,'center_y': .8}


'''
)






	def portifolio(self):
		webbrowser.open("https://razaugun500.github.io/LucasMateus.github.io/")
		
	def natron(self):
		webbrowser.open("https://natrongithub.github.io/")

	def natronGlitch(self):
		webbrowser.open("https://www.youtube.com/watch?v=H73v27O2Tb8")


	def opensea(self):
		webbrowser.open("https://opensea.io")

	def metamask(self):
		webbrowser.open("https://metamask.io")



	def  nftimage2(self):



		if self.root.ids.Text1.text == "":
			a15 = "nft2475693229049.png"

		else:
			a15 = self.root.ids.Text1.text + ".png"


		def n1(x,y):
			resultado =  random.uniform(-1,1)* x**2 - math.sin(y**2)+ abs(y-x)
			return resultado

		def n2 (x,y):
			resultado = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
			return resultado


		if self.root.ids.t1.active == True:
			c1 ='black'
		if self.root.ids.t2.active == True:
			c1 ='red'
		if self.root.ids.t3.active == True:
			c1 ='blue'
		if self.root.ids.t4.active == True:
			c1 ='yellow'
		if self.root.ids.t5.active == True:
			c1 ='orange'
		if self.root.ids.t6.active == True:
			c1 ='green'
		if self.root.ids.t7.active == True:
			c1 = 'white'
		if self.root.ids.c2t1.active == True:
			c2 = 'white'
		if self.root.ids.c2t2.active == True:
			c2 = 'black'
		if self.root.ids.c2t3.active == True:
			c2 = 'transparent'

		def tk15():
			I2 = GenerativeImage(n1,n2)
			I2.generate()
			I2.plot(color=c1, bgcolor=c2)
			I2.save_image(file_adr=a15)

			if self.root.ids.ef1.active == True:
				i = self.root.ids.Text1.text + '.png'
				glitchart.png(i, max_amount=3, inplace=True)
			if self.root.ids.ef1.active == False:
				pass

		tk2 = threading.Thread(target = tk15)
		tk2.start()

		


	def nftimage3(self):


		if self.root.ids.Text1.text == "":
			a1 = "nft9843985387.png"
		else:
			a1 = self.root.ids.Text1.text + ".png"

		def n1(x,y):
			resultado =  random.uniform(-1,1)* x**2 - math.sin(y**2)+ abs(y-x)
			return resultado

		def n2 (x,y):
			resultado = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
			return resultado

		if self.root.ids.t1.active == True:
			c1 ='black'
		if self.root.ids.t2.active == True:
			c1 ='red'
		if self.root.ids.t3.active == True:
			c1 ='blue'
		if self.root.ids.t4.active == True:
			c1 ='yellow'
		if self.root.ids.t5.active == True:
			c1 ='orange'
		if self.root.ids.t6.active == True:
			c1 ='green'
		if self.root.ids.t7.active == True:
			c1 = 'white'
		if self.root.ids.c2t1.active == True:
			c2 = 'white'
		if self.root.ids.c2t2.active == True:
			c2 = 'black'
		if self.root.ids.c2t3.active == True:
			c2 = 'transparent'

		def tk153():
			I3 = GenerativeImage(n1, n2)
			I3.generate()
			I3.plot(color =c1, bgcolor=c2, projection=Projection.POLAR)
			I3.save_image(file_adr=a1)

			if self.root.ids.ef1.active == True:
				i = self.root.ids.Text1.text + '.png'
				glitchart.png(i, max_amount=3, inplace=True)
			if self.root.ids.ef1.active == False:
				pass


		tk3 = threading.Thread(target = tk153)
		tk3.start()



	def nftimage4(self):
		if self.root.ids.Text1.text == "":
			a55 = "nft9204948580668.png"

		else:
			a55 = self.root.ids.Text1.text + ".png"

		def n1(x,y):
			resultado = random.uniform(-1,1)* x**2 - math.sin(y**2)+abs(y-x)
			return resultado
		def n2(x,y):
			resultado = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
			return resultado

		if self.root.ids.t1.active == True:
			c1 ='black'
		if self.root.ids.t2.active == True:
			c1 ='red'
		if self.root.ids.t3.active == True:
			c1 ='blue'
		if self.root.ids.t4.active == True:
			c1 ='yellow'
		if self.root.ids.t5.active == True:
			c1 ='orange'
		if self.root.ids.t6.active == True:
			c1 ='green'
		if self.root.ids.t7.active == True:
			c1 = 'white'
		if self.root.ids.c2t1.active == True:
			c2 = 'white'
		if self.root.ids.c2t2.active == True:
			c2 = 'black'
		if self.root.ids.c2t3.active == True:
			c2 = 'transparent'

		def tk154():
			I4 = GenerativeImage(n1,n2)
			I4.generate()
			I4.plot(color=c1 , bgcolor=c2, projection=Projection.LAMBERT)
			I4.save_image(file_adr=a55)

			if self.root.ids.ef1.active == True:
				i = self.root.ids.Text1.text + '.png'
				glitchart.png(i, max_amount=3, inplace=True)
			if self.root.ids.ef1.active == False:
				pass

		tk4 = threading.Thread(target = tk154)
		tk4.start()



if __name__ == "__main__":
       M1 = M1()


threading.Thread(target=M1.run())

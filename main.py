import pygame #importing pygame library
pygame.init() #initializing pygame


user_input=input("Do you need instructions ") #getting user input for instruction
ghost_image=""
background_image=""
if(user_input=="Yes")or(user_input=="YES")or(user_input=="yes")or(user_input=="y")or(user_input=="Y"):#if the user wants instruction
	ghost_image=input("Enter the file name of the ghost image ") #prompting for ghost image
	background_image=input("Enter the file name of the background image ")#prompting for background image
	ghost_image=pygame.image.load(ghost_image) #loading image
	background_image=pygame.image.load(background_image) #loading image
	(w,h)=background_image.get_rect().size #getting the background width and length
	screen=pygame.display.set_mode((w,h)) #setting up display
	screen.blit(background_image,(0,0)) #displaying image
	pygame.display.update() #updating display
	x_ghost=int(input("Enter the x co-ordiante where you want to place the ghost "))#getting the coordinate for ghost
	y_ghost=int(input("Enter the y co-ordinate where you want to place the ghost "))
	while(x_ghost<0)or(x_ghost>w):#checking to see if the coordiante is valid
		x_ghost=int(input("Enter valid x co-ordinate to place the ghost "))
	while(y_ghost<0)or(y_ghost>h):#checking if the coordinate is valid
		y_ghost=int(input("Enter valid y co-ordinate to place the ghost "))
	(w,h)=ghost_image.get_rect().size#getting the size of ghost image
	x_pixel=0
	y_pixel=0
	while(x_pixel != w) and (y_pixel !=h):#loop to run through all the pixel in the picture
		(r,g,b,rand)=ghost_image.get_at((x_pixel,y_pixel))
		(r_back,g_back,b_back,rand)=background_image.get_at((x_pixel,y_pixel))
		if(g!=255):#checking to see if the pixel is green or not
			red=(r+r_back)//2#getting the average of the pixel
			green=(g+g_back)//2
			blue=(b+b_back)//2
			screen.set_at((x_pixel+x_ghost,y_pixel+y_ghost),(red,green,blue))#setting the screen with the averaged pixel
		x_pixel=x_pixel+1
		if(x_pixel==w)and(y_pixel!=h):#count loop to go through all the pixel
			x_pixel=0
			y_pixel=y_pixel+1

	pygame.display.update()
elif (user_input=="NO")or(user_input=="no")or(user_input=="n")or(user_input=="N"):
	ghost_image=(input(""))
	background_image=(input(""))
	while(ghost_image=="")or(background_image==""):
		print ("Please enter the file name of ghost and background picture respectively")
		ghost_image=(input(""))
		background_image=(input(""))
	ghost_image=pygame.image.load(ghost_image) #loading image
	background_image=pygame.image.load(background_image) #loading image
	(w,h)=background_image.get_rect().size #getting the background width and length
	screen=pygame.display.set_mode((w,h)) #setting up display
	screen.blit(background_image,(0,0)) #displaying image
	pygame.display.update() #updating display
	x_ghost=int(input("Enter the x co-ordiante where you want to place the ghost "))#getting the coordinate for ghost
	y_ghost=int(input("Enter the y co-ordinate where you want to place the ghost "))
	while(x_ghost<0)or(x_ghost>w):#checking to see if the coordiante is valid
		x_ghost=int(input("Enter valid x co-ordinate to place the ghost "))
	while(y_ghost<0)or(y_ghost>h):#checking if the coordinate is valid
		y_ghost=int(input("Enter valid y co-ordinate to place the ghost "))
	(w,h)=ghost_image.get_rect().size#getting the size of ghost image
	x_pixel=0
	y_pixel=0
	while(x_pixel != w) and (y_pixel !=h):#loop to run through all the pixel in the picture
		(r,g,b,rand)=ghost_image.get_at((x_pixel,y_pixel))
		(r_back,g_back,b_back,rand)=background_image.get_at((x_pixel,y_pixel))
		if(g!=255):#checking to see if the pixel is green or not
			red=(r+r_back)//2#getting the average of the pixel
			green=(g+g_back)//2
			blue=(b+b_back)//2
			screen.set_at((x_pixel+x_ghost,y_pixel+y_ghost),(red,green,blue))#setting the screen with the averaged pixel
		x_pixel=x_pixel+1
		if(x_pixel==w)and(y_pixel!=h):#count loop to go through all the pixel
			x_pixel=0
			y_pixel=y_pixel+1

	pygame.display.update()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()


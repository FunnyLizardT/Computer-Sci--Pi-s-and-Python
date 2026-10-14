def main():
	from gpiozero import RotaryEncoder, PWMLED
	

	rotor = RotaryEncoder(18, 17, wrap=True, max_steps=180) # DT goes to 16, CLK goes to 20
	led = PWMLED(23)


	LCheck = rotor.steps #start of rotor steps (0)
	RCheck = 0

	
	print(rotor.steps)

	while True:
		x = rotor.steps 
		LCheck = rotor.steps  #updating rotor steps, 0,1,2 ect....
		#lamd function define with in line and use that to call back something else

		Brightness = ((x/180)**2 )   # B = x/180 does not work because of negative numbers
		led.value = Brightness

		if LCheck != RCheck: 
			print(rotor.steps) # the value of rotor.steps will change as you rotate the device
			RCheck = rotor.steps
#MAKE SURE TOO MAKE IT DETECT LIKE IF IT MOVES YK

#end=" "  to keep in one line or  end = "/" for new like





main()
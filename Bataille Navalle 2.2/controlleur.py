from view import *

placementTousBatO()

# terrain1.bind("<Enter>",souris)
# terrain2.bind("<Enter>",souris)
terrain1.bind("<Button-3>",orientation)
terrain1.bind("<Button-1>",placement)
terrain2.bind("<Button-1>",attaquer)


root.mainloop()
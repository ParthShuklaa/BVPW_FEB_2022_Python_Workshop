
import tkinter
top = tkinter.Tk()
top.title("3 Step to Master GUI iin Python ...")
C = tkinter.Canvas(top,bg="Yellow",height=250,width=300)
coord = 10,50,250,220
arc = C.create_arc(coord,start =0,extent =150,fill ="black")

points = [150, 100, 200, 120, 240, 180,
                  210, 200, 150, 150, 100, 200]
poly = C.create_polygon(points,outline="blue", fill= "orange", width=2)
rect = C.create_rectangle(230,10,290,60, outline="black" , fill="red", width=2)
C.pack()
top.mainloop()

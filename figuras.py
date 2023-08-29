print("Figuras disponibles:\n","1.Círculo\n 2.Triángulo\n 3.Cuadrado")
fig=input("Seleccione una figura:")
A="Inválido" ; figura= fig
if(fig=="Círculo") or (fig=="1"):
  r=eval(input("ingrese el valor del radio:"))
  A=3.1416*r**2
elif(fig=="Trángulo") or (fig=="2"):
  b=eval(input("ingrese la base:"))
  h=eval(input("ingrese la altura:"))
  A=(b*h)/2
elif(fig=="Cuadrado") or (fig=="3"):
  b=eval(input("ingrese la base:"))
  h=eval(input("ingrese la altura:"))
  A=(b*h)
else:
  print("Seleccione una figura válida")
print("Para un", figura," el valor del área es",A)
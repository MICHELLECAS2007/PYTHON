print("---------------")
print("programa que calcula el salario")
print("---------------")

#inputs
print("digite el salario del empleado:")
salario=float(input())

#process
aumento=(salario*15)/100
salarionuevo=(salario+aumento)

#ouputs
if(salario<1000):
    print("su salario nuevo es:",salarionuevo)
    
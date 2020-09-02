#How would yo express the following operations? 

#El número es mútiplo de 4 y también es negativo 
numero%4==0 and número<0

"""
Decidiste comprar un auto usado, pero debe cumplir con ciertas 
condiciones: El kilometraje debe ser menor que 3000 y el modelo
debe estar 2015 y 2017

"""
km<3000 and (modelo>=2015 and modelo<=2017) #Los paréntesis son opcionales

"""
Una agrupación académica tiene ciertos requisitos para cualquier
estudiante que desee ingresar: debe tener más del 30% de sus estudios 
completos y no debe ser miembro de otra agrupación académica en 
la misma universidad
"""

porcentaje completo>30 and not(miembro_agrupación)

#Una persona pasa frío si es invierno y además no tiene calefacción ni está abrigada

es_invierno and not tiene_calefacción and not está_abrigada
es_invierno and not (tiene_calefacción or está_abrigada)



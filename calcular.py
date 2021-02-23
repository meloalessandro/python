#!/usr/bin/env python
# coding: utf-8

print ('Bem vindo, este é o meu primeiro programa \nSiga as instruções na tela\n\n')
nome= input ('Informe seu nome:')
idade= int(input ('Informe sua idade:'))
print ('\n\n\nRealizando cáculos..')
dias = idade *365
horas = dias *24
minutos = horas*60
segundos = minutos * 60
print  ('\n',nome,', você já viveu ', dias, 'dias. Isto equivale a \n', horas,' horas ou\n', minutos, ' minutos ou\n', segundos, 'segundos.')

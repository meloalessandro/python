#!/usr/bin/env python
# coding: utf-8

import math
import random
##dct={} ## Define o dicionário dct como vazio
dct = {1: 'HTML', 2: 'BASIC', 3: 'JAVA', 4: 'COBOL', 5: 'FORTRAN', 6: 'DELPHI', 7: 'C#', 8: 'C++', 9: 'PASCAL'} ## PARA TESTES

def linguagem (lg): ## lg é a váriável que contém a linguagem que está sendo pesquisada
    c=len(dct)+1 ## Inicia a váriavel c (Novo valor de CHAVE) como sendo o tamanho do dicionário+1
    r=0 ## Inicia a váriavel r (resposta SE a linguagem pesquisada foi encontrada) como 0
    for k,i in dct.items(): ## inicia a busca no dicionário
        if i==lg: ## caso linguagem exista no dicionário
            fk= k; r=1 ## registra fk (Found_Key) como o valor de k (Chave) e define r (resposta) como 1
    if r== 1: ## no final da busca, verifica o valor de r (resposta)
        print(lg,"é uma linguagem válida e está na chave", fk)
    else:
        print(lg,'nao é uma linguagem registrada'); conf=input ('Deseja cadastrar? (S/N)') ## caso a linguagem não seja encontrada, pergunta se quer cadastrar
        if conf=="S" or conf =="s" : 
            cadl(c,lg) ## invoca metodo cadl para cadastrar a linguagem
        elif conf=="N" or conf=="n" : print (lg,"não foi cadastrada")
        else: print (conf, "não é uma resposta válida. A linguagem",lg,"não foi cadastrada!")

def cadl (i,l):
    dct[i]=l ## cadastra a linguagem (lg) na chave (c)
    print (l,'foi cadastrada na chave',i)

def cadastra():
    c=len(dct)+1 ## Inicia a váriavel c (Novo valor de CHAVE) como sendo o tamanho do dicionário+1
    cad=input ('Informe a liguagem a ser cadastrada: ')
    print (cad, ' será cadastrada. Confirma? (S/N)')
    conf=input ()
    if conf=="S" or conf =="s" : 
        cadl(c,cad) ## invoca metodo cadl para cadastrar a linguagem
    elif conf=="N" or conf=="n" : print (cad,"não foi cadastrada")
    else: print (conf, "não é uma resposta válida. A linguagem",cad,"não foi cadastrada!")

def pesquisa ():
    lg =input ('\nQual linguagem deseja pesquisar?: ')
    linguagem (lg)
    dnv = input ('Deseja nova pesquisa? (S/N): ')
    if dnv=="S" or dnv =="s": pesquisa()
    else:
        if dnv=="N" or dnv=="n": print ("")
            
def lista ():
    print ('Esta são as linguagens cadastradas no sistema:')
    print (dct)

def aleat ():
    c=len(dct)
    r=int(random.random()*100)
    while (r > c):
        r = int(random.random()*100)
    print ('Linguagem aleatória: ',dct[r])
    
def menu ():
    op= int (input ('''
    Por favor, selecione a função
    1 para listar
    2 para pesquisar
    3 para cadastrar
    4 para escolher uma linguagem aleatória
    0 para sair
    \n'''))
    if op ==1:
        lista()
        menu()
    elif op==2:
        pesquisa()
        menu()
    elif op==3:
        cadastra()
        menu()
    elif op==4:
        aleat()
        menu()     
    elif op==0:
        print ('\n\nAté logo!')
    else : menu()

menu()
# -*- coding: utf-8 -*-
#
#  Geopy_main.py
#  
#  Copyright 2018 Nathan Renner <nathanrenner25@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#




from Geopy_oper import *
from Geopy_graf import *
from functools import *
from tkinter import *
from random import *
from math import *
from time import *

FONT_ = 'Verdana'
TYPE_FONT = 'bold'
COR_1_SOF='#4848FF'
COR_2_SOF='#FF3838'
COR_3_SOF='#FFFF52'
COR_4_SOF='#45FF45'
COR_5_SOF='#FF2EFF'

STD_3 = '#4D4D4D'
STD_2 = '#FFFFFF'
STD_1 = '#1A1A1A'
STD_LE = '#FFFFFF'


def Error_input_user(tipo_erro):
	
	def destroy_error_window():
		error_window.destroy()
		
	
	error_window = Toplevel()
	error_window.title("~GEOPY~")
	error_window["bg"] = STD_2 
	
	cores=['#FF0000','#0000FF','#000069','#FFA500','#800080','#DB4AC3','#0D5A00','#8B6914'
		  ,'#1E90FF','#A52A2A','#1FFF00','#948DFF','#38BB38','#1A1A1A','#FFFFFF','#830000','#FFE67A']
	cor_sort = randint(0,len(cores)-1)
	
	LB_error_2=Label(error_window,bg = STD_2,fg = STD_1,text = '»ERRO«',width = 10,font=(FONT_,20,TYPE_FONT))
	LB_error_2.grid(rowspan = 1,column = 1,ipadx = 50)
	
	LB_error_1=Label(error_window,text = "",font = (FONT_,15,TYPE_FONT),bg = STD_2,fg = STD_1)
	LB_error_1.grid(row = 1,column = 1)
	
	BT_error=Button(error_window,text = "Continuar",font = (FONT_,15,TYPE_FONT),bg = STD_1,fg = STD_2,border = 0)
	BT_error['command'] = destroy_error_window
	BT_error.grid(row = 2,column = 1,pady = 10) 
	
	if tipo_erro == 1:
		LB_error_1["text"] = "Vetores Nulos\ne/ou\nNomes Incorretos"
	if tipo_erro == 2:
		LB_error_1["text"] = "Selecione no Mínimo\nDois Vetores "
	if tipo_erro == 3:
		LB_error_1["text"] = "Selecione Apenas\nUm Unico Vetor  "
	if tipo_erro == 4:
		 LB_error_1["text"] = "Preencha o Campo\n'em Cinza'\nCorretamente"
	if tipo_erro == 5:
		LB_error_1["text"] = "No Mínimo Um Vetor\nDeve ser Escolhido"
	if tipo_erro == 6:
		LB_error_1["text"] = "Selecione Apenas\nDois Vetores"
	if tipo_erro == 7:
		LB_error_1["text"] = "É Exigido 3\n Vetores Para\nEssa Operação "


def Num_or_str(nom_vt):
	cheknom = 0
	try:
		int_str = int(nom_vt)
	except ValueError:
		cheknom = 0
	else:	
		cheknom = 1
	return cheknom
	

def Vet_2d(em_2d):
	
	vet_2d_coord = Tk()
	vet_2d_coord.title("~GEOPY~")
	vet_2d_coord["bg"] = STD_2 
	vta=[]
	vtb=[]
	vtc=[]
	vtd=[]
	vte=[]
	T_ipadx = 5
	T_ipady = 5
	T_padx = 10
	T_pady = 10
	nom_v1 = str()
	nom_v2 = str()
	nom_v3 = str()
	nom_v4 = str()
	nom_v5 = str()
	def rand_vets_2d():
		b = -5
		a = 5
		vet_nao_nulo = 5
		nom_vet = []
		cor_vet = []
		all_vt = []
		v1x = randint(b,a)
		v1y = randint(b,a)
		v1x = float(v1x)
		v1y = float(v1y)
		vta.append(v1x)
		vta.append(v1y)
	
		v2x = randint(b,a)
		v2y = randint(b,a)
		v2x = float(v2x)
		v2y = float(v2y)
		vtb.append(v2x)
		vtb.append(v2y)

		v3x = randint(b,a)
		v3y = randint(b,a)
		v3x = float(v3x)
		v3y = float(v3y)
		vtc.append(v3x)
		vtc.append(v3y)

		v4x = randint(b,a)
		v4y = randint(b,a)
		v4x = float(v4x)
		v4y = float(v4y)
		vtd.append(v4x)
		vtd.append(v4y)
		
		v5x = randint(b,a)
		v5y = randint(b,a)
		v5x = float(v5x)
		v5y = float(v5y)
		vte.append(v5x)
		vte.append(v5y)
		
		all_vt.append(vta)
		all_vt.append(vtb)
		all_vt.append(vtc)
		all_vt.append(vtd)
		all_vt.append(vte)
		nom_vet.append('a')
		nom_vet.append('b')
		nom_vet.append('c')
		nom_vet.append('d')
		nom_vet.append('e')
		cor_vet.append('blue')
		cor_vet.append('red')
		cor_vet.append('yellow')
		cor_vet.append('green')
		cor_vet.append('purple')
		vet_2d_coord.destroy()
		
		Main_window(all_vt,nom_vet,cor_vet,vet_nao_nulo,em_2d)
		
	def ok_vet_go_M():
		
		nom_va = ET_nom_v1.get()
		vt1_x = ET_vet1_x.get()
		vt1_y = ET_vet1_y.get()
		
		nom_vb = ET_nom_v2.get()
		vt2_x = ET_vet2_x.get()
		vt2_y = ET_vet2_y.get()
		
		nom_vc = ET_nom_v3.get()
		vt3_x = ET_vet3_x.get()
		vt3_y = ET_vet3_y.get()
		
		nom_vd = ET_nom_v4.get()
		vt4_x = ET_vet4_x.get()
		vt4_y = ET_vet4_y.get()
	
		nom_ve = ET_nom_v5.get()
		vt5_x = ET_vet5_x.get()
		vt5_y = ET_vet5_y.get()
		
		if nom_va == '':
			nom_va = 'a'
		if nom_vb == '':
			nom_vb = 'b'
		if nom_vc == '':
			nom_vc = 'c'
		if nom_vd == '':
			nom_vd = 'd'
		if nom_ve == '':
			nom_ve = 'e'
		
		vet_nao_nulo = 0
		nom_vet = []
		cor_vet = []
		all_vt = []
		check=0
		
		if vt1_x!='' and vt1_y!='':
			check=Num_or_str(nom_va)
			if check == 1:
				ET_nom_v1.delete(0,END)
			if check == 0:
				nom_val=nom_va.lower()
				nom_vet.append(nom_val)
				cor_vet.append('blue')
				vt1_x = float(vt1_x)
				vt1_y = float(vt1_y)
				vta.append(vt1_x)
				vta.append(vt1_y)
				all_vt.append(vta)
				tam_va = len(vta)
				vet_nao_nulo = vet_nao_nulo + 1
		
		if vt2_x!='' and vt2_y!='':
			check=Num_or_str(nom_vb)
			if check == 1:
				ET_nom_v2.delete(0,END)
			if check == 0:
				nom_vbl=nom_vb.lower()
				nom_vet.append(nom_vbl)
				cor_vet.append('red')
				vt2_x = float(vt2_x)
				vt2_y = float(vt2_y)
				vtb.append(vt2_x)
				vtb.append(vt2_y)	
				all_vt.append(vtb)
				tam_vb = len(vtb)
				vet_nao_nulo = vet_nao_nulo + 1
		
		if vt3_x!='' and vt3_y!='':
			check=Num_or_str(nom_vc)
			if check == 1:
				ET_nom_v3.delete(0,END)
			if check == 0:
				nom_vcl=nom_vc.lower()
				nom_vet.append(nom_vcl)
				cor_vet.append('yellow')
				vt3_x = float(vt3_x)
				vt3_y = float(vt3_y)		
				vtc.append(vt3_x)
				vtc.append(vt3_y)			
				all_vt.append(vtc)
				tam_vc = len(vtc)
				vet_nao_nulo = vet_nao_nulo + 1
		
		if vt4_x!='' and vt4_y!='':
			check=Num_or_str(nom_vd)
			if check == 1:
				ET_nom_v4.delete(0,END)
			if check == 0:
				nom_vdl=nom_vd.lower()
				nom_vet.append(nom_vdl)
				cor_vet.append('green')
				vt4_x = float(vt4_x)
				vt4_y = float(vt4_y)		
				vtd.append(vt4_x)
				vtd.append(vt4_y)		
				all_vt.append(vtd)
				tam_vd = len(vtd)
				vet_nao_nulo = vet_nao_nulo + 1
				
		if vt5_x!='' and vt5_y!='':
			check=Num_or_str(nom_ve)
			if check == 1:
				ET_nom_v5.delete(0,END)
			if check == 0:
				nom_vel=nom_ve.lower()
				nom_vet.append(nom_vel)
				cor_vet.append('purple')
				vt5_x = float(vt5_x)
				vt5_y = float(vt5_y)		
				vte.append(vt5_x)
				vte.append(vt5_y)			
				all_vt.append(vte)
				tam_ve = len(vte)
				vet_nao_nulo = vet_nao_nulo + 1
		
		if all_vt != []:
			
			vet_2d_coord.destroy()
			
			Main_window(all_vt,nom_vet,cor_vet,vet_nao_nulo,em_2d)
		else:
			Error_input_user(1)
			
	def clean_all():
		
		ET_nom_v1.delete(0,END)
		ET_nom_v2.delete(0,END)
		ET_nom_v3.delete(0,END)
		ET_nom_v4.delete(0,END)
		ET_nom_v5.delete(0,END)
		ET_vet1_x.delete(0,END)
		ET_vet1_y.delete(0,END)
		ET_vet2_x.delete(0,END)
		ET_vet2_y.delete(0,END)
		ET_vet3_x.delete(0,END)
		ET_vet3_y.delete(0,END)
		ET_vet4_x.delete(0,END)
		ET_vet4_y.delete(0,END)
		ET_vet5_x.delete(0,END)
		ET_vet5_y.delete(0,END)
	
	LB_x = Label(vet_2d_coord,text = "X",fg = STD_1,bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_x.grid(row = 0,column = 2)
	LB_y = Label(vet_2d_coord,text = "Y",fg = STD_1,bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_y.grid(row = 0,column = 3)
	LB_nom = Label(vet_2d_coord,text = 'NOME',fg = STD_1, bg = STD_2,font=((FONT_),12,TYPE_FONT))
	LB_nom.grid(row = 0, column = 1)
	
	ET_nom_v1 = Entry(vet_2d_coord,width = 5,bg = COR_1_SOF,textvariable=nom_v1,font = (FONT_,10,TYPE_FONT))
	ET_nom_v1.grid(row = 1,column = 1)
	ET_vet1_x = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet1_x.grid(row = 1,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet1_y = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet1_y.grid(row = 1,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v2 = Entry(vet_2d_coord,width = 5,bg = COR_2_SOF,textvariable=nom_v2,font = (FONT_,10,TYPE_FONT))
	ET_nom_v2.grid(row = 2,column = 1)
	ET_vet2_x = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet2_x.grid(row = 2,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet2_y = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet2_y.grid(row = 2,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v3 = Entry(vet_2d_coord,width = 5,bg = COR_3_SOF,textvariable=nom_v3,font = (FONT_,10,TYPE_FONT))
	ET_nom_v3.grid(row = 3,column = 1)
	ET_vet3_x = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet3_x.grid(row = 3,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet3_y = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet3_y.grid(row = 3,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v4 = Entry(vet_2d_coord,width = 5,bg = COR_4_SOF,textvariable=nom_v4,font = (FONT_,10,TYPE_FONT))
	ET_nom_v4.grid(row = 4,column = 1)
	ET_vet4_x = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet4_x.grid(row = 4,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet4_y = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet4_y.grid(row = 4,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v5 = Entry(vet_2d_coord,width = 5,bg = COR_5_SOF,textvariable=nom_v5,font = (FONT_,10,TYPE_FONT))
	ET_nom_v5.grid(row = 5,column = 1)
	ET_vet5_x = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet5_x.grid(row = 5,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet5_y = Entry(vet_2d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet5_y.grid(row = 5,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	BT_continue_menu = Button(vet_2d_coord,text = "Confirmar",bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_continue_menu['fg'] = STD_2
	BT_continue_menu.grid(row = 1, column = 5,ipadx = 8)
	BT_continue_menu["command"] = ok_vet_go_M
	
	BT_clean_vets = Button(vet_2d_coord,text = "Limpar",bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_clean_vets['fg'] = STD_2
	BT_clean_vets.grid(row = 2, column = 5, ipadx = 20)
	BT_clean_vets["command"] = clean_all
	
	BT_randon_vets = Button(vet_2d_coord,text = "Randômico",bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_randon_vets['fg'] = STD_2
	BT_randon_vets.grid(row = 3,column = 5, ipadx = 5)
	BT_randon_vets["command"] = rand_vets_2d


def Vet_3d(em_3d):
	
	vet_3d_coord = Tk()
	vet_3d_coord.title("~GEOPY~")
	vet_3d_coord["bg"] = STD_2 
	vta=[]
	vtb=[]
	vtc=[]
	vtd=[]
	vte=[]
	T_ipadx = 5
	T_ipady = 5
	T_padx = 10
	T_pady = 10
	nom_v1 = str()
	nom_v2 = str()
	nom_v3 = str()
	nom_v4 = str()
	nom_v5 = str()

	def ok_vet_go_M():
		
		nom_va = ET_nom_v1.get()
		vt1_x = ET_vet1_x.get()
		vt1_y = ET_vet1_y.get()
		vt1_z = ET_vet1_z.get()
		
		nom_vb = ET_nom_v2.get()
		vt2_x = ET_vet2_x.get()
		vt2_y = ET_vet2_y.get()
		vt2_z = ET_vet2_z.get()
		
		nom_vc = ET_nom_v3.get()
		vt3_x = ET_vet3_x.get()
		vt3_y = ET_vet3_y.get()
		vt3_z = ET_vet3_z.get()
		
		nom_vd = ET_nom_v4.get()
		vt4_x = ET_vet4_x.get()
		vt4_y = ET_vet4_y.get()
		vt4_z = ET_vet4_z.get()
		
		nom_ve = ET_nom_v5.get()
		vt5_x = ET_vet5_x.get()
		vt5_y = ET_vet5_y.get()
		vt5_z = ET_vet5_z.get()
		
		if nom_va == '':
			nom_va = 'a'
		if nom_vb == '':
			nom_vb = 'b'
		if nom_vc == '':
			nom_vc = 'c'
		if nom_vd == '':
			nom_vd = 'd'
		if nom_ve == '':
			nom_ve = 'e'
		
		vet_nao_nulo = 0
		
		nom_vet = []
		cor_vet = []
		all_vt = []
		
		if vt1_x!='' and vt1_y!='' and vt1_z!='':
			check=Num_or_str(nom_va)
			if check == 1:
				ET_nom_v1.delete(0,END)
			if check == 0:
				nom_val=nom_va.lower()
				nom_vet.append(nom_val)
				cor_vet.append('blue')
				vt1_x = float(vt1_x)
				vt1_y = float(vt1_y)
				vt1_z = float(vt1_z)
				vta.append(vt1_x)
				vta.append(vt1_y)
				vta.append(vt1_z)
				all_vt.append(vta)
				tam_va = len(vta)
				vet_nao_nulo = vet_nao_nulo + 1
			
		if vt2_x!='' and vt2_y!='' and vt2_z!='':
			check=Num_or_str(nom_vb)
			if check == 1:
				ET_nom_v2.delete(0,END)
			if check == 0:
				nom_vbl=nom_vb.lower()
				nom_vet.append(nom_vbl)
				cor_vet.append('red')
				vt2_x = float(vt2_x)
				vt2_y = float(vt2_y)
				vt2_z = float(vt2_z)
				vtb.append(vt2_x)
				vtb.append(vt2_y)
				vtb.append(vt2_z)
				all_vt.append(vtb)
				tam_vb = len(vtb)
				vet_nao_nulo = vet_nao_nulo + 1
			
		if vt3_x!='' and vt3_y!='' and vt3_z!='':
			check=Num_or_str(nom_vc)
			if check == 1:
				ET_nom_v3.delete(0,END)
			if check == 0:
				nom_vcl=nom_vc.lower()
				nom_vet.append(nom_vcl)
				cor_vet.append('yellow')
				vt3_x = float(vt3_x)
				vt3_y = float(vt3_y)
				vt3_z = float(vt3_z)
				vtc.append(vt3_x)
				vtc.append(vt3_y)
				vtc.append(vt3_z)
				all_vt.append(vtc)
				tam_vc = len(vtc)
				vet_nao_nulo = vet_nao_nulo + 1
			
		if vt4_x!='' and vt4_y!='' and vt4_z!='':
			check=Num_or_str(nom_vc)
			if check == 1:
				ET_nom_v4.delete(0,END)
			if check == 0:
				nom_vdl=nom_vd.lower()
				nom_vet.append(nom_vdl)
				cor_vet.append('green')
				vt4_x = float(vt4_x)
				vt4_y = float(vt4_y)
				vt4_z = float(vt4_z)
				vtd.append(vt4_x)
				vtd.append(vt4_y)
				vtd.append(vt4_z)
				all_vt.append(vtd)
				tam_vd = len(vtd)
				vet_nao_nulo = vet_nao_nulo + 1
			
		if vt5_x!='' and vt5_y!='' and vt5_z!='':
			check=Num_or_str(nom_ve)
			if check == 1:
				ET_nom_v5.delete(0,END)
			if check == 0:
				nom_vel=nom_ve.lower()
				nom_vet.append(nom_vel)
				cor_vet.append('purple')
				vt5_x = float(vt5_x)
				vt5_y = float(vt5_y)
				vt5_z = float(vt5_z)
				vte.append(vt5_x)
				vte.append(vt5_y)
				vte.append(vt5_z)
				all_vt.append(vte)
				tam_ve = len(vte)
				vet_nao_nulo = vet_nao_nulo + 1
			
			
		if all_vt != []:
			vet_3d_coord.destroy()
		
			Main_window(all_vt,nom_vet,cor_vet,vet_nao_nulo,em_3d)
		else:
			Error_input_user(1)
		
	def clean_all():
	
		ET_vet1_x.delete(0,END)
		ET_vet1_y.delete(0,END)
		ET_vet1_z.delete(0,END)
		ET_vet2_x.delete(0,END)
		ET_vet2_y.delete(0,END)
		ET_vet2_z.delete(0,END)
		ET_vet3_x.delete(0,END)
		ET_vet3_y.delete(0,END)
		ET_vet3_z.delete(0,END)
		ET_vet4_x.delete(0,END)
		ET_vet4_y.delete(0,END)
		ET_vet4_z.delete(0,END)
		ET_vet5_x.delete(0,END)
		ET_vet5_y.delete(0,END)
		ET_vet5_z.delete(0,END)
		
	def rand_vets_3d():
	
		b = -5
		a = 5
		vet_nao_nulo = 5
		nom_vet = []
		cor_vet = []
		all_vt = []
		v1x = randint(b,a)
		v1y = randint(b,a)
		v1z = randint(b,a)
		v1x = float(v1x)
		v1y = float(v1y)
		v1z = float(v1z)
		vta.append(v1x)
		vta.append(v1y)
		vta.append(v1z)
	
		v2x = randint(b,a)
		v2y = randint(b,a)
		v2z = randint(b,a)
		v2x = float(v2x)
		v2y = float(v2y)
		v2z = float(v2z)
		vtb.append(v2x)
		vtb.append(v2y)
		vtb.append(v2z)
		
		v3x = randint(b,a)
		v3y = randint(b,a)
		v3z = randint(b,a)
		v3x = float(v3x)
		v3y = float(v3y)
		v3z = float(v3z)
		vtc.append(v3x)
		vtc.append(v3y)
		vtc.append(v3z)
		
		v4x = randint(b,a)
		v4y = randint(b,a)
		v4z = randint(b,a)
		v4x = float(v4x)
		v4y = float(v4y)
		v4z = float(v4z)
		vtd.append(v4x)
		vtd.append(v4y)
		vtd.append(v4z)
		
		v5x = randint(b,a)
		v5y = randint(b,a)
		v5z = randint(b,a)
		v5x = float(v5x)
		v5y = float(v5y)
		v5z = float(v5z)
		vte.append(v5x)
		vte.append(v5y)
		vte.append(v5z)
		
		all_vt.append(vta)
		all_vt.append(vtb)
		all_vt.append(vtc)
		all_vt.append(vtd)
		all_vt.append(vte)
		nom_vet.append('a')
		nom_vet.append('b')
		nom_vet.append('c')
		nom_vet.append('d')
		nom_vet.append('e')
		cor_vet.append('blue')
		cor_vet.append('red')
		cor_vet.append('yellow')
		cor_vet.append('green')
		cor_vet.append('purple')
		vet_3d_coord.destroy()
		Main_window(all_vt,nom_vet,cor_vet,vet_nao_nulo,em_3d)
	
	LB_x = Label(vet_3d_coord,text = "X",fg = STD_1,bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_x.grid(row = 0,column = 2)
	LB_y = Label(vet_3d_coord,text = "Y",fg = STD_1,bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_y.grid(row = 0,column = 3)
	LB_z = Label(vet_3d_coord,text = "Z",fg = STD_1,bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_z.grid(row = 0,column = 4)
	LB_nom = Label(vet_3d_coord,text = "NOME", fg = STD_1, bg = STD_2 ,font=((FONT_),12,TYPE_FONT))
	LB_nom.grid(row = 0, column = 1)
	
	ET_nom_v1 = Entry(vet_3d_coord,width = 5,bg = COR_1_SOF,textvariable=nom_v1,font = (FONT_,10,TYPE_FONT),border = 0)
	ET_nom_v1.grid(row = 1,column = 1)
	ET_vet1_x = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet1_x.grid(row = 1,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet1_y = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet1_y.grid(row = 1,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet1_z = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet1_z.grid(row = 1,column = 4,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v2 = Entry(vet_3d_coord,width = 5,bg = COR_2_SOF,textvariable=nom_v2,font = (FONT_,10,TYPE_FONT),border = 0)
	ET_nom_v2.grid(row = 2,column = 1)
	ET_vet2_x = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet2_x.grid(row = 2,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet2_y = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet2_y.grid(row = 2,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet2_z = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet2_z.grid(row = 2,column = 4,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v3 = Entry(vet_3d_coord,width = 5,bg = COR_3_SOF,textvariable=nom_v3,font = (FONT_,10,TYPE_FONT),border = 0)
	ET_nom_v3.grid(row = 3,column = 1)
	ET_vet3_x = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet3_x.grid(row = 3,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet3_y = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet3_y.grid(row = 3,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet3_z = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet3_z.grid(row = 3,column = 4,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v4 = Entry(vet_3d_coord,width = 5,bg = COR_4_SOF,textvariable=nom_v4,font = (FONT_,10,TYPE_FONT),border = 0)
	ET_nom_v4.grid(row = 4,column = 1)
	ET_vet4_x = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet4_x.grid(row = 4,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet4_y = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet4_y.grid(row = 4,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet4_z = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet4_z.grid(row = 4,column = 4,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	ET_nom_v5 = Entry(vet_3d_coord,width = 5,bg = COR_5_SOF,textvariable=nom_v5,font = (FONT_,10,TYPE_FONT),border = 0)
	ET_nom_v5.grid(row = 5,column = 1)
	ET_vet5_x = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet5_x.grid(row = 5,column = 2,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet5_y = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet5_y.grid(row = 5,column = 3,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	ET_vet5_z = Entry(vet_3d_coord,width = 4,font = (FONT_,10,TYPE_FONT),bg = STD_3,fg = STD_LE,border = 0)
	ET_vet5_z.grid(row = 5,column = 4,ipadx = T_ipadx, ipady = T_ipady,padx = T_padx, pady = T_pady)
	
	BT_continue_menu = Button(vet_3d_coord,text = "Confirmar",fg = STD_2,bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_continue_menu.grid(row = 1, column = 5,ipadx = 8)
	BT_continue_menu["command"] = ok_vet_go_M
	
	BT_clean_vets = Button(vet_3d_coord,text = "Limpar",fg = STD_2,bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_clean_vets.grid(row = 2, column = 5, ipadx = 20)
	BT_clean_vets["command"] = clean_all
	
	BT_randon_vets = Button(vet_3d_coord,text = "Randômico", fg = STD_2,bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_randon_vets.grid(row = 3,column = 5, ipadx = 5)
	BT_randon_vets["command"] = rand_vets_3d
	

def Mod_2d_3d():
	def go_to_2d_coord():
		opt_dimension_vet.destroy()
		em_2d = 2
		Vet_2d(em_2d)
	def go_to_3d_coord():
		opt_dimension_vet.destroy()
		em_3d = 3
		Vet_3d(em_3d)
	opt_dimension_vet = Tk()
	opt_dimension_vet.title("~GEOPY~")
	opt_dimension_vet["bg"] = STD_2 
	LB_mod_opt = Label(opt_dimension_vet, text = "Escolha a Dimenção",bg = STD_2 ,fg = STD_1,font=(FONT_, 20,TYPE_FONT))
	LB_mod_opt.grid(rowspan = 1,columnspan = 2)
	BT_mod_2d = Button(opt_dimension_vet,text = " 2D ",fg = STD_2,bg = STD_1,font=(FONT_,20,TYPE_FONT),border = 0)
	BT_mod_2d['command'] = go_to_2d_coord
	BT_mod_2d.grid(row = 1,column = 0,padx = 5,pady = 5)
	BT_mod_3d = Button(opt_dimension_vet,text = " 3D ",fg = STD_2,bg = STD_1,font=(FONT_,20,TYPE_FONT),border = 0)
	BT_mod_3d['command'] = go_to_3d_coord
	BT_mod_3d.grid(row = 1,column = 1,padx = 5,pady = 5)
	opt_dimension_vet.mainloop()
	

def Entry_window():
	
	def go_to_mod_window():
		entry_window.destroy()
		
		Mod_2d_3d()
	entry_window = Tk()
	entry_window.title("~GEOPY~")
	entry_window.geometry("310x170")
	entry_window["bg"] = STD_2 
	LB_entry_window = Label(entry_window,text = "Geometria Analítica",bg = STD_2 ,fg = STD_1,font=(FONT_, 20,TYPE_FONT))
	LB_entry_window.pack()
	LB_entry_window = Label(entry_window,text = "Professor: Acelmo",bg = STD_2 ,fg = STD_1,font=(FONT_,15,TYPE_FONT))
	LB_entry_window.pack()
	LB_entry_window = Label(entry_window,text = "Aluno: Nathan",bg = STD_2 ,fg = STD_1,font=(FONT_,15,TYPE_FONT),pady = 10)
	LB_entry_window.pack()
	BT_entry_window = Button (entry_window,text = "Continuar", fg = STD_2,bg = STD_1,font = (FONT_, 10, TYPE_FONT),border = 0)
	BT_entry_window['pady'] = 10 
	BT_entry_window.pack()
	BT_entry_window["command"] = go_to_mod_window
	entry_window.mainloop()


def Main_window(all_vt,nom_vt,cor_vt,num_select_vet,dim_vet):
	
	main_M_W = Tk()
	main_M_W.title("~GEOPY~")
	main_M_W["bg"]= STD_2 
	
	
	_ipadx = 3
	_ipady = 3
	_padx = 20
	_pady = 2
	_width = 11
	co_tx = 3
	co_vt = 4
	co_cb = 6
	_v1 = IntVar()
	_v2 = IntVar()
	_v3 = IntVar()
	_v4 = IntVar()
	_v5 = IntVar()
	seed = [] 
	
	

	def organiza_vetores(num_vt):
	
		lim = 0
		lim2 = 0
		
		if num_vt in seed:
			while lim < len(seed):
				if num_vt == seed[lim]:
					del(seed[lim])
					if num_vt == 1:
						BT_vet1['text'] = '0°'
					if num_vt == 2:
						BT_vet2['text'] = '0°'
					if num_vt == 3:
						BT_vet3['text'] = '0°'
					if num_vt == 4:
						BT_vet4['text'] = '0°'
					if num_vt == 5:
						BT_vet5['text'] = '0°'
				lim=lim+1
		
		
		elif len(seed) == 0:
			if num_vt == 1:
				seed.append(1)
			if num_vt == 2:
				seed.append(2)
			if num_vt == 3:
				seed.append(3)
			if num_vt == 4:
				seed.append(4)
			if num_vt == 5:
				seed.append(5)
				
		elif len(seed) == 1:
			if num_vt == 1:
				seed.append(1)
			if num_vt == 2:
				seed.append(2)
			if num_vt == 3:
				seed.append(3)
			if num_vt == 4:
				seed.append(4)
			if num_vt == 5:
				seed.append(5)
				
		elif len(seed) == 2:
			if num_vt == 1:
				seed.append(1)
			if num_vt == 2:
				seed.append(2)
			if num_vt == 3:
				seed.append(3)
			if num_vt == 4:
				seed.append(4)
			if num_vt == 5:
				seed.append(5)
				
		elif len(seed) == 3:
			if num_vt == 1:
				seed.append(1)
			if num_vt == 2:
				seed.append(2)
			if num_vt == 3:
				seed.append(3)
			if num_vt == 4:
				seed.append(4)
			if num_vt == 5:
				seed.append(5)
			
		elif len(seed) == 4:
			if num_vt == 1:
				seed.append(1)
			if num_vt == 2:
				seed.append(2)
			if num_vt == 3:
				seed.append(3)
			if num_vt == 4:
				seed.append(4)
			if num_vt == 5:
				seed.append(5)
				
		if len(seed) > 0:
			try:
				if 1 == seed[0]:
					BT_vet1['text'] = '1°'
				if 2 == seed[0]:
					BT_vet2['text'] = '1°'
				if 3 == seed[0]:
					BT_vet3['text'] = '1°'
				if 4 == seed[0]:
					BT_vet4['text'] = '1°'
				if 5 == seed[0]:
					BT_vet5['text'] = '1°'
				
				if 1 == seed[1]:
					BT_vet1['text'] = '2°'
				if 2 == seed[1]:
					BT_vet2['text'] = '2°'
				if 3 == seed[1]:
					BT_vet3['text'] = '2°'
				if 4 == seed[1]:
					BT_vet4['text'] = '2°'
				if 5 == seed[1]:
					BT_vet5['text'] = '2°'
				
				if 1 == seed[2]:
					BT_vet1['text'] = '3°'
				if 2 == seed[2]:
					BT_vet2['text'] = '3°'
				if 3 == seed[2]:
					BT_vet3['text'] = '3°'
				if 4 == seed[2]:
					BT_vet4['text'] = '3°'
				if 5 == seed[2]:
					BT_vet5['text'] = '3°'
				
				if 1 == seed[3]:
					BT_vet1['text'] = '4°'
				if 2 == seed[3]:
					BT_vet2['text'] = '4°'
				if 3 == seed[3]:
					BT_vet3['text'] = '4°'
				if 4 == seed[3]:
					BT_vet4['text'] = '4°'
				if 5 == seed[3]:
					BT_vet5['text'] = '4°'
					
				if 1 == seed[4]:
					BT_vet1['text'] = '5°'
				if 2 == seed[4]:
					BT_vet2['text'] = '5°'
				if 3 == seed[4]:
					BT_vet3['text'] = '5°'
				if 4 == seed[4]:
					BT_vet4['text'] = '5°'
				if 5 == seed[4]:
					BT_vet5['text'] = '5°'
			except IndexError:
				pass
			else:
				pass

	def new_vets_mod():
		
		main_M_W.destroy()
		
		Mod_2d_3d()
	
	def view_result(tipo_oper):
		
		#Label Resultado
		LB_result = Label(main_M_W,bg = 'white', width = 15,font=(FONT_,15),relief='sunken',border = 0)
		LB_result.grid(row = 11,columnspan = 5,padx = 10,pady = 10)
		LB_result['text']= ""
		
		vt_result = []
		
		def view_result_oper(vt_result):
			dim_vt = Verify_2d_3d(all_vt)
			if dim_vt == 2:
				vt_result.append(1)
				View_2d_vts(all_vt,nom_vt,cor_vt,select_vet,num_select_vet,vt_result)
			else:
				vt_result.append(0)
				View_3d_vts(all_vt,nom_vt,cor_vt,select_vet,num_select_vet,vt_result)
			pass
		tipo_resu_view = 1
		view_bt_view = 0
		
		if tipo_oper == 0:
			if len(seed) < 1:
				Error_input_user(5)
			else:
				#LB_result['text']='98'
				Select_view_dim(all_vt,nom_vt,cor_vt,seed,dim_vet)
		
		if tipo_oper == 1:##Soma_oper
			view_bt_view = 1
			if len(seed) < 2:
				Error_input_user(2)
			else:
				LB_result['text']=("")
				vt_result = Soma_oper(all_vt,nom_vt,cor_vt,seed)
				if len(vt_result) == 2:
					a = vt_result[0]
					b = vt_result[1]
					LB_result['text'] = ("(%.1f, %.1f)")%(a,b)
				else:
					a = vt_result[0]
					b = vt_result[1]
					c = vt_result[2]
					LB_result['text'] = ("(%.1f, %.1f,%.1f)")%(a,b,c)
					
		if tipo_oper == 2:##Difer_oper
			view_bt_view = 1
			if len(seed) < 2:
				Error_input_user(2)
			else:
				LB_result['text']=("")
				vt_result = Difer_oper(all_vt,nom_vt,cor_vt,seed)
				if len(vt_result) == 2:
					a = vt_result[0]
					b = vt_result[1]
					LB_result['text'] = ("(%.1f, %.1f)")%(a,b)
				else:
					a = vt_result[0]
					b = vt_result[1]
					c = vt_result[2]
					LB_result['text'] = ("(%.1f, %.1f,%.1f)")%(a,b,c)
				
		if tipo_oper == 3:##Prod_constante
			view_bt_view = 1
			num_prod = 0
			vt_result = []
			num_prod = ET_num_prod.get()
			ET_num_prod['bg'] = '#FFFFFF'
			if len(seed) > 1 or len(seed) < 1:
				Error_input_user(3)
			else:
				LB_result['text']=("")
				try:
					num_prod = int(num_prod)
				except ValueError:
					ET_num_prod['bg'] = '#7F7F7F'
					Error_input_user(4)
				else:
					vt_result = Prod_constante(all_vt,nom_vt,cor_vt,seed,num_prod)
					if len(vt_result) == 2:
						a = vt_result[0]
						b = vt_result[1]
						LB_result['text'] = ("(%.1f, %.1f)")%(a,b)
					else:
						a = vt_result[0]
						b = vt_result[1]
						c = vt_result[2]
						LB_result['text'] = ("(%.1f, %.1f,%.1f)")%(a,b,c)
		
		if tipo_oper == 4:##Norma
			view_bt_view = 0
			raiz_result = Norma(all_vt,nom_vt,cor_vt,seed)
			if len(seed)< 1:
				LB_result['text'] = 'Erro'
			else:
				vt_result = Norma(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = ("√%i = %.3f")%(raiz_result,sqrt(raiz_result))
				
		if view_bt_view == 1:
			#BT_view = Button(main_M_W,text = 'Visualizar Resultado', fg = "white",bg = "red",font = (FONT_, 10, TYPE_FONT))
			#BT_view.grid(row = 12,columnspan = 5,sticky = N)
			#BT_view['command'] = partial(view_result_oper,vt_result)
			pass
		
		if tipo_oper == 6:#Prod_escalar
			if len(seed) < 2 or len(seed)>2:
				Error_input_user(6)
			else:
				result=Prod_escalar(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = '%.1f'%(result)
				
		if tipo_oper == 7:##Angulo
			result = 0
			if len(seed) < 2 or len(seed) > 2:
				Error_input_user(6)
			else:
				result=Angulo(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = '%.3f°'%(result)
		
		if tipo_oper == 8:##Coplanaridade
			if len(seed) < 3 or len(seed) > 3:
				Error_input_user(7)
			else:
				Result = Coplanaridade(all_vt,nom_vt,cor_vt,seed)
				if Result == True:
					LB_result['text'] = "É Coplanar"
				else:
					LB_result['text'] = "Não é Coplanar"
			
		if tipo_oper == 9:##Prod_vetorial
			if len(seed) < 2 or len(seed) > 2:
				Error_input_user(2)
			else:
				vt_result = Prod_vetorial(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = vt_result
				
		if tipo_oper == 10:##Prod_misto
			if len(seed) < 3 or len(seed) > 3:
				Error_input_user(7)
			else:
				result = Prod_misto(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = result
		
		if tipo_oper == 11:##Projeção
			if len(seed) < 2 or len(seed) > 2:
				Error_input_user(6)
			else:
				vtresult = []
				vtresult = Projecao(all_vt,nom_vt,cor_vt,seed)
				a = vtresult[0]
				b = vtresult[1]
				c = vtresult[2]
				LB_result['text'] = ("(%.2f, %.2f, %.2f)")%(a,b,c)
		
		if tipo_oper == 12:##Vol Paralelogramo
			if len(seed) < 3 or len(seed) > 3:
				Error_input_user(7)
			else:
				vol_para = VolParalelogramo(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = ("%.2f u.v.")%(vol_para)
		
		if tipo_oper == 13:##Vol Prisma
			if len(seed) < 3 or len(seed) > 3:
				Error_input_user(7)
			else:
				vol_para = VolParalelogramo(all_vt,nom_vt,cor_vt,seed)
				vol_prism = vol_para/2
				LB_result['text'] = ("%.2f u.v.")%(vol_prism)
		
		if tipo_oper == 14:##Vol Tetraedro
			if len(seed) < 3 or len(seed) > 3:
				Error_input_user(7)
			else:
				vol_para = VolParalelogramo(all_vt,nom_vt,cor_vt,seed)
				vol_tetra = (vol_para/6)
				LB_result['text'] = ("%.2f u.v.")%(vol_tetra)
		
		if tipo_oper == 15:##Área do Triângulo
			if len(seed) < 2 or len(seed) > 2:
				Error_input_user(6)
			else:
				vt_result = AreaTriangulo(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = ("%.4f")%(vt_result)
				
		if tipo_oper == 16:##Área do Paralelogramo
			if len(seed) < 2 or len(seed) > 2:
				Error_input_user(6)
			else:
				vt_result = AreaParalelogramo(all_vt,nom_vt,cor_vt,seed)
				LB_result['text'] = ("√%i = %.3f")%(vt_result,sqrt(vt_result))
			
				
	#Labels dos Vetores
	BT_padx = 10
	BT_pady = 7
	
	if num_select_vet == 1:
	
		LB_vet1_text = Label(main_M_W, text = nom_vt[0],bg = cor_vt[0],font=(FONT_, 12))
		LB_vet1_text.grid(row = 1,column = co_tx,ipadx = _ipadx)
		LB_vet1 = Label(main_M_W, text = all_vt[0],bg = STD_2 ,fg = STD_1,font = (FONT_, 15))
		LB_vet1.grid(row = 1, column = co_vt, ipadx = 8)
		BT_vet1 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet1['command'] = partial (organiza_vetores,1)
		BT_vet1.grid(row = 1,column = co_cb,padx = BT_padx,pady = BT_pady)
		
	elif num_select_vet == 2:
	
		LB_vet1_text = Label(main_M_W, text = nom_vt[0],bg = cor_vt[0],font=(FONT_, 12))
		LB_vet1_text.grid(row = 1,column = co_tx,ipady = _ipadx)
		LB_vet1 = Label(main_M_W, text = all_vt[0],bg = STD_2 ,fg = STD_1,font = (FONT_,15))
		LB_vet1.grid(row = 1, column = co_vt, ipadx = 8)
		BT_vet1 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet1['command'] = partial (organiza_vetores,1)
		BT_vet1.grid(row = 1,column = co_cb,padx = BT_padx,pady = BT_pady)
		
	
		LB_vet2_text = Label(main_M_W, text = nom_vt[1],bg = cor_vt[1],font=(FONT_, 12))
		LB_vet2_text.grid(row = 2,column = co_tx,ipady = _ipadx)
		LB_vet2 = Label(main_M_W, text = all_vt[1],bg = STD_2 ,fg = STD_1,font = (FONT_, 15))
		LB_vet2.grid(row = 2, column = co_vt, ipadx = 8)
		BT_vet2 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet2['command'] = partial (organiza_vetores,2)
		BT_vet2.grid(row = 2,column = co_cb,padx = BT_padx,pady = BT_pady)
		
	elif num_select_vet == 3:
		
		LB_vet1_text = Label(main_M_W, text = nom_vt[0],bg = cor_vt[0],font=(FONT_, 12))
		LB_vet1_text.grid(row = 1,column = co_tx,ipady = _ipadx)
		LB_vet1 = Label(main_M_W, text = all_vt[0],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet1.grid(row = 1, column = co_vt, ipadx = 8)
		BT_vet1 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet1['command'] = partial (organiza_vetores,1)
		BT_vet1.grid(row = 1,column = co_cb,padx = BT_padx,pady = BT_pady)
	
		LB_vet2_text = Label(main_M_W, text = nom_vt[1] ,bg = cor_vt[1],font=(FONT_, 12))
		LB_vet2_text.grid(row = 2,column = co_tx,ipady = _ipadx)
		LB_vet2 = Label(main_M_W, text = all_vt[1],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet2.grid(row = 2, column = co_vt, ipadx = 8)
		BT_vet2 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet2['command'] = partial (organiza_vetores,2)
		BT_vet2.grid(row = 2,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet3_text = Label(main_M_W, text = nom_vt[2] ,bg = cor_vt[2],font=(FONT_, 12))
		LB_vet3_text.grid(row = 3,column = co_tx,ipady = _ipadx)
		LB_vet3 = Label(main_M_W, text = all_vt[2],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet3.grid(row = 3, column = co_vt, ipadx = 8)
		BT_vet3 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet3['command'] = partial (organiza_vetores,3)
		BT_vet3.grid(row = 3,column = co_cb,padx = BT_padx,pady = BT_pady)
	
	elif num_select_vet == 4:
		
		LB_vet1_text = Label(main_M_W, text = nom_vt[0],bg = cor_vt[0],font=(FONT_, 12))
		LB_vet1_text.grid(row = 1,column = co_tx,ipady = _ipadx)
		LB_vet1 = Label(main_M_W, text = all_vt[0],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet1.grid(row = 1, column = co_vt, ipadx = 8)
		BT_vet1 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet1['command'] = partial (organiza_vetores,1)
		BT_vet1.grid(row = 1,column = co_cb,padx = BT_padx,pady = BT_pady)
	
		LB_vet2_text = Label(main_M_W, text = nom_vt[1] ,bg = cor_vt[1],font=(FONT_, 12))
		LB_vet2_text.grid(row = 2,column = co_tx,ipady = _ipadx)
		LB_vet2 = Label(main_M_W, text = all_vt[1],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet2.grid(row = 2, column = co_vt, ipadx = 8)
		BT_vet2 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet2['command'] = partial (organiza_vetores,2)
		BT_vet2.grid(row = 2,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet3_text = Label(main_M_W, text = nom_vt[2] ,bg = cor_vt[2],font=(FONT_, 12))
		LB_vet3_text.grid(row = 3,column = co_tx,ipady = _ipadx)
		LB_vet3 = Label(main_M_W, text = all_vt[2],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet3.grid(row = 3, column = co_vt, ipadx = 8)
		BT_vet3 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet3['command'] = partial (organiza_vetores,3)
		BT_vet3.grid(row = 3,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet4_text = Label(main_M_W, text = nom_vt[3] ,bg = cor_vt[3],font=(FONT_, 12))
		LB_vet4_text.grid(row = 4,column = co_tx,ipady = _ipadx)
		LB_vet4 = Label(main_M_W, text = all_vt[3],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet4.grid(row = 4, column = co_vt, ipadx = 8)
		BT_vet4 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet4['command'] = partial (organiza_vetores,4)
		BT_vet4.grid(row = 4,column = co_cb,padx = BT_padx,pady = BT_pady)
		
	else:
		
		LB_vet1_text = Label(main_M_W, text = nom_vt[0],bg = cor_vt[0],font=(FONT_, 12))
		LB_vet1_text.grid(row = 1,column = co_tx,ipady = _ipadx)
		LB_vet1 = Label(main_M_W, text = all_vt[0],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet1.grid(row = 1, column = co_vt, ipadx = 8)
		BT_vet1 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet1['command'] = partial (organiza_vetores,1)
		BT_vet1.grid(row = 1,column = co_cb,padx = BT_padx,pady = BT_pady)
	
		LB_vet2_text = Label(main_M_W, text = nom_vt[1] ,bg = cor_vt[1],font=(FONT_, 12))
		LB_vet2_text.grid(row = 2,column = co_tx,ipady = _ipadx)
		LB_vet2 = Label(main_M_W, text = all_vt[1],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet2.grid(row = 2, column = co_vt, ipadx = 8)
		BT_vet2 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet2['command'] = partial (organiza_vetores,2)
		BT_vet2.grid(row = 2,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet3_text = Label(main_M_W, text = nom_vt[2] ,bg = cor_vt[2],font=(FONT_, 12))
		LB_vet3_text.grid(row = 3,column = co_tx,ipady = _ipadx)
		LB_vet3 = Label(main_M_W, text = all_vt[2],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet3.grid(row = 3, column = co_vt, ipadx = 8)
		BT_vet3 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet3['command'] = partial (organiza_vetores,3)
		BT_vet3.grid(row = 3,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet4_text = Label(main_M_W, text = nom_vt[3] ,bg = cor_vt[3],font=(FONT_, 12))
		LB_vet4_text.grid(row = 4,column = co_tx,ipady = _ipadx)
		LB_vet4 = Label(main_M_W, text = all_vt[3],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet4.grid(row = 4, column = co_vt, ipadx = 8)
		BT_vet4 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet4['command'] = partial (organiza_vetores,4)
		BT_vet4.grid(row = 4,column = co_cb,padx = BT_padx,pady = BT_pady)
		
		LB_vet5_text = Label(main_M_W, text = nom_vt[4] ,bg = cor_vt[4],font=(FONT_, 12))
		LB_vet5_text.grid(row = 5,column = co_tx,ipady = _ipadx)
		LB_vet5 = Label(main_M_W, text = all_vt[4],bg = STD_2 ,fg = STD_1, font = (FONT_, 15))
		LB_vet5.grid(row = 5, column = co_vt, ipadx = 8)
		BT_vet5 = Button(main_M_W,text = '0°',bg = STD_1,fg = STD_2,font=(FONT_,10,TYPE_FONT),border = 0)
		BT_vet5['command'] = partial (organiza_vetores,5)
		BT_vet5.grid(row = 5,column = co_cb,padx = BT_padx,pady = BT_pady)
    
    
	def ProdEscalar():
		view_result(6)
		
	def ProdMisto():
		view_result(10)
		
	def ProdNum():
		view_result(3)
		
	def ProdVetorial():
		view_result(9)
		
	def ArParalelogramo():
		view_result(16)
	
	def ArTriangulo():
		view_result(15)
		
	def VoluParalelogramo():
		view_result(12)
	
	def VoluPrisma():
		view_result(13)
	
	def VoluTetraedro():
		view_result(14)
		
	###PRODUTOS
	MenuProdutos = Menubutton(main_M_W,text = "Produtos",width = 12,height = 1)
	MenuProdutos['font'] = (FONT_, 10, TYPE_FONT)
	MenuProdutos['bg'] = STD_1
	MenuProdutos['fg'] = STD_2
	MenuProdutos.grid(row = 1, column = 1, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	SubMProd = Menu(MenuProdutos,tearoff = 0,font = (FONT_, 10, TYPE_FONT))
	SubMProd['bg'] = STD_1
	SubMProd['fg'] = STD_2
	MenuProdutos.config(menu=SubMProd)
	SubMProd.add_command(label = "Escalar",command = ProdEscalar)
	SubMProd.add_command(label = "Numérico",command = ProdNum)
	if dim_vet == 3:
		SubMProd.add_command(label = "Misto",command = ProdMisto)
		SubMProd.add_command(label = "Vetorial",command = ProdVetorial)
	
	
	###ÁREAS
	MenuArea = Menubutton(main_M_W,text = "Áreas",width = 12)
	MenuArea['font'] = (FONT_,10,TYPE_FONT)
	MenuArea['bg'] = STD_1
	MenuArea['fg'] = STD_2
	MenuArea.grid(row = 3, column = 1, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	SubMArea = Menu(MenuArea,tearoff = 0,font = (FONT_, 10, TYPE_FONT))
	SubMArea['bg'] = STD_1
	SubMArea['fg'] = STD_2
	MenuArea.config(menu=SubMArea)
	if dim_vet == 3:
		SubMArea.add_command(label = "Paralelogramo",command = ArParalelogramo)
		SubMArea.add_command(label = "Triângulo",command = ArTriangulo)
	else:
		SubMVolume.add_command(label = "Apenas em Vetores 3D")
	
	
	###VOLUMES
	MenuVolume = Menubutton(main_M_W,text = "Volumes",width = 12)
	MenuVolume['font'] = (FONT_,10,TYPE_FONT)
	MenuVolume['bg'] = STD_1
	MenuVolume['fg'] = STD_2
	MenuVolume.grid(row = 2, column = 1, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	SubMVolume = Menu(MenuVolume,tearoff = 0,font = (FONT_, 10, TYPE_FONT))
	SubMVolume['bg'] = STD_1
	SubMVolume['fg'] = STD_2
	MenuVolume.config(menu=SubMVolume)
	if dim_vet == 3:
		SubMVolume.add_command(label = "Paralelogramo",command = VoluParalelogramo)
		SubMVolume.add_command(label = "Prisma",command = VoluPrisma)
		SubMVolume.add_command(label = "Tetraedro",command = VoluTetraedro)
	else:
		SubMVolume.add_command(label = "Apenas em Vetores 3D")
	
	
	#Botões de ação
	BT_new_vet = Button(main_M_W, text = "Novos Vetores",font = (FONT_, 10, TYPE_FONT), fg = STD_2,bg = STD_1)
	BT_new_vet["command"] = new_vets_mod
	BT_new_vet["border"] = 0
	BT_new_vet.grid(row = 0, column = 1, padx = 5, pady = 20)
	
	BT_view_vet = Button(main_M_W, text = "Visualizar",font = (FONT_, 10, TYPE_FONT), fg = STD_2,bg = STD_1)
	BT_view_vet["command"] = partial (view_result,0)
	BT_view_vet["border"] = 0
	BT_view_vet.grid(row = 0, column = 2, padx = 5, pady = 20, ipadx = 15)

	
	#Botões das Operações
	BT_adicao_main = Button (main_M_W, text = " Adição ", width = _width , height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_adicao_main['fg'] = STD_2
	BT_adicao_main['bg'] = STD_1
	BT_adicao_main['border'] = 0 
	BT_adicao_main["command"] = partial (view_result,1)
	BT_adicao_main.grid(row = 1, column = 2, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	BT_diferenca_main = Button (main_M_W, text = " Diferença ", width = _width, height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_diferenca_main['fg'] = STD_2
	BT_diferenca_main['bg'] = STD_1
	BT_diferenca_main['border'] = 0 
	BT_diferenca_main["command"] = partial (view_result,2)
	BT_diferenca_main.grid(row = 5, column = 2, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	BT_coplanar_main = Button (main_M_W, text = "Coplanaridade",width = _width, height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_coplanar_main['fg'] = STD_2
	BT_coplanar_main['bg'] = STD_1
	BT_coplanar_main['border'] = 0 
	BT_coplanar_main["command"] = partial (view_result,8)
	BT_coplanar_main.grid(row = 4, column = 2, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
    
	BT_norma_main = Button (main_M_W, text = " Norma ", width = _width, height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_norma_main['fg'] = STD_2
	BT_norma_main['bg'] = STD_1
	BT_norma_main['border'] = 0 
	BT_norma_main["command"] = partial (view_result,4)
	BT_norma_main.grid(row = 4, column = 1, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	BT_ortogonalidade_main = Button (main_M_W, text="Ortogonalidade",width=_width,height=1,font=(FONT_,10,TYPE_FONT))
	BT_ortogonalidade_main['fg'] = STD_2
	BT_ortogonalidade_main['bg'] = STD_1
	BT_ortogonalidade_main['border'] = 0 
	BT_ortogonalidade_main["command"] = partial (view_result,5)
	BT_ortogonalidade_main.grid(row = 5, column = 1, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	
	BT_angvet_main = Button (main_M_W, text = "Ângulo", width=_width,height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_angvet_main['fg'] = STD_2
	BT_angvet_main['bg'] = STD_1
	BT_angvet_main['border'] = 0 
	BT_angvet_main["command"] = partial (view_result,7)
	BT_angvet_main.grid(row = 2, column = 2, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	BT_paralelo_main = Button (main_M_W, text = "Projeção", width = _width, height = 1,font=(FONT_, 10,TYPE_FONT))
	BT_paralelo_main['fg'] = STD_2
	BT_paralelo_main['bg'] = STD_1
	BT_paralelo_main['border'] = 0 
	BT_paralelo_main["command"] = partial (view_result,11)
	BT_paralelo_main.grid(row = 3, column = 2, ipadx = _ipadx , ipady = _ipady, padx = _padx, pady = _pady)
	
	
	#Labels de entrada
	ET_num_prod = Entry(main_M_W,width = 5,font=(FONT_,15,TYPE_FONT))
	ET_num_prod.grid(row = 0, column = 4,padx = 10,pady = 10,ipadx = 10)
		
	
	
	main_M_W.mainloop()
	


#Entry_window()
Mod_2d_3d()

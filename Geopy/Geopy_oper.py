# -*- coding: utf-8 -*-
#  Geopy_oper.py
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



from Geopy_graf import *
from math import *

def Soma_oper(all_vt,nom_vt,cor_vt,seed):
	

	dim_vt = Verify_2d_3d(all_vt)
	
	vt_result = []
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	if dim_vt == 2:
		if len(seed) == 2:
			a=(sel_vt[0][0]+sel_vt[1][0])
			b=(sel_vt[0][1]+sel_vt[1][1])
			vt_result.append(a)
			vt_result.append(b)
	
		elif len(seed) == 3:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1])
			vt_result.append(a)
			vt_result.append(b)		
			
		elif len(seed) == 4:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0]+sel_vt[3][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1]+sel_vt[3][1])
			vt_result.append(a)
			vt_result.append(b)
		
		elif len(seed) == 5:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0]+sel_vt[3][0]+sel_vt[4][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1]+sel_vt[3][1]+sel_vt[4][1])
			vt_result.append(a)
			vt_result.append(b)
		
	else:
		if len(seed) == 2:
			a=(sel_vt[0][0]+sel_vt[1][0])
			b=(sel_vt[0][1]+sel_vt[1][1])
			c=(sel_vt[0][2]+sel_vt[1][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
	
		elif len(seed) == 3:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1])
			c=(sel_vt[0][2]+sel_vt[1][2]+sel_vt[2][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
		elif len(seed) == 4:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0]+sel_vt[3][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1]+sel_vt[3][1])
			c=(sel_vt[0][2]+sel_vt[1][2]+sel_vt[2][2]+sel_vt[3][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
		elif len(seed) == 5:
			a=(sel_vt[0][0]+sel_vt[1][0]+sel_vt[2][0]+sel_vt[3][0]+sel_vt[4][0])
			b=(sel_vt[0][1]+sel_vt[1][1]+sel_vt[2][1]+sel_vt[3][1]+sel_vt[4][1])
			c=(sel_vt[0][2]+sel_vt[1][2]+sel_vt[2][2]+sel_vt[3][2]+sel_vt[4][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
	return vt_result
	
	
def Difer_oper(all_vt,nom_vt,cor_vt,seed):
	

	dim_vt = Verify_2d_3d(all_vt)
	vt_result = []
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	if dim_vt == 2:
		if len(seed) == 2:
			a=(sel_vt[0][0])-(sel_vt[1][0])
			b=(sel_vt[0][1])-(sel_vt[1][1])
			vt_result.append(a)
			vt_result.append(b)
	
		elif len(seed) == 3:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1])
			vt_result.append(a)
			vt_result.append(b)
		
		elif len(seed) == 4:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0]-sel_vt[3][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1]-sel_vt[3][1])
			vt_result.append(a)
			vt_result.append(b)
	
		elif len(seed) == 5:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0]-sel_vt[3][0]-sel_vt[4][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1]-sel_vt[3][1]-sel_vt[4][1])
			vt_result.append(a)
			vt_result.append(b)
		
			
		
	else:
		if len(seed) == 2:
			a=(sel_vt[0][0]-sel_vt[1][0])
			b=(sel_vt[0][1]-sel_vt[1][1])
			c=(sel_vt[0][2]-sel_vt[1][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
		elif len(seed) == 3:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1])
			c=(sel_vt[0][2]-sel_vt[1][2]-sel_vt[2][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
		elif len(seed) == 4:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0]-sel_vt[3][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1]-sel_vt[3][1])
			c=(sel_vt[0][2]-sel_vt[1][2]-sel_vt[2][2]-sel_vt[3][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
		
		elif len(seed) == 5:
			a=(sel_vt[0][0]-sel_vt[1][0]-sel_vt[2][0]-sel_vt[3][0]-sel_vt[4][0])
			b=(sel_vt[0][1]-sel_vt[1][1]-sel_vt[2][1]-sel_vt[3][1]-sel_vt[4][1])
			c=(sel_vt[0][2]-sel_vt[1][2]-sel_vt[2][2]-sel_vt[3][2]-sel_vt[4][2])
			vt_result.append(a)
			vt_result.append(b)
			vt_result.append(c)
			
	return vt_result
	

def Norma(all_vt,nom_vt,cor_vt,seed):

	dim_vt = Verify_2d_3d(all_vt)
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	if dim_vt == 2:
		xpow = pow(sel_vt[0][0],2)
		ypow = pow(sel_vt[0][1],2)
		raiz_result = (xpow+ypow)
		
	else:
		xpow = pow(sel_vt[0][0],2)
		ypow = pow(sel_vt[0][1],2)
		zpow = pow(sel_vt[0][2],2)
		raiz_result = (xpow+ypow+zpow)
	
	return raiz_result


def Paralelismo(all_vt,nom_vt,cor_vt,seed):#????????????
	dim_vt = Verify_2d_3d(all_vt)
	
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	
	if dim_vt == 2:
		div_x = (float (sel_vt[0][0]) / floar(sel_vt[1][0]))
		div_y = (float (sel_vt[0][1]) / floar(sel_vt[1][1]))
		if div_x == div_y:
			return True
		else:
			return False
	else:
		div_x = (float (sel_vt[0][0]) / floar(sel_vt[1][0]))
		div_y = (float (sel_vt[0][1]) / floar(sel_vt[1][1]))
		div_z = (float (sel_vt[0][2]) / floar(sel_vt[1][2]))
		if div_x == div_y and div_x == div_z:
			return True
		else:
			return False


def Angulo(all_vt,nom_vt,cor_vt,seed):
	
	sel_seed = []
	prod_AB = Prod_escalar(all_vt,nom_vt,cor_vt,seed)
	sel_seed.append(seed[0])
	sel_seed.append(seed[1])
	module_A = Norma(all_vt,nom_vt,cor_vt,sel_seed)
	del(sel_seed[0])
	module_B = Norma(all_vt,nom_vt,cor_vt,sel_seed)
	raiz_multiply_module_AB = sqrt(module_A * module_B)
	coss_ang_in_rad = (prod_AB/raiz_multiply_module_AB)
	arco_ang_in_rad = acos(coss_ang_in_rad)
	ang_in_graus = Convert_rad_graus(arco_ang_in_rad)
	return ang_in_graus


def Prod_misto(all_vt,nom_vt,cor_vt,seed):

	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	opr_1 = sel_vt[0][0] * sel_vt[1][1] * sel_vt[2][2]
	opr_2 = sel_vt[0][1] * sel_vt[1][2] * sel_vt[2][0]
	opr_3 = sel_vt[0][2] * sel_vt[1][0] * sel_vt[2][1]
	opr_4 = sel_vt[0][2] * sel_vt[1][1] * sel_vt[2][0]
	opr_5 = sel_vt[0][0] * sel_vt[1][2] * sel_vt[2][1]
	opr_6 = sel_vt[0][1] * sel_vt[1][0] * sel_vt[2][2]
	opr_result = (opr_1+opr_2+opr_3-opr_4-opr_5-opr_6)
	return opr_result


def Prod_constante(all_vt,nom_vt,cor_vt,seed,num_oper):
	

	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	dim_vt = Verify_2d_3d(all_vt)
	x = 0
	y = 0
	z = 0
	result_vt = []

	if dim_vt == 2:
		x = (sel_vt[0][0])*(num_oper)
		y = (sel_vt[0][1])*(num_oper)
		result_vt.append(x)
		result_vt.append(y)

	else:
		x = (sel_vt[0][0])*(num_oper)
		y = (sel_vt[0][1])*(num_oper)
		z = (sel_vt[0][2])*(num_oper)
		result_vt.append(x)
		result_vt.append(y)
		result_vt.append(z)

	return result_vt


def Prod_escalar(all_vt,nom_vt,cor_vt,seed):
	
	dim_vt = Verify_2d_3d(all_vt)
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	if dim_vt == 2:
		prod_x = (sel_vt[0][0]*sel_vt[1][0])
		prod_y = (sel_vt[0][1]*sel_vt[1][1])
		prod = prod_x+prod_y
	else:
		prod_x = (sel_vt[0][0]*sel_vt[1][0])
		prod_y = (sel_vt[0][1]*sel_vt[1][1])
		prod_z = (sel_vt[0][2]*sel_vt[1][2])
		prod = prod_x+prod_y+prod_z
		
	return prod


def Prod_vetorial(all_vt,nom_vt,cor_vt,seed):

	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	vt_result = []
	op_i1 = (sel_vt[0][1] * sel_vt[1][2])
	op_i2 = (sel_vt[0][2] * sel_vt[1][1])
	op_j1 = (sel_vt[0][0] * sel_vt[1][2])
	op_j2 = (sel_vt[0][2] * sel_vt[1][0])
	op_k1 = (sel_vt[0][0] * sel_vt[1][1])
	op_k2 = (sel_vt[0][1] * sel_vt[1][0])
	vt_result.append(op_i1 - op_i2)
	vt_result.append(-op_j1 + op_j2)
	vt_result.append(op_k1 - op_k2)
	
	return vt_result
	

def Projecao(all_vt,nom_vt,cor_vt,seed):
	sel_vt, nom_sel, cor_sel = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	seed_ = []
	seed_.append(seed[1])
	seed_.append(seed[1])
	dim_vt = Verify_2d_3d(all_vt)
	if dim_vt == 2:
		VxU = Prod_escalar(all_vt,nom_vt,cor_vt,seed)
		UxU = Prod_escalar(all_vt,nom_vt,cor_vt,seed_)
		div = (VxU/UxU)
		proj = []
		proj.append(div*sel_vt[1][0])
		proj.append(div*sel_vt[1][1])
	else:
		VxU = Prod_escalar(all_vt,nom_vt,cor_vt,seed)
		UxU = Prod_escalar(all_vt,nom_vt,cor_vt,seed_)
		div = (VxU/UxU)
		proj = []
		proj.append(div*sel_vt[1][0])
		proj.append(div*sel_vt[1][1])
		proj.append(div*sel_vt[1][2])
		
	return proj
	
	
	
def AreaParalelogramo(all_vt,nom_vt,cor_vt,seed):
	prod_vt = Prod_vetorial(all_vt,nom_vt,cor_vt,seed)
	xpow = pow(prod_vt[0],2)
	ypow = pow(prod_vt[1],2)
	zpow = pow(prod_vt[2],2)
	raiz_result = (xpow+ypow+zpow)
	return raiz_result

def AreaTriangulo(all_vt,nom_vt,cor_vt,seed):
	prod_vt = Prod_vetorial(all_vt,nom_vt,cor_vt,seed)
	xpow = pow(prod_vt[0],2)
	ypow = pow(prod_vt[1],2)
	zpow = pow(prod_vt[2],2)
	raiz_result = (xpow+ypow+zpow)
	raiz = sqrt(raiz_result)
	resultado = raiz/2
	return resultado
	

def VolParalelogramo(all_vt,nom_vt,cor_vt,seed):
	Prod_Misto = Prod_misto(all_vt,nom_vt,cor_vt,seed)
	all_vt.append(Prod_Misto)
	seed_ = [5]
	if Prod_Misto < 0:
		Prod_Misto = Prod_Misto*-1
	#Mod_Misto = Norma(all_vt,nom_vt,cor_vt,seed)
	return Prod_Misto
	

def Coplanaridade(all_vt,nom_vt,cor_vt,seed):
	result = Prod_misto(all_vt,nom_vt,cor_vt,seed)
	if result == 0:
		return True
	else:
		return False


def Verify_2d_3d(all_vt):
	
	num_vt = len(all_vt)
	dim = 0
	if num_vt == 1:
		a = len(all_vt[0])
		if a == 2:
			dim =  2
		else:
			dim =  3
	if num_vt == 2:
		a = len(all_vt[0])
		b = len(all_vt[1])
		if a == 2 or b == 2:
			dim =  2
		else:
			dim =  3
	if num_vt == 3:
		a = len(all_vt[0])
		b = len(all_vt[1])
		c = len(all_vt[2])
		if a == 2 or b == 2 or c == 2:
			dim =  2
		else:
			dim =  3
	if num_vt == 4:
		a = len(all_vt[0])
		b = len(all_vt[1])
		c = len(all_vt[2])
		d = len(all_vt[3])
		if a == 2 or b == 2 or c == 2 or d == 2:
			dim =  2
		else:
			dim =  3
	if num_vt == 5:
		a = len(all_vt[0])
		b = len(all_vt[1])
		c = len(all_vt[2])
		d = len(all_vt[3])
		e = len(all_vt[3])
		if a == 2 or b == 2 or c == 2 or d == 2 or e == 2:
			dim =  2
		else:
			dim =  3
	return dim
	

def Convert_rad_graus(num_em_rad):
	
	
	graus=num_em_rad*180/pi

	return graus

# -*- coding: utf-8 -*-
#
#  Geopy_graf.py
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


from mpl_toolkits.mplot3d import Axes3D		
import matplotlib.pyplot as plt

TAM_A = 100
TAM_B = -100
COR_EIXO = '#000000'

def View_2d_vts(all_vt,nom_vt,cor_vt,seed,vt_result):
	
	all_sel_vt, nom_sel_vt, cor_sel_vt,  = Org_vet_f(all_vt,nom_vt,cor_vt,seed)
	
	if len(seed) == 1:
		plt.plot((0,all_sel_vt[0][0]),(0,all_sel_vt[0][1]),cor_sel_vt[0])
		plt.text(all_sel_vt[0][0],all_sel_vt[0][1],nom_sel_vt[0])
		
		
	if len(seed) == 2:
		plt.plot((0,all_sel_vt[0][0]),(0,all_sel_vt[0][1]),cor_sel_vt[0])
		plt.text(all_sel_vt[0][0],all_sel_vt[0][1],nom_sel_vt[0])
		
		plt.plot((0,all_sel_vt[1][0]),(0,all_sel_vt[1][1]),cor_sel_vt[1])
		plt.text(all_sel_vt[1][0],all_sel_vt[1][1],nom_sel_vt[1])
		
	
	if len(seed) == 3:
		plt.plot((0,all_sel_vt[0][0]),(0,all_sel_vt[0][1]),cor_sel_vt[0])
		plt.text(all_sel_vt[0][0],all_sel_vt[0][1],nom_sel_vt[0])
		
		plt.plot((0,all_sel_vt[1][0]),(0,all_sel_vt[1][1]),cor_sel_vt[1])
		plt.text(all_sel_vt[1][0],all_sel_vt[1][1],nom_sel_vt[1])
		
		plt.plot((0,all_sel_vt[2][0]),(0,all_sel_vt[2][1]),cor_sel_vt[2])
		plt.text(all_sel_vt[2][0],all_sel_vt[2][1],nom_sel_vt[2])
		
		
	if len(seed)  == 4:
		plt.plot((0,all_sel_vt[0][0]),(0,all_sel_vt[0][1]),cor_sel_vt[0])
		plt.text(all_sel_vt[0][0],all_sel_vt[0][1],nom_sel_vt[0])
		
		plt.plot((0,all_sel_vt[1][0]),(0,all_sel_vt[1][1]),cor_sel_vt[1])
		plt.text(all_sel_vt[1][0],all_sel_vt[1][1],nom_sel_vt[1])
		
		plt.plot((0,all_sel_vt[2][0]),(0,all_sel_vt[2][1]),cor_sel_vt[2])
		plt.text(all_sel_vt[2][0],all_sel_vt[2][1],nom_sel_vt[2])
		
		plt.plot((0,all_sel_vt[3][0]),(0,all_sel_vt[3][1]),cor_sel_vt[3])
		plt.text(all_sel_vt[3][0],all_sel_vt[3][1],nom_sel_vt[3])
		
		
	if len(seed) == 5:
		plt.plot((0,all_sel_vt[0][0]),(0,all_sel_vt[0][1]),cor_sel_vt[0])
		plt.text(all_sel_vt[0][0],all_sel_vt[0][1],nom_sel_vt[0])
		
		plt.plot((0,all_sel_vt[1][0]),(0,all_sel_vt[1][1]),cor_sel_vt[1])
		plt.text(all_sel_vt[1][0],all_sel_vt[1][1],nom_sel_vt[1])
		
		plt.plot((0,all_sel_vt[2][0]),(0,all_sel_vt[2][1]),cor_sel_vt[2])
		plt.text(all_sel_vt[2][0],all_sel_vt[2][1],nom_sel_vt[2])
		
		plt.plot((0,all_sel_vt[3][0]),(0,all_sel_vt[3][1]),cor_sel_vt[3])
		plt.text(all_sel_vt[3][0],all_sel_vt[3][1],nom_sel_vt[3])
		
		plt.plot((0,all_sel_vt[4][0]),(0,all_sel_vt[4][1]),cor_sel_vt[4])
		plt.text(all_sel_vt[4][0],all_sel_vt[4][1],nom_sel_vt[4])
	
	cont_vt_result = len(vt_result)
	if cont_vt_result != 0:
		if vt_result[2] == 1:
			plt.plot((0,vt_result[0]),(0,vt_result[1]),'k')
			plt.text(vt_result[0],vt_result[1],'r')
		
	
	
	plt.ylabel('EIXO Y')
	plt.xlabel('EIXO X')
	plt.axis((-10,10,-10,10))
	plt.plot((0,TAM_A),(0,0),'k--' )
	plt.plot((TAM_B,0),(0,0),'k--' )
	plt.plot((0,0),(TAM_A,0),'k--' )
	plt.plot((0,0),(TAM_B,0),'k--' )
	plt.grid(True)
	plt.show()


def View_3d_vts(all_vt,nome_vt,cor_vt,seed,vt_result):
	
	all_sel_vt, nom_sel_vt, cor_sel_vt,  = Org_vet_f(all_vt,nome_vt,cor_vt,seed)
	
	fig = plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	
	if len(seed) == 1:

		ax.text(all_sel_vt[0][0],all_sel_vt[0][1],all_sel_vt[0][2],nom_sel_vt[0])
		ax.plot_wireframe((all_sel_vt[0][0],0),(all_sel_vt[0][1],0),(all_sel_vt[0][2],0),color = cor_sel_vt[0])

	if len(seed) == 2:
		
		
		ax.text(all_sel_vt[0][0],all_sel_vt[0][1],all_sel_vt[0][2],nom_sel_vt[0])
		ax.plot_wireframe((all_sel_vt[0][0],0),(all_sel_vt[0][1],0),(all_sel_vt[0][2],0),color = cor_sel_vt[0])
		
		ax.text(all_sel_vt[1][0],all_sel_vt[1][1],all_sel_vt[1][2],nom_sel_vt[1])
		ax.plot_wireframe((all_sel_vt[1][0],0),(all_sel_vt[1][1],0),(all_sel_vt[1][2],0),color = cor_sel_vt[1])

	if  len(seed)== 3:
		
		ax.text(all_sel_vt[0][0],all_sel_vt[0][1],all_sel_vt[0][2],nom_sel_vt[0])
		ax.plot_wireframe((all_sel_vt[0][0],0),(all_sel_vt[0][1],0),(all_sel_vt[0][2],0),color = cor_sel_vt[0])
		
		ax.text(all_sel_vt[1][0],all_sel_vt[1][1],all_sel_vt[1][2],nom_sel_vt[1])
		ax.plot_wireframe((all_sel_vt[1][0],0),(all_sel_vt[1][1],0),(all_sel_vt[1][2],0),color = cor_sel_vt[1])
		
		ax.text(all_sel_vt[2][0],all_sel_vt[2][1],all_sel_vt[2][2],nom_sel_vt[2])
		ax.plot_wireframe((all_sel_vt[2][0],0),(all_sel_vt[2][1],0),(all_sel_vt[2][2],0),color = cor_sel_vt[2])
		
	if  len(seed)== 4:
		ax.text(all_sel_vt[0][0],all_sel_vt[0][1],all_sel_vt[0][2],nom_sel_vt[0])
		ax.plot_wireframe((all_sel_vt[0][0],0),(all_sel_vt[0][1],0),(all_sel_vt[0][2],0),color = cor_sel_vt[0])
		
		ax.text(all_sel_vt[1][0],all_sel_vt[1][1],all_sel_vt[1][2],nom_sel_vt[1])
		ax.plot_wireframe((all_sel_vt[1][0],0),(all_sel_vt[1][1],0),(all_sel_vt[1][2],0),color = cor_sel_vt[1])
		
		ax.text(all_sel_vt[2][0],all_sel_vt[2][1],all_sel_vt[2][2],nom_sel_vt[2])
		ax.plot_wireframe((all_sel_vt[2][0],0),(all_sel_vt[2][1],0),(all_sel_vt[2][2],0),color = cor_sel_vt[2])
	
		ax.text(all_sel_vt[3][0],all_sel_vt[3][1],all_sel_vt[3][2],nom_sel_vt[3])
		ax.plot_wireframe((all_sel_vt[3][0],0),(all_sel_vt[3][1],0),(all_sel_vt[3][2],0),color = cor_sel_vt[3])

	if  len(seed)== 5:
		
		
		ax.text(all_sel_vt[0][0],all_sel_vt[0][1],all_sel_vt[0][2],nom_sel_vt[0])
		ax.plot_wireframe((all_sel_vt[0][0],0),(all_sel_vt[0][1],0),(all_sel_vt[0][2],0),color = cor_sel_vt[0])
		
		ax.text(all_sel_vt[1][0],all_sel_vt[1][1],all_sel_vt[1][2],nom_sel_vt[1])
		ax.plot_wireframe((all_sel_vt[1][0],0),(all_sel_vt[1][1],0),(all_sel_vt[1][2],0),color = cor_sel_vt[1])
		
		ax.text(all_sel_vt[2][0],all_sel_vt[2][1],all_sel_vt[2][2],nom_sel_vt[2])
		ax.plot_wireframe((all_sel_vt[2][0],0),(all_sel_vt[2][1],0),(all_sel_vt[2][2],0),color = cor_sel_vt[2])
	
		ax.text(all_sel_vt[3][0],all_sel_vt[3][1],all_sel_vt[3][2],nom_sel_vt[3])
		ax.plot_wireframe((all_sel_vt[3][0],0),(all_sel_vt[3][1],0),(all_sel_vt[3][2],0),color = cor_sel_vt[3])
		
		ax.text(all_sel_vt[4][0],all_sel_vt[4][1],all_sel_vt[4][2],nom_sel_vt[3])
		ax.plot_wireframe((all_sel_vt[4][0],0),(all_sel_vt[4][1],0),(all_sel_vt[4][2],0),color = cor_sel_vt[4])
	
	
	cont_vt_result = len(vt_result)
	if cont_vt_result != 0:
		if vt_result[3] == 0:
			ax.text(vt_result[0],vt_result[1],vt_result[2],'r')
			ax.plot_wireframe((vt_result[0],0),(vt_result[1],0),(vt_result[2],0),color = 'k')
		
	ax.set(ylabel='Eixo X', xlabel='Eixo Y', zlabel='Eixo Z')
	plt.axis((-8,8,-8,8))
	plt.plot((0,TAM_A),(0,0),'k--')
	plt.plot((TAM_B,0),(0,0),'k--')
	plt.plot((0,0),(TAM_A,0),'k--')
	plt.plot((0,0),(TAM_B,0),'k--')
	plt.plot((0,0),(0,0),(0,100),'k--')
	plt.grid(True)
	plt.show()


def Select_view_dim(all_vt,nom_vt,cor_vt,seed,dimencao_vets):
	vt_result =[]
	if dimencao_vets == 2:
		View_2d_vts(all_vt,nom_vt,cor_vt,seed,vt_result)
	else:
		View_3d_vts(all_vt,nom_vt,cor_vt,seed,vt_result)


def Org_vet_f(all_vt,nom_vt,cor_vt,seed):
	
	sel_vet = []
	sel_cor = []
	sel_nom = []
	if len(seed) == 1:
		 
		if seed[0] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[0] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[0] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[0] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[0] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
			
	if len(seed) == 2:
		 
		if seed[0] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[0] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
		
		if seed[0] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[0] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[0] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
	
		if seed[1] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[1] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[1] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[1] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[1] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
	
	if len(seed) == 3:
		 
		if seed[0] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[0] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[0] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[0] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[0] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
			
		if seed[1] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[1] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[1] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[1] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[1] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
	
		if seed[2] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[2] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[2] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[2] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[2] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
	
	if len(seed) == 4:
		 
		if seed[0] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[0] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[0] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[0] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[0] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
			
		if seed[1] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[1] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[1] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[1] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[1] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
	
		if seed[2] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[2] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[2] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[2] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[2] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
		
		if seed[3] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[3] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[3] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[3] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[3] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
	
	if len(seed) == 5:
		 
		if seed[0] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[0] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[0] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[0] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[0] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
			
		if seed[1] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[1] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[1] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[1] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[1] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
	
		if seed[2] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[2] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[2] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[2] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[2] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
		
		if seed[3] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[3] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[3] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[3] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[3] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
			
			
		if seed[4] == 1:
			sel_vet.append(all_vt[0])
			sel_cor.append(cor_vt[0])
			sel_nom.append(nom_vt[0])
			
		if seed[4] == 2:
			sel_vet.append(all_vt[1])
			sel_cor.append(cor_vt[1])
			sel_nom.append(nom_vt[1])
			
		if seed[4] == 3:
			sel_vet.append(all_vt[2])
			sel_cor.append(cor_vt[2])
			sel_nom.append(nom_vt[2])
			
		if seed[4] == 4:
			sel_vet.append(all_vt[3])
			sel_cor.append(cor_vt[3])
			sel_nom.append(nom_vt[3])
			
		if seed[4] == 5:
			sel_vet.append(all_vt[4])
			sel_cor.append(cor_vt[4])
			sel_nom.append(nom_vt[4])
	
	return sel_vet,sel_nom,sel_cor


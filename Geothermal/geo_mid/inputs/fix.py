#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas
#Ejecutamos un par de cosas para que el modelo cambie bien


#Añadimos reservas al csv, a todos los generadores que no son viento y PV
tab = pandas.read_table('generation_projects_info.tab')
tab['gen_can_provide_cap_reserves'] = [1 if tab['gen_tech'][i] not in ['PV','Wind', 'mini_hydro', 'Hydro-RoR'] else 0 for i in tab.index]
tab.to_csv('generation_projects_info.tab', index=False, sep='\t')

#Limitamos los variable capacity factors a <= 1
tab = pandas.read_table('variable_capacity_factors.tab')
for i in tab.index:
	if tab.ix[i,2]>=1.0:
		tab.ix[i,2] = 1.0

tab.to_csv('variable_capacity_factors.tab', index=False, sep='\t')

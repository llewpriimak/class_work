# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:21:01 2021

@author: Masa Prodanovic


Installing PyVista 2D/3D visualizer.

On a Mac, please open Terminal (can be found in Utilities).
On a Windows machine, from Anaconda Navigator open Powershell Prompt.
In both cases you will need to run the commands as an administrator of your 
computer (installation requires ability to save things in system files).

Note that "pip" is one of the main Python utilities for installation of new
components (though not the only one). It has to be used in a 
terminal/console/Unix-type shell such as the one opened above.

Then type in the following (wait for each command to execute)
    pip install vtk
    pip install pyvista
        
    
Alternative installation using conda (sometimes stalls, in my experience)    
    conda install -c conda-forge vtk
    conda install -c conda-forge pyvista
"""

#%% Simple Pyvista test using a geometric object. 
# A separate window should open.
import pyvista as pv
sphere = pv.Sphere()
sphere.plot()

# You can learn more about other pre-existing geometric objects on this page:
# https://docs.pyvista.org/examples/00-load/create-geometric-objects.html

#%% Point clouds

import numpy as np
import pyvista as pv

# Create some very simple point data. In this case x, y, z are
# corners of a [0,1] by [0,1] by [0,1] box

# PyVista needs to be provided with a 2D numpy array whose COLUMNS
# are x, y and z coordinates of those box vertices respectively.
# Alternatively, three coordinates of each row define a vertex 

xyz = np.array([[0,0,0],[0,1,0],[1,0,0],[1,1,0],
                [0,0,1],[0,1,1],[1,0,1],[1,1,1]])
point_cloud = pv.PolyData(xyz)                

# Make data array using z values (0 and 1 in our case)
# and convert those to some other values (arbitrarily)
data = xyz[:,2]

# Add that data to the mesh. The name for it is "data", feel free to change.
point_cloud["data"] = data

point_cloud.plot()



#%% Surface plots


## Create data

import numpy as np
import pyvista as pv

# We will first play with meshgrid function and creating regular 2D arrays of coordinates
# You can change how many points you want the domain to have here
nx = 20
ny = 20

# Domain [-2,2] by [-2,2]
# Recall that linspace is run as np.linspace(lowlimit,highlimit,spacing)
# and provides equally spaces points between the limits.
# You can, of course, use np.arange function as well (if you want to specify spacing)
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)

X, Y = np.meshgrid(x, y)
# print(X)
# print(Y)

# you can now calculate values for any function Z=f(x,y) using coordinates
# stored in matrices X and Y. For instance f(x,y) = 2-x**2-y**2

#Z = 2-X**2-Y**2                 # f(x,y) = 2-x**2-y**2
Z = -5*X*(np.exp(- X**2 - Y**2)) # f(x,y) = -5*x*exp(-x**2-y**2)

## Create and plot structured grid using PyVista
surface_grid = pv.StructuredGrid(X, Y, Z)

# This function will run and open a separate window and
# show the surface using default settings:
surface_grid.plot()


# I prefer white background instead of default gray, 
# and this theme sets it. Predefined themes: 
# https://docs.pyvista.org/api/plotting/_autosummary/pyvista.set_plot_theme.html   
pv.set_plot_theme('document') #this sets the theme for all plots

# More informations on the settings for plot function are here:
# https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html
surface_grid.plot(show_bounds = 1, show_axes = 1, show_edges = 0, 
                  window_size=[800,800],color=[191/255.0,87/255.0,0])

#%% Questions to play with.
'''
1. Change the number of points from nx,ny set above to different numbers & what happened to the plot?
Which parameter in surface_grid.plot() above do you need to change?



'''

#%% Contour plots

#Contours are lines that indicate constant values in the elevation function.
# They are typically plot when hiking, and in subsurface they indicate
# depths (of a reservoir) and not height. 
# If plotted as a 2D projection in a plane, we can go to our friend matplotlib
# for plotting.


import matplotlib.pyplot as plt
# replot X,Y,Z defined above with 2D contours
fig = plt.figure() 
            
levels = np.linspace(-2,2,10) # equally spaced contours from -2 to 2
C=plt.contour(X,Y,Z,levels,cmap='rainbow')
plt.colorbar()

# Dressing the plot up
# contours specifications

plt.clabel(C, inline=1, fontsize=10)

#enforce equal axis by changing box limits
plt.axis('equal')
plt.axis('tight')
plt.show()
#Let's save this figure. Try both options below and see the difference
#in figure quality.
fig.savefig('Contours.png')
#fig.savefig('Contours.png',dpi=300,bbox_inches='tight')

#%%
'''
Assignment: Create a surface and contour plot of function z=f(x,y)
[-5,5] by [-5,5]. Take a pick to plot from any of the choices below.

(01) f(x,y,) = x*y**3-y*x**3
(02) f(x,y) = (x**2+3*y**2)*exp(-x**2-y**2)
(03) f(x,y) = -1/(x**2+y**2) 
(04) f(x,y) = cos(abs(x)+abs(y))

- Use at least 500 points in each direction to discretize 
domain and create the grid.
- Make the surface plot blue and without grid lines.
- For contour plot, specify contour levels to go from minimum and 
maximum Z values on the entire domain and include at 
least 15 contour levels.
- Pick a colormap you like
 
'''

def my_plot():
    nx = 500
    ny = 500
    x = np.linspace(-5,5,nx)
    y = np.linspace(-5,5,ny)
    X,Y = np.meshgrid(x,y)
    Z = (X**2+3*Y**2)*np.exp(-X**2-Y**2)
    surface_grid = pv.StructuredGrid(X,Y,Z)
    surface_grid.plot()

my_plot()

## Create data

import numpy as np
import pyvista as pv

# We will first play with meshgrid function and creating regular 2D arrays of coordinates
# You can change how many points you want the domain to have here
nx = 50
ny = 50

# Domain [-5,5] by [-5,5]
# Recall that linspace is run as np.linspace(lowlimit,highlimit,spacing)
# and provides equally spaces points between the limits.
# You can, of course, use np.arange function as well (if you want to specify spacing)
x = np.linspace(-5, 5, nx)
y = np.linspace(-5, 5, ny)

X, Y = np.meshgrid(x, y)
#print(X)
#print(Y)

# you can now calculate values for any function Z=f(x,y) using coordinates
# stored in matrices X and Y. For instance f(x,y) = 2-x**2-y**2

#Z = 2-X**2-Y**                  # f(x,y) = 2-x**2-y**2
Z = np.cos(np.abs(X)+np.abs(Y)) 

## Create and plot structured grid using PyVista
surface_grid = pv.StructuredGrid(X, Y, Z)

# This function will run and open a separate window and
# show the surface using default settings:
# surface_grid.plot()


# I prefer white background instead of default gray, 
# and this theme sets it. Predefined themes: 
# https://docs.pyvista.org/api/plotting/_autosummary/pyvista.set_plot_theme.html   
pv.set_plot_theme('document') #this sets the theme for all plots

# More informations on the settings for plot function are here:
# https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html
surface_grid.plot(show_bounds = 0, show_axes = 1, show_edges = 1, 
                  window_size=[800,800],color=[24/255.0,91/255.0,150/255.0])

#%%
import matplotlib.pyplot as plt
# replot X,Y,Z defined above with 2D contours
fig = plt.figure() 
            
levels = np.linspace(-2,2,15) # equally spaced contours from -2 to 2
C=plt.contour(X,Y,Z,cmap='rainbow')

# Dressing the plot up
# contours specifications

plt.clabel(C, inline=1, fontsize=10)

#enforce equal axis by changing box limits
plt.axis('equal')
plt.axis('tight')
#%% Cool Mount St. Helens example that comes with PyVista

import pyvista as pv
from pyvista import examples

mesh = examples.download_st_helens()
warped = mesh.warp_by_scalar('Elevation')
surf = warped.extract_surface().triangulate()
surf = surf.decimate_pro(0.75)  # reduce the density of the mesh by 75%
surf.plot(cmap='gist_earth')


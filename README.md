# Sugarcane-AI-Interface
This is web based AI system interface 


Json for map view
csv for live data

convert csv to json when display map view

Json:{

    id: 1
    time: "asd"
        pos {
            lan: 12
            lon:32
        }
        image: 1212.jpag
    numberOfCane: 2
}


real GPS location generator

--# Sugarcane-AI-Interface
This is web based AI system interface 

0. change py to real gps data generator.

1. set up the basic mapviews (Choropleth Map)
2. fitch data from csv to map (convert database if needed)
3. 

2 ways of showing the map:

1. show clean map, display pin when odd number shows
2. show map with full of color cubes 

----update by 2.1-----
At this stage, I finish the 50% of choropleth map with D3,
I realized the d3 choropleth draw the map and block, then change the colour is not what I need.

I want use D3 load csv data, display mark on real google map.

PS: my business plan:
this is why I use google map istead of draw our own shap of map,
because the client can be the machine companly, the machine can be located on anywhere on the earth.
the AI system can be a optional module for machine, the controller will be direact connect to the AI system, hence the machine can auto adjust the angle of pan.

--------ends-----------

the rest can be done by use js. 
1. fitch data from database
2. generate real gps location (check)
3. use if fuction {
    if the number is below 3: return red color
    if the number is between 4 - 12, return green.
    if the number is above 12: return purpol
}
4. read line of database ForEach():
    draw box ( lat, lng)
    fill color (function(number));
    (optional: rise flg & show picture).
5. show sidebar for map display
6. more gauges

Bigger question:
what type of data input?
host web online
enbad web in tablet
business road map

------new-------
I should work:
in map view, load csv file before show map view.


---------Apr 19 update---------
now, I can input manual csv data to show rectengal on map,
I can display different color based on number
add a user input for color and rectangle size.


/// testr

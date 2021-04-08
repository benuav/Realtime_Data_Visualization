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

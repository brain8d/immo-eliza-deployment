import folium
import pandas as pd

data = pd.read_csv('data/properties.csv')



def maps(zipcode,size_sqm,type):

    map = folium.Map(location=[50.850346, 4.351721], zoom_start=12)

    last_location_add = []
    count = 0
    count_red = 0
    count_orange = 0
    count_green = 0
    count_blue = 0
    count_apartment = 0
    count_black = 0
    count_house = 0

    for index, row in data.iterrows():

        if row['property_type'] == type:
            if row['zip_code'] == zipcode:
                if(size_sqm-10) <= row["total_area_sqm"] <=(size_sqm+10):


                    
                    if pd.notna(row['latitude']) and pd.notna(row['longitude']):
                        color = 'black'
                        icon = 'house'
                        count += 1
                        if row['price'] <= 800000:
                            color = 'blue'
                        if row['price'] <= 600000:
                            color = 'green'
                        if row['price'] <= 400000:
                            color = 'orange'
                        if row['price'] <= 200000:
                            color = 'red'
                        if row['property_type'] == 'APARTMENT':
                            icon = 'building'

                        #if(size_sqm-10) <= row["total_area_sqm"] <=(size_sqm+10):
                        #    icon = "star"
                        
                        coords = [row['latitude'], row['longitude']]
                        folium.Marker(coords, tooltip="Click for More", popup=(f"\nID:{row['id']}"
                                                                            f"\nPrice:{row['price']}"
                                                                            f"\nEnergy:{row['epc']}"
                                                                            f"\nPostal:{row['zip_code']}"
                                                                            f"\nBedrooms:{row['nbr_bedrooms']}"
                                                                            f"\nSurface:{row['total_area_sqm']}"),
                                    icon=folium.Icon(icon=icon, prefix='fa', color=color)).add_to(map)
                        if icon == 'building':
                            count_apartment += 1
                        if icon == 'house':
                            count_house += 1
                        if color == 'blue':
                            count_blue += 1
                        if color == 'green':
                            count_green += 1
                        if color == 'orange':
                            count_orange += 1
                        if color == 'red':
                            count_red += 1
                        if color == 'black':
                            count_black += 1

                        last_location_add = row['latitude'], row['longitude']



    legenda_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 160px; height: 220px; 
     border:2px solid grey; z-index:9999; font-size:14px; background-color: white;
     "><br>&nbsp; <i class="fa fa-building" style="color:black"></i> Apartments &nbsp; <br>
      &nbsp; <i class="fa fa-house" style="color:black"></i> Houses &nbsp; <br>
      <br>
      &nbsp; <style="color:black"></i> Prices: &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:blue"></i> <= 200k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:green"></i> > 200k and <= 400k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:orange"></i> > 400k and <= 600k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:red"></i> > 600k and <= 800k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:black"></i> > 800k &nbsp; 
     </div>
     '''


    print(f"Total of Houses and Apartments: {count}")
    print(f"Total of Houses: {count_house}")
    print(f"% of Houses: {count_house/count*100:.2f}%")
    print(f"Total of Apartments: {count_apartment}")
    print(f"% of Apartments: {count_apartment/count*100:.2f}%")

    print(f"Total of Houses and Apartments Price less than 200k: {count_blue}")
    print(
        f"% of Houses and Apartments Price less than 200k: {count_blue/count*100:.2f}%")

    print(f"% of Houses and Apartments Price between 200k to 400k: {count_green}")
    print(
        f"Total of Houses and Apartments Price between 200k to 400k: {count_green/count*100:.2f}%")

    print(
        f"Total of Houses and Apartments Price between 600k to 800k: {count_orange}")
    print(
        f"% of Houses and Apartments Price between 600k to 800k: {count_orange/count*100:.2f}%")

    print(
        f"Total of Houses and Apartments Price between 600k to 800k: {count_red}")
    print(
        f"% of Houses and Apartments Price between 600k to 800k: {count_red/count*100:.2f}%")

    print(f"Total of Houses and Apartments Price More than 800k: {count_black}")
    print(
        f"% of Houses and Apartments Price More than 800k: {count_black/count*100:.2f}%")

    map.location = last_location_add
    map.get_root().html.add_child(folium.Element(legenda_html))
    #map.show_in_browser()
    return map


def maps_neighborhood(zipcode):

    map = folium.Map(location=[50.850346, 4.351721], zoom_start=12)

    last_location_add = []
    count = 0
    count_red = 0
    count_orange = 0
    count_green = 0
    count_blue = 0
    count_apartment = 0
    count_black = 0
    count_house = 0

    for index, row in data.iterrows():
        if row['zip_code'] == zipcode:             
            if pd.notna(row['latitude']) and pd.notna(row['longitude']):
                color = 'black'
                icon = 'house'
                count += 1
                if row['price'] <= 800000:
                    color = 'blue'
                if row['price'] <= 600000:
                    color = 'green'
                if row['price'] <= 400000:
                    color = 'orange'
                if row['price'] <= 200000:
                    color = 'red'
                if row['property_type'] == 'APARTMENT':
                    icon = 'building'
                
                coords = [row['latitude'], row['longitude']]
                folium.Marker(coords, tooltip="Click for More", popup=(f"\nID:{row['id']}"
                                                                    f"\nPrice:{row['price']}"
                                                                    f"\nEnergy:{row['epc']}"
                                                                    f"\nPostal:{row['zip_code']}"
                                                                    f"\nBedrooms:{row['nbr_bedrooms']}"
                                                                    f"\nSurface:{row['total_area_sqm']}"),
                            icon=folium.Icon(icon=icon, prefix='fa', color=color)).add_to(map)
                if icon == 'building':
                    count_apartment += 1
                if icon == 'house':
                    count_house += 1
                if color == 'blue':
                    count_blue += 1
                if color == 'green':
                    count_green += 1
                if color == 'orange':
                    count_orange += 1
                if color == 'red':
                    count_red += 1
                if color == 'black':
                    count_black += 1

                last_location_add = row['latitude'], row['longitude']



    legenda_html = '''
     <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 160px; height: 220px; 
     border:2px solid grey; z-index:9999; font-size:14px; background-color: white;
     "><br>&nbsp; <i class="fa fa-building" style="color:black"></i> Apartments &nbsp; <br>
      &nbsp; <i class="fa fa-house" style="color:black"></i> Houses &nbsp; <br>
      <br>
      &nbsp; <style="color:black"></i> Prices: &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:blue"></i> <= 200k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:green"></i> > 200k and <= 400k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:orange"></i> > 400k and <= 600k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:red"></i> > 600k and <= 800k &nbsp; <br>
      &nbsp; <i class="fa fa-map-marker" style="color:black"></i> > 800k &nbsp; 
     </div>
     '''


    print(f"Total of Houses and Apartments: {count}")
    print(f"Total of Houses: {count_house}")
    print(f"% of Houses: {count_house/count*100:.2f}%")
    print(f"Total of Apartments: {count_apartment}")
    print(f"% of Apartments: {count_apartment/count*100:.2f}%")

    print(f"Total of Houses and Apartments Price less than 200k: {count_blue}")
    print(
        f"% of Houses and Apartments Price less than 200k: {count_blue/count*100:.2f}%")

    print(f"% of Houses and Apartments Price between 200k to 400k: {count_green}")
    print(
        f"Total of Houses and Apartments Price between 200k to 400k: {count_green/count*100:.2f}%")

    print(
        f"Total of Houses and Apartments Price between 600k to 800k: {count_orange}")
    print(
        f"% of Houses and Apartments Price between 600k to 800k: {count_orange/count*100:.2f}%")

    print(
        f"Total of Houses and Apartments Price between 600k to 800k: {count_red}")
    print(
        f"% of Houses and Apartments Price between 600k to 800k: {count_red/count*100:.2f}%")

    print(f"Total of Houses and Apartments Price More than 800k: {count_black}")
    print(
        f"% of Houses and Apartments Price More than 800k: {count_black/count*100:.2f}%")

    map.location = last_location_add
    map.get_root().html.add_child(folium.Element(legenda_html))
    #map.show_in_browser()
    return map
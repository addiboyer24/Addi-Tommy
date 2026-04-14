import folium

# Create a map centered on the US East Coast
m = folium.Map(location=[40.7, -74.0], zoom_start=6)

# Add city markers
folium.Marker([40.7128, -74.0060], popup='New York').add_to(m)
folium.Marker([40.7430, -74.0324], popup='Hoboken').add_to(m)
folium.Marker([46.8722,-113.9940], popup='Missoula' ).add_to(m)
folium.Marker([45.76698,9.33934], popup='Dolzago, Italy (Tomasso)' ).add_to(m)


# Save to HTML file
m.save('us_cities_map.html')
print("Map saved as us_cities_map.html")
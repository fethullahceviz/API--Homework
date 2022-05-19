import requests
import csv

apiKey='qy7cWu1jwNn98Hv4PzDfgYbi6UEF5f6cpyYlh14W'

my_responses = []
for i in range(1,31):
    if i >=10:
        d='2016-07-'+f"{i}"
    else:
        d='2016-07-0'+f"{i}"
        
    my_links = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='f"{d}"+'&end_date='f"{d}"
    respons = requests.get(my_links,params={'api_Key':apiKey})
    #number of asteroids for today  
    x=len(respons.json()['near_earth_objects'][f"{d}"]) 
    print("Day of astreoid number"+ f"{x}")

    if  x!=0:
        print('got response from {}'.format(d))
    
        for _ in range(x):
            pothaz=respons.json()['near_earth_objects'][f"{d}"][_]['is_potentially_hazardous_asteroid']
            #print(elementcount)

            if pothaz==True:                
                my_responses.append([respons.json()['near_earth_objects'][f"{d}"][_]]) 
            else:
                pass
    else:
        print("No asteroids found for this"+ f"{d}" +"date")


with open('astroid.csv', 'w', newline='\n') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerows(my_responses)
        print("astroid.csv file created")
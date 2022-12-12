import requests

lista= [{'depth': '-0.5m', 'Temperature': [30.62, 30.76, 30.98, 30.96, 31.06, 31.16, 31.18, 31.25, 31.44], 
'pH': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0], 
'Dissolve(d Oxygen Concentration ': [7.14, 7.11, 7.1, 7.08, 7.08, 7.06, 7.08, 7.05, 7.04], 
'Dissolved Oxygen Saturation ': [95.6, 95.5, 95.6, 95.5, 95.7, 95.6, 95.8, 95.5, 95.5], 
'Conductivity ': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
'Turbidity': [4.6, 4.6, 4.3, 4.4, 4.2, 4.5, 3.8, 4.4, 4.3],
 'Chlorophyll-a ': [13.92, 17.2, 12.07, 19.23, 6.4, 11.76, 15.86, 12.77, 7.26], 
 'Total Dissolved Solids ': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
 'Salinity ': [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 
 'Bromide  ': []},
 {'depth': '-1.0m', 
 'Temperature': [30.69, 30.76, 30.96, 31.07, 31.19, 31.17, 31.25, 31.48], 
 'pH': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
 'Dissolved Oxygen Concentration ': [7.14, 7.12, 7.11, 7.08, 7.05, 7.08, 7.07, 7.04], 
 'Dissolved Oxygen Saturation ': [95.6, 95.6, 95.8, 95.6, 95.3, 95.7, 95.6, 95.7],
  'Conductivity ': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
  'Turbidity': [3.8, 5.2, 3.9, 5.0, 4.3, 3.9, 4.0, 4.5], 
  'Chlorophyll-a ': [9.23, 11.39, 9.09, 6.89, 6.86, 7.33, 13.6, 9.6], 
  'Total Dissolved Solids ': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
  'Salinity ': [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01], 
  'Bromide  ': []}, {'parameter': 'weather'}]


listb ={'Temperature': [29.4, 29.5, 29.6], 
'pH': [7.78, 7.72, 7.66], 
'Dissolved Oxygen Concentration': [3.6, 2.76, 2.26], 
'Dissolved Oxygen Saturation ': [47.2, 36.2, 29.7], 
'Conductivity': [436.0, 439.0, 440.0], 
'Turbidity': [71.9, 71.9, 71.9], 
'Chlorophyll-a ': [18.95, 19.57, 20.44], 
'Total Dissolved Solids': [261.0, 263.0, 263.0], 
'Salinity': [0.19, 0.19, 0.19], 
'Bromide': []}

listc= [{'depth': '-0.5m', 'Temperature': [26.0, 26.0, 26.0, 26.0, 26.0, 26.0, 26.0, 20.0], 'pH': [12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 10.0], 'Dissolved Oxygen Concentration ': [10.5, 10.5, 10.5, 10.5, 10.5, 10.5], 'Dissolved Oxygen Saturation ': [3.2, 3.2, 3.2, 3.2, 3.2], 'Conductivity ': 
[3.2], 'Turbidity': [3.2], 'Chlorophyll-a ': [56.0, 56.0, 56.0, 56.0], 'Total Dissolved Solids ': [299.0, 299.0, 299.0], 'Salinity ': [1.8, 1.8], 'Bromide  ': []}, {'depth': '-1.0m', 'Temperature': [26.0, 26.0, 26.0], 'pH': [12.0, 12.0, 12.0], 'Dissolved Oxygen Concentration ': [10.5, 10.5, 10.5], 'Dissolved Oxygen Saturation ': [3.2, 3.2, 3.2], 'Conductivity ': [3.2, 3.2], 'Turbidity': [3.2], 'Chlorophyll-a ': [56.0, 56.0, 56.0], 'Total Dissolved Solids ': [299.0, 299.0, 299.0], 'Salinity ': [1.8, 1.8, 1.8], 'Bromide  ': []}, {'depth': '-1.5m', 'Temperature': [20.0, 20.0], 'pH': [10.0, 10.0], 'Dissolved Oxygen Concentration ': [10.5, 10.5], 'Dissolved Oxygen Saturation ': [3.2, 3.2], 'Conductivity ': [3.2, 3.2], 'Turbidity': [3.2, 3.2], 'Chlorophyll-a ': [56.0, 56.0], 'Total Dissolved Solids ': [299.0, 299.0], 'Salinity ': [1.8, 1.8], 'Bromide  ': []}, {'depth': '-2.0m', 'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'depth': '-2.5m', 'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'depth': '-3.0m', 'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'depth': '-3.5m', 'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'depth': '-4.0m', 'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'depth': '-4.5m', 
'Temperature': [], 'pH': [], 'Dissolved Oxygen Concentration ': [], 'Dissolved Oxygen Saturation ': [], 'Conductivity ': [], 'Turbidity': [], 
'Chlorophyll-a ': [], 'Total Dissolved Solids ': [], 'Salinity ': [], 'Bromide  ': []}, {'parameter': 'weather'}]

def test():
    listval = []

    no_of_depths = len(lista)-1
    #print(no_of_depths)

    outlist = list(list(lista[0].items())[1][1]) # to get the number of record_time   
    no_record = len(outlist)
    
    info = []

    
    for i in range(no_record):
        dc = 1
        try:
            try:
                # data = requests.request('GET',url="https://wqprofiling.flotech.io/api/data/chart/depth/?device_tag=SE511&start_time=2022-11-04T05:44:54Z&parameter_tag=Temperature")
                # datatext = data.json()
                # record_time= datatext.get('record_time')[i]
                # print(datatext.get('record_time')[i])
                data = requests.request('GET',url="https://wqprofiling.flotech.io/api/data/chart/?device_tag=SE541&start_time=2022-11-07T00:04:54Z&parameter_tag=Temperature")
                datatext = data.json()
                record_time= datatext.get('record_time')
                
                #print(datatext.get('record_time')[i])   

                #print(datatext)
            except:
                print("except")  
        except:
            print("no record time !")

        count = 1
        listd= []
        for n in range(no_of_depths):
            innerlist = list(lista[n].items())
            depthlist = innerlist.pop(0) # to remove dept
            depthlist = list(depthlist) # convert tuple to list
            #print(innerlist)
            depth = depthlist[1]
            listf = []
            
            for j in range(len(innerlist)):
                    try:
                        #print(n)
                        #print(innerlist[j][1][i])
                        listf.append(innerlist[j][1][i])
                    except:
                        pass
            #print()
            for l in range(len(listf)):
                if(l==0):
                    temp = listf[l]
                elif(l==1):
                    ph = listf[l]
                elif(l==2):
                    do_conc = listf[l]
                elif(l==3):
                    do_sat = listf[l]
                elif(l==4):
                    conductivity = listf[l]
                elif(l==5):
                    turbidity = listf[l]
                elif(l==6):
                    chl_a = listf[l]
                elif(l==7):
                    tds = listf[l]
                elif(l==8):
                    #print("salinity")
                    salinity = listf[l]
                else:
                    pass

            info= [{"depth_id":n+1,"temperature":temp,"pH":ph,"conductivity":conductivity,"chl-a":chl_a,"do_conc":do_conc,"do_sat":do_sat,"salinity":salinity,"turbidity":turbidity,"depth":depth}]
            count = count+1

            listd.append(info)
        listd = [{"wq_data":listd}]
        listval.append(listd)
        

        
    
        #print("***********")  
    print(listval)
    '''
        for k in range(len(listloop)):
                                try:
                                    if(k!=0):
                                        print(listloop)

                                except:
                                    pass
    '''       

                            #print(innerlist[j][1][i])
                    # if(i!=0): # to avoid depth
                        #listloop = innerlist[j][i]
                        #print(listloop)
                        #for i in range(no_record):
                        #   print(i)
    for i in range(no_record):
        info= [{"wq_data":[{"depth":"0.5","temp":"26.0"}]}]
        listf.append(info)

    
    for i in range(len(lista)-1):
        listf = []
        listo = lista[i]
        #to convert 'dict' to list
        listt = list(listo.items())
        #print(len(listt))
        for j in range(len(listt)):
            listv= listt[j]
            #print(listv)
            #print(len(listv))
            if(j==0):
                listf.append(listv)
            else:
                pass



test()



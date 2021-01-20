import colorgram

colors=colorgram.extract(r"C:\Users\sanskar'pc\Source\Repos\sanskarlather\100-days-of-code-with-python\Day 17\spot_refrence.jpeg",25)
color_list=[]
for i in range(0,len(colors)):
    
    color=colors[i]
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    colrt=(r,g,b)
    
    color_list.append(colrt)
print(color_list)

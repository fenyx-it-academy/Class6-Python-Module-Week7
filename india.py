with open('india.text','w') as  f:
    f.write("""India is the fastest-growing economy. India is 
looking for more investments around the globe. The 
whole world is looking at India as a great market. 
Most of the Indians can foresee the heights that 
India is capable of reaching.
        """)

count = 0
with open('india.text','r',encoding='utf8') as f:
    f_contents = f.readlines()
for line in f_contents:
    if 'India' in line:
        count+=1
print(count)
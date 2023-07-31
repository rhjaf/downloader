base_url = "https://dl5.downloadha.com/hosein/Game/June2023/27/Updates/Cities.Skylines.Deluxe.Edition.v1.17.1.F4-ElAmigos_www.Downloadha.com_.part"
with open("link.txt","a+") as file:
    for i in range(1,4):
        link_url = base_url
        # if i<10:
        #     link_url+="0"
        file.write(link_url+str(i)+".rar"+"\n")

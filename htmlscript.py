uris = open("stories.txt", "r")
images = open("images.txt", "r")
buttons = open("buttons.txt", "a")

urilist = uris.readlines()
imagelist = images.readlines()
for i in range(20):
    buttons.write("<!-- story #"+str((i+1))+" --> <input type=\"image\" src=\""+str(imagelist[i]).strip()+"\" class=\"playlist\" data-spotify-id=\"spotify:playlist:"+str(urilist[i]).strip()+"\"/>\n")
uris.close()
images.close()
buttons.close()
from PIL import Image

template = Image.open('meme 2.0.png')  # 163,77  size=66x81
pfp = Image.open('my profile pic.png')
pf2 = Image.open('Alis profile pic.png')  # 151,214 size=66x81

pfp = pfp.resize((75, 81))
pf2 = pf2.resize((66, 81))

template.paste(pfp, (163, 77))
template.paste(pf2, (151, 214))

template.save("Saved2.jpg")
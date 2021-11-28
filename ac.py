import pandas as pd
from PIL import Image,ImageDraw,ImageFont
data = pd.read_excel(r'C:\\Users\\JALAX\\Desktop\\Participants.xlsx')


name_list = data["Name"].tolist()


mentor_list = data["PM"].tolist()


cert_list = data["C_no"].tolist()


for i in name_list:
    im = Image.open(r'C:\\Users\\JALAX\\Desktop\\c6.jpg')
    d = ImageDraw.Draw(im)
    n_loc = (217,128)
    cn_loc = (218,225)
    c2_loc = (356,231)
    s_loc = (126,304)
    d_loc = (330,303)
    if(im.mode=='RGBA'):
        im = im.convert('RGB')
    text_color = (0,0,0)
    font = ImageFont.truetype("arial.ttf",20)
    d.text(n_loc,i,fill = text_color,font = font)
    d.text(cn_loc,"IOT",fill = text_color,font = font)
    d.text(c2_loc,"3G tech park chennai",fill = text_color,font = font)
    d.text(s_loc,"sundar",fill = text_color,font = font)
    d.text(d_loc,"21/2/19",fill = text_color,font = font)
    im.save("certificate_"+i+".pdf")


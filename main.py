from pilmoji import Pilmoji
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor
import textwrap
import discord
import io
import random
import requests
from time import sleep  
from random import randint
from urllib.request import urlopen

scale = 2
fnt = None
font_url = 'https://github.com/TYSON-Alii/XsLib/blob/cf63491d0b570a7ba65c21da8d3f5d0dcdffa5b6/XsLib/demos/data/font.ttf?raw=true'
fnt = ImageFont.truetype(font=io.BytesIO(urlopen(font_url).read()), size=45 * scale)
ifnt = ImageFont.truetype(font=io.BytesIO(urlopen(font_url).read()), size=55 * scale)
trhfnt = ImageFont.truetype(font=io.BytesIO(urlopen(font_url).read()), size=39 * scale)
botl=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/XsLib/blob/0aaec967a98fd887e2e8556c185d23ee5b3b06a4/XsLib/demos/data/fdsfds.png?raw=true').read()))
print('basladi')

client = discord.Client()
@client.event
async def on_message(message):
	global fnt, scale, botl
	try:
		vra = False
		if message.content.startswith('q') or message.content.startswith('Q') or message.content.startswith('/q') or message.content.startswith('/Q'):
			vra = True
		if vra == True:
			sayili_mi = False
			neks = [int(s) for s in message.content.split() if s.isdigit()]
			try:
				neks = neks[0]
				sayili_mi = True
			except:
				pass
			if sayili_mi == False:
				rep = await message.channel.fetch_message(message.reference.message_id)
				uss = await message.guild.fetch_member(rep.author.id)
				isim = uss.display_name
				metin = rep.content
				satir_limit = 40
				date = str(rep.created_at)[11:16]
				rdate = int(date[0:2]) + 3
				date = date[2:]
				date = "Today at " + str(rdate) + date

				lines = textwrap.wrap(metin, width=satir_limit)
				hey = ''
				for i in lines:
					hey += i + '\n'

				width = 1400 * scale
				height = (130 * scale) + (len(lines) * (60 * scale))
					
				aimg = None
				f = 1
				if rep.attachments:
					aimg=Image.open(io.BytesIO(requests.get(rep.attachments[0].url).content)) 
					awidth, aheight = aimg.size
					f = aheight / awidth
					height += int((width - 160 * scale) * f - 120) + 165

				white = (255, 255, 255, 255)
				grey = (154, 154, 154, 255)
				opak = (0,0,0,0)
				dc_bg = (54,57,64, 255)
				isim_renk = (255,0,0,255)

				for i in message.content.split():
					if i[0] == '#':
						dc_bg = ImageColor.getcolor(i, "RGB")
						break

				isim_renk = ImageColor.getcolor(str(uss.colour), "RGB")
				image1 = Image.new("RGBA", (width, height), dc_bg)
				draw = ImageDraw.Draw(image1)
				ppimg=Image.open(io.BytesIO(await uss.avatar_url_as(size=128).read()))
				ppimg = ppimg.resize((160 * scale, 160 * scale))
				ppdraw = ImageDraw.Draw(ppimg)
				ppwidth, ppheight = ppimg.size
				ppx = (ppwidth - ppheight)//2
				img_cropped = ppimg.crop((ppx, 0, ppx+ppheight, ppheight))
				mask = Image.new('L', img_cropped.size)
				mask_draw = ImageDraw.Draw(mask)
				cpwidth, cpheight = img_cropped.size
				mask_draw.ellipse((0, 0, cpwidth, cpheight), fill=255)
				t_pp = Image.composite(ppimg, image1, mask)
				ppimg = t_pp
				image1.paste(ppimg, (20 * scale, 20 * scale))
				#draw.text((220 * scale, 90 * scale), hey, font=fnt, fill=white)
				with Pilmoji(image1) as pilmoji:
					pilmoji.text((220 * scale, 90 * scale), hey, white, fnt, emoji_scale_factor=1.45)
				draw.text((220 * scale, 15 * scale), isim, font=ifnt, fill=isim_renk)
				asdx, asdy = ifnt.getsize(isim)
				if rep.author.bot:
					botl = botl.resize((100 * scale, 50 * scale))
					image1.paste(botl, (int(220 * scale + asdx + 30), int(32.5 * scale + 5)))
					draw.text((220 * scale + asdx + 100 * scale + 60, 32.5 * scale), date, font=trhfnt, fill=grey)
				else:
					draw.text((220 * scale + asdx + 30, 32.5 * scale), date, font=trhfnt, fill=grey)

				if aimg != None:
					aimg = aimg.resize((int(width - 160 * scale) - 250, int((int(width - 160 * scale) - 250) * f)))
					image1.paste(aimg, (220 * scale, (90 * scale) * (len(lines) + 1) + (150 if hey == '' else 0)))

				with io.BytesIO() as image_bin:
					image1.save(image_bin, 'PNG')
					image_bin.seek(0)
					await message.channel.send(file=discord.File(fp=image_bin, filename='fosya.png'))
			else:
				rep = await message.channel.fetch_message(message.reference.message_id)
				rmsg = rep.id
				msg = await message.channel.history(limit=170).flatten()
				msg.reverse() 

				sy = 0
				vr = False
				for i in msg:
					if i.id == rmsg:
						vr = True
						break
					sy += 1

				mesajs = []

				class u_type:
					def __init__(self, au, co, dt, ib):
						self.author = au
						self.content = co
						self.date = dt
						self.isbot = ib
					author = None
					content = ['']
					date = None
					isbot = False

				if vr == True:
					uys = 0
					for j in range(neks):
						if uys > 0 and mesajs[uys-1].author.id == msg[sy+j].author.id:
							mesajs[uys-1].content.append(msg[sy+j].content)
						else:
							ib = False
							if msg[sy+j].author.bot:
								ib = True
							date = str(msg[sy+j].created_at)[11:16]
							rdate = int(date[0:2]) + 3
							date = date[2:]
							date = "Today at " + str(rdate) + date
							mesajs.append(u_type(msg[sy+j].author, [msg[sy+j].content], date, ib))
							uys += 1

					satir_limit = 40
					pys = 0
					for q in mesajs:
						for y in q.content:
							lines = textwrap.wrap(y, width=satir_limit)
							pys += len(lines)
						
					width = 1400 * scale
					height = 0

					height += len(mesajs) * 200 + (pys * (80 * scale))

					white = (255, 255, 255, 255)
					grey = (154, 154, 154, 255)
					opak = (0,0,0,0)
					dc_bg = (54,57,64, 255)
					isim_renk = (255,0,0,255)
					
					for i in message.content.split():
						if i[0] == '#':
							dc_bg = ImageColor.getcolor(i, "RGB")
							break

					image1 = Image.new("RGBA", (width, height), dc_bg)
					draw = ImageDraw.Draw(image1)
					dcimage = Image.new("RGBA", (width, height), dc_bg)

					tys = 0
					onck = 0
					for q in mesajs:
						lenline = 0
						for li in q.content:
							mlines = textwrap.wrap(li, width=satir_limit)
							lenline += len(mlines)
						uss = await message.guild.fetch_member(q.author.id)
						isim_renk = ImageColor.getcolor(str(uss.colour), "RGB")
						ppimg=Image.open(io.BytesIO(await q.author.avatar_url_as(size=128).read()))
						ppimg = ppimg.resize((160 * scale, 160 * scale))
						ppdraw = ImageDraw.Draw(ppimg)
						ppwidth, ppheight = ppimg.size
						ppx = (ppwidth - ppheight)//2
						img_cropped = ppimg.crop((ppx, 0, ppx+ppheight, ppheight))
						mask = Image.new('L', img_cropped.size)
						mask_draw = ImageDraw.Draw(mask)
						cpwidth, cpheight = img_cropped.size
						mask_draw.ellipse((0, 0, cpwidth, cpheight), fill=255)
						t_pp = Image.composite(ppimg, dcimage, mask)
						ppimg = t_pp
						image1.paste(ppimg, (20 * scale, (20 * scale) + onck))
						draw.text((220 * scale, (15 * scale) + onck), q.author.display_name, font=ifnt, fill=isim_renk)
						asdx, asdy = ifnt.getsize(q.author.display_name)
						if q.isbot == True:
							botl = botl.resize((100 * scale, 50 * scale))
							image1.paste(botl, (int(220 * scale + asdx + 30), int((15 * scale) + onck + 32.5 * scale / 2)))
							draw.text((220 * scale + asdx + 100 * scale + 60, int((15 * scale) + onck + 32.5 * scale / 2)), date, font=trhfnt, fill=grey)
						else:
							draw.text((220 * scale + asdx + 30, (15 * scale) + onck + 32.5 * scale / 2), q.date, font=trhfnt, fill=grey)
						rys = 0
						for gp in q.content:
							qlines = textwrap.wrap(gp, width=satir_limit)
							hey = ''
							for i in qlines:
								with Pilmoji(image1) as pilmoji:
									pilmoji.text((220 * scale, (100 * scale) + (rys * 130) + onck), i, font=fnt, fill=white, emoji_scale_factor=1.45)
								rys += 1

						onck += (100 * scale) + (rys * 130)
						tys += 1
					with io.BytesIO() as image_bin:
						image1.save(image_bin, 'PNG')
						image_bin.seek(0)
						await message.channel.send(file=discord.File(fp=image_bin, filename='dsdfdsfgdg.png'))
				else:
					await message.reply('sayi ile q atilan mesaj son 700 mesaj arasinda olmali')
	except:
		pass
	
client.run('')

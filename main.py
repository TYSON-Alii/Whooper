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
rw = urlopen(font_url).read()
fbyts = io.BytesIO(rw)
ifbtys = io.BytesIO(rw)
trhfbtys = io.BytesIO(rw)
fnt = ImageFont.truetype(font=fbyts, size=45 * scale)
ifnt = ImageFont.truetype(font=ifbtys, size=55 * scale)
trhfnt = ImageFont.truetype(font=trhfbtys, size=39 * scale)
botl=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/628d4aac4fe85aa51b01d98df031f860c1e9e0b1/data/fdsfds.png?raw=true').read()))
m1img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/628d4aac4fe85aa51b01d98df031f860c1e9e0b1/data/m1.jpg?raw=true').read()))
m2img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/628d4aac4fe85aa51b01d98df031f860c1e9e0b1/data/m2.jpg?raw=true').read()))
m3img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/628d4aac4fe85aa51b01d98df031f860c1e9e0b1/data/m3.jpg?raw=true').read()))
chp1img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/ab8d22f34a4dbbe20a6b5b524124b1e510629c0b/data/chp1.jpg?raw=true').read()))
chp2img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/ab8d22f34a4dbbe20a6b5b524124b1e510629c0b/data/chp2.jpg?raw=true').read()))
ziya1img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/8f0065b4b73bf67a4b2f7ef2c0ba8658a1759513/data/ziya1.jpg?raw=true').read()))
ziya2img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/8f0065b4b73bf67a4b2f7ef2c0ba8658a1759513/data/ziya2.jpg?raw=true').read()))
hdpimg=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/a5ade5ae2e5b71bbbcc9744ece9aed0bb931102c/data/hdp.jpg?raw=true').read()))
bebeimg=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/6a73b07631098506b4fe0d86a5c90065ec9d01f1/data/veled.jpg?raw=true').read()))
gayimg=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/a5ade5ae2e5b71bbbcc9744ece9aed0bb931102c/data/gay.jpg?raw=true').read()))
ata1img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata1.jpg?raw=true').read()))
ata2img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata2.jpg?raw=true').read()))
ata3img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata3.jpg?raw=true').read()))
ata4img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata4.jpg?raw=true').read()))
ata6img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata6.jpg?raw=true').read()))
ata7img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata7.jpg?raw=true').read()))
ata8img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata8.jpg?raw=true').read()))
ata9img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata9.jpg?raw=true').read()))
ata10img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata10.jpg?raw=true').read()))
ata11img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata11.jpg?raw=true').read()))
ata12img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata12.jpg?raw=true').read()))
ata13img=Image.open(io.BytesIO(urlopen('https://github.com/TYSON-Alii/Q-Bot-Discord/blob/eae58d634bb87ef20617c7b4270fcfd91cded8a3/data/ata13.jpg?raw=true').read()))
print('basladi')

fun = "none"

client = discord.Client()
@client.event
async def on_message(message):
	global fnt, scale, botl, fun, m1img
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
				for i in message.content.split():
					if i == 'm':
						fun = random.choice(['m1', "m2", "m3"])
						break
					elif i == 'm1':
						fun = 'm1'
						break
					elif i == 'm2':
						fun = 'm2'
						break
					elif i == 'm3':
						fun = 'm3'
						break
					elif i == 'chp':
						fun = random.choice(['chp1', "chp2"])
						break
					elif i == 'chp1':
						fun = 'chp1'
						break
					elif i == 'chp2':
						fun = 'chp2'
						break
					elif i == 'ziya':
						fun = random.choice(['ziya1', "ziya2"])
						break
					elif i == 'ziya1':
						fun = 'ziya1'
						break
					elif i == 'ziya2':
						fun = 'ziya2'
						break
					elif i == 'hdp':
						fun = 'hdp'
						break
					elif i == 'bebe':
						fun = 'bebe'
						break
					elif i == 'gay':
						fun = 'gay'
						break
					elif i == 'ata':
						fun = random.choice(['ata1', 'ata2', 'ata3', 'ata4', 'ata5', 'ata6', 'ata7', 'ata8', 'ata9', 'ata10', 'ata11', 'ata12', 'ata13'])
						break
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

				if fun == 'm1':
					cimg = m1img
					sx, sy = cimg.size
					cimg = cimg.resize((sx * 2, sy * 2))
					image1 = image1.resize((int(width / 2.5), int(height / 2.5)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (75, 378), mask)
					image1 = cimg
				elif fun == 'm2':
					cimg = m2img
					sx, sy = cimg.size
					image1 = image1.resize((int(width / 2.75), int(height / 2.75)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (30, 278), mask)
					image1 = cimg
				elif fun == 'm3':
					cimg = m3img
					sx, sy = cimg.size
					cimg = cimg.resize((sx * 2, sy * 2))
					image1 = image1.resize((int(width / 2.25), int(height / 2.25)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (75, 278), mask)
					image1 = cimg
				elif fun == 'chp1':
					cimg = chp1img
					sx, sy = cimg.size
					image1 = image1.resize((sx, int((sx / width) * height)))
					image1.putalpha(180)
					cimg.paste(image1, (0, int(sy / 2 - ((sx / width) * height) / 2)), image1)
					image1 = cimg
				elif fun == 'chp2':
					cimg = chp2img
					sx, sy = cimg.size
					cimg = cimg.resize((int(sx / 2), int(sy / 2)))
					sx, sy = cimg.size
					image1 = image1.resize((sx, int((sx / width) * height)))
					image1.putalpha(140)
					cimg.paste(image1, (0, int(sy / 2 - ((sx / width) * height) / 2)), image1)
					image1 = cimg
				elif fun == 'ziya1':
					cimg = ziya1img
					sx, sy = cimg.size
					cimg = cimg.resize((int(sx * 2), int(sy * 2)))
					image1 = image1.resize((int(width / 4), int(height / 4)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (75, 238), mask)
					image1 = cimg
				elif fun == 'ziya2':
					cimg = ziya2img
					sx, sy = cimg.size
					cimg = cimg.resize((int(sx * 2.5), int(sy * 2.5)))
					image1 = image1.resize((int(width / 2), int(height / 2)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (150, 358), mask)
					image1 = cimg
				elif fun == 'hdp':
					cimg = hdpimg
					sx, sy = cimg.size
					cimg = cimg.resize((sx, sy))
					image1 = image1.resize((int(width / 3.3), int(height / 3.3)))
					mask = Image.new('L', image1.size, 255)
					mask = mask.rotate(15, expand=True)
					image1 = image1.rotate(15, expand=True)
					cimg.paste(image1, (35, 418), mask)
					image1 = cimg
				elif fun == 'bebe':
					cimg = bebeimg
					sx, sy = cimg.size
					cimg = cimg.resize((sx, sy))
					sx, sy = cimg.size
					image1 = image1.resize((sx, int((sx / width) * height)))
					ix, iy = image1.size
					cimg.paste(image1, (0, sy - iy))
					image1 = cimg
				elif fun == 'gay':
					cimg = gayimg
					sx, sy = cimg.size
					image1 = image1.resize((sx, int((sx / width) * height)))
					image1.putalpha(140)
					cimg.paste(image1, (0, int(sy / 2 - ((sx / width) * height) / 2)), image1)
					image1 = cimg
				elif fun[0:3] == 'ata':
					print(fun[0:3], fun, sep='\n')
					if fun == 'ata1': cimg = ata1img
					elif fun == 'ata2': cimg = ata2img
					elif fun == 'ata3': cimg = ata3img
					elif fun == 'ata4': cimg = ata4img
					elif fun == 'ata6': cimg = ata6img
					elif fun == 'ata7': cimg = ata7img
					elif fun == 'ata8': cimg = ata8img
					elif fun == 'ata9': cimg = ata9img
					elif fun == 'ata10': cimg = ata10img
					elif fun == 'ata11': cimg = ata11img
					elif fun == 'ata12': cimg = ata12img
					elif fun == 'ata13': cimg = ata13img
					sx, sy = cimg.size
					image1 = image1.resize((sx, int((sx / width) * height)))
					image1.putalpha(180)
					cimg.paste(image1, (0, int(sy / 2 - ((sx / width) * height) / 2)), image1)
					image1 = cimg


				fun = "none"
				with io.BytesIO() as image_bin:
					image1.save(image_bin, 'PNG')
					image_bin.seek(0)
					await message.channel.send(file=discord.File(fp=image_bin, filename=random.choice(['bett', 'enco', 'canis', 'vaze', 'hakki']) + '_anani_patpat.png'))
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
						await message.channel.send(file=discord.File(fp=image_bin, filename=random.choice(['bett', 'enco', 'canis', 'vaze', 'hakki']) + '_anani_patpat.png'))
				else:
					await message.reply('sayi ile q atilan mesaj son 100 mesaj arasinda olmali')
	except:
		pass
	
client.run('')

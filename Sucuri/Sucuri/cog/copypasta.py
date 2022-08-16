import asyncio
from discord.ext import commands
from random import choice, randint

class copypasta_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='thefuckdidyousay')
    async def thefuckdidyousaycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            return await ctx.send('What the fuck did you just fucking say about me, you little bitch? I\'ll have you know I graduated top of my class in the Navy Seals, and I\'ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I\'m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You\'re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that\'s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn\'t, you didn\'t, and now you\'re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You\'re fucking dead, kiddo.')
        else:
            pass
    
    @commands.command(name='notarealgamer')
    async def notarealgamercmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await ctx.message.delete()

            return await ctx.send('''No, you’re NOT a real gamer.

I’m so sick of all these people that think they’re gamers. No, you’re not. Most of you are not even close to being gamers. I see these people saying “I put well over 100 hours in this game, it’s great!” that’s nothing, most of us can easily put 300+ hours in all our games. I see people who only have a Nintendo Switch and claim to be gamers. Come talk to me when you pick up a PS4 controller then we be friends.

Also DEAR ALL WOMEN: Pokémon is not a real game. Animal Crossing is not a real game. The Sims is not a real game. Mario is not a real game. Stardew valley is not a real game. Mobile games are NOT.REAL.GAMES. put down the baby games and play something that requires challenge and skill for once.

Sincerely, all of the ACTUAL gamers.''')
        else:
            pass

    @commands.command(name='gfapplication')
    async def gfapplicationcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('''Now taking applications for a gf. You must be:
1. Female (and only female!)
2. Age 16-23
3. Japanese (exceptions will be made for white girls if small and skinny)
4. Willing to do as I ask
5. Have an IQ lower than mine (164)
6. Have 0 male friends
7. Cook 3 meals for me a day
8. Be willing to split the bill on a date
9. Be into kinky stuff (will discuss in PM)
10. Send nudes every day I do not see you nude in person
11. Have sex with me as I ask
12. Be on birth control (condoms make me feel trapped, I simply can’t find anything that fits)
13. Ideally not have a job
14. Install a tracking app on your phone so that I know your location at all points
I am a kind gentlemen who will protect you at all times and in return all i ask is you pledge yourself to me. 
Please message me if you feel you fit this quota.''')
        else:
            pass
    
    @commands.command(name='antichrist')
    async def undocumentedlol(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('antichrist is gae') # nah just joking
        else:
            pass
    
    @commands.command(name='notarealwoman')
    async def notarealwomancmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('''You will never be a real woman. You have no womb, you have no ovaries, you have no eggs. You are a homosexual man twisted by drugs and surgery into a crude mockery of nature’s perfection.

All the “validation” you get is two-faced and half-hearted. Behind your back people mock you. Your parents are disgusted and ashamed of you, your “friends” laugh at your ghoulish appearance behind closed doors.

Men are utterly repulsed by you. Thousands of years of evolution have allowed men to sniff out frauds with incredible efficiency. Even trannies who “pass” look uncanny and unnatural to a man. Your bone structure is a dead giveaway. And even if you manage to get a drunk guy home with you, he’ll turn tail and bolt the second he gets a whiff of your diseased, infected axe wound.

You will never be happy. You wrench out a fake smile every single morning and tell yourself it’s going to be ok, but deep inside you feel the depression creeping up like a weed, ready to crush you under the unbearable weight.

Eventually it’ll be too much to bear - you’ll buy a rope, tie a noose, put it around your neck, and plunge into the cold abyss. Your parents will find you, heartbroken but relieved that they no longer have to live with the unbearable shame and disappointment. They’ll bury you with a headstone marked with your birth name, and every passerby for the rest of eternity will know a man is buried there. Your body will decay and go back to the dust, and all that will remain of your legacy is a skeleton that is unmistakably male.

This is your fate. This is what you chose. There is no turning back.''')
        else:
            pass
    
    @commands.command(name='veganejaculation')
    async def veganejaculationcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('If he ejaculates semen it’s because his body is full of toxins and he has had too many sexual partners. Men are not supposed to have semen it’s unclean. Vegan men with few sex partners ejaculate fresh water. Find a virginal man and leave these McDonald’s eating thots alone! \n\nStay woke sis 👁👁🧠🧘🏿‍♀️')
        else:
            pass
    
    @commands.command(name='yaoifangirl')
    async def yaoifangirlcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('No. No. You just wait a FUCKING SECOND. What the fuck did you just call me? WHAT THE FUCK DID YOU JUST CALL ME? I’ll have you know that I’m a yaoi fangirl and PROUD. You don’t INSULT me. And by the way, no. No, it’s not “gay.” Do you even KNOW where that came from? Japan. “GAY” CAME FROM JAPAN. THE PROPER TERM FOR “GAY” IS YAOI. Just because I’m eleven doesn’t mean that I can’t be a perv. I’m mature. I write yaoi fanfiction. I have many people who like my yaoi posts on fanfiction.net and deviantART. I read yaoi every day. Yaoi is my life. I couldn’t live without yaoi. I would die without it. I know everything about yaoi sex. I read a fanfiction where the seme (that’s the dominant male in the relationship.) fingered the uke. (that’s the smaller guy.) He used four fingers. That’s to prepare him for sex. I’M NOT STUPID. I read my first doujinshi when I was ten. I’m NOT like other kids, SO STOP SAYING THAT I AM. I’m sick of it. I’m so fucking sick of all of it. I’ll have you know that I knew what a penis does when I was NINE FUCKING YEARS OLD. NINE. I WAS FUCKING NINE. I BET THAT YOU DIDN’T KNOW WHAT A PENIS WAS WHEN YOU WERE NINE. I type with proper grammar, and you don’t. You aren’t better than me. You don’t even use the right word for yaoi. It’s not gay. Do your research. By the way, gay porn is disgusting. It’s nothing like yaoi and it’s unrealistic, and gross. The ukes are usually not even shorter than the seme. It’s disgusting. Fuck all of you. I’m eleven and I’m not “stupid” because I actually know about the origin of yaoi and you don’t. Fuck you. Fuck off')
        else:
            pass
    
    @commands.command(name='titanfallreference')
    async def titanfallreferencecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('‼️‼️HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING TITANFALL REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 TITANFALL IS THE BEST FUCKING VIDEOGAME 🔥🔥🔥🔥💯💯💯💯 BT-7274 IS SO BADASSSSS 😎😎😎😎😎😎😎👊👊👊👊👊 TONE BAD SPITFIRE BAD CAR BAD SCORCH HAHA FUNNY WARCRIMES HEY IS THAT ANOTHER TITANFALL 3 LEAK APEX BAD 😩😩😩😩😩😩😩😩 😩😩😩😩 GOT YOU IN THE PIPE FIVE BY FIVE YOU GOTTA MOVE FASTER THAN THAT SON SPEED IS LIFE THE SKIES BELONG TO ME 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡THEY\'RE TRYING TO CORNER US!!!!! Trust me! 🗿 🗿 Trust me!🗿 🗿 Trust me! Trust me!🗿 Trust me! 🗿 Trust me!🗿 🗿 Trust me! 🗿 🗿Trust me! 🗿 🗿 🗿 🗿 Trust me!Trust me!Trust me!Trust me!Trust me!Trust me!Trust me!🗿 Trust me! 🗿Trust me!Trust me!🗿 🗿 Trust me! 🗿 🗿 🗿 🗿 🗿 🗿 Trust me! 🗿 Trust me! 🗿 Trust me!🗿 🗿 🗿 🗿 Trust me! 🗿 🗿Trust me!🗿 Trust me! 🗿 🗿 Trust me!🗿 🗿 Trust me! 🗿 Trust me!Trust me! 🗿 🗿 🗿 🗿 🗿 🗿 🗿 Trust me!🗿 🗿 🗿 Trust me!🗿 🗿 🗿 🗿 Trust me!🗿 Trust me!Trust me!Trust me!Trust me!Trust me!🗿 🗿 🗿 🗿 🗿 🗿 Oh you’re flame coring me❓❓❓❓❓❓❓❓❓❓But it was me, Cooper‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂')
        else:
            pass
    
    @commands.command(aliases=['chinesecommunistparty', 'ccp'])
    async def chinesecommunistpartycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('''ATTENTION CITIZEN! 市民请注意! 

This is the Central Intelligentsia of the Chinese Communist Party. (:flag_cn:)
您的 Internet 浏览器历史记录和活动引起了我们的注意。
因此，您的个人资料中的 15 ( -15 Social Credits) 个社会积分将打折。
:red_circle: DO NOT DO THIS AGAIN! 不要再这样做! :red_circle: If you not hesitate, more Social Credits ( - Social Credits )will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 CCP)
You'll also be sent into a re-education camp in the Xinjiang Uyghur Autonomous Zone.
如果您毫不犹豫，更多的社会信用将从您的个人资料中打折，从而导致口粮供应减少。
您还将被送到新疆维吾尔自治区的再教育营。

为党争光! Glory to the PRC!''')
        else:
            pass
    
    @commands.command(name='okand')
    async def okandcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('"ok and?" and? and what? suck my dick? what the fuck do you want me to say? i already got my point across to your pubic brain and here you are acting like a smug smartass in a miserable way to be funny and trying to win an argument against me cause you won\'t accept fair criticism')
        else:
            pass
    
    @commands.command(name='analsquirting')
    async def analsquirtingcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('I was fingering a guy, and I was really getting in there and fingering his prostate. He eventually start to tense up and say "I\'m going to cum" so I thought I was milking his prostate. But something else happened instead. a diarhea like substance started spewing from his anus. At first I thought he shit the bed, but he insisted it was anal squirting. There substance was creamier than shit and had a lighter brown color to it. I sniffed my finger and it smelt like cum, not shit. So is anal squiting a thing? ')
        else:
            pass
    
    @commands.command(name='dreamphobic')
    async def dreamphobiccmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('''TW: 🚨 Dreamphobia 🚨, school, self-defense, Nazism, saying Dream cheated

This happened a few days ago. I was looking at fanart of Dream in class. The kid sitting next to me looked over at my computer and then made some insensitive comment about how Dream cheated (obvious Nazi propaganda) and that his videos suck.

This made me irritated - yet another Dreamphobe harassing me. I called him out and told him that he was acting Dreamphobic because he was oppressing me, a Dreamsexual person, and then he laughed in my face.

He said, "Dreamsexual? Is that when you want to suck Dream's dick or something?" I said yes and he looked at me weirdly and asked if I was joking.

I decided to pull up this subreddit to help explain Dreamsexuality and Dreamgender. He said that it "didn't exist" and that we were "just overly-obsessed Dream stans", then said that we were mentally ill.

I was livid. I was shaking, too - he doesn't have the right to speak about Dreamsexuality like this. I figured I should follow the advice given to me on this sub before, which is that you should always defend yourself if a Dreamphobe is harassing you.

I turn to him and give him a punch to his face (I was only using a bit of power to teach him a lesson). A bunch of people turn around and the entire class was looking at us.

My ignorant teacher went over and pulled me into the hall and told me that I was being "highly inappropriate" and violent. I said that the kid was discriminating against my sexuality, but he claimed that didn't warrant me punching him and that I could've handled it in a "more civil manner".

I ended up in detention. The school staff said they're "looking into" the other kid's harassment. I hate being in my Dreamphobic school.

Has anyone else here been wrongfully punished for defending yourself? Dreamphobes are true evil and it's a shame that they have so many bigots willing to defend them.''')
        else:
            pass
    
    @commands.command(name='daddieslittletidepod')
    async def daddieslittletidepodcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('i\'m daddies wittle tide pod hehe (ꈍ꒳ꈍ)i\'m all squishy and wet for daddy! (ﾉ´ヮ´)ﾉ*:･ﾟ✧ he loves how my bitter taste nuzzles his taste buds and my Botanical Raintm scent!!!! (。・ω・。)but he knows how im not meant to be eaten...(´･ω･`)waaah!!! dont eat all of me daddy(　；∀；) hehehe my soap-pussy is so wet >///< 1 lick 2 lick 3 lick 4... no more daddy i\'ll break~(●///▽///●) hehe i\'m daddies wittle tide pod so wet and squishy =w=')
        else:
            pass
    
    @commands.command(name='donda')
    async def dondacmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('Donda, Donda Donda Donda, Donda, Donda, Donda Donda Donda, Donda, Donda, Donda, Donda Donda, Donda, Donda, Donda, Donda Donda Donda, Donda, Donda, Donda, Donda Donda, Donda Donda, Donda, Donda, Donda, Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda Donda, Donda, Donda, Donda, Donda Donda, Donda Donda, Donda, Donda, Donda, Donda Donda, Donda Donda')
        else:
            pass
    
    @commands.command(name='itouchedgrass')
    async def itouchedgrasscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('It was a saturday afternoon, and I was exhausted after an intense 17-part masturabation session to dream minecraft manhunt, when i suddenly had the urge to go outside. I was scared. It\'s been so long since i\'ve left the warmth of my parents basement with my dream body pillows. I didnt know what to expect. Clutching my dream figurine in front of my chest, i opened the door to the outside world. The gleaming sun blared through the door, bequeathing a brilliant warmth on my cum-covered boxers. I quaverly took a step outside. My body flintched from the strange feel of the dirt under my feet. And then i saw it. The lustrous field of grass, covered in a light sprinkle of water from the noon rain shower. And then i realized. Dream.. grass.. the trees.. it was all coming together. Grass is green, just like Dream. Dream is everpresent, in the grass, the flowers, He was there. I immediately new what to do next. I flinged off my clothes faster than the speed at which i would click on a new dream rule 34 post. My dick was already throbbing as i leaped onto the field of grass, dorito dust stained shirt getting carried away by the wind. I dug a small hole in the ground, and passionately thrust my 7-inch erect cock into it. I knew, this was Dream. His spirit was in this grass, and he felt my dick in his boy pussy as i fucked that grass. I lost track how long i was there. Hours went by, day turned to night, but it didnt matter. I was finally together, with Dream. Nothing could separate us. I took a long stem of a flower, and forced it in my asshole. I imagined it being Dream\'s hot penis being lustfully forced into me in bed. I stayed there on my front yard for god knows how long. Until my butt was sore, balls drier than the Saharan desert after a long drought. The lawn looked like there was a layer of fresh snow on a Christmas morning. Trudging indoors, i had a enormous smile stretching across my face. I couldn\'t wait until tomorrow, when i may go outside again and be with Dream.')
        else:
            pass
    
    @commands.command(name='gotthewholechatlaughing')
    async def gotthewholechatlaughingcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            copypastas = [
                'You got the whole chat laughing 😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐',
                'Damn fam got the whole squad laughing 😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐',
                'Damn bro you got the whole chat laughing 😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😐😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😑😐😑😑😐😐😐😐😐😐😑😑😑😑😑😑😑😑😑😑😑😐😐😐😐😐😐😐😐😐😐😐😐😐😐😐😑😑😐😑😑😐😑😑😐😑😑😑😐'
            ]
            return await ctx.send(choice(copypastas))
        else:
            pass

def setup(bot):
    bot.add_cog(copypasta_cog(bot))
import asyncio, discord
from discord.ext import commands
from random import uniform, randint

from src.utils import *
from src.config import *

# the horrors i've had to go through to add this
# don't go down the same path, and just use the copypastas in here
# trust me.

class cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['help.copy', 'h.copy', 'commands.copy'])
    async def help(self, ctx) -> None:    
        '''
        await help_copy(context object) -> None

        about: Shows the copypasta's
        syntax: <prefix>help.copy
        aliases: help.copy, h.copy, commands.copy
        returns: The copypasta commands

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            pref = Configuration().prefix
            help_msg = Utils().ansify([
                f'$(cyan) - $(reset)Copypasta\'s',
                f'$(lcyan) - $(reset){pref}YWNBAW        : Based',
                f'$(lcyan) - $(reset){pref}yaoifangirl   : :|',
                f'$(lcyan) - $(reset){pref}tfreference   : HOLY SHIT IS THAT A TITANFALL REFERENCE!?',
                f'$(lcyan) - $(reset){pref}socialcredits : -1500000 social credits for not donating to Nexuzzzz >:(',
                f'$(lcyan) - $(reset){pref}dreamphobe    : Only fatherless people watch dream',
                f'$(lcyan) - $(reset){pref}itouchedgrass : Average dream fan',
                ], 
                fakeshell=True, 
                user=ctx.message.author, 
                message='help.copy'
            )

            await Utils().send_msg(ctx, help_msg, uniform(15,25))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['ywnbaw', 'YWNBAW', 'youwillneverbeawoman', 'notawoman'])
    async def ywnbaw(self, ctx) -> None:    
        '''
        await ywnbaw(context object) -> None

        about: Muhh sexuality
        syntax: <prefix>ywnbaw
        aliases: ywnbaw, YWNBAW, youwillneverbeawoman, notawoman
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            copypasta = '''You will never be a real woman. You have no womb, you have no ovaries, you have no eggs. You are a homosexual man twisted by drugs and surgery into a crude mockery of nature\'s perfection.

All the “validation” you get is two-faced and half-hearted. Behind your back people mock you. Your parents are disgusted and ashamed of you, your “friends” laugh at your ghoulish appearance behind closed doors.

Men are utterly repulsed by you. Thousands of years of evolution have allowed men to sniff out frauds with incredible efficiency. Even trannies who “pass” look uncanny and unnatural to a man. Your bone structure is a dead giveaway. And even if you manage to get a drunk guy home with you, he\'ll turn tail and bolt the second he gets a whiff of your diseased, infected axe wound.

You will never be happy. You wrench out a fake smile every single morning and tell yourself it\'s going to be ok, but deep inside you feel the depression creeping up like a weed, ready to crush you under the unbearable weight.

Eventually it\'ll be too much to bear - you\'ll buy a rope, tie a noose, put it around your neck, and plunge into the cold abyss. Your parents will find you, heartbroken but relieved that they no longer have to live with the unbearable shame and disappointment. They\'ll bury you with a headstone marked with your birth name, and every passerby for the rest of eternity will know a man is buried there. Your body will decay and go back to the dust, and all that will remain of your legacy is a skeleton that is unmistakably male.

This is your fate. This is what you chose. There is no turning back.'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(name='yaoifangirl')
    async def yaoifangirl(self, ctx) -> None:    
        '''
        await yaoifangirl(context object) -> None

        about: :|
        syntax: <prefix>yaoifangirl
        aliases: yaoifangirl
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            copypasta = '''No. No. You just wait a FUCKING SECOND. What the fuck did you just call me? WHAT THE FUCK DID YOU JUST CALL ME? I\'ll have you know that I\'m a yaoi fangirl and PROUD. You don\'t INSULT me. And by the way, no. No, it\'s not “gay.” Do you even KNOW where that came from? Japan. “GAY” CAME FROM JAPAN. THE PROPER TERM FOR “GAY” IS YAOI. Just because I\'m eleven doesn\'t mean that I can\'t be a perv. I\'m mature. I write yaoi fanfiction. I have many people who like my yaoi posts on fanfiction.net and deviantART. I read yaoi every day. Yaoi is my life. I couldn\'t live without yaoi. I would die without it. I know everything about yaoi sex. I read a fanfiction where the seme (that\'s the dominant male in the relationship.) fingered the uke. (that\'s the smaller guy.) He used four fingers. That\'s to prepare him for sex. I\'M NOT STUPID. I read my first doujinshi when I was ten. I\'m NOT like other kids, SO STOP SAYING THAT I AM. I\'m sick of it. I\'m so fucking sick of all of it. I\'ll have you know that I knew what a penis does when I was NINE FUCKING YEARS OLD. NINE. I WAS FUCKING NINE. I BET THAT YOU DIDN\'T KNOW WHAT A PENIS WAS WHEN YOU WERE NINE. I type with proper grammar, and you don\'t. You aren\'t better than me. You don\'t even use the right word for yaoi. It\'s not gay. Do your research. By the way, gay porn is disgusting. It\'s nothing like yaoi and it\'s unrealistic, and gross. The ukes are usually not even shorter than the seme. It\'s disgusting. Fuck all of you. I\'m eleven and I\'m not “stupid” because I actually know about the origin of yaoi and you don\'t. Fuck you. Fuck off'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['tfreference', 'titanfallreference'])
    async def tfreference(self, ctx) -> None:    
        '''
        await tfreference(context object) -> None

        about: HOLY SHIT IS THAT A TITANFALL REFERENCE!?
        syntax: <prefix>tfreference
        aliases: tfreference, titanfallreference
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            copypasta = '''!!!!HOLY FUCKING SHIT!!!!!!!! IS THAT A MOTHERFUCKING TITANFALL REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 TITANFALL IS THE BEST FUCKING VIDEOGAME 🔥🔥🔥🔥💯💯💯💯 BT-7274 IS SO BADASSSSS 😎😎😎😎😎😎😎👊👊👊👊👊 TONE BAD SPITFIRE BAD CAR BAD SCORCH HAHA FUNNY WARCRIMES HEY IS THAT ANOTHER TITANFALL 3 LEAK APEX BAD 😩😩😩😩😩😩😩😩 😩😩😩😩 GOT YOU IN THE PIPE FIVE BY FIVE YOU GOTTA MOVE FASTER THAN THAT SON SPEED IS LIFE THE SKIES BELONG TO ME 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡THEY\'RE TRYING TO CORNER US!!!!! Trust me! 🗿 🗿 Trust me!🗿 🗿 Trust me! Trust me!🗿 Trust me! 🗿 Trust me!🗿 🗿 Trust me! 🗿 🗿Trust me! 🗿 🗿 🗿 🗿 Trust me!Trust me!Trust me!Trust me!Trust me!Trust me!Trust me!🗿 Trust me! 🗿Trust me!Trust me!🗿 🗿 Trust me! 🗿 🗿 🗿 🗿 🗿 🗿 Trust me! 🗿 Trust me! 🗿 Trust me!🗿 🗿 🗿 🗿 Trust me! 🗿 🗿Trust me!🗿 Trust me! 🗿 🗿 Trust me!🗿 🗿 Trust me! 🗿 Trust me!Trust me! 🗿 🗿 🗿 🗿 🗿 🗿 🗿 Trust me!🗿 🗿 🗿 Trust me!🗿 🗿 🗿 🗿 Trust me!🗿 Trust me!Trust me!Trust me!Trust me!Trust me!🗿 🗿 🗿 🗿 🗿 🗿 Oh you’re flame coring me❓❓❓❓❓❓❓❓❓❓But it was me, Cooper!!!!!!!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['socialcredits', 'ccp'])
    async def socialcredits(self, ctx) -> None:    
        '''
        await socialcredits(context object) -> None

        about: Ching chong bing bong
        syntax: <prefix>socialcredits
        aliases: socialcredits, ccp
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            minus_credits = str(randint(25,2000))

            copypasta = f'''ATTENTION CITIZEN! 市民请注意! 

This is the Central Intelligentsia of the Chinese Communist Party. (:flag_cn:)
您的 Internet 浏览器历史记录和活动引起了我们的注意。
因此，您的个人资料中的 {minus_credits} ( -{minus_credits} Social Credits) 个社会积分将打折。
:red_circle: DO NOT DO THIS AGAIN! 不要再这样做! :red_circle: If you not hesitate, more Social Credits ( - {str(randint(500,2000))} )will be subtracted from your profile, resulting in the subtraction of ration supplies. (由人民供应部重新分配 CCP)
You'll also be sent into a re-education camp in the Xinjiang Uyghur Autonomous Zone.
如果您毫不犹豫，更多的社会信用将从您的个人资料中打折，从而导致口粮供应减少。
您还将被送到新疆维吾尔自治区的再教育营。

为党争光! Glory to the PRC!'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['dreamphobe', 'dreamphobic'])
    async def dreamphobe(self, ctx) -> None:    
        '''
        await dreamphobe(context object) -> None

        about: Dream is a cheater, and a fat ass
        syntax: <prefix>dreamphobe
        aliases: dreamphobe, dreamphobic
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            copypasta = f'''TW: 🚨 Dreamphobia 🚨, school, self-defense, Nazism, saying Dream cheated

This happened a few days ago. I was looking at fanart of Dream in class. The kid sitting next to me looked over at my computer and then made some insensitive comment about how Dream cheated (obvious Nazi propaganda) and that his videos suck.

This made me irritated - yet another Dreamphobe harassing me. I called him out and told him that he was acting Dreamphobic because he was oppressing me, a Dreamsexual person, and then he laughed in my face.

He said, "Dreamsexual? Is that when you want to suck Dream's dick or something?" I said yes and he looked at me weirdly and asked if I was joking.

I decided to pull up this subreddit to help explain Dreamsexuality and Dreamgender. He said that it "didn't exist" and that we were "just overly-obsessed Dream stans", then said that we were mentally ill.

I was livid. I was shaking, too - he doesn't have the right to speak about Dreamsexuality like this. I figured I should follow the advice given to me on this sub before, which is that you should always defend yourself if a Dreamphobe is harassing you.

I turn to him and give him a punch to his face (I was only using a bit of power to teach him a lesson). A bunch of people turn around and the entire class was looking at us.

My ignorant teacher went over and pulled me into the hall and told me that I was being "highly inappropriate" and violent. I said that the kid was discriminating against my sexuality, but he claimed that didn't warrant me punching him and that I could've handled it in a "more civil manner".

I ended up in detention. The school staff said they're "looking into" the other kid's harassment. I hate being in my Dreamphobic school.

Has anyone else here been wrongfully punished for defending yourself? Dreamphobes are true evil and it's a shame that they have so many bigots willing to defend them.'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['itouchedgrass', 'avgdreamfan'])
    async def itouchedgrass(self, ctx) -> None:    
        '''
        await itouchedgrass(context object) -> None

        about: Average dream fan
        syntax: <prefix>itouchedgrass
        aliases: itouchedgrass, avgdreamfan
        returns: The copypasta

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            copypasta = f'''It was a saturday afternoon, and I was exhausted after an intense {str(randint(5,20))}-part masturabation session to dream minecraft manhunt, when i suddenly had the urge to go outside. I was scared. It\'s been so long since i\'ve left the warmth of my parents basement with my dream body pillows. I didnt know what to expect. Clutching my dream figurine in front of my chest, i opened the door to the outside world. The gleaming sun blared through the door, bequeathing a brilliant warmth on my cum-covered boxers. I quaverly took a step outside. My body flintched from the strange feel of the dirt under my feet. And then i saw it. The lustrous field of grass, covered in a light sprinkle of water from the noon rain shower. And then i realized. Dream.. grass.. the trees.. it was all coming together. Grass is green, just like Dream. Dream is everpresent, in the grass, the flowers, He was there. I immediately new what to do next. I flinged off my clothes faster than the speed at which i would click on a new dream rule 34 post. My dick was already throbbing as i leaped onto the field of grass, dorito dust stained shirt getting carried away by the wind. I dug a small hole in the ground, and passionately thrust my 7-inch erect cock into it. I knew, this was Dream. His spirit was in this grass, and he felt my dick in his boy pussy as i fucked that grass. I lost track how long i was there. Hours went by, day turned to night, but it didnt matter. I was finally together, with Dream. Nothing could separate us. I took a long stem of a flower, and forced it in my asshole. I imagined it being Dream\'s hot penis being lustfully forced into me in bed. I stayed there on my front yard for god knows how long. Until my butt was sore, balls drier than the Saharan desert after a long drought. The lawn looked like there was a layer of fresh snow on a Christmas morning. Trudging indoors, i had a enormous smile stretching across my face. I couldn\'t wait until tomorrow, when i may go outside again and be with Dream.'''

            await Utils().send_msg(ctx, copypasta, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')

def setup(client):
    '''
    setup(client object) -> None

    Adds all the commands in a "commands.Cog" class to the main instance

    :param client discord.ext.commands.Bot:
    :returns None: Nothing
    '''

    client.add_cog(cog(client))
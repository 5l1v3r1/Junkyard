import asyncio
from discord.ext import commands
from random import randint

class help_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['911', 'nineeleven', '9/11', 'twintowers']) # credits to idk, found it online
    async def _911cmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            invis = ""
            message = await ctx.send(f'{invis}:man_wearing_turban::airplane:    :office:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content=f'{invis} :man_wearing_turban::airplane:   :office:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content=f'{invis}  :man_wearing_turban::airplane:  :office:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content=f'{invis}   :man_wearing_turban::airplane: :office:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content=f'{invis}    :man_wearing_turban::airplane::office:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content=':boom::boom::boom:')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.delete()
        else:
            pass
    
    @commands.command(aliases=['jerkoff', 'cum', 'nut'])
    async def _jerkoffcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            message = await ctx.send('''
                    :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant: 
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
                    ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:     
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
            ''')
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
            ''')

            await message.delete()

def setup(bot):
    bot.add_cog(help_cog(bot))
import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    images = os.listdir("images")
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:

       picture = discord.File(f)
    await ctx.send(file=picture)
    images = (os.listdir('images'))


    
@bot.command()
async def mem2(ctx):
    a = random.randint(0, 40)
    if a > 0 and a < 5:
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 6 and a < 14:
        with open('images/mem2.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 15 and a < 20:
        with open('images/mem3.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif a > 21 and a < 40:
        with open('images/mem4.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mul(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def sub(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def battery(ctx):
    await ctx.send('''Их необходимо сдавать в специальные пункты приема, 
                    которые есть во всех крупных городах страны. Чаще всего
                     они располагаются в крупных магазинах или торговых центрах. 
                     Чтобы не носить каждый раз по одной или двум батарейкам, можно
                      накопить несколько батареек и сразу сдать на утилизацию большую партию.
                      Утилизация батареек должна происходить согласно санитарным нормам, то есть
                       в специализированный контейнер. На каждом таком изделии есть обозначение, 
                       что его нельзя выкидывать вместе с обычными бытовыми отходами.''')

@bot.command()
async def glass(ctx):
    await ctx.send('''На переработку можно сдать и листовое стекло,
                    которое осталось при замене окон. Однако его принимают
                     только в компании «Стеклобой»: листовое стекло надо
                      оставить у контейнера. Прежде чем сдать стекло, его
                       надо ополоснуть от остатков содержимого и снять с тары крышку.
                        Этикетку отрывать не нужно.i
                        Перед тем, как отправить разбитое стеклянное изделие в контейнер с 
                        синей наклейкой, лучше всего сложить все осколки в коробку,
                         чтобы обезопасить сотрудников сортировочного комплекса.''')

@bot.command()
async def plastic(ctx):
    await ctx.send('''Есть три основных способа переработки пластика: механический,
                    химический и термический. Механическая переработка – способ,
                     при котором пластик сортируют, моют, дробят и делают гранулу.
                      При механическом методе полимерную цепочку пластика не разрушают,
                       а очищают, измельчают и плавят подготовленный материал.
                       Пластиковые предметы, которые нельзя переработать или использовать повторно,
                        например пластиковые пакеты, не следует выбрасывать в мусорную корзину.
                         Вместо этого их следует отнести в местный продуктовый магазин или центр
                          переработки для надлежащей утилизации.''')


@bot.command()
async def paper(ctx):
    await ctx.send('''Вначале макулатура помещается в гидроразбиватели,
                    где она распускается на волокна путем вращения в водной среде.
                    Там же от нее отделяются посторонние включения. На выходе получается суспензия
                    содержащая волокнистую массу и неразбитые куски бумаги.
                    После чего смесь очищают от примесей.
                    организации, которые занимаются сбором макулатуры постоянно;
                    разовые акции, проводящиеся различными учреждениями;
                    ящики для отдельного сбора бумаги, установленные рядом с мусорными баками,
                     возле дома или в общественных местах.''')

@bot.command()
async def cardboard(ctx):
    await ctx.send('''Упаковку из картона можно сдать в ближайший центр переработки отходов.
                    Для этого нужно удалить всю липкую ленту, находящуюся на ее поверхности.
                    Бумажную ленту можно не снимать — ее допустимо утилизировать вместе с картоном,
                    так как она более экологична.''')

@bot.command()
async def sanitary_waste(ctx):
    await ctx.send('''сбор в специальные пакеты и контейнеры;
                    сбор одноразовых емкостей в многоразовую тару;
                    транспортировка многоразовых контейнеров на тележке с ножной педалью
                    к месту дезинфекции, а затем на участок временного хранения;
                    вывоз на утилизацию специализированной компанией.
                    Разделяйте отходы на 2 типа: вторсырье
                    (пластик, металл, стекло, макулатура, упаковка типа тетра-пак);
                    смешанные отходы (пищевые отходы, средства личной гигиены, одноразовые вещи).
                    Утилизируйте в подходящий контейнер: Найдите контейнер для вторсырья на карте.
                    Биологические отходы утилизируют путем переработки на ветеринарно-санитарных
                    утилизационных заводах (цехах) в соответствии с действующими правилами,
                    обеззараживают в биотермических ямах, уничтожают сжиганием или в исключительных
                    случаях захоранивают в специально отведенных местах.''')

bot.run("tyt token")

from discord.ext import commands


class VsGradeCalc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grade", help="Calculates the VS grade based on provided parameters.")
    async def grade(self, ctx, *args):
        if len(args) != 4:
            await ctx.send("Please provide exactly 4 arguments: <parameter1> <parameter2> <parameter3> <parameter4>")
            return

        try:
            param1 = int(args[0])
            param2 = int(args[1])
            param3 = int(args[2])
            param4 = int(args[3])

            vs_grade = ((param1 * 5) + (param2 * 3) + (param3 * 2) + param4)
            await ctx.send(f"The calculated VS grade is: {vs_grade}")
        except ValueError:
            await ctx.send("Please ensure all parameters are whole numbers.")


async def setup(bot):
    await bot.add_cog(VsGradeCalc(bot))

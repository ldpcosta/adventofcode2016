global bot_inventory
global instructions
global outputs
bot_inventory = dict()
instructions = []
outputs = dict()

def parser(inp):
    def parse_initial_state(init):
        bot = int(init[-1])
        chip = int(init[1])
        give_to_bot(chip, bot)

    def parse_instructions(inst):
        global instructions
        giver = int(inst[1])
        receiver_low = int(inst[6])
        receiver_high = int(inst[-1])
        typeHi = inst[-2]
        typeLow = inst[5]
        instructions += [(giver, (receiver_low, typeLow), (receiver_high, typeHi))]

    for elem in inp:
        if elem[:5] == "value" and len(elem) > 1:
            parse_initial_state(elem.split(" "))
        elif len(elem) > 1:
            parse_instructions(elem.split(" "))


def give_chips(receiver_low, receiver_high, chips):
    def give_to_bot(chip, bot):
        if bot_inventory.get(bot) is None or bot_inventory.get(bot) == [None, None]:
            bot_inventory[bot] = [chip, None]
        else:
            bot_inventory[bot][1] = chip

    def give_to_output(chip, out):
        if outputs.get(out) is None:
            outputs[out] = chip

    if receiver_low[1] == "bot":
        give_to_bot(chips[0], receiver_low[0])
    else:
        give_to_output(chips[0], receiver_low[0])
    if receiver_high[1] == "bot":
        give_to_bot(chips[1], receiver_high[0])
    else:
        give_to_output(chips[1], receiver_high[0])


def has_2chips(bot):
    if bot_inventory.get(bot) is not None:
        if None not in bot_inventory.get(bot):
            return True
    return False


def main(instructions, lo=17, hi=61):
    while len(instructions) >= 1:
        instructions_new = []
        for inst in instructions:
            giver, receiver_low, receiver_high = inst

            if not has_2chips(giver):
                instructions_new += [inst]
                continue

            if bot_inventory.get(giver) is not None:
                chips = sorted(bot_inventory.get(giver))
            else:
                continue

            exercise1(chips, giver, lo, hi)

            give_chips(receiver_low, receiver_high, chips)
            bot_inventory[giver] = None

        instructions = instructions_new
    exercise2()


def exercise1(chips, giver, lo, hi):
    if chips == [lo, hi]:
        print "exercise1 =", giver


def exercise2():
    print outputs[0] * outputs[1] * outputs[2]


if __name__ == "__main__":
    inp = """...""".split("\n")
    parser(inp)
    main(instructions)

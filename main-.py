# for mark in range(0,101):
#     # eval = ['F', 'E', 'D', 'C', 'B', 'A'][min(5, max(0,mark//10-4))]
#     eval = max(ord('A'), min(ord('F'), 74 - mark//10))
#     print(f'{mark} : {chr(eval)}')


# grades = ['F'] * 51 + ['E'] * 10 + ['D'] * 10 + ['C'] * 10 + ['B'] * 10 + ['A'] * 10 + ['A']
# print('\n'.join([f"{i} : {grades[i]}" for i in range(101)]))
#
# print('\n'.join([f"{i} : {['F'] * 51 + ['E'] * 10 + ['D'] * 10 + ['C'] * 10 + ['B'] * 10 + ['A'] * 11}[i]" for i in range(101)]))
#
# eval = lambda x: ['F', 'E', 'D', 'C', 'B', 'A'][min(5, max(0,x//10-4))]
# for x in range(0,101):
#     print(f'{x} : {eval(x)}')

# N = int(input('enter N '))
# i = 0
# while i < N:
#     print("Hello " + str(i))
#     i = i + 1


def describe_status_1(g1_entry, g2_entry, g1_exit, g2_exit):
    if g1_entry == 0:
        print(f"🌉⬅️ Gate-1 entry is open ✅️🚧")
    else:
        print(f"🌉⬅️ Gate-1 entry is closed ⛔🚧")

    if g1_exit == 0:
        print(f"🌉⬅️ Gate-1 exit is open ✅️🚧")
    else:
        print(f"🌉⬅️ Gate-1 exit is closed ⛔🚧")

    if g2_entry == 0:
        print(f"🌉⬅️ Gate-2 entry is open ✅️🚧")
    else:
        print(f"🌉⬅️ Gate-2 entry is closed ⛔🚧")

    if g2_exit == 0:
        print(f"🌉⬅️ Gate-2 exit is open ✅️🚧")
    else:
        print(f"🌉⬅️ Gate-2 exit is closed ⛔🚧")


status = {
    "0": " is open ✅️🚧",
    "1": " is closed ⛔🚧"
}


def describe_status_2(g1_entry, g2_entry, g1_exit, g2_exit):
    print(f"🌉⬅️ Gate-1 entry {status[g1_entry]}")
    print(f"⬅️🌉 Gate-1 exit {status[g1_exit]}")
    print(f"➡️🌉 Gate-2 entry {status[g2_entry]}")
    print(f"🌉➡️ Gate-2 exit {status[g2_exit]}")

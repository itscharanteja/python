import random
MAX_LINES = 3
MIN_BET = 100
MAX_BET = 500

ROWS = 3
COLS = 3
symbols_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
    
 }
symbols_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2 
    
 }

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

    


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:                
                print(column[row],end=" ")
              
        print( )  

def deposit():
    while True:
        amt = input("Enter an amount to deposit: ")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Enter amount greater than 0")
        else:
            print("Enter a number")
    return amt

def number_of_lines():
    while True:
        lines = input("Enter valid number of lines (1 "+ str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter valid number of lines: ")
        else:
            print("Enter a number")
    return lines

def get_bet():
    while True:
        bet = input("Enter amount you want to bet: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter valid bet amount between {MIN_BET} - {MAX_BET}: ")
        else:
            print("Enter a number")
    return bet

def main():
    balance = deposit()
    lines = number_of_lines()
    
    while True:
        bet = get_bet()
        total_amt = bet * lines
        if bet > total_amt:
            print(f"You do not have enough balance to bet. You're available balance is {balance}")
        else:
            break
    print(f"You are betting {bet} on {lines} and total cost is {total_amt}")
    slots = get_slot_machine_spin(ROWS,COLS,symbols_count)
    print_slot_machine(slots)

main()


from .models import GameState, WinState, UserSymbol
from django.shortcuts import render,redirect
from django.db import transaction
from django.contrib import messages
SYMBOL_X = "X"
SYMBOL_O = "O"




def main(request):
    if request.method == "POST":
       if "symbol" in request.POST:
           symbol = UserSymbol.objects.first()
           symbol = UserSymbol(User_s = request.POST["symbol"])
           symbol.save()

           User_symbol = UserSymbol.objects.first()
           User_symbol = User_symbol.User_s
    return render(request, "main.html")


       

def game(request):
    game_state = get_or_create_game_state()
    
    if request.method == "POST":
        if "cell" in request.POST:
            handle_cell_click(request.POST["cell"], game_state, request)
        elif "refresh" in request.POST:
            refresh_game()
            return redirect('main')
        
    winner = get_winner()
    User = UserSymbol.objects.first().User_s
    context = {
        "game_state": game_state,
        "winner": winner,
        "User": User
    }

    return render(request, "game.html", context)


def get_or_create_game_state():
    game_state = GameState.objects.first()

    if game_state is None:
        game_state = GameState(state="-" * 9)
        game_state.save()

    return game_state


@transaction.atomic
def handle_cell_click(cell_number, game_state,request):
    if game_state.state.count("-") != 9:
        current_symbol = get_current_symbol(game_state.state)

        game_state.state = update_game_state(game_state.state, cell_number, current_symbol)
        game_state.save()

        if win_check(game_state.state, current_symbol):
            create_winner(current_symbol)
            game_state.delete()

        elif full_board_check(game_state):
            messages.info(request, 'TIE GAME',extra_tags='danger') 
    else:
        
        
        game_state.state = update_game_state(game_state.state, cell_number, UserSymbol.objects.first().User_s)
        game_state.save()


def get_current_symbol(game_state):
    count_x = game_state.count(SYMBOL_X)
    count_o = game_state.count(SYMBOL_O)

    if  UserSymbol.objects.first().User_s == SYMBOL_X:
        return SYMBOL_X if count_x == count_o else SYMBOL_O
    elif UserSymbol.objects.first().User_s == SYMBOL_O:
        return SYMBOL_O if count_x == count_o else SYMBOL_X
def update_game_state(current_state, cell_number, new_value):
    index = int(cell_number) - 1
    return current_state[:index] + new_value + current_state[index + 1:]


def win_check(state, symbol):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [2, 4, 6],
        [0, 4, 8]
    ]

    for combination in winning_combinations:
        if all(state[index] == symbol for index in combination):
            return True

    return False

#checking for the position is full or not
def space_check(game_state,cell_number):
    if game_state[cell_number] not in ['X','O']:
        return True
    else:
        pass 
    return False

def full_board_check(game_state):
    for i in range(0,9):
        if space_check(game_state.state,i):
            return False
    return True

def create_winner(symbol):
    winner = WinState(symbol=symbol)
    winner.save()


@transaction.atomic
def refresh_game():
    GameState.objects.all().delete()
    WinState.objects.all().delete()
    UserSymbol.objects.all().delete()
    

def get_winner():
    return WinState.objects.first

   
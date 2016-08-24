from toolspy import write_xlsx_sheet
import sys


def tournament_round(round_number, players):
    row = [players[-1]]
    row += players[round_number: -1]
    row += players[0: round_number]
    return [(row[i], row[-(1 + i)]) for i in range(len(row) / 2)]


def tournament(players):
    if len(players) % 2 != 0:
        players.append('GHOST')
    no_of_players = len(players)
    no_of_rounds = no_of_players - 1
    return [tournament_round(r, players) for r in range(no_of_rounds)]


def create_tournament_schedule_xlsx(xlsx_file_name, players):
    rows = []
    for round_number, tournament_round in enumerate(tournament(players)):
        for pairing in tournament_round:
            if "GHOST" not in pairing:
                rows.append({"Round No.": round_number + 1, "Player 1": pairing[0], "Player 2": pairing[1] })
    write_xlsx_sheet(xlsx_file_name, rows=rows, cols=["Round No.", "Player 1", "Player 2"])

if __name__ == '__main__':
    """
    Invoke as
    python tournament.py "Avinash, Avinash Vijay, Gopi, Shiva" tournament.xlsx
    """
    players = [name.strip() for name in sys.argv[1].split(",")]
    create_tournament_schedule_xlsx(sys.argv[2], players)

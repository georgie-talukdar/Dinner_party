from data_extraction import get_data
from one_thing import assign_confessions_equally
import pandas as pd

def main():
    df=get_data()
    dinner_party_teams = {
    1: ["Harry", "Rhiannon", "George", "Sienna", "Max"],
    2: ["Georgie", "Nic", "Ben", "James"],
    3: ["Andrew", "Ellie", "Matthew", "Marcus", "Jisu"]
}

    column_names=['One Thing Game','Name']
    one_thing_df = df[column_names]

    team1q,team2q,team3q = assign_confessions_equally(one_thing_df,dinner_party_teams)


    print(team1q)
    print(team2q)
    print(team3q)

if __name__ == "__main__":
    main()
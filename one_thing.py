import random

def assign_confessions_equally(df, teams):

    df = df.sample(frac=1).reset_index(drop=True)


    team1q = {}
    team2q = {}
    team3q = {}

    # Iterate through the DataFrame rows
    for index, row in df.iterrows():
        test=[team1q, team2q, team3q]
        # Determine the dictionary with the shortest length
        shortest_dict = min(test, key=len)

        if shortest_dict==team1q:
            team=1
        elif shortest_dict==team2q:
            team=2
        else:
            team=3

        quote = row['One Thing Game']
        person = row['Name']

        if person in teams[team]:  
            if team == 1:
                test=[team2q, team3q]
                shortest_dict = min(test, key=len)
            elif shortest_dict is team2q:
                test=[team1q, team3q]
                shortest_dict = min(test, key=len)
            else:
                test=[team1q, team2q]
                shortest_dict = min(test, key=len)
            # If the shortest_dict is team3q, it wraps around to team1q
        
        # Add the index to the shortest dictionary
        shortest_dict[person] = quote
        
    return team1q,team2q,team3q

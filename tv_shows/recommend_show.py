import numpy as np

def recommend_episode():
    '''
    Recommend a random show
    '''
    shows = ['The Bear','Ahsoka','I Think You Should Leave']
    selected_show = np.random.choice(shows)
    seasons = np.random.randint(1,4)
    episode = np.random.randint(1,16)
    
    print(f'You should watch {selected_show}, season {seasons}, episode {episode}')
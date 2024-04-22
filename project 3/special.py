import plotly.express as px
#code that displays nhl point leaders in 2024 regular season
#all info used is from https://www.nhl.com/stats/skaters?reportType=season&seasonFrom=20232024&seasonTo=20232024&gameType=2&sort=points,goals,assists&page=0&pageSize=50
def hockey_data():
    data = {
        'Player': ['Auston Matthews', 'David Pastrnak', 'Artmei Panarin', 'Connor McDavid', 'Nathan MacKinnon', 'Nikita Kucherov'],
        'Goals': [69, 47, 49, 32, 51, 44],
        'Assists': [38, 63, 71, 100, 89, 100],
        'Penalty_Minutes': [20, 47, 24, 30, 42, 22],
        'Position_Standing': [6, 5, 4, 3, 2 , 1],
        'Points': [107, 110, 120, 132, 140, 144]
    }
    return data

def plot_data(data):
    fig = px.bar(data, x='Player', y=['Goals', 'Assists', 'Points', 'Penalty_Minutes', 'Position_Standing'], barmode='group', title='NHL Point Leaders 2024')
    fig.update_layout(xaxis_title='Player', yaxis_title='Scale of Points')
    fig.show()

def main():
    data = hockey_data()
    plot_data(data)

if __name__ == "__main__":
    main()
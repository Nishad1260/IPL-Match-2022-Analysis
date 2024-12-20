# -*- coding: utf-8 -*-
"""IPL 2022 Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V3apbtDCkxz3hSEHmYThNx8ORkTLIIqu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#import warnings
#warnings.filterwarnings('ignore')

data = pd.read_csv('/content/IPL 2022.csv.csv')
data

data.shape

data.head()

data.isnull().sum()

data.columns





data



#no. of match won by each team in ipl 2022



figure = px.bar(data['match_winner'] ,title='Number of match won in ipl 2022')

figure.show()

#defending and chasing

data['won_by'] = data['won_by'].map({'Wickets' : 'Chasing','Runs' : 'Defending'})



won_by = data['won_by'].value_counts()
label = won_by.index
counts = won_by.values

colors = ['red','lightgreen']

figure = go.Figure(data=[go.Pie(labels=label,values = counts)])
figure.update_layout(title_text='Defending and chasing')
figure.update_traces(hoverinfo='label+percent',
                     textinfo='value',
                     textfont_size=30,
                    marker=dict(colors=colors,
                                line=dict(color='black',width=3)))
figure.show()

#best bowling

figure = px.bar(data['best_bowling'],title='best bowling')
figure.update_xaxes(tickangle=45)
figure.show()

figure = px.bar(data['player_of_the_match'],title = 'High scorer 2022')

figure.show()

#top scorer in ipl 2022

figure = px.bar(data, x = ['top_scorer'],
                y = data['highscore'],
                title = 'Top scorer in ipl 2022')

figure.show()

#To visualize the distribution of a numerical variable

plt.hist(data['highscore'], bins = 10)
plt.xlabel('Highscore')
plt.ylabel('Frequency')
plt.title('Distribution of Highscore in IPL 2022')
plt.show()

#To visualize the replationship between two numerical variables

sns.scatterplot(x = 'highscore', y = 'first_ings_score', data = data)
plt.xlabel('Highscore')
plt.ylabel('First Innings Score')
plt.title('Relationship between Highscore and First Innings score')
plt.show()

#To visualize the replationship between two numerical variables

sns.scatterplot(x = 'highscore', y = 'second_ings_score', data = data)
plt.xlabel('Highscore')
plt.ylabel('Second Innings Score')
plt.title('Relationship between Highscore and Second Innings Score')
plt.show()

sns.boxplot(x = 'won_by' , y = 'highscore', data = data)
plt.xlabel('Match Outcome (Won by)')
plt.ylabel('Highscore')
plt.title('Highscore Distribution by Match Outcome')
plt.show()

#venue performance

venue_performance = data.groupby(['venue','match_winner'])['match_id'].count().reset_index()
fig = px.bar(venue_performance, x='venue',y='match_id',color='match_winner',title='Venue Performance')
fig.show()

#Top Scorer by team

colors = ['red','Lightgreen','pink','yellow','blue','orange','purple','brown','lightpink']

top_scorers = data.groupby('team1')['highscore'].max().reset_index()
fig = px.bar(top_scorers, x='team1', y='highscore',color=colors, title='Top Scorers by Team')
fig.show()

top_scorers = data.groupby('team2')['highscore'].max().reset_index()
fig = px.bar(top_scorers, x='team2', y='highscore',color=colors, title='Top Scorers by Team')
fig.show()

#Toss decision

toss_decision = data.groupby(['toss_decision','won_by'])['match_id'].count().reset_index()
fig = px.bar(toss_decision, x='toss_decision', y='match_id', color='won_by', title='Toss Decision')
fig.show()
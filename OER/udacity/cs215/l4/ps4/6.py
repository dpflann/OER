import sys
import re

actors_to_movies = {}
movies_to_actors = {}

def fill_data_structures():
  f = open('file.tsv', 'r')  
  for line in f:
    actor, movie, year = line.strip('\n').split("\t")
    if actor in actors_to_movies:
      actors_to_movies[actor].append((movie,year))
    else:
      actors_to_movies[actor] = [(movie, year)]
    if (movie, year) in movies_to_actors:
      movies_to_actors[(movie, year)].append(actor)
    else:
      movies_to_actors[(movie, year)] = [actor]
  f.close()

average_centrality_table = {} #centrality --> actor
def average_centrality(actor):
  distance_from_actor = {}
  distance_from_actor[actor] = 0
  connections = [actor]
  while len(connections) > 0:
    current = connections.pop()
    for a in obtain_actor_connections(current):
      if a not in distance_from_actor:
        distance_from_actor[a] = distance_from_actor[current] + 1
        connections.append(a)
  avg_centrality = sum(distance_from_actor.values()) * 1.0 / len(distance_from_actor)
  #distance_from_actor["average_centrality"] = avg_centrality
  print avg_centrality, " = ", actor
  return distance_from_actor

def process_all_actors():
  for actor in actors_to_movies:
    #distances = average_centrality(actor)
    average_centrality(actor)
    #if actor not in average_centrality_table:
      #average_centrality_table[actor] = distances

def obtain_actor_connections(actor):
  connections = set({})
  for movie in actors_to_movies[actor]:
    for actor in movies_to_actors[movie]:
      connections.add(actor)
  return list(connections)

fill_data_structures()
process_all_actors()
#centralities = { actor: average_centrality_table[actor]["average_centrality"] for actor in average_centrality_table }
#sorted_cents = sorted(centralities, key=centralities.get)
#for actor in sorted_cents:
#  print centralities[actor], " = ", actor

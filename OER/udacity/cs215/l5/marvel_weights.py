import re
import sys

def fill_data_structures():
  f = open('marvel.tsv', 'r')  
  for line in f:
    hero, comic = line.strip('\n').split("\t")
    hero = hero.strip('\"')
    comic = comic.strip('\"')
    if hero in hero_to_comics:
      hero_to_comics[hero].append(comic)
    else:
      hero_to_comics[hero] = [comic]
    if comic in comic_to_heroes:
      comic_to_heroes[comic].append(hero)
    else:
      comic_to_heroes[comic] = [hero]
  f.close()

def compute_weights(hero, weighted_graph):
  hero_connections = {}
  for comic in hero_to_comics[hero]:
    for co_hero in comic_to_heroes[comic]:
      if co_hero != hero:
        if co_hero in hero_connections:
          hero_connections[co_hero] += 1
        else:
          hero_connections[co_hero] = 1
  if hero_connections:
    recalibrated = { hero: (1.0 / hero_connections[hero]) for hero in hero_connections }
    weighted_graph[hero] = recalibrated
#    highest_connection = max(hero_connections, key=hero_connections.get)
#    weighted_graph[hero] = hero_connections
#    print "%d - %s <-> %s" % (hero_connections[highest_connection], hero, highest_connection)

def compute_unit_weights(hero, unit_weighted_graph):
  hero_connections = {}
  for comic in hero_to_comics[hero]:
    for co_hero in comic_to_heroes[comic]:
      if co_hero != hero:
        if co_hero not in hero_connections:
          hero_connections[co_hero] = 1
  unit_weighted_graph[hero] = hero_connections

def compute_all_heroes_weighted():
  weighted_graph = {}
  for hero in hero_to_comics:
    compute_weights(hero, weighted_graph)
  return weighted_graph

def compute_all_heroes_unit_weighted():
  unit_weighted_graph = {}
  for hero in hero_to_comics:
    compute_unit_weights(hero, unit_weighted_graph)
  return unit_weighted_graph

hero_to_comics = {}
comic_to_heroes = {}

fill_data_structures()
weighted = compute_all_heroes_weighted()
unit_weighted = compute_all_heroes_unit_weighted()

heroes = ['SPIDER-MAN/PETER PAR', 'GREEN GOBLIN/NORMAN ', 'WOLVERINE/LOGAN ', 'PROFESSOR X/CHARLES ', 'CAPTAIN AMERICA']

## Operating only on these given nodes
#1. Construct Paths on Unit Weighted
# BFS and keep track of path

def bfs_path(graph, node):
  if node not in graph or len(graph) == 0:
    return
  visited = [node]
  current_level = [node]
  next_level = []
  level = 0
  distances = {}
  while (current_level):
    current_node = current_level.pop()
    for n in graph[current_node]:
      if n not in visited:
        next_level.append(n)
        distances[n] = level
    if len(current_level) == 0:
      current_level = next_level
      next_level = []
      level += 1
  return distances

#2. Construct Paths on Weighted
# DIJKSTRA and keep track of path

distances = bfs_path(unit_weighted, heroes[0])
for h in distances:
  print h, distances[h]

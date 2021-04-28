# CMPM146 Game AI
Files for Game AI UCSC

## P1 - Dijkstra's Search Dungeon

Created a pathfinding algorithm using Dijkstra's algorithm for a custom maze. 

## P2 - Navmesh Pathfinding

Takes in a custom user image, converts it into a binary representation of navmeshes and uses bi-directional A* search in order to find a path from one point to another.

**Example:**

<img width="203" alt="Screen Shot 2021-04-28 at 12 20 10 PM" src="https://user-images.githubusercontent.com/35155820/116460632-1df3ce00-a81c-11eb-90df-7b895dfcb002.png">

## P3 - Monte Carlo Tree Search for Ultimate Tic-Tac-Toe

Implemented AI using Monte Carlo Tree Search with full, random rollout. 

## P4 - BT for Planet Wars

Can easily beat easy bots provided by professor using Behavioural Trees.

Strategies implemented:
- Attacks weakest enemy planet using my strongest planet
- If there is a neutral planet, try to spread troops to inhabit it
- Defend a planet if being attacked by enemy
- Finish the enemy when it has one planet left

## P5 - Minecraft Recipe Planner

Implemented A* Search in order to find the fastest and most efficient way of reaching a certain Item goal in Minecraft.
Heuristics used to help with the algorithm:
- Do not include tools in the search if we already have a tool (since we don't want duplication)
- Limit number of consumables that we need (since we don't want large numbers of the consumable when we need a little)
- Seperates the item tier into Wooden, Stone, and Iron. Prioritizes the items wanted into tiers to make the searches easier.

## P6 - Mario Level Generator

Creates a Mario level using a evolutionary algorithm able to mutate and generate children in order to implement more challenges and detail.

## Final Creative Project

Creates a Minecraft dungeon generator that is able to put in different puzzles. The dungeon also has sections seperated with locked doors where players need to 
complete certain puzzles and find the key to go into the next level. Dungeon generator generates layout in a python text file first then is able to be run on a 
Minecraft server to be playable in-game.



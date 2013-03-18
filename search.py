# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  
  """
  ################       THIS IS  MY FUNCTIONS ###############

   
    
    
    
    

  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e= Dirrection.East
  n= Direction.North
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
   
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  ### These are define directions ###
  
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e= Dirrection.East
  n= Direction.North
  
  ### These are defining some lists and dictionary and objects and etc. ###
  
  
  aveilable = []
  checked_node = []    ###   go to a node twice is useless ; therefore we creat this list for prevention from that ###
  final_directions = [] ### at the end we must return a list that contains directions that we need to riche the goal ###
  how_to_rich = {} ### this is a dictioanari . and every element  in it  is  { last direction to rich this node : a_State}
  aveilable.append(problem.getStartState())  ### at first we have to add start_node  in available list ###
  
  while len(aveilable) > 0 :
    for i in aveilable :
      
      if i not in checked_node:
        checked_node.append(i)
        i = problem.getSuccessors(i) ###   WATCH OUT : this part is a f**king code and need to repair and this is usefull for understanding other parts ###
           
        if  problem.isGoalState(i) == True :
             while i != getStartState() :
                direction = how_to_rich[i]
                final_directions.append(direction)
    
                nodes=problem.getSuccessors(i)
                for u in nodes:
                  if u[1] == direction:
                    u[0] = problem.getStartState()
             return finall_directions
    
          
          
  
      
      for j in problem.getSuccessors(i) :
               aveilable.append(j[0])
      for k in problem.getSuccessors(problem.getStartState()) :
             how_to_rich.update({k[0] : k[1]})
    aveilable.remove(i)
  print 'you must go :' final_directions
            
      
      
      
  
  
  
 

    
        
      
      
    
  



  
  
 
 



  
  
    
    



  
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

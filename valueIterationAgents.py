# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        #print(self.mdp.getStates())
        states = self.mdp.getStates()
        st_iterator = self.mdp.getStates()[1]

        for i in range (iterations):
          vals = self.values.copy()
          #print(vals)


          for st_iterator in states:
            final_val = None


            for i in self.mdp.getPossibleActions(st_iterator):
              temp_val = self.computeQValueFromValues(st_iterator,i)
              if  final_val < temp_val or final_val == None:
                  final_val = temp_val
                  #print("nonono++++++++++++++++++")
            if final_val == None:
                final_val = 0
                #print("hahahah@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            vals[st_iterator] = final_val



          self.values = vals


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        t_function = self.mdp.getTransitionStatesAndProbs(state,action)
        #print(t_function)
        val = 0
        for nxt_st, t_prob in t_function:
            val = val+(t_prob * (self.mdp.getReward(state, action, nxt_st)+ (self.discount * self.values[nxt_st])))
        #print(val)
        return val
        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        val = None
        actons_available = self.mdp.getPossibleActions(state)
        action_taken = None
        for i in actons_available:
            actionx_val = self.computeQValueFromValues(state, i)
            #print(actionx_val)
            if  actionx_val > val or val == None:
                #print("blahblah#####################")
                val = actionx_val
                action_taken = i
        return action_taken
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

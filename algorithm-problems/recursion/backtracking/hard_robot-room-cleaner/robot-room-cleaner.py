# LeetCode 489. Robot Room Cleaner
#
# Notes:
# This is a problem that can be solved using backtracking. There two main
# concepts involved in the solution:
#
# 1. constrained programming - That basically means to put restrictions after
# each robot move. Robot moves, and the cell is marked as visited. That
# propagates constraints and helps to reduce the number of combinations to
# consider.
#
# 2.backtracking - Let's imagine that after several moves the robot is
# surrounded by the visited cells. But several steps before there was a cell
# which proposed an alternative path to go. That path wasn't used and hence the
# room is not yet cleaned up. What to do? To backtrack. That means to come back
# to that cell, and to explore the alternative path.
#
# The algorithm can be broke down as the following:
# - Mark the cell as visited and clean it up.
# - Explore 4 directions : up, right, down, and left (the order is important
#   since the idea is always to turn right):
#     - Check the next cell in the chosen direction :
#       - If it's not visited yet and there is no obtacles :
#           - Move forward.
#           - Explore next cells backtrack(new_cell, new_direction).
#           - Backtrack, i.e. go back to the previous cell.
#       - Turn right because now there is an obstacle (or a virtual obstacle)
#         just in front, and we explore an alternative path.
#
# Complexity:
# O(n - m) time | O(n - m) space - where n is the number of cells i nthe room,
# and m is the number of obstacles.
# time complexity:
#   - We visit each non-obstacle cell once and only once;
#   - At each visit, we will check 4 directions around the cell. Therefore, the
#     total number of operations would be 4(n − m).
# space complexity:
#   - We employed a hashtable to keep track of whether a non-obstacle cell is
#     visited or not.
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            # turn around
            robot.turnRight()
            robot.turnRight()
            # move forward one step
            robot.move()
            # turn around again
            robot.turnRight()
            robot.turnRight()

        # this function takes 2 params: cell - the current cell cleaning robot is at,
        # default to (0, 0); d - direction the robot is going
        def backtrack(cell = (0, 0), d = 0):
            # mark the cell 'visited'
            visited.add(cell)
            # clean the cell
            robot.clean()
            # going clockwise: 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d  = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise: 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
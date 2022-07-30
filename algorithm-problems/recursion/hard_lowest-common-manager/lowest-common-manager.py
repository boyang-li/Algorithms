# Notes:
# This problem is a perfectly suitable for recursion. We want to create a
# separate class, OrgInfo, to carry the information we need over recursive
# calls, and once the criteria is satisfied in one of the recursive calls,
# we jump out of recusion and returning the results. The result would be
# guaranteed to be the lowest common manager in the tree by the setup.
#
# Complexity:
# O(n) time | O(d) space - where n is the number of nodes/people in the
# tree/organization, and d is the depth(height) of the tree/org chart.
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # start the recursive call at the root node.
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
    # we want to find whether the two important reports are contained in the
    # subtree rooted at the current node.
    numImportantReports = 0
    # traverse the direct reports
    for directReport in manager.directReports:
        # recursive call to get the OrgInfo of the node.
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        # if we have found the lowest common manager, return immediately to
        # jump out of recursion. This guarantees that the the common manager
        # is the lowest.
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        # Update the number of important reports in the current subtree.
        numImportantReports += orgInfo.numImportantReports

    # we check whether the current node is one of the important reports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    # it there are two important reports, then we have found the lowerst
    # common manager.
    lowestCommonManager = manager if numImportantReports == 2 else None
    return OrgInfo(lowestCommonManager, numImportantReports)

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

# This is a class for carrying the data we need over recursive calls:
# The current lowest common manager, and the current number of important
# reports found.
class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

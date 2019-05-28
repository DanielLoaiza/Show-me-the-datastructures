# Active Directory
to solve this problem recurssion is used, starting from the root each group is visited checking if user is present , if the user matches then it returns

since its not known how many files we need to go through , its easier to reason about the iterations using recurssion, visiting the group and making the recurssive call for each of his children

the worst case scenario is if the user is not present on any group and the group structure has the same subgroups on each, taking O(n!) worst case, since a stack if used for recurssion the space complexity would be O(n)

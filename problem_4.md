# Active Directory
to solve this problem recurssion is used, starting from the root each group is visited checking if user is present , if the user matches then it returns

the worst case scenario is if the user is not present on any group and the group structure has the same subgroups on each, taking O(n!) worst case

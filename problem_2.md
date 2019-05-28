# Finding Files
  to find files starting from a path x we need to go through the entire file directory to make sure everything is checked, so time complexity is O(n) and since recurssion is used the previous recursive calls will be stored on a stack giving us O(n) in terms of space
  
  the easiest way to reason about this problem is using recurssion , we start from the root dir and then listing and going to every directory in there checking its files, we repeat this process until there are no more subdirectories on each branch

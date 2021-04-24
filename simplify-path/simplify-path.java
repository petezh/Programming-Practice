class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new LinkedList<>();
        // non-directories
        Set<String> skip = new HashSet<>(Arrays.asList("..",".",""));
        // process in stack
        for (String dir : path.split("/")) {
            // go up one directory
            if (dir.equals("..") && !stack.isEmpty()) stack.pop();
            // otherwise, add folder
            else if (!skip.contains(dir)) stack.push(dir);
        }
        // build result
        String res = "";
        for (String dir : stack) res = "/" + dir + res;
        // handle null case
        return res.isEmpty() ? "/" : res;
    }
}
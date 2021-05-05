/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        std::stack<TreeNode*> toVisit;
        while(1) {
            // explore leftmost
            while(root) { toVisit.push(root); root=root->left; }
            if(toVisit.empty()) break;
            root=toVisit.top(); toVisit.pop();
            // add val
            nodes.push_back(root->val);
            // explore right
            root=root->right;
        }
        return nodes;
    }
};
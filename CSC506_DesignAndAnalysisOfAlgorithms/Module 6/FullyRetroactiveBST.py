# Name: Tobias Boggess
# Date: July 25, 2023
# Purpose: Creates a full retroactive search tree.
from PartialRetroactiveBST import PartialRetroactiveBST
import warnings


class FullRetroactiveBST(PartialRetroactiveBST):
    pass

    # Prints the tree from passed iterations
    def query(self, time_ago=0):
        # Check time_ago to see if it is valid
        if time_ago >= len(self.tree_history) - 1 or self.tree_history[self.latest_tree - time_ago] is None:

            while time_ago > len(self.tree_history) - 1:
                warnings.warn(f'Insert a valid tree to delete from.')
                time_ago = input(f'Enter a numerical value for a previous version of the BST or \'exit\''
                                 f'(i.e., Time_ago = 2 will insert into the binary tree 2 iterations ago.): ')

                if time_ago == 'exit':
                    print(f'Cancelling deletion.')
                    return
                else:
                    time_ago = int(time_ago)

        # Search past tree for key given
        self.bst = self.tree_history[self.latest_tree - time_ago]
        print(self.bst)

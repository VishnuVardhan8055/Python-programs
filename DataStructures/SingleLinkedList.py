import dstructure
#import SingleLinked List
from dstructure.SLL import SLL
single_ll = SLL()
# insert an elements to linked list
single_ll.insert('India')
single_ll.insert('USA')
single_ll.insert('Russia')
single_ll.insert('Vishnu')
single_ll.insert('Sanjay')
single_ll.print()
single_ll.delete_l()# it will delete last node of the list
single_ll.delete_f()# it will delete first node of the list
single_ll.print()
single_ll.delete('Russia')
single_ll.print()



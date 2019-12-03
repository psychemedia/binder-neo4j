# # neo4j - Demo
#
# Example of getting started with neo4j.
#
# Docs: https://py2neo.org/3.0/intro.html (although https://py2neo.org/2.0/intro.html#getting-connected is more useful, albeit with an older (broken) syntax in many places...).

from py2neo import Graph
graph = Graph(password="neo4jbinder")

from py2neo import Node, Relationship

alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)


graph.run("CREATE (c:Person {name:{N}}) RETURN c", {"N": "Carol"})

for record in graph.run("MATCH (p:Person) RETURN p.name AS name"):
    print(record['name'])

# ## Simple IPython Magic Demo
#
#
# Load the magic with:
#
# `%load_ext cypher_magic`
#
# The magic allows you to run Cypher commands against the connected database using default credentials (the default password is set to `neo4jbinder`). You can change the password with the `-p`/`--password` variable; the `-q` flag suppresses the cell output.
#
# ```
# # %cypher -r
# # %cypher -q -p neo4jbinder
# ```
#
# Call as line magic `%cypher` or block magic: `%%cypher`
#
# The line magic is perhaps most useful when called with a query passed via a variable. For example:
#
# ```
# q='MATCH (p:Person) RETURN p.name AS name'
# # %cypher -v q
# ```
#
# the magic will return a `pandas` dataframe by default. Other return formats, set using the `-o`/`--output` parameter, include `table` and `matrix` (the latter requires `sympy` to be installed).
#

# %cypher -r
# %cypher -q -p neo4jbinder

# %%cypher -o matrix
MATCH (p:Person) RETURN p.name AS name

# %%cypher -p neo4jbinder
CREATE (c:Person {name:"Helen"}) RETURN c

q='MATCH (p:Person) RETURN p.name AS name'
# %cypher -v q

_


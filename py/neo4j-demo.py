# # neo4j - Demo
#
# Example of getting started with neo4j.
#
# The simple cypher magic can also be used.
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


_


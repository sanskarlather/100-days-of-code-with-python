import prettytable
table=prettytable.PrettyTable()
pokemon_name=['Pikachu',"Squirtle","Charmander","Bulbasaur"]
types=["Electric","Water","Fire","Land"]
table.add_column("Pokemon Name",pokemon_name,)
table.add_column("Type",types)
table.align="l"
print(table)
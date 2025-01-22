import numpy as np
import pypsa
network=pypsa.Network()

n_bus =3
for i in range(n_bus):
    network.add("Bus", f"My bus{i}", v_nom=20.0)
network.buses
for i in range(n_bus):
    network.add("Line",f"My line{i}",bus0=f"My bus{i}",bus1=f"My bus{(i+1)% n_bus}",x=0.1,r=0.1)
network.add("Generator","My gen", bus="My bus0", p_set=100, control="PQ")
network.generators
network.generators.p_set


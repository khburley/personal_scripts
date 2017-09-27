import mdtraj as md
import numpy as np

di_dataFN = "dihedrals_MD_divwat.txt"
traj = md.load_dcd('trajectory.dcd', top = 'watDivaline.prmtop')
indicies = np.array([[0, 4, 6, 8]])
dihedraldata = md.compute_dihedrals(traj, indicies)
datafile = open(di_dataFN,'w')
for value in dihedraldata:
	datafile.write("%s\n" % str(value)[1:-1])

datafile.close()

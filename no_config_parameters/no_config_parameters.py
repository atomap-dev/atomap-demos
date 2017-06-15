import hyperspy.api as hs
import atomap.api as am

s = hs.load("srtio3_100.hdf5")

######## Finding optimal peak separation

s_separation = am.get_feature_separation(s)
# Look at images in the folder to find an optimal peak separation
# 13 pixels is a good value 

process_parameter = am.process_parameters.GenericStructure()
atom_lattice = am.make_atom_lattice_from_image(
        s,
        process_parameter=process_parameter,
        pixel_separation=13)

s_atom_list = atom_lattice.get_sublattice_atom_list_on_image()
s_atom_list.plot()
atom_lattice.save()

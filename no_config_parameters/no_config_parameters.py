import hyperspy.api as hs
import atomap.api as am

s = hs.load("srtio3_100.hspy")

######## Finding optimal peak separation
s_separation = am.get_feature_separation(s)
s_separation.plot()

process_parameter = am.process_parameters.GenericStructure()
atom_lattice = am.make_atom_lattice_from_image(
        s,
        process_parameter=process_parameter,
        pixel_separation=13)

atom_lattice.plot()
atom_lattice.save(overwrite=True)

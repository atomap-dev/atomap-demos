import hyperspy.api as hs
import atomap.api as am

s = hs.load("srtio3_100.hdf5")
s.axes_manager[0].scale = 10*0.3905/296.09
s.axes_manager[1].scale = 10*0.3905/296.09

###############
generic_structure = am.process_parameters.GenericStructure()

sublattice_0 = generic_structure.sublattice_list[0]
sublattice_1 = am.process_parameters.GenericSublattice()
generic_structure.add_sublattice_config(sublattice_1)
sublattice_1.atom_subtract_config[0]['sublattice'] = sublattice_0.name
sublattice_1.sublattice_position_sublattice = sublattice_0.name
sublattice_1.sublattice_position_zoneaxis = sublattice_0.zone_axis_list[2]['name']

atom_lattice = am.make_atom_lattice_from_image(
        s,
        process_parameter=generic_structure,
        pixel_separation=13)

s_atom_list = atom_lattice.get_sublattice_atom_list_on_image()
s_atom_list.plot()
atom_lattice.save()

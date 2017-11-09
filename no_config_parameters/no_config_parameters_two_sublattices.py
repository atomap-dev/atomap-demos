import hyperspy.api as hs
import atomap.api as am

s = hs.load("srtio3_100.hspy")
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
atom_lattice.name = 'srtio3_100_two_sublattices'

atom_lattice.plot()
atom_lattice.save(overwrite=True)

import hyperspy.api as hs
from atomap.atom_finding_refining import plot_feature_separation
from atomap.main import make_atom_lattice_from_image
from atomap.process_parameters import GenericStructure, GenericSublattice

s = hs.load("srtio3_100.hdf5")
s.axes_manager[0].scale = 10*0.3905/296.09
s.axes_manager[1].scale = 10*0.3905/296.09

###############
model_parameters = GenericStructure()
sublattice_0 = model_parameters.sublattice_list[0]
sublattice_1 = GenericSublattice()
model_parameters.add_sublattice_config(sublattice_1)
sublattice_1.atom_subtract_config[0]['sublattice'] = sublattice_0.name
sublattice_1.sublattice_position_sublattice = sublattice_0.name
sublattice_1.sublattice_position_zoneaxis = sublattice_0.zone_axis_list[2]['name']

atom_lattice = make_atom_lattice_from_image(
        s,
        model_parameters=model_parameters,
        pixel_separation=13)
atom_lattice.plot_all_sublattices()
atom_lattice.save_atom_lattice()

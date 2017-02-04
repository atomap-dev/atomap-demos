import hyperspy.api as hs
from atomap.atom_finding_refining import plot_feature_separation
from atomap.main import make_atom_lattice_from_image
from atomap.process_parameters import PerovskiteOxide110

s = hs.load("test_ADF_cropped.hdf5")
s_abf = hs.load("test_ABF_cropped.hdf5")

plot_feature_separation(s)
model_parameters = PerovskiteOxide110()

atom_lattice = make_atom_lattice_from_image(
        s,
        model_parameters=model_parameters,
        pixel_separation=19,
        s_image1=s_abf)
atom_lattice.plot_all_sublattices()
atom_lattice.save_atom_lattice()

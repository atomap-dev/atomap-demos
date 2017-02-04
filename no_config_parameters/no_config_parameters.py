import hyperspy.api as hs
from atomap.atom_finding_refining import plot_feature_separation
from atomap.main import make_atom_lattice_from_image
from atomap.process_parameters import GenericStructure

s = hs.load("srtio3_100.hdf5")

######## Finding optimal peak separation

plot_feature_separation(s) 
# Look at images in the folder to find an optimal peak separation
# 13 pixels is a good value 

######## Calibrate the signal, must be in nanometers
# The HyperSpy ROI functionality can be used:
# line_roi = hs.roi.Line2DROI(1., 1., 50., 50., 1)
# s.plot()
# roi1D = line_roi.interactive(s, color="yellow")
# pixels = roi1D.data.size
#
# Alternatively, an external program can be used to find the
# calibration value
s.axes_manager[0].scale = 10*0.3905/296.09
s.axes_manager[1].scale = 10*0.3905/296.09

model_parameters = GenericStructure()

atom_lattice = make_atom_lattice_from_image(
        s,
        model_parameters=model_parameters,
        pixel_separation=13)
atom_lattice.plot_all_sublattices()
atom_lattice.save_atom_lattice()

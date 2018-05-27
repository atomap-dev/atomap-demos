import hyperspy.api as hs
import atomap.api as am

s = hs.load("test_ADF_cropped.hspy")
s_abf = hs.load("test_ABF_cropped.hspy")

s_separation = am.get_feature_separation(s)

process_parameter = am.process_parameters.PerovskiteOxide110()

atom_lattice = am.make_atom_lattice_from_image(
        s_image0=s,
        process_parameter=process_parameter,
        pixel_separation=17,
        s_image1=s_abf)
atom_lattice.plot()
atom_lattice.save(overwrite=True)

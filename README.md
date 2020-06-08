# ObscuredSubaperture-Python

This repository contains Python code for Shack-Hartmann sensing with an arbitrarily shaped pupil, 
leading to obscured subapertures. The code updates the wavefront corrector control matrix and 
command vector for both zonal and modal correction methods.

The code is intended for integration into an existing working Shack-Hartmann sensing and deformable 
mirror control software using either the zonal or modal method. It can be either integrated directly into 
the main correction loop or called as a separate function. Names and dimensions of matrices should be 
modified accordingly.

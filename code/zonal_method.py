"""
zonal_method.py

Function: To update the wavefront corrector control matrix and command vector for the zonal correction method
after obtaining the wavefront slope information in both x and y directions. Slope values for obscured 
subapertures are initially set as zero during the centroiding process.

Arguments:
    slope: concatenated x,y slope vector with the value for obscured subapertures initially set as zero
    response_matrix_slopes: the DM slope response matrix
    control_matrix_slopes: the DM slope control matrix
    DM_command: the updated DM command vector

Author: Jiahe Cui

Date: 2020.06

Email: jiahe.cui@eng.ox.ac.uk
"""

import numpy

# Find the indices of the unmeasurable slopes in the slope vector which were set to zero during centroiding
index_remove = numpy.where(slope == 0)[1]

# Remove the unmeasurable slopes from the slope vector
slope = numpy.delete(slope, index_remove, axis = 0)

# Remove rows corresponding to invalid subapertures from the original slope response matrix
response_matrix_slopes = numpy.delete(response_matrix_slopes, index_remove, axis = 0)

# Calculate the new slope control matrix
control_matrix_slopes = numpy.linalg.pinv(response_matrix_slopes)

# Calculate the updated DM command vector
DM_command = numpy.dot(control_matrix_slopes, slope)


"""
modal_method.py

Function: To update the wavefront corrector control matrix and command vector for the modap correction method
after obtaining the wavefront slope information in both x and y directions. Slope values for obscured 
subapertures are initially set as zero during the centroiding process.

Arguments:
    slope: concatenated x,y slope vector with the value for obscured subapertures initially set as zero
    zern_matrix: Zernike polynomials used for wavefront reconstruction defined over each subaperture
    zern_grad_matrix: x,y gradient of Zernike polynomials used for wavefront reconstruction defined over each subaperture
    p_matrix: matrix obtained uniquely by computing the Cholesky decomposition of numpy.dot(zern_matrix.T, zern_matrix)
    conv_matrix: conversion matrix between slope vector and new modal coefficient vector
    response_matrix_slopes: the DM slope response matrix
    response_matrix_modal: the new DM modal response matrix
    control_matrix_modal: the new DM modal control matrix
    modal_coeff: the new modal coefficient vector
    DM_command: the updated DM command vector

Author: Jiahe Cui

Date: 2020.06

Email: jiahe.cui@eng.ox.ac.uk
"""

import numpy

# Find the indices of the unmeasurable slopes in the slope vector which were set to zero during centroiding
index_remove = numpy.where(slope == 0)[1]

# Remove rows corresponding to invalid subapertures from the original zernike matrix
zern_matrix = numpy.delete(zern_matrix, index_remove, axis = 0)

# Remove rows corresponding to invalid subapertures from the original Zernike gradient matrix
zern_grad_matrix = numpy.delete(zern_grad_matrix, index_remove_inf, axis = 0)

# Obtain matrix P by computing the Cholesky decomposition of numpy.dot(zern_matrix.T, zern_matrix)
p_matrix = numpy.linalg.cholesky(numpy.dot(zern_matrix.T, zern_matrix))

# Check whether matrix P is an upper triangular matrix
if numpy.allclose(p_matrix, numpy.tril(p_matrix)):
    p_matrix = p_matrix.T

# Calculate the new conversion matrix
conv_matrix = numpy.dot(p_matrix, numpy.linalg.pinv(zern_grad_matrix))

# Remove rows corresponding to invalid subapertures from the original slope response matrix
response_matrix_slopes = numpy.delete(response_matrix_slopes, index_remove, axis = 0)

# Calculate the new modal response matrix
response_matrix_modal = numpy.dot(conv_matrix, response_matrix_slopes)

# Calculate the new modal control matrix
control_matrix_modal = numpy.linalg.pinv(response_matrix_modal)

# Remove the unmeasurable slopes from the original slope vector
slope = numpy.delete(slope, index_remove, axis = 0)

# Retrieve the modal coefficient vector from the new slope vector
modal_coeff = numpy.dot(conv_matrix, slope)

# Calculate the updated DM command vector
DM_command = numpy.dot(control_matrix_modal, modal_coeff)


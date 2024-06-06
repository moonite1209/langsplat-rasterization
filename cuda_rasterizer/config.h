/*
 * Copyright (C) 2023, Inria
 * GRAPHDECO research group, https://team.inria.fr/graphdeco
 * All rights reserved.
 *
 * This software is free for non-commercial, research and evaluation use 
 * under the terms of the LICENSE.md file.
 *
 * For inquiries contact  george.drettakis@inria.fr
 */

#ifndef CUDA_RASTERIZER_CONFIG_H_INCLUDED
#define CUDA_RASTERIZER_CONFIG_H_INCLUDED

#define NUM_CHANNELS 3 // Default 3, RGB
#define NUM_CHANNELS_language_feature 3 // CLIP_feature
#define NUM_CHANNELS_language_feature_3d 3
#define BLOCK_X 16
#define BLOCK_Y 16
#define M_3DGS 0
#define M_LANGSPLAT 1
#define M_OURS 2

#endif
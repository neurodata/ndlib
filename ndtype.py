# Copyright 2014 NeuroData (http://neurodata.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

# ND Servers
LOCALHOST = 'localhost'
ND_servermap = {'localhost':'localhost'}

# ND_Channel Types, Mapping, Groups
ANNOTATION = 'annotation'
TIMESERIES = 'timeseries'

ND_channeltypes = {1:ANNOTATION,2:TIMESERIES}

TIMESERIES_CHANNELS = [ TIMESERIES ]
ANNOTATION_CHANNELS = [ ANNOTATION ]

# ND Data Types, Mapping, Groups
UINT8 = 'uint8'
UINT16 = 'uint16'
UINT32 = 'uint32'
UINT64 = 'uint64'
FLOAT32 = 'float32'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'
INT64 = 'int64'

DTYPE_uint8 = [ UINT8 ]
DTYPE_uint16 = [ UINT16 ]
DTYPE_uint32 = [ UINT32 ]
DTYPE_uint64 = [ UINT64 ]
DTYPE_int8 = [ INT8 ]
DTYPE_int16 = [ INT16 ]
DTYPE_int32 = [ INT32 ]
DTYPE_int64 = [ INT64 ]
DTYPE_float32 = [ FLOAT32 ]

ND_dtypetonp = {UINT8:np.uint8, UINT16:np.uint16, UINT32:np.uint32, UINT64:np.uint64, FLOAT32:np.float32, INT8:np.int8, INT16:np.int16, INT32:np.int32}

# ND KeyValue,MetaData Engines
MYSQL = 'MySQL'

# ND Version
ND_VERSION = '1.1'
SCHEMA_VERSION = '1.1'

# Propagated Values
PROPAGATED = 2
UNDER_PROPAGATION = 1
NOT_PROPAGATED = 0

# ReadOnly Values
READONLY_TRUE = 1
READONLY_FALSE = 0

# SCALING OPTIONS
ZSLICES = 0
ISOTROPIC = 1
ND_scalingtoint = {'zslices':ZSLICES, 'xyz':ISOTROPIC}

# Exception Values
EXCEPTION_TRUE = 1
EXCEPTION_FALSE = 0

# Public Values
PUBLIC_TRUE = 1
PUBLIC_FALSE = 0

# S3 Backend Values
S3_TRUE = 1
S3_FALSE = 0

# Backup Values
FILE_SYSTEM = 'local'
AMAZON_S3 = 's3'

